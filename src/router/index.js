import { createRouter, createWebHistory } from 'vue-router'
import InfusionDetails from '@/components/InfusionDetails.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/infusion/:infusionId',
      name: 'Infusion-details',
      component: InfusionDetails,
    },
  ],
})

export default router
