import { useEffect, useState } from "react";

type Planet = {
  name: string;
  distance_from_sun: number;
  diameter: number;
  orbital_period: number;
};

export default function Planets() {
  const [planets, setPlanets] = useState<Planet[] | null>(null);

  useEffect(() => {
    const fetchPlanet = async () => {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/planets/`);
      const data = await response.json();

      setPlanets(data);
    };

    fetchPlanet();
  }, []);

  if (!planets) return <div>Chargement...</div>;

  return (
    <section>
      <h1 className="font-bold text-xl">Planètes du système solaire</h1>
      <ul className="grid grid-cols-3 gap-2">
        {planets.map((planet) => (
          <article
            key={planet.name}
            className="border border-astro-border rounded-lg p-2"
          >
            <h2 className="font-bold text-lg">{planet.name}</h2>
            <h3 className="text-sm">Distance du soleil</h3>
            <p>{planet.distance_from_sun} millions de km</p>
            <h3 className="text-sm">Diamètre</h3>
            <p>{planet.diameter} km</p>
            <h3 className="text-sm">Période orbitale</h3>
            <p>{planet.orbital_period} jours</p>
          </article>
        ))}
      </ul>
    </section>
  );
}
