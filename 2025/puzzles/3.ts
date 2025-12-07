import { readDataset } from "../helpers/read-dataset";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ..
//Part 2: ..

const testing: Boolean = true;
const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);
const rawData: Array<string> = await readDataset(
  testing ? `${puzzleNo}T` : puzzleNo,
  ","
);
let dataset: Array<any> = [];

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  /* GOOD LUCK :) */

  console.log(`Part 1: ${partOneAnswer}`);
  console.log(`Part 2: ${partTwoAnswer}`);
  return "✅";
}

function structureData(): void {
  rawData?.forEach((datapoint, i) => {
    dataset[i] = datapoint; //Do something with your data
  });
}
