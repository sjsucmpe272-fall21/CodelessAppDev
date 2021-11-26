import React from "react";
import { Link } from "react-router-dom";

function LandingPage() {
  return (
    <div>
      Landing Page
      <a target="_self" href="http://localhost:5000/logout" target="_self">
        <button
          onClick={() => window.open("http://localhost:5000/login", "_self")}
          className="btn btn-primary"
        >
          Logout
        </button>
      </a>
    </div>
  );
}

export default LandingPage;
