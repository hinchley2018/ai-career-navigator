import { FaLinkedin, FaInstagram, FaTwitter, FaYoutube } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className=" text-black py-6 shadow-sm">
      <div className="container mx-auto flex flex-col md:flex-row items-center justify-between px-4">
        <p className="text-center md:text-left mb-4 md:mb-0">
          © {new Date().getFullYear()} Your Company. All rights reserved.
        </p>
        <div className="flex space-x-6">
          <a
            href="https://www.linkedin.com" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="text-black hover:text-blue-500 transition-colors duration-300"
            aria-label="LinkedIn"
          >
            <FaLinkedin size={24} />
          </a>
          <a 
            href="https://www.instagram.com" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="text-black hover:text-pink-500 transition-colors duration-300"
            aria-label="Instagram"
          >
            <FaInstagram size={24} />
          </a>
          <a 
            href="https://www.twitter.com" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="text-black hover:text-blue-400 transition-colors duration-300"
            aria-label="Twitter"
          >
            <FaTwitter size={24} />
          </a>
          <a 
            href="https://www.youtube.com" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="text-black hover:text-red-600 transition-colors duration-300"
            aria-label="YouTube"
          >
            <FaYoutube size={24} />
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
