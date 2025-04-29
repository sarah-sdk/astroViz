import { Link } from "react-router-dom";
import planet from "../../assets/planet.svg";
import "./Navbar.css";

export default function Navbar() {
  return (
    <header className="p-4 h-full w-[30vw] flex flex-col border border-astro-border rounded-l-lg text-astro-primary">
      <div className="flex justify-center gap-2">
        <img src={planet} alt="" />
        <h1 className="font-bold inline-block text">AstroViz</h1>
      </div>

      <nav className="flex flex-col">
        <Link to="/">Accueil</Link>
        <Link to="/planets">Planètes</Link>
        <Link to="/data">Données</Link>
        <Link to="/settings">Paramètres</Link>
      </nav>
    </header>
  );
}
