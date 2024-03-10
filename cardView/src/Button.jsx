// import './index.css';

function Button({ backgroundColor, imageUrl }) {

  return (
    <div className="button-container">
      <div className="card-view">
        <div className="rectangleOne">
        <div className="nested-rectangle-one">
            </div>
            <div className="regBack">
              <div className="regFront">
              <span className="Regtext">Register</span>
              </div>
          </div>
        </div>
        <div className="rectangleSecond">
          <div className="nested-rectangle">
            <span className="text">GenScript</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Button;
