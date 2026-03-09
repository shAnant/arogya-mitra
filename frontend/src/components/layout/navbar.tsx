import {Link} from "react-router-dom"
import { useAuthStore } from "../../stores/authstore"

function Navbar() {
  const logout = useAuthStore((state) => state.logout)
  return (
    <div className="w-full bg-white shadow-md p-4 flex justify-between items-center">

      <h1 className="text-xl font-bold text-blue-600">
        ArogyaMitra
      </h1>

      <div className="flex gap-4">

        <button className="bg-blue-500 text-white px-4 py-2 rounded">
          Dashboard
        </button>

        <button className="bg-gray-200 px-4 py-2 rounded">
          Logout
        </button>

      </div>

      <div className="bg-white shadow p-4 flex gap-6">

      <Link to="/">Dashboard</Link>

      <Link to="/workouts">Workouts</Link>

      <Link to="/nutrition">Nutrition</Link>

      <Link to="/health-assessment">Health</Link>

      <Link to="/progress">Progress</Link>
      <button onClick={logout}>
        Logout
      </button>
    </div>

    </div>
  )
}

export default Navbar