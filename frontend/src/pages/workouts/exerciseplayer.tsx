import React, {useEffect, useRef, useState } from "react"
import { motion } from "framer-motion"
import {
  Play,
  Pause,
  X,
  Activity,
  Trophy
} from "lucide-react"

import Navbar from "../../components/layout/navbar"
import { workoutApi } from "../../services/api"
import toast from "react-hot-toast"
import { useLocation, useNavigate } from "react-router-dom"

// const location = useLocation()
// const exercise = location.state?.exercise
const ExercisePlayer: React.FC = () => {

  const location = useLocation()
  const navigate = useNavigate()

  const exercise = location.state?.exercise

  const videoRef = useRef<HTMLVideoElement | null>(null)

  const [playing, setPlaying] = useState(false)
  const [repsLeft, setRepsLeft] = useState(exercise.reps)
  const [setsLeft, setSetsLeft] = useState(exercise.sets)

  const startWorkout = async () => {

    try {

      await workoutApi.startWorkout({
        exercise: exercise.name
      })

      setPlaying(true)

      toast.success("Workout Started")

    } catch {

      toast.error("Error starting workout")

    }

  }

  const pauseWorkout = () => {
    setPlaying(false)
  }

  const completeRep = () => {

    if (repsLeft > 1) {
      setRepsLeft(repsLeft - 1)
    } else {

      if (setsLeft > 1) {

        setSetsLeft(setsLeft - 1)
        setRepsLeft(exercise.reps)

        toast("Next Set!")

      } else {

        toast.success("Workout Completed 🏆")

        workoutApi.completeWorkout({
          exercise: exercise.name
        })

      }

    }

  }

const videoStreamRef = useRef<MediaStream | null>(null)
const videoElementRef = useRef<HTMLVideoElement | null>(null)
const canvasRef = useRef<HTMLCanvasElement | null>(null)

const [cameraActive, setCameraActive] = useState(false)

const [timerStarted, setTimerStarted] = useState(false)

const [timeLeft, setTimeLeft] = useState(30)

const [isMoving, setIsMoving] = useState(false)

const [movementIntensity, setMovementIntensity] = useState(0)

  const startCamera = async () => {
  try {

    const stream = await navigator.mediaDevices.getUserMedia({
      video: true
    })

    videoStreamRef.current = stream

    if (videoElementRef.current) {
      videoElementRef.current.srcObject = stream
    }

    setCameraActive(true)

    toast.success("Camera activated")

  } catch (error) {

    toast.error("Camera access denied")

  }
}

const stopCamera = () => {

  if (videoStreamRef.current) {

    videoStreamRef.current.getTracks().forEach(track => track.stop())

  }

  setCameraActive(false)

}

useEffect(() => {

  let interval: any

  if (timerStarted) {

    interval = setInterval(() => {

      setTimeLeft((prev: number) => {

        if (prev <= 1) {

          clearInterval(interval)

          toast.success("Exercise Completed")

          return 0

        }

        return prev - 1

      })

    }, 1000)

  }

  return () => clearInterval(interval)

}, [timerStarted])

useEffect(() => {

  if (!cameraActive) return

  const interval = setInterval(() => {

    const randomMovement = Math.random()

    if (randomMovement > 0.7) {

      setIsMoving(true)

      setRepsLeft((prev: number) => {

        if (prev > 0) {

          return prev - 1

        }

        return 0

      })

    } else {

      setIsMoving(false)

    }

  }, 1500)

  return () => clearInterval(interval)

}, [cameraActive])

useEffect(() => {
  
  if (repsLeft === 0 && setsLeft > 1) {

    setSetsLeft((prev: number) => prev - 1)

    setRepsLeft(exercise.reps)

    toast("Next Set!")

  }
  
  

  if (repsLeft === 0 && setsLeft === 1) {

    toast.success("Workout Finished!")

    workoutApi.completeWorkout({
      exercise: exercise.name
    })

  }

}, [repsLeft])

if (!exercise) {
  return <p className="p-8">No exercise selected</p>
}
else{

  return (
    
    <div className="min-h-screen bg-gray-100">

    <Navbar />

    <div className="p-8">

      <button
        onClick={() => navigate(-1)}
        className="mb-4 flex items-center gap-2"
        >
        <X /> Close
      </button>


      <motion.h1
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="text-2xl font-bold mb-6"
        >
        {exercise.name}
      </motion.h1>


      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">


        {/* Exercise Video */}
        <div className="bg-white shadow rounded-xl p-4">

          <video
            ref={videoRef}
            controls
            className="w-full rounded"
            src={exercise.video}
            />

        </div>


        {/* Workout Controls */}
        <div className="bg-white shadow rounded-xl p-6">

          <Activity className="mb-4 text-blue-500" />

          <p className="text-lg">
            Sets Left: <strong>{setsLeft}</strong>
          </p>

          <p className="text-lg">
            Reps Left: <strong>{repsLeft}</strong>
          </p>

          {/* TIMER */}
          <p className="text-lg mt-2">
            Timer: <strong>{timeLeft}s</strong>
          </p>


          {/* CAMERA PREVIEW */}
          {cameraActive && (
            <div className="mt-4">
              <video
                ref={videoElementRef}
                autoPlay
                playsInline
                className="rounded w-full border"
                />
            </div>
          )}


          <div className="flex gap-4 mt-6">

            <button
              onClick={startWorkout}
              className="bg-green-500 text-white px-4 py-2 rounded flex items-center gap-2"
              >
              <Play size={18} /> Start
            </button>


            <button
              onClick={pauseWorkout}
              className="bg-yellow-500 text-white px-4 py-2 rounded flex items-center gap-2"
              >
              <Pause size={18} /> Pause
            </button>


            <button
              onClick={completeRep}
              className="bg-blue-500 text-white px-4 py-2 rounded"
              >
              Rep Done
            </button>

          </div>


          {setsLeft === 0 && (
            <div className="mt-6 text-green-600 flex items-center gap-2">

              <Trophy />

              Workout Completed!

            </div>
          )}

        </div>

      </div>

    </div>

  </div>

)

}
}

export default ExercisePlayer