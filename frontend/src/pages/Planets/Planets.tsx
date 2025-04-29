import { useEffect, useState } from "react";

export default function Planets() {
  const [planets, setPlanets] = useState([]);

  useEffect(() => {
    const fetchPlanet = async () => {
      const data = await fetch(`${import.meta.env.VITE_API_URL}/planets`);
      console.log(data);
    };

    fetchPlanet();
  }, []);

  return <h1>Pouet</h1>;
}
