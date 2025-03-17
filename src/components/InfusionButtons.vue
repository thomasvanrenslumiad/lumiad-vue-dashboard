<script>
export default {
  name: 'InfusionsButtons',
  props: {
    id: String,
    status: String,
    ward: String,
    bed: String,
    drug: String,
  },
  methods: {
    routeIt(infusionID) {
      this.$router.push({ name: 'Infusion-details', params: { infusionId: infusionID } })
    },
  },
}
</script>

<template>
  <div>
    <button
      @click="routeIt(id)"
      class="m-2 flex 4xl:w-[19.5VW] w-[19VW] cursor-pointer rounded-[1vw] bg-gray-400 hover:bg-gray-500 hover:text-white focus:bg-gray-600 focus:text-white focus:outline-2 focus:outline-offset-2 focus:outline-black active:bg-gray-700 active:text-white ove"
    >
      <div
        class="mr-2 ml-1 bg-${data.status}-500 rounded-2xl pr-2 pl-2 text-center bg-[var(--customPadding)]-500"
        :style="{ '--customPadding': this.status }"
      >
        1
      </div>
      <div class="w-4/5 truncate pl-2 text-ellipsis">{{ ward }} {{ bed }}</div>
      <div class="rounded-2xl bg-red-500 truncate pl-2 w-[4vw] absolute right-3">
        {{ drug }}
      </div>
    </button>
  </div>
</template>

<style scoped></style>
