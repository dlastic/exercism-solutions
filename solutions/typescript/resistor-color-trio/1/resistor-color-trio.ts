const COLOR_MAP = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
} as const;

const PREFIXES = [
  [1e9, "giga"],
  [1e6, "mega"],
  [1e3, "kilo"],
] as const;

type Color = keyof typeof COLOR_MAP;

export function decodedResistorValue(colors: Color[]): string {
  const baseValue = 10 * COLOR_MAP[colors[0]] + COLOR_MAP[colors[1]];
  const multiplier = 10 ** COLOR_MAP[colors[2]];
  const resistanceOhms = baseValue * multiplier;

  for (const [factor, prefix] of PREFIXES) {
    if (resistanceOhms >= factor) {
      const value = resistanceOhms / factor;
      return `${value} ${prefix}ohms`;
    }
  }

  return `${resistanceOhms} ohms`;
}
