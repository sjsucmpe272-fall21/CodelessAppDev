import React from "react";
import { Link } from "react-router-dom";

function Homepage() {
  function go_to_login() {
    console.log("going to the login page");
  }
  return (
    <div>
      <Link to="/login">
        <button onClick={go_to_login} className="btn btn-primary">
          Login Using Github
        </button>
      </Link>
    </div>
  );
}

export default Homepage;
