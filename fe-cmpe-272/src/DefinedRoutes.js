import { BrowserRouter, Route, Routes } from "react-router-dom";
import Homepage from "./components/Homepage";
import Login from "./components/Login";
import LandingPage from "./components/LandingPage";
import Func1 from "./components/Func1";

export default function DefinedRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        {/* <Route path="/login" element={<Login />} /> */}
        <Route path="/landingpage" element={<LandingPage />} />
        <Route path="/func1" element={<Func1 />} />
      </Routes>
    </BrowserRouter>
  );
}
