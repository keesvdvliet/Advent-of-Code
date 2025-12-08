import { readDataset } from "../helpers/read-dataset";
import { tester } from "../helpers/tester";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ..
//Part 2: ..

let testing: Boolean = false;
const testOneAnswer: number = 0;
const testTwoAnswer: number = 0;

const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);

let dataSeparator: string = "\n";
let rawData: Array<string> = await readDataset(puzzleNo, dataSeparator);
const testData: Array<string> = await readDataset(
  `${puzzleNo}T`,
  dataSeparator
);
let dataset: Array<any> = [];

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  /* GOOD LUCK :) */

  return `✅ 1: ${partOneAnswer} | ✅ 2: ${partTwoAnswer}`;
}

function structureData(): void {
  if (testing) rawData = testData;

  rawData?.forEach((datapoint, i) => {
    dataset[i] = datapoint; //Do something with your data
  });
}

export function test(): string {
  testing = true;
  solve();
  return tester(testOneAnswer, testTwoAnswer, partOneAnswer, partTwoAnswer);
}
