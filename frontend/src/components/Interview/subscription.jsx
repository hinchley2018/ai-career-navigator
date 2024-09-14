import { useState } from "react"



function Subscribe() {
    const[mail,setEmail] = useState(false)
    const handleSubmit = (e) => {
        e.preventDefault();
        
        if (mail) {
          alert(`Subscribed with email: ${mail}`);
          setEmail("");  // Clears the input after submission
        } else {
          alert("Please enter a valid email address");
        }
      };
    return (
        <>
        <div className="hero-section w-full h-screen bg-grau-100 items-center flex justify-center" >
             <div className="hero-content flex flex-col items-center text-center px-4  " >
                 <h1 className="text-4xl md:text-2xl font-bold mb-4 " >
                         Follow the Latest Trends
                 </h1>
                 <h2 className="font-semibold text-gray-500" > With Our daily NewsLetter </h2>
                  <form onSubmit={handleSubmit} >
                  <input
                  className=" mt-5 apperance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none  "
                  type="email"
                  placeholder="Enter your email"
                  value={mail}
                  onChange={(e)=> setEmail(e.target.value)}
                  required 
                  />
                  <button
            className=" mt-4 flex-shrink-0 bg-black hover:bg-blue-700  hover:border-blue-700 text-sm  text-white py-2 px-2 rounded"
            type="submit"
          >
            Subscribe
          </button>
                  </form>
             </div>

        </div>
        </>
    )
}
export default Subscribe