import { readDataset } from "../helpers/read-dataset";
import { fileURLToPath } from "url";
import { basename } from "path";
import { modulo } from "../helpers/functions";

/* Status */
//Part 1: ✅
//Part 2: ..

const testing: Boolean = true;
const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);
const rawData: Array<string> = await readDataset(
  testing ? `${puzzleNo}T` : puzzleNo,
  "\n"
);
let dataset: Array<number> = [];

const dialStart: number = 50;
const dialMax: number = 100;
let dialCurrent: number = dialStart;

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  dataset?.forEach((delta) => {
    const cycles = countCycles(dialCurrent, delta);
    partTwoAnswer += cycles;

    dialCurrent = modulo(dialCurrent, dialMax);

    console.log(`${delta} : ${cycles}`);

    if (dialCurrent === 0) partOneAnswer++;
  });

  console.log(`Part 1: ${partOneAnswer}`);
  console.log(`Part 2: ${partTwoAnswer}`);
  return "✅";
}

function structureData(): void {
  rawData?.forEach((datapoint, i) => {
    dataset[i] = Number(
      datapoint.startsWith("R") ? datapoint.slice(1) : `-${datapoint.slice(1)}`
    );
  });
}

function countCycles(start: number, delta: number): number {
  dialCurrent += delta;

  //TODO: Fix edge case errors....
  const end = modulo(dialCurrent, dialMax);
  let cycles = Math.floor(Math.abs(delta) / dialMax);
  if (delta > 0 && end < start) cycles += 1;
  if (delta < 0 && end > start) cycles += 1;
  if (end === 0 && Math.abs(delta) < dialMax) cycles += 1;

  cycles = cycles >= 0 ? cycles : cycles * -1;

  return cycles;
}
