import { BrowserRouter, Route, Routes } from "react-router-dom";
import Homepage from "./components/Homepage";
import Login from "./components/Login";
import LandingPage from "./components/LandingPage";

export default function DefinedRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/landingpage" element={<LandingPage />} />
      </Routes>
    </BrowserRouter>
  );
}
