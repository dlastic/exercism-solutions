const planetToEarthYears = {
  mercury: 0.2408467,
  venus: 0.61519726,
  earth: 1.0,
  mars: 1.8808158,
  jupiter: 11.862615,
  saturn: 29.447498,
  uranus: 84.016846,
  neptune: 164.79132,
};

type Planet = keyof typeof planetToEarthYears;

const SECONDS_PER_EARTH_YEAR = 365.25 * 24 * 60 * 60;

export const age = (planet: Planet, seconds: number): number =>
  Math.round(
    (seconds / planetToEarthYears[planet] / SECONDS_PER_EARTH_YEAR) * 100
  ) / 100;
