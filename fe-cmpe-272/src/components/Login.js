import React from "react";
import axios from "axios";
import { GITHUB_LOGIN_URL } from "../settings";

function Login() {
  axios
    .get(GITHUB_LOGIN_URL, { "Content-Type": "application/json;charset=UTF-8" })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.log(error);
    });
  return <div>something</div>;
}

export default Login;
