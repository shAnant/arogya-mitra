import { BrowserRouter, Routes, Route } from "react-router-dom"
import React, {useState} from "react"

import Dashboard from "./pages/dashboard/dashboard"
import WorkoutPlans from "./pages/workouts/workoutplan"
import ExercisePlayer from "./pages/workouts/exerciseplayer"
import NutritionPlans from "./pages/nutrition/nutritionplans"
import HealthAssessment from "./pages/health/healthassessment"
import ProgressTracking from "./pages/progress/progresstracking"
import ArogyaCoach from "./components/arogyacoach"

function App() {
  const [coachOpen, setCoachOpen] = useState(false)
  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Dashboard />} />

        <Route path="/workouts" element={<WorkoutPlans />} />

        <Route path="/exercise" element={<ExercisePlayer />} />

        <Route path="/nutrition" element={<NutritionPlans />} />

        <Route path="/health-assessment" element={<HealthAssessment />} />

        <Route path="/progress" element={<ProgressTracking />} />

      </Routes>
      <ArogyaCoach
        isOpen={coachOpen}
        onClose={() => setCoachOpen(false)}
      />
      <button
        onClick={() => setCoachOpen(true)}
        className="fixed bottom-6 right-6 bg-blue-600 text-white p-4 rounded-full shadow-lg"
      >
        AROMI
      </button>
    </BrowserRouter>

  )

}

export default App