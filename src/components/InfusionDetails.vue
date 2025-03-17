<script>
import dummy from '@/assets/generated_data_unique.json'
export default {
  name: 'InfusionsButtons',
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
</template>
