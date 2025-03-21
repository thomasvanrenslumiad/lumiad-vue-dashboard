import { createRouter, createWebHistory } from 'vue-router'
// import InfusionDetails from '@/components/InfusionDetails.vue'
import InfusionDetailsComposition from '@/components/infusionDetailsComposition.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/infusion/:infusionId',
      name: 'Infusion-details',
      component: InfusionDetailsComposition,
    },
  ],
})

export default router
