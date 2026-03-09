import { useEffect, useState } from "react"
import Navbar from "../../components/layout/navbar"

const NutritionPlans: React.FC = () => {

  const [plan, setPlan] = useState<any[]>([])

  useEffect(() => {

    setPlan([
      { day: "Monday", meal: "Oatmeal + Fruits", calories: 450 },
      { day: "Tuesday", meal: "Grilled Chicken Salad", calories: 500 },
      { day: "Wednesday", meal: "Vegetable Stir Fry", calories: 420 }
    ])

  }, [])

  return (

    <div>

      <Navbar />

      <div className="p-8">

        <h1 className="text-2xl font-bold mb-6">
          Nutrition Plan
        </h1>

        {plan.map((meal, index) => (

          <div
            key={index}
            className="bg-white shadow p-6 rounded-lg mb-4"
          >

            <h2 className="font-semibold">
              {meal.day}
            </h2>

            <p>{meal.meal}</p>

            <p>{meal.calories} kcal</p>

          </div>

        ))}

      </div>

    </div>

  )

}

export default NutritionPlans