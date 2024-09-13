import FramerMotionCard from "../components/card-component"
import Footer from "../components/footer"
import Navbar from "../components/navbar"
import HeroSection from "./hero-section"




const LandingPage = () => {

    return (
        <>
        <div className="flex flex-col min-h-screen " >
            <Navbar/>
            <HeroSection/>
            <main className="flex-grow mt-20 " >
                 <FramerMotionCard/>
            </main>
            <Footer/>
        </div>
        </>
    )
}
export default LandingPage