import axios from "axios"

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000"
})

export const userApi = {
  getDashboard: () => api.get("/dashboard"),
}

export const authApi = {
  login: (data:any) => api.post("/auth/login", data)
}

export const workoutApi = {

  getWorkoutPlan: () => api.get("/workouts/plan"),

  startWorkout: (data:any) => api.post("/workouts/start", data),

  completeWorkout: (data:any) => api.post("/workouts/complete", data)

}

export const chatApi = {
  sendMessage: (message: string) =>
    api.post("/chat", { message })
}