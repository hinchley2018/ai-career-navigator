import React, { useState } from "react";
import { FaHeart } from "react-icons/fa";

const WishList = () => {
  const [isWishlist, setIsWishlist] = useState(false);

  const handleWishlist = () => {
    setIsWishlist(!isWishlist);
  };

  return (
    <div className="rounded overflow-hidden shadow-lg bg-white p-6 w-full lg:w-1/2">
      <img
        className="w-full h-48 object-cover"
        src="https://via.placeholder.com/150"
        alt="Product"
      />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">Product Name</div>
        <p className="text-gray-700 text-base">Product description goes here.</p>
      </div>
      <div className="px-6 py-4 flex justify-end">
        <button onClick={handleWishlist}>
          <FaHeart
            size={24}
            className={`${
              isWishlist ? "text-red-500" : "text-gray-400"
            } cursor-pointer`}
          />
        </button>
      </div>
    </div>
  );
};

export default WishList;
