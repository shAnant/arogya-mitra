import { useEffect, useState } from "react"
import Navbar from "../../components/layout/navbar"

const ProgressTracking: React.FC = () => {

  const [stats, setStats] = useState({
    workouts: 12,
    calories: 3500,
    weightLost: 2
  })

  return (

    <div>

      <Navbar />

      <div className="p-8">

        <h1 className="text-2xl font-bold mb-6">
          Progress Tracking
        </h1>

        <div className="grid grid-cols-3 gap-6">

          <div className="bg-white shadow p-6 rounded">
            Workouts Completed
            <p className="text-3xl">{stats.workouts}</p>
          </div>

          <div className="bg-white shadow p-6 rounded">
            Calories Burned
            <p className="text-3xl">{stats.calories}</p>
          </div>

          <div className="bg-white shadow p-6 rounded">
            Weight Lost (kg)
            <p className="text-3xl">{stats.weightLost}</p>
          </div>

        </div>

      </div>

    </div>

  )

}

export default ProgressTracking