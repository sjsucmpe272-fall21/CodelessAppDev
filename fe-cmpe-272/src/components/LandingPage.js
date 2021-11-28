import React from "react";
import { Link } from "react-router-dom";
import { browserHistory } from "react-router";
import cookie from "react-cookies";
import Cookies from "js-cookie";
import { useCookies } from "react-cookie";

function LandingPage() {
  // function ClearHistory() {
  //   var backlen = history.length;
  //   history.go(-backlen);
  //   window.location.href = loggedOutPageUrl;
  // }
  // function emptyCache() {
  //   if ("caches" in window) {
  //     if ("caches" in window) {
  //       caches.keys().then((names) => {
  //         names.forEach((name) => {
  //           caches.delete(name);
  //         });
  //       });

  //       window.location.reload(true);
  //     }
  //   }
  // }
  const [cookies, setCookie] = useCookies();
  return (
    <div>
      Landing Page
      {/* {console.log(Cookies.get("session"))} */}
      {console.log("heree!") + Cookies.session}
      {cookies.session && <p>{Cookies.session}</p>}
      <br />
      <a target="_self" href="http://localhost:5000/logout" target="_self">
        <button
          // onClick={emptyCache}
          // () => window.open("http://localhost:5000/login", "_self")}
          className="btn btn-primary"
        >
          Logout
        </button>
      </a>
    </div>
  );
}

export default LandingPage;
