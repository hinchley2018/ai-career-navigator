import { Link } from "react-router-dom";

const HeroSection = () => {
    return (
      <>
        {/* Hero Section */}
        <div
          className="hero-section w-full h-screen bg-gray-100 flex items-center justify-center"
          aria-label="Career navigator hero section"
        >
          <div className="hero-content flex flex-col items-center text-center px-4">
            {/* Heading */}
            <h1 className="text-4xl md:text-6xl font-bold mb-4">
              Career Navigator
            </h1>
            
            {/* Paragraph */}
            <p className="text-lg md:text-2xl mb-8">
              Find your path to success with our personalized career guidance tools and resources.
            </p>
  
            {/* Buttons */}
            <div className="flex space-x-4">
              <button className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded">
                Learn More
              </button>
              <Link to='interview'>
              <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Get Started
              </button>
              </Link>
            </div>
          </div>
        </div>
      </>
    );
  };
  
  export default HeroSection;
  