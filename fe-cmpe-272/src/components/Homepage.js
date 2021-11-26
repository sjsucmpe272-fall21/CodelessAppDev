import React from "react";
import { Link } from "react-router-dom";

function Homepage() {
  function go_to_login() {
    console.log("going to the login page");
  }
  return (
    <div>
      {/* <Link to="www.google.https://www.google.com/?client=safari"> */}
      <button
        onClick={() => window.open("http://localhost:5000/login", "_self")}
        className="btn btn-primary"
      >
        Login Using Github
      </button>
      {/* </Link> */}
      <br />
      {/* <Link to="www.google.https://www.google.com/"> */}
      <a target="_self" href="www.google.com" target="_self">
        <button className="btn btn-primary">Login Using Github button 2</button>
      </a>
      {/* </Link> */}
    </div>
  );
}

export default Homepage;
