const dnaToRnaMap: Record<string, string> = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
} as const;

export function toRna(dna: string): string {
  let rna = "";
  for (const base of dna) {
    const mapped = dnaToRnaMap[base];
    if (!mapped) {
      throw new Error("Invalid input DNA.");
    }
    rna += mapped;
  }
  return rna;
}
