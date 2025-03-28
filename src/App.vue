<script setup>
import { RouterView } from 'vue-router'
import AllInfusions from '@/assets/generated_data_unique_with_time.json'
import { provide, ref, watch } from 'vue'
import { ToggleGroupItem, ToggleGroupRoot } from 'radix-vue'
import InfusionButtons from '@/components/InfusionButtons.vue'

let currentInfusions = AllInfusions

const options = [
  'Overzicht',
  'Spoedeisende Hulp',
  'Chirurgie',
  'Geriatrie',
  'Kardiochirurgie',
  'Verloskunde',
  'Oncologie',
  'Pediatrie',
  'Psychiatrie',
]
const afdeling = defineModel()
provide('afdeling', afdeling)

const sortChoice = ref(null)
// a save location for the previous sorting choice to permit sorting in reverse
const prevSort = ref(null)

function filterAllInfusions(afdeling) {
  currentInfusions = AllInfusions.filter((infusion) => infusion.department === afdeling)
}
function returnToAllInfusions() {
  currentInfusions = AllInfusions
}

watch(afdeling, (newAfdeling) => {
  if (newAfdeling === 'Overzicht') {
    returnToAllInfusions()
    return
  }
  filterAllInfusions(newAfdeling)
})

function filterButtons(filter) {
  if (filter === 'nonRun') {
    currentInfusions = currentInfusions.filter(
      (infusion) => infusion.timeRemaining === 'Infusion not running',
    )
  } else if (filter === 'below10') {
    currentInfusions = currentInfusions.filter(
      (infusion) => infusion.totalMl / infusion.remainingMl > 10,
    )
    console.log('we filteren op infusen die minder dan 10% vulling bevatten')
  } else if (filter === '1hour') {
    currentInfusions = currentInfusions.filter((infusion) => {
      if (!(infusion.timeRemaining === 'Infusion not running')) {
        var splitstring = infusion.timeRemaining.split(':')
        if (splitstring[0] === '0') {
          return infusion
        }
      }
    })
    console.log('we filteren op infusen die minder dan 10 minuten doorlopen')
  } else {
    currentInfusions = AllInfusions
  }

  // currentInfusions = currentInfusions.filter((infusion) => infusion.timeRemaining === 'Infusion not running')
}

function calculatePercentage(infusion) {
  return parseFloat(((infusion.remainingMl / infusion.totalMl) * 100).toFixed(1))
}

function timeToSeconds(time)
{
  // Ensure the time has a valid format like HH:SS
  const [hours, seconds] = time.split(':').map(Number);

  // Calculate the total time in minutes (convert to seconds if needed)
  return hours * 60 + seconds; // Convert to total minutes (HH treated as minutes)
}


function sortInfusions(newSortChoice) {
  switch (true) {
    case newSortChoice === 'remainingMl':
      for (let i = 0; i < currentInfusions.length; i++) {
        for (let j = 0; j < currentInfusions.length - 1 - i; j++) {
          const value1 = calculatePercentage(currentInfusions[j])
          const value2 = calculatePercentage(currentInfusions[j + 1])
          if (value1 > value2) {
            const temp = currentInfusions[j]
            currentInfusions[j] = currentInfusions[j + 1]
            currentInfusions[j + 1] = temp
          }
        }
      }
      return
    case newSortChoice === 'time':
      console.log('time')
      currentInfusions.sort((a, b) => {
        // If 'Infusion not running', treat it as the largest possible time value
        const timeA = a.timeRemaining === 'Infusion not running' ? '9999:59' : a.timeRemaining;
        const timeB = b.timeRemaining === 'Infusion not running' ? '9999:59' : b.timeRemaining;

        // Normalize the time (pad single-digit hours) before calculating the seconds
        const normalizedTimeA = timeA.length < 5 ? `0${timeA}` : timeA;
        const normalizedTimeB = timeB.length < 5 ? `0${timeB}` : timeB;

        // Compare by total seconds (timeToSeconds) but treat 'Infusion not running' as the last
        return timeToSeconds(normalizedTimeA) - timeToSeconds(normalizedTimeB);
      })
      return
    case newSortChoice === 'ward': {
      console.log('ward')
      currentInfusions = currentInfusions.reduce((acc, curr) => {
        let ind = acc.findIndex((item) => item.ward > curr.ward)
        if (ind === -1) ind = acc.length
        acc.splice(ind, 0, curr)
        currentInfusions = acc
        return acc
      }, [])
      return
    }
    case newSortChoice === 'bed': {
      console.log('bed')
      currentInfusions = currentInfusions.reduce((acc, curr) => {
        let ind = acc.findIndex((item) => item.bed > curr.bed)
        if (ind === -1) ind = acc.length
        acc.splice(ind, 0, curr)
        currentInfusions = acc
        return acc
      }, [])
      return
    }
    case newSortChoice === 'drug':
      console.log('drug')
      for (let i = 0; i < currentInfusions.length; i++) {
        for (let j = 0; j < currentInfusions.length - 1 - i; j++) {
          const value1 = Object.values(currentInfusions[j])[3]
          const value2 = Object.values(currentInfusions[j + 1])[3]
          if (value1 > value2) {
            const temp = currentInfusions[j]
            currentInfusions[j] = currentInfusions[j + 1]
            currentInfusions[j + 1] = temp
          }
        }
      }
      return
  }
}

watch(sortChoice, (newSortChoice) => {
  sortInfusions(newSortChoice)
})

const toggleStateMultiple = ref()

watch(toggleStateMultiple, (newToggleStateMultiple) => {
  filterButtons(newToggleStateMultiple)
})

const toggleGroupItemClasses =
  'hover:bg-gray-100  data-[state=on]:bg-gray-200  flex h-[35px] xl:w-[20vw] md:w-[35vw] w-[30vw] items-center justify-center bg-white text-base leading-4 first:rounded-l last:rounded-r focus:z-10 focus:shadow-[0_0_0_2px] focus:shadow-black focus:outline-none dark:bg-gray-300  dark:border-gray-600 dark:hover:bg-gray-400 dark:data-[state=on]:bg-gray-400 '
</script>

<template>
  <body class="bg-white dark:bg-black">
    <header class="md:flex h-[8vh] bg-blue-500 p-6 md:overflow-hidden">
      <img
        src="./assets/LumiadLogo.svg"
        alt="logo"
        class="md:mr-[30vw] md:h-[2vw] md:visible invisible"
      />
      <img
        src="./assets/dashboardnaam.svg"
        alt="logo"
        class="relative md:mr-[24vw] mr-[4vw] md:visible invisible h-[3vw]"
      />
      <select
        v-model="afdeling"
        class="md:flex md:static absolute top-3 left-25 w-[70vw] md:w-full bg-gray-50 border border-gray-300 hover:bg-gray-100 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-300 dark:border-gray-600 dark:hover:bg-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
      >
        <option v-for="(option, index) in options" :value="option" :key="index">
          {{ option }}
        </option>
      </select>
    </header>
    <section class="xl:flex xl:h-[78.9vh] overflow-hidden dark:bg-black">
      <div
        class="xl:m-3 xl:h-[77vh] h-[0vh] xl:w-[70vw] flex-initial md:rounded-[1vw] bg-gray-200 dark:bg-gray-500 p-2 xl:visible invisible"
      >
        <h1>{{ afdeling }}</h1>
      </div>
      <div
        class="xl:w-[30vw] w-[98vw] xl:h-[77vh] m-3 flex-initial bg-gray-200 dark:bg-gray-500 md:rounded-[1vw] rounded-[3vw] p-2 overflow-x-hidden"
      >
        <div>
          <ToggleGroupRoot v-model="toggleStateMultiple" type="single" class="flex">
            <ToggleGroupItem value="nonRun" :class="toggleGroupItemClasses">
              Non-running
            </ToggleGroupItem>
            <ToggleGroupItem value="below10" :class="toggleGroupItemClasses">
              below 10%
            </ToggleGroupItem>
            <ToggleGroupItem value="1hour" :class="toggleGroupItemClasses">
              Less then 1 hour
            </ToggleGroupItem>
          </ToggleGroupRoot>
        </div>
        <div>
          <select
            v-model="sortChoice"
            class="w-[95vw] xl:w-full bg-gray-50 border border-gray-300 hover:bg-gray-100 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-300 dark:border-gray-600 dark:hover:bg-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
          >
            <option selected disabled>Sort by</option>
            <option value="remainingMl">remaining %IV</option>
            <option value="time">Remaining time</option>
            <option value="ward">Ward</option>
            <option value="bed">bed</option>
            <option value="drug">Drug</option>
          </select>
        </div>
        <div
          class="4xl:m-3 md:m-1 m-2 4xl:h-[68vh] xl:h-[67vh] md:h-[60.2vh] h-[51.3vh] xl:w-[28vw] overflow-auto"
        >
          <div v-for="infusion in currentInfusions" :key="infusion.id + Math.random()">
            <InfusionButtons
              :department="infusion.department"
              :ward="infusion.ward"
              :bed="infusion.bed"
              :drug="infusion.drug"
              :status="infusion.status"
              :totalMl="infusion.totalMl"
              :remainingMl="infusion.remainingMl"
              :mlPerHour="infusion.mlPerHour"
              :time-running="infusion.timeRunning"
              :timeRemaining="infusion.timeRemaining"
              :id="infusion.id"
            />
          </div>
        </div>
      </div>
    </section>
    <section class="xl:flex overflow-hidden dark:bg-black">
      <div
        class="xl:m-3 4xl:h-[11.25vh] xl:static xl:h-[12.5vh] 4XL:w-[100vw] xl:w-[100vw] flex-initial md:rounded-[1vw] rounded-[3vw] bg-gray-200 dark:bg-gray-500"
      >
        <div
          id="infuusDetails"
          class="4XL:w-[98vw] xl:static xl:w-[96vw] flex-initial overflow-hidden rounded-[2vw] p-5 font-[Open_Sans] text-2xl text-ellipsis [&::-webkit-scrollbar]:[width:10px] [&::-webkit-scrollbar]:rounded-full [&::-webkit-scrollbar-thumb]:bg-gray-400"
        >
          <RouterView />
        </div>
      </div>
    </section>
  </body>
</template>

<style scoped></style>
