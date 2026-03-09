import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import Navbar from "../../components/layout/navbar"
import { workoutApi } from "../../services/api"

const WorkoutPlans: React.FC = () => {

  const navigate = useNavigate()

  const [plan, setPlan] = useState<any[]>([])

  useEffect(() => {

    const fetchPlan = async () => {

      const res = await workoutApi.getWorkoutPlan()

      setPlan(res.data.plan)

    }

    fetchPlan()

  }, [])

  if (!plan.length) return <p className="p-8">Loading workout plan...</p>

  return (

    <div>

      <Navbar />

      <div className="p-8">

        <h1 className="text-2xl font-bold mb-6">
          7 Day Workout Plan
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {plan.map((exercise:any, index:number) => (

            <div
              key={index}
              className="bg-white shadow p-6 rounded-lg"
            >

              <h2 className="font-semibold text-lg">
                {exercise.name}
              </h2>

              <p>Sets: {exercise.sets}</p>

              <p>Reps: {exercise.reps}</p>

              <button
                onClick={() =>
                  navigate("/exercise", {
                    state: { exercise }
                  })
                }
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
              >
                Start Exercise
              </button>

            </div>

          ))}

        </div>

      </div>

    </div>

  )

}

export default WorkoutPlans