import { create } from "zustand"
import { persist } from "zustand/middleware"
import { authApi } from "../services/api"

interface User {
  id: number
  username: string
  email: string
  full_name: string
  role: "user" | "admin"
  is_active: boolean
  fitness_level?: string
  fitness_goal?: string
  workout_preference?: string
  diet_preference?: string
  streak_points: number
  total_workouts: number
  charity_donations: number
  phone?: string
  age?: number
  height?: number
  weight?: number
  gender?: string
  bio?: string
  profile_photo_url?: string
}

interface AuthState {
  user: User | null
  token: string | null
  loading: boolean

  login: (email: string, password: string) => Promise<void>
  logout: () => void
  setUser: (user: User) => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({

      user: null,
      token: null,
      loading: false,

      login: async (email: string, password: string) => {

        set({ loading: true })

        try {

          const res = await authApi.login({
            email,
            password
          })

          set({
            user: res.data.user,
            token: res.data.access_token,
            loading: false
          })

        } catch (error) {

          set({ loading: false })
          throw error

        }

      },

      logout: () => {

        set({
          user: null,
          token: null
        })

      },

      setUser: (user: User) => set({ user })

    }),
    {
      name: "arogyamitra-auth"
    }
  )
)