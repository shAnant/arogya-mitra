interface Props {
  amount: number
}

function CharityImpactCard({ amount }: Props) {

  return (

    <div className="bg-white shadow-lg rounded-xl p-6">

      <h2 className="text-lg font-bold mb-2">
        ❤️ Charity Impact
      </h2>

      <p className="text-3xl font-bold text-green-500">
        ${amount}
      </p>

      <p className="text-gray-500">
        donated through workouts
      </p>

    </div>

  )

}

export default CharityImpactCard