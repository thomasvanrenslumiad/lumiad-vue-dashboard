<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
const props = defineProps({
  id: String,
  status: String,
  ward: String,
  bed: String,
  drug: String,
  totalMl: Number,
  remainingMl: Number,
  mlPerHour: Number,
})
const remainingPercentage = computed(() => (props.remainingMl / (props.totalMl / 100)).toFixed(2))
const route = useRouter()
function routeIt(infusionID) {
  route.push({ name: 'Infusion-details', params: { infusionId: infusionID } })
}

const backgroundClass = computed(() => {
  switch (true) {
    case remainingPercentage.value > 80:
      return 'mr-2 4xl:w-[2.5VW] w-[2VW] ml-1 bg-green-500 rounded-2xl pr-2 pl-2 text-center text-white' // Green for status > 80
    case remainingPercentage.value > 40:
      return 'mr-2 4xl:w-[2.5VW] w-[2VW] ml-1 bg-yellow-500 rounded-2xl pr-2 pl-2 text-center text-white' // Yellow for status > 40
    case remainingPercentage.value > 20:
      return 'mr-2 4xl:w-[2.5VW] w-[2VW] ml-1 bg-orange-500 rounded-2xl pr-2 pl-2 text-center text-white' // Orange for status > 20
    default:
      return 'mr-2 4xl:w-[2.5VW] w-[2VW] ml-1 bg-red-500 rounded-2xl pr-2 pl-2 text-center text-white' // Red for status <= 20
  }
})
</script>

<template>
  <div>
    <button
      @click="routeIt(props.id)"
      class="m-2 flex 4xl:w-[19VW] w-[18.5VW] cursor-pointer rounded-[1vw] bg-gray-400 hover:bg-gray-500 hover:text-white focus:bg-gray-600 focus:text-white focus:outline-2 focus:outline-offset-2 focus:outline-black active:bg-gray-700 active:text-white ove"
    >
      <div :class="backgroundClass">{{ remainingPercentage }}%</div>
      <div class="4xl:w-[5.25VW] w-[5VW] truncate pl-2 text-ellipsis">{{ props.ward }}</div>
      <div class="4xl:w-[5.25VW] w-[5VW] truncate pl-2 text-ellipsis">{{ props.bed }}</div>
      <div class=" 4xl:w-[3.5VW] w-[3VW] rounded-2xl bg-red-500 truncate pl-2  absolute right-3 text-white">
        {{ props.drug }}
      </div>
    </button>
  </div>
</template>

<style scoped></style>
