import { reactive } from 'vue'

export const store = reactive({
  department: String,
  ward: String,
  bed: String,
  drug: String,
  status: String,
  totalMl: Number,
  remainingMl: Number,
  mlPerHour: Number,
  timeRunning: String,
  timeRemaining: String,
  id: String,
  softwareVersion: String,
  medicalLibraryVersion: String,
})
