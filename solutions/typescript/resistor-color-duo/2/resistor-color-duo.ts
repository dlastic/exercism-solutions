const COLOR_LIST: string[] = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
];

export function decodedValue(colors: string[]): number {
  return 10 * COLOR_LIST.indexOf(colors[0]) + COLOR_LIST.indexOf(colors[1]);
}
