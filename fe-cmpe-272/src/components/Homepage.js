import React from "react";
import { Link } from "react-router-dom";

function Homepage() {
  return (
    <div>
      <button
        onClick={() => window.open("http://localhost:5000/login", "_self")}
        className="btn btn-primary"
      >
        Login Using Github
      </button>
    </div>
  );
}

export default Homepage;
