import { Route, Routes } from "react-router-dom"
 
import LandingPage from "./pages/landing-page"
import InterviewPreparation from "./pages/interview-prep"



function App(){

  return (
    <>
    <Routes>
      <Route path="/" element={<LandingPage/>} />
      <Route path="/interview" element={<InterviewPreparation/>}/>
    </Routes>
    
    </>
  )
}
export default App