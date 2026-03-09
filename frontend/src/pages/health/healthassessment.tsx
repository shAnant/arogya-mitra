import { useState } from "react"
import Navbar from "../../components/layout/navbar"

const HealthAssessment: React.FC = () => {

  const [form, setForm] = useState({
    age: "",
    weight: "",
    height: "",
    goal: ""
  })

  const handleSubmit = (e:any) => {

    e.preventDefault()

    console.log("Health Data:", form)

    alert("Assessment Submitted!")

  }

  return (

    <div>

      <Navbar />

      <div className="p-8 max-w-lg">

        <h1 className="text-2xl font-bold mb-6">
          Health Assessment
        </h1>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">

          <input
            placeholder="Age"
            className="border p-2"
            onChange={(e)=>setForm({...form,age:e.target.value})}
          />

          <input
            placeholder="Weight"
            className="border p-2"
            onChange={(e)=>setForm({...form,weight:e.target.value})}
          />

          <input
            placeholder="Height"
            className="border p-2"
            onChange={(e)=>setForm({...form,height:e.target.value})}
          />

          <input
            placeholder="Fitness Goal"
            className="border p-2"
            onChange={(e)=>setForm({...form,goal:e.target.value})}
          />

          <button className="bg-green-500 text-white p-2 rounded">
            Submit
          </button>

        </form>

      </div>

    </div>

  )

}

export default HealthAssessment