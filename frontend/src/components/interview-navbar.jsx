// src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import { FaSignInAlt, FaUserPlus } from 'react-icons/fa'; // Icons for SignIn and Register

const Navbar = () => {
  return (
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
          <div className="hidden md:flex space-x-6">
            <Link to="/pricing" className="text-gray-600 hover:text-gray-900">
              Pricing
            </Link>
            <Link
              to="/solutions"
              className="text-gray-600 hover:text-gray-900"
            >
              Solutions
            </Link>
            <Link
              to="/community"
              className="text-gray-600 hover:text-gray-900"
            >
              Community
            </Link>
            <Link
              to="/resources"
              className="text-gray-600 hover:text-gray-900"
            >
              Resources
            </Link>
            <Link to="/contact" className="text-gray-600 hover:text-gray-900">
              Contact
            </Link>

            {/* SignIn and Register Buttons */}
            <div className="flex space-x-4">
              <Link
                to="/signin"
                className="flex items-center bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
              >
                <FaSignInAlt className="mr-2" /> Sign In
              </Link>
              <Link
                to="/register"
                className="flex items-center bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              >
                <FaUserPlus className="mr-2" /> Register
              </Link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
