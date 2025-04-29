import Navbar from "./components/Navbar/Navbar";
import "./App.css";
import { Outlet } from "react-router-dom";

function App() {
  return (
    <main className="bg-astro-dark p-8 h-screen flex">
      <Navbar />
      <div className="p-4 h-full w-full border border-astro-border rounded-r-lg">
        <Outlet />
      </div>
    </main>
  );
}

export default App;
