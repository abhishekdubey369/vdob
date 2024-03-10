import './index.css'; // Import your CSS file for additional styles

function Button({ backgroundColor, imageUrl }) {
  return (
    <div className="button-container">
      <div className="card-view bg-gradient-to-r from-blue-500 to-transparent bg-cover bg-center relative w-164 h-70 rounded-lg shadow-md border-2 border-black">
        <div className="rectangleOne absolute w-80 h-43.588 top-10 left-82 bg-red-600 rounded-md">
          <div className="nested-rectangle-one w-80 h-43.588 bg-blue-500 rounded-md overflow-hidden">
            <div className="regBack w-28.5 h-10.8 absolute top-[-12px] left-[40px] bg-cyan-400"></div>
            <div className="regFront w-28.5 h-10.8 absolute top-[-2px] left-4 bg-blue-900"></div>
            <span className="Regtext absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 uppercase text-white font-bold text-xs">Register</span>
          </div>
        </div>
        <div className="rectangleSecond absolute w-58.5 h-30 top-[20px] left-8 bg-indigo-900 rounded-md">
          <div className="nested-rectangle w-58.5 h-19.8 bg-cyan-400 border-2 border-black rounded-md overflow-hidden">
            <span className="text absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 uppercase text-white font-bold text-xs">GenScript</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Button;
