<script setup>
import { computed } from 'vue'
const props = defineProps({
  department: String,
  ward: String,
  bed: String,
  drug: String,
  status: String,
  totalMl: Number,
  remainingMl: Number,
  mlPerHour: Number,
  timeRunning: String,
  timeRemaining: String,
  id: String,
  softwareVersion: String,
  medicalLibraryVersion: String,
})
import { store } from '@/stores/infusionStore.js'



const remainingPercentage = computed(() => (props.remainingMl / (props.totalMl / 100)).toFixed(1))

function storeIt(infusion) {
    store.department= infusion.department
    store.ward = infusion.ward
    store.bed = infusion.bed
    store.drug = infusion.drug
    store.status = infusion.status
    store.totalMl = infusion.totalMl
    store.remainingMl = infusion.remainingMl
    store.mlPerHour = infusion.mlPerHour
    store.timeRunning = infusion.timeRunning
    store.timeRemaining = infusion.timeRemaining
    store.id = infusion.id
    store.softwareVersion = infusion.softwareVersion
    store.medicalLibraryVersion = infusion.medicalLibraryVersion
}

const backgroundClass = computed(() => {
  switch (true) {
    case remainingPercentage.value > 80:
      return 'mr-2 4xl:w-[2.5VW] md:w-[7VW] w-[17vw] ml-1 bg-green-500 rounded-2xl pr-2 pl-2 text-center text-white' // Green for status > 80
    case remainingPercentage.value > 40:
      return 'mr-2 4xl:w-[2.5VW] md:w-[7VW] w-[17vw] ml-1 bg-yellow-500 rounded-2xl pr-2 pl-2 text-center text-white' // Yellow for status > 40
    case remainingPercentage.value > 20:
      return 'mr-2 4xl:w-[2.5VW] md:w-[7VW] w-[17vw] ml-1 bg-orange-500 rounded-2xl pr-2 pl-2 text-center text-white' // Orange for status > 20
    default:
      return 'mr-2 4xl:w-[2.5VW] md:w-[7VW] w-[17vw] ml-1 bg-red-500 rounded-2xl pr-2 pl-2 text-center text-white' // Red for status <= 20
  }
})

const notifier = computed(() => {
  if (props.remainingMl === 0) {
    return 'm-2 flex 4xl:w-[27VW] xl:w-[25.5VW]  md:w-[92vw] w-[86vw] cursor-pointer rounded-full bg-red-200 hover:bg-red-500 hover:text-white focus:bg-red-700 focus:text-white focus:outline-2 data-[state=on]:bg-red-700 focus:outline-offset-2 focus:outline-red-800 active:bg-gray-700 active:text-white outline-red-500 outline-5  '
  } else if (props.mlPerHour === 0) {
    return 'm-2 flex 4xl:w-[27VW] xl:w-[25.5VW]  md:w-[92vw] w-[86vw] cursor-pointer rounded-full bg-yellow-200 hover:bg-yellow-500 hover:text-white focus:bg-yellow-700 data-[state=on]:bg-yellow-700 focus:text-white focus:outline-2 focus:outline-offset-2 focus:outline-red-500 active:bg-gray-700 active:text-white outline-orange-500 outline-3  '
  } else {
    return 'm-2 flex 4xl:w-[27VW] xl:w-[25.5VW]   md:w-[92vw] w-[86vw] cursor-pointer rounded-full bg-gray-400 hover:bg-gray-500 hover:text-white focus:bg-gray-700 data-[state=on]:bg-gray-700 focus:text-white focus:outline-2 focus:outline-offset-2 focus:outline-black active:bg-gray-700 active:text-white dark:bg-gray-300 dark:hover:bg-gray-400  '
  }
})
</script>

<template>
  <div>
    <button @click="storeIt(props)" :class="notifier">
      <div :class="backgroundClass">{{ remainingPercentage }}%</div>
      <div class="4xl:w-[6.85VW] w-[25vw] truncate text-ellipsis">
        {{ props.timeRemaining }}
      </div>
      <div class="4xl:w-[6.85VW] w-[25vw] truncate pl-2 text-ellipsis">
        {{ props.ward }}
      </div>
      <div class="4xl:w-[6.85VW] w-[25vw] truncate pl-2 text-ellipsis">
        {{ props.bed }}
      </div>
      <div
        class="4xl:w-[3.5VW] xl:w-[3VW] w-[20vw] rounded-2xl bg-red-500 truncate pl-2 text-ellipsis text-white"
      >
        {{ props.drug }}
      </div>
    </button>
  </div>
</template>

<style scoped></style>
