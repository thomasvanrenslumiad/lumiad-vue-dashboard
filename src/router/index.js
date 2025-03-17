import { createRouter, createWebHistory } from 'vue-router'
import Infusiondetails from '@/components/Infusiondetails.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/infusion/:infusionId',
      name: 'Infusion-details',
      component: Infusiondetails,
    },
  ],
})

export default router
