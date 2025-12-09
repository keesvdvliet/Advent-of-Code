export function modulo(a: number, b: number): number {
  return ((a % b) + b) % b;
}

export function normalize(input: string): string {
  return input.replace(/\s+/g, " ").trim();
}

export function normalizeSwap(input: string, filler: string): string {
  return input.replace(
    / {2,}/g,
    (spaces) => `${filler}`.repeat(spaces.length - 1) + " "
  );
}
