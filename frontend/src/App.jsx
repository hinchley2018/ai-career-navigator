import { Route, Routes } from "react-router-dom"
 
import LandingPage from "./pages/landing-page"
import InterviewPrepPage from "./pages/interview-prep"

function App(){

  return (
    <>
    <Routes>
      <Route path="/" element={<LandingPage/>} />
      <Route path="/interview-prep" element={<InterviewPrepPage/>} />
    </Routes>
    
    </>
  )
}
export default App