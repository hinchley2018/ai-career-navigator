
import { Link } from "react-router-dom"



function Navbar(){

    return (
        <>
          <nav className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo on the left */}
          <div className="flex-shrink-0">
            <Link to="/">
               Logo
            </Link>
          </div>
          {/* Menu items on the right */}
          <div className="hidden md:flex space-x-8">
            <Link to="/pricing" className="text-gray-600 hover:text-gray-900">Pricing</Link>
            <Link to="/solutions" className="text-gray-600 hover:text-gray-900">Solutions</Link>
            <Link to="/contact" className="text-gray-600 hover:text-gray-900">Contact</Link>
            <Link to="/get-started" className="text-blue-600 hover:text-blue-800 font-medium">Get Started</Link>
          </div>
        </div>
      </div>
    </nav>
        
        </>
    )
}
export default Navbar