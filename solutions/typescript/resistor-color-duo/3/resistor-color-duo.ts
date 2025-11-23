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

type Color = keyof typeof COLOR_MAP;

export function decodedValue(colors: Color[]): number {
  return 10 * COLOR_MAP[colors[0]] + COLOR_MAP[colors[1]];
}
