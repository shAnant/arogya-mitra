import React from "react"

interface ArogyaCoachProps {
  isOpen: boolean
  onClose: () => void
}

const ArogyaCoach: React.FC<ArogyaCoachProps> = ({ isOpen, onClose }) => {

  if (!isOpen) return null

  return (

    <div className="fixed bottom-20 right-6 w-80 bg-white shadow-xl rounded-xl p-6 z-50">

      <div className="flex justify-between items-center mb-3">

        <h2 className="text-lg font-bold">
          🤖 AROMI AI Coach
        </h2>

        <button
          onClick={onClose}
          className="text-red-500 font-bold"
        >
          ✕
        </button>

      </div>

      <p className="text-gray-600">
        Ask AROMI for workout advice or fitness tips.
      </p>

      <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded w-full">
        Chat with AROMI
      </button>

    </div>

  )

}

export default ArogyaCoach