<script setup>
import { ref, watch, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import dummy from '@/assets/generated_data_unique.json'
import { ProgressIndicator, ProgressRoot } from 'radix-vue'
const infusion = ref(null)
const percentage = ref(null)
const allInfusions = dummy
const route = useRoute() // Get the current route to access the params

// Fetch the infusion based on the ID
const fetchItem = (id) => {
  infusion.value = allInfusions.find((infusion) => infusion.id === id)
}
const calculatePercentage = (currentInfusion) => {
  percentage.value = parseFloat(
    ((currentInfusion.value.remainingMl / currentInfusion.value.totalMl) * 100).toFixed(1),
  )
}
const backgroundClass = computed(() => {
  switch (true) {
    case percentage.value > 80:
      return 'bg-linear-to-l from-green-500 to-green-800 rounded-full w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]' // Green for status > 80
    case percentage.value > 40:
      return 'bg-linear-to-l from-yellow-500 to-yellow-800 rounded-full w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]' // Yellow for status > 40
    case percentage.value > 20:
      return 'bg-linear-to-l from-orange-500 to-orange-800 rounded-full w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]' // Orange for status > 20
    default:
      return 'bg-linear-to-l from-red-500 to-red-800 rounded-full w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]' // Red for status <= 20
  }
})

// Watch for changes in the route's infusionId parameter
watch(
  () => route.params.infusionId,
  (newId) => {
    fetchItem(newId)
    calculatePercentage(infusion)
    console.log(percentage)
  },
)

// Initial fetch when component is mounted
onMounted(() => {
  const id = route.params.infusionId
  fetchItem(id)
  calculatePercentage(infusion)
  console.log(percentage)
})
</script>

<template>
  <div class="grid grid-cols-5">
    <div class="col-span-4 grid grid-cols-3 gap-2" v-if="infusion">
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">ward</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.ward }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">bed:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.bed }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">totalMl:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.totalMl }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">Infusion Id:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.id }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">drug:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.drug }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">remainingMl:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.remainingMl }}</div>
      </div>
    </div>
    <div class="" v-if="percentage">
      <ProgressRoot
        v-model="percentage"
        class="bg-gray-500 relative overflow-hidden bg-blackA9 rounded-full w-full h-4 sm:h-[5vh]"
        style="transform: translateZ(0)"
      >
        <ProgressIndicator
          :class="backgroundClass"
          :style="`transform: translateX(-${100 - percentage}%)`"
        />
      </ProgressRoot>
    </div>
  </div>
</template>
