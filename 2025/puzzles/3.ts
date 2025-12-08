import { readDataset } from "../helpers/read-dataset";
import { tester } from "../helpers/tester";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ✅
//Part 2: ✅

let testing: Boolean = false;
const testOneAnswer: number = 357;
const testTwoAnswer: number = 3121910778619;

const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);

let dataSeparator: string = "\n";
let rawData = (await readDataset(puzzleNo, dataSeparator)) as string[];
const testData = (await readDataset(`${puzzleNo}T`, dataSeparator)) as string[];
let dataset: Array<Array<number>> = [];

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  dataset.forEach((batteries) => {
    const batteryOne: number = Number(createBattery(batteries, 2));
    const batteryTwo: number = Number(createBattery(batteries, 12));

    console.log(`Bat1: ${batteryOne} | Bat2: ${batteryTwo}`);

    partOneAnswer += batteryOne;
    partTwoAnswer += batteryTwo;
  });

  return `✅ 1: ${partOneAnswer} | ✅ 2: ${partTwoAnswer}`;
}

function structureData(): void {
  if (testing) rawData = testData;

  rawData?.forEach((datapoint, i) => {
    dataset[i] = datapoint.split("").map((line) => Number(line.trim()));
  });
}

function createBattery(input: Array<number>, size: number): string {
  let battery: string = "";
  let batteryBuild: Array<number> = [];
  let batteryBank: Array<number> = [...input];

  let checkFrom: number = 0;
  let partsRemaining: number = size - 1;

  for (let sizeIndex = 0; sizeIndex < size; sizeIndex++) {
    let highest: number = 0;
    let highestIndex: number = 0;
    let loopLength: number = batteryBank.length - partsRemaining;

    for (let checkIndex = checkFrom; checkIndex < loopLength; checkIndex++) {
      if (batteryBank[checkIndex] > highest) {
        highest = batteryBank[checkIndex];
        highestIndex = checkIndex;
      }
    }

    batteryBuild[sizeIndex] = highest;
    checkFrom = highestIndex;
    partsRemaining--;
    batteryBank = batteryBank.filter((_, index) => index !== highestIndex);
  }

  for (let buildIndex = 0; buildIndex < batteryBuild.length; buildIndex++) {
    battery = `${battery}${batteryBuild[buildIndex]}`;
  }

  return battery;
}

export function test(): string {
  testing = true;
  solve();
  return tester(testOneAnswer, testTwoAnswer, partOneAnswer, partTwoAnswer);
}
