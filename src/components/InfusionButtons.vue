<script>
import dummy from '../assets/dummyInfusions.json'
import { watchEffect } from 'vue'
export default {
  name: 'InfusionsButtons',
  props: ['afdeling'],
  data() {
    return {
      allInfusions: dummy,
    }
  },
  watch: {
    '$component.props.afdeling'(newAfdeling) {
      this.filterByDepartment(newAfdeling) //Fetch item on component creation
    },
  },
  created() {
    const afdeling = this.afdeling
    this.filterByDepartment(afdeling);
  },

  watchEffect:(() => {
  // runs only once before 3.5
  // re-runs when the "foo" prop changes in 3.5+
  console.log(this.afdeling)
}),
  methods: {
    routeIt(infusionID) {
      this.$router.push({ name: 'Infusion-details', params: { infusionId: infusionID } })
    },
    filterByDepartment(newAfdeling) {
      let filterKey = newAfdeling
      const result = Object.entries(dummy).filter(([k, v]) => k === filterKey)
      console.log(Object.fromEntries(result))
      console.log(this.afdeling);
    },
  },

}
</script>

<template>
  <div>
    <div v-for="infusion in allInfusions" :key="infusion.id" class="">
      <button
        @click="routeIt(infusion.id)"
        class="m-2 flex 4xl:w-[19.5VW] w-[19VW] cursor-pointer rounded-[1vw] bg-gray-400 hover:bg-gray-500 hover:text-white focus:bg-gray-600 focus:text-white focus:outline-2 focus:outline-offset-2 focus:outline-black active:bg-gray-700 active:text-white active:text-white"
      >
        <div
          class="mr-2 ml-1 bg-${data.status}-500 rounded-2xl pr-2 pl-2 text-center bg-[var(--customPadding)]-500"
          :style="{ '--customPadding': infusion.status }"
        >
          1
        </div>
        <div class="w-4/5 truncate pl-2 text-ellipsis">{{ infusion.ward }} {{ infusion.bed }}</div>
        <div class="rounded-2xl bg-red-500 truncate pl-2 w-[4vw]  absolute right-3">{{ infusion.drug }}</div>
      </button>
    </div>
  </div>
</template>

<style scoped></style>
