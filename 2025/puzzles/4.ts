import { readDataset } from "../helpers/read-dataset";
import { tester } from "../helpers/tester";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ✅
//Part 2: ✅

let testing: Boolean = false;
const testOneAnswer: number = 13;
const testTwoAnswer: number = 43;

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
let dataset: Array<Array<string>> = [];

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

let updateCoords: Array<[number, number]> = [];

export default function solve(): string {
  structureData();

  let dataset_duplicate: Array<Array<string>> = [...dataset];
  let continueChecking: boolean = true;
  let iteration: number = 1;

  while (continueChecking === true) {
    if (updateCoords) {
      updateCoords.forEach((update) => {
        if (
          dataset_duplicate[update[0]] &&
          dataset_duplicate[update[0]][update[1]]
        ) {
          dataset_duplicate[update[0]][update[1]] = ".";
        }
      });

      updateCoords = [];
    }

    continueChecking = loop(dataset_duplicate, iteration);
    iteration++;
  }

  return `✅ 1: ${partOneAnswer} | ✅ 2: ${partTwoAnswer}`;
}

function loop(dataset: Array<Array<string>>, iteration: number): boolean {
  let didRemove: boolean = false;

  dataset?.forEach((row: Array<string>, y: number) => {
    row.forEach((column: string, x: number) => {
      let updateRequired: boolean = false;
      if (column === "@") updateRequired = checkMap(x, y, iteration);

      if (updateRequired) {
        updateCoords.push([y, x]);
        didRemove = true;
      }
    });
  });

  return didRemove;
}

function checkMap(x: number, y: number, iteration: number): boolean {
  let hits: number = 0;

  const checkCoords: Array<[number, number]> = [
    [y - 1, x],
    [y - 1, x - 1],
    [y - 1, x + 1],
    [y, x - 1],
    [y, x + 1],
    [y + 1, x],
    [y + 1, x - 1],
    [y + 1, x + 1],
  ];

  checkCoords.forEach((coord) => {
    if (dataset[coord[0]] && dataset[coord[0]][coord[1]]) {
      if (dataset[coord[0]][coord[1]] === "@") hits++;
    }
  });

  if (hits < 4) {
    if (iteration === 1) partOneAnswer++;
    partTwoAnswer++;
    return true;
  } else {
    return false;
  }
}

function structureData(): void {
  if (testing) rawData = testData;

  rawData?.forEach((datapoint, i) => {
    dataset[i] = datapoint.split("").map((line) => line.trim());
  });
}

export function test(): string {
  testing = true;
  solve();
  return tester(testOneAnswer, testTwoAnswer, partOneAnswer, partTwoAnswer);
}
