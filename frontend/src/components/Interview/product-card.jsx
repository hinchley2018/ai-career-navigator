import React from "react";

const InfoCard = () => {
  return (
    <div className="rounded overflow-hidden shadow-lg bg-white p-6  h-96 w-full lg:w-1/2">
      <h2 className="text-2xl font-bold mb-2">Product Name</h2>
      <span className="inline-block bg-green-100 text-green-700 text-xs font-semibold px-3 py-1 rounded-full mb-4">
        In Stock
      </span>
      <div className="text-3xl font-bold text-gray-900 mb-6">$50</div>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Buy Now
      </button>
    </div>
  );
};

export default InfoCard;
