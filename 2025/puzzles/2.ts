import { readDataset } from "../helpers/read-dataset";
import { tester } from "../helpers/tester";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ✅
//Part 2: ✅

let testing: Boolean = false;
const testOneAnswer: number = 1227775554;
const testTwoAnswer: number = 4174379265;

const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);

let dataSeparator: string = ",";
let rawData = (await readDataset(puzzleNo, dataSeparator)) as string[];
const testData = (await readDataset(`${puzzleNo}T`, dataSeparator)) as string[];
let dataset: Array<Array<number>> = [];

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  dataset?.forEach((range) => {
    console.log(range);

    for (let index = range[0]; index <= range[1]; index++) {
      console.log(
        `${index} | 1: ${checkRepeat(1, index)} | 2: ${checkRepeat(2, index)}`
      );

      if (checkRepeat(1, index)) partOneAnswer += index;
      if (checkRepeat(2, index)) partTwoAnswer += index;
    }
  });

  return `✅ 1: ${partOneAnswer} | ✅ 2: ${partTwoAnswer}`;
}

function structureData(): void {
  if (testing) rawData = testData;

  rawData?.forEach((datapoint, i) => {
    dataset[i] = datapoint.split("-").map((line) => Number(line.trim()));
  });
}

function checkRepeat(pattern: number, input: string | number): boolean {
  const regex = pattern === 1 ? /^(\d+)\1$/ : /^(\d+)\1+$/;
  const str = input as string;
  return regex.test(str);
}

export function test(): string {
  testing = true;
  solve();
  return tester(testOneAnswer, testTwoAnswer, partOneAnswer, partTwoAnswer);
}
