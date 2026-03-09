import { motion } from "framer-motion"
import { useQuery } from "@tanstack/react-query"
import {
  Sparkles,
  TrendingUp,
  Target,
  Calendar,
  Heart,
  Zap
} from "lucide-react"

import Navbar from "../../components/layout/navbar"
import LoadingSpinner from "../../components/ui/loadingspinner"
import ArogyaCoach from "../../components/arogyacoach"
import CharityImpactCard from "../../components/charityimpactcard"
import BackgroundImage from "../../components/layout/backgroundimage"

import { userApi } from "../../services/api"
import { useAuthStore } from "../../stores/authstore"

function Dashboard() {

  const { data, isLoading } = useQuery({
    queryKey: ["dashboard"],
    queryFn: async () => {
      const res = await userApi.getDashboard()
      return res.data
    }
  })

  const user = useAuthStore((state) => state.user)

  if (isLoading) return <LoadingSpinner />

  return (
    <BackgroundImage>
      <h1>Welcome {user?.full_name}</h1>

      <Navbar />

      <div className="p-8">

        <motion.h1
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-3xl font-bold mb-8"
        >
          Your Fitness Dashboard
        </motion.h1>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

          {/* Calories */}
          <motion.div
            whileHover={{ scale: 1.05 }}
            className="bg-white shadow-lg rounded-xl p-6"
          >
            <Zap className="text-blue-500 mb-3" />

            <h2 className="text-lg font-semibold">
              Calories Burned
            </h2>

            <p className="text-3xl font-bold">
              {data?.calories_today}
            </p>
          </motion.div>


          {/* Workout Streak */}
          <motion.div
            whileHover={{ scale: 1.05 }}
            className="bg-white shadow-lg rounded-xl p-6"
          >
            <TrendingUp className="text-green-500 mb-3" />

            <h2 className="text-lg font-semibold">
              Workout Streak
            </h2>

            <p className="text-3xl font-bold">
              {data?.workout_streak} days
            </p>
          </motion.div>


          {/* Sessions */}
          <motion.div
            whileHover={{ scale: 1.05 }}
            className="bg-white shadow-lg rounded-xl p-6"
          >
            <Calendar className="text-purple-500 mb-3" />

            <h2 className="text-lg font-semibold">
              Upcoming Sessions
            </h2>

            <p className="text-3xl font-bold">
              {data?.sessions}
            </p>
          </motion.div>

        </div>


        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">

          <CharityImpactCard amount={data?.charity_impact} />

        </div>

      </div>

    </BackgroundImage>
  )
}

export default Dashboard