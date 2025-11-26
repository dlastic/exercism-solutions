const dnaToRnaMap: Record<string, string> = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
} as const;

function throwError(): never {
  throw new Error("Invalid input DNA.");
}

export function toRna(dna: string): string {
  return dna
    .split("")
    .map((nucleotide) => dnaToRnaMap[nucleotide] || throwError())
    .join("");
}
