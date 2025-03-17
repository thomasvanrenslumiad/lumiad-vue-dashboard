<script setup>
import { RouterView } from 'vue-router'
import AllInfusions from '@/assets/dummyInfusions.json'
import InfusionButtons from '@/components/InfusionButtons.vue'

import { Icon } from '@iconify/vue'
import { provide, watch } from 'vue'
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
</script>

<template>
  <header class="flex h-[8vh] bg-blue-500 p-6 overflow-hidden">
    <img src="./assets/LumiadLogo.svg" alt="logo" class="mr-[30vw] h-[2vw]" />
    <img src="./assets/dashboardnaam.svg" alt="logo" class="relative mr-[28vw] h-[3vw]" />
    <SelectRoot v-model="afdeling">
      <SelectTrigger
        class="inline-flex min-w-[10vw] min-h-[5vh] items-center justify-between rounded px-[15px] text-[13px] leading-none h-[35px] gap-[5px] bg-white text-grass11 shadow-[0_2px_10px] shadow-black/10 hover:bg-mauve3 focus:shadow-[0_0_0_2px] focus:shadow-black data-[placeholder]:text-green9 outline-none"
        aria-label="Customise options"
      >
        <SelectValue placeholder="Afdeling" />
        <Icon icon="radix-icons:chevron-down" class="h-3.5 w-3.5" />
      </SelectTrigger>

      <SelectPortal>
        <SelectContent
          class="min-w-[10vw] min-h-[5vh] bg-white rounded shadow-[0px_10px_38px_-10px_rgba(22,_23,_24,_0.35),_0px_10px_20px_-15px_rgba(22,_23,_24,_0.2)] will-change-[opacity,transform] data-[side=top]:animate-slideDownAndFade data-[side=right]:animate-slideLeftAndFade data-[side=bottom]:animate-slideUpAndFade data-[side=left]:animate-slideRightAndFade z-[100]"
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
  <section class="md:flex xl:h-[78vh] overflow-hidden">
    <div class="m-3 md:w-4/5 flex-initial bg-gray-200 p-2">
      <h1>{{ afdeling }}</h1>
    </div>
    <aside class="md:w-[21vw] m-3 flex-initial bg-gray-200 p-2 overflow-x-hidden">
      <table class="table-fixed">
        <thead class="fixed pb-5">
          <tr>
            <th class="mr-2 ml-2 pr-1 pl-2">Status</th>
            <th class="w-4/5 pl-2">Location</th>
            <th class="mr-10 ml-2 pr-6 pl-2">Drug</th>
          </tr>
        </thead>
      </table>
      <div class="fixed 4xl:top-40 md:top-32 h-[72vh] w-[20vw] overflow-auto">
        <div v-for="infusion in currentInfusions" :key="infusion.id  + Math.random()">
          <InfusionButtons
            :id="infusion.id"
            :status="infusion.status"
            :ward="infusion.ward"
            :bed="infusion.bed"
            :drug="infusion.drug"
          />
        </div>
      </div>
    </aside>
  </section>
  <section class="md:flex bg-gray-100 overflow-hidden">
    <div class="mr-5 mb-3 ml-5 h-[10vh] md:w-[90vw] flex-initial rounded-[3vw] bg-gray-200">
      <div
        id="infuusDetails"
        class="m-5 h-[10vh] md:w-[88vw] flex-initial overflow-hidden rounded-[2vw] bg-gray-200 p-5 font-[Open_Sans] text-2xl text-ellipsis md:overflow-auto [&::-webkit-scrollbar]:[width:10px] [&::-webkit-scrollbar]:rounded-full [&::-webkit-scrollbar-thumb]:bg-gray-400"
      >
        <RouterView />
      </div>
    </div>
    <div class="mr-5 mb-3 h-[11vh] md:w-[15vw] flex-initial rounded-[3vw] bg-gray-200">
      <button
        type="button"
        class="mb-1font-[Open_Sans] m-5 h-[8vh] md:w-[8vw] flex-initial cursor-pointer place-content-center overflow-hidden rounded-[5vw] bg-sky-300 p-5 text-center text-[4vh] hover:bg-sky-400 active:bg-sky-600 active:text-white"
      >
        Report
      </button>
    </div>
  </section>
</template>

<style scoped></style>
