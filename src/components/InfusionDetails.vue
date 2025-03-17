<script>
import dummy from '@/assets/generated_data_unique.json'
import { ProgressIndicator, ProgressRoot } from 'radix-vue'
export default {
  name: 'InfusionsButtons',
  components: { ProgressIndicator, ProgressRoot },
  props: ['infusionId'],
  data() {
    return {
      infusion: null,
      allInfusions: dummy,
    }
  },
  watch: {
    '$route.params.infusionId'(newId) {
      this.fetchItem(newId) //Fetch item on component creation
    },
  },
  created() {
    const id = this.$route.params.infusionId
    this.fetchItem(id)
  },
  methods: {
    fetchItem(id) {
      this.infusion = this.allInfusions.find((infusion) => infusion.id === id) //check all the dummydata for the single dataitem with the matching Id
    },
  },
}
</script>
<div></div>
<div></div>
<template>
  <div class="grid grid-cols-2">
    <div class="grid grid-cols-3 gap-2" v-if="infusion">
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">ward</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.ward }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">bed:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.bed }}</div>
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
        <div class="bg-blue-200 rounded-full">totalMl:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.totalMl }}</div>
      </div>
      <div class="text-center grid grid-cols-2">
        <div class="bg-blue-200 rounded-full">remainingMl:</div>
        <div class="bg-gray-300 rounded-full">{{ infusion.remainingMl }}</div>
      </div>
    </div>
    <div>
      <ProgressRoot
        v-model="progressValue"
        class="relative overflow-hidden bg-blackA9 rounded-full w-full sm:w-[300px] h-4 sm:h-5"
        style="transform: translateZ(0)"
      >
        <ProgressIndicator
          class="bg-green-500 rounded-full w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]"
          :style="`transform: translateX(-${100 - 80}%)`"
        />
      </ProgressRoot>
    </div>
  </div>
</template>
