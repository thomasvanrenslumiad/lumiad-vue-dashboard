<script setup>
import { RouterView } from 'vue-router'
import AllInfusions from '@/assets/generated_data_unique_with_time.json'

import { Icon } from '@iconify/vue'
import { provide, watch, ref } from 'vue'
import {
  SelectContent,
  SelectItem,
  SelectItemIndicator,
  SelectItemText,
  SelectPortal,
  SelectRoot,
  SelectScrollDownButton,
  SelectScrollUpButton,
  SelectTrigger,
  SelectValue,
  SelectViewport,
} from 'radix-vue'
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

function sortInfusions(newSortChoice) {
  switch (true) {
    case newSortChoice === 'remainingMl':
      for (let i = 0; i < currentInfusions.length; i++) {
        for (let j = 0; j < currentInfusions.length - 1 - i; j++) {
          const value1 = Object.values(currentInfusions[j])[6]
          const value2 = Object.values(currentInfusions[j + 1])[6]
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
      for (let i = 0; i < currentInfusions.length; i++) {
        for (let j = 0; j < currentInfusions.length - 1 - i; j++) {
          const value1 = Object.values(currentInfusions[j])[9]
          const value2 = Object.values(currentInfusions[j + 1])[9]
          if (value1 > value2) {
            const temp = currentInfusions[j]
            currentInfusions[j] = currentInfusions[j + 1]
            currentInfusions[j + 1] = temp
          }
        }
      }
      return
    case newSortChoice === 'ward': {
      console.log('ward')
      let WardSort = currentInfusions.reduce((acc, curr) => {
        let ind = acc.findIndex((item) => item.ward > curr.ward)
        if (ind === -1) ind = acc.length
        acc.splice(ind, 0, curr)
        currentInfusions = acc
        return acc
      }, [])
      currentInfusions = WardSort
      return
    }
    case newSortChoice === 'bed': {
      console.log('bed')
      let BedSort = currentInfusions.reduce((acc, curr) => {
        let ind = acc.findIndex((item) => item.bed > curr.bed)
        if (ind === -1) ind = acc.length
        acc.splice(ind, 0, curr)
        currentInfusions = acc
        return acc
      }, [])
      currentInfusions = BedSort
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
</script>

<template>
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
    <SelectRoot v-model="afdeling">
      <SelectTrigger
        class="md:flex md:static absolute top-3 left-25 min-w-[15vw] 2xl:w-[20vw] w-[50vw] min-h-[5vh] items-center justify-between rounded px-[15px] text-[13px] leading-none h-[35px] gap-[5px] bg-white text-grass11 shadow-[0_2px_10px] shadow-black/10 hover:bg-gray-200 focus:shadow-black outline-none truncate text-ellipsis"
        aria-label="Customise options"
      >
        <SelectValue placeholder="Kies uw afdeling" />
        <Icon icon="radix-icons:chevron-down" class="h-3.5 w-3.5" />
      </SelectTrigger>

      <SelectPortal>
        <SelectContent
          class="min-w-[10vw] min-h-[25vh] md:h-[28vh] h-[40vh] bg-white rounded will-change-[opacity,transform] data-[side=top]:animate-slideDownAndFade data-[side=right]:animate-slideLeftAndFade data-[side=bottom]:animate-slideUpAndFade data-[side=left]:animate-slideRightAndFade"
          :side-offset="5"
        >
          <SelectScrollUpButton
            class="flex items-center justify-center h-[25px] bg-white text-violet11 cursor-default"
          >
            <Icon icon="radix-icons:chevron-up" />
          </SelectScrollUpButton>

          <SelectViewport class="p-[5px]">
            <SelectItem
              v-for="(option, index) in options"
              :key="index"
              class="text-[13px] leading-none text-grass11 rounded-[3px] flex items-center h-[25px] pr-[35px] pl-[25px] relative select-none data-[disabled]:text-gray-500 data-[disabled]:pointer-events-none data-[highlighted]:outline-none data-[highlighted]:bg-blue-900 data-[highlighted]:text-white"
              :value="option"
            >
              <SelectItemIndicator
                class="absolute left-0 w-[25px] inline-flex items-center justify-center"
              >
                <Icon icon="radix-icons:check" />
              </SelectItemIndicator>
              <SelectItemText>
                {{ option }}
              </SelectItemText>
            </SelectItem>
          </SelectViewport>

          <SelectScrollDownButton
            class="flex items-center justify-center h-[25px] bg-white text-violet11 cursor-default"
          >
            <Icon icon="radix-icons:chevron-down" />
          </SelectScrollDownButton>
        </SelectContent>
      </SelectPortal>
    </SelectRoot>
  </header>
  <section class="md:flex xl:h-[78vh] md:h-[70vh] overflow-hidden">
    <div
      class="m-3 xl:h-[76vh] md:h-[68vh] h-[0vh] xl:w-[70vw] md:w-3/5 flex-initial md:rounded-[1vw] bg-gray-200 p-2 md:visible invisible"
    >
      <h1>{{ afdeling }}</h1>
    </div>
    <div
      class="xl:w-[30vw] md:w-[40vw] m-3 flex-initial bg-gray-200 md:rounded-[1vw] rounded-[3vw] p-2 overflow-x-hidden"
    >
      <div>
        <select
          id="countries"
          v-model="sortChoice"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        >
          <option selected disabled hidden>Sort by</option>
          <option value="remainingMl">Remaining IV</option>
          <option value="time">Remaining time</option>
          <option value="ward">Ward</option>
          <option value="bed">bed</option>
          <option value="drug">Drug</option>
        </select>
      </div>
      <div class="4xl:m-3 md:m-1 m-2 md:h-[74vh] h-[40vh] xl:w-[28vw] md:w-[39vw] overflow-auto">
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
  <section class="xl:flex overflow-hidden">
    <div
      class="mr-5 mb-3 ml-5 4xl:h-[10vh] xl:h-[11vh] 4XL:w-[100vw] xl:w-[100vw] flex-initial md:rounded-[1vw] rounded-[3vw] bg-gray-200"
    >
      <div
        id="infuusDetails"
        class="mr-5 mb-3 ml-5 4xl:h-[10vh] xl:h-[11vh] 4XL:w-[98vw] xl:w-[96vw] flex-initial overflow-hidden rounded-[2vw] bg-gray-200 p-5 font-[Open_Sans] text-2xl text-ellipsis [&::-webkit-scrollbar]:[width:10px] [&::-webkit-scrollbar]:rounded-full [&::-webkit-scrollbar-thumb]:bg-gray-400"
      >
        <RouterView />
      </div>
    </div>
  </section>
</template>

<style scoped></style>
