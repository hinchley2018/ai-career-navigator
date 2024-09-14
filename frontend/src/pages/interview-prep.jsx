import Footer from "../components/footer";
import Navbar from "../components/interview-navbar";
import InfoCard from "../components/Interview/product-card";
import Subscribe from "../components/Interview/subscription";
import WishList from "../components/Interview/wishlist-card";

function InterviewPreparation() {
  return (
    <>
      <div className="flex flex-col min-h-screen">
        <Navbar />
        <main className="flex-grow mt-20">
          {/* Use flex to place the cards side by side */}
          <div className="flex flex-col lg:flex-row justify-between items-start lg:space-x-6 p-6">
            <WishList />
            <InfoCard />
             
          </div>
          <Subscribe/>
         
        </main>
        <Footer/>
      </div>
    </>
  );
}

export default InterviewPreparation;
