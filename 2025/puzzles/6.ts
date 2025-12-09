import { readDataset } from "../helpers/read-dataset";
import { tester } from "../helpers/tester";
import { fileURLToPath } from "url";
import { basename } from "path";
import { normalize, normalizeSwap } from "../helpers/functions";

/* Status */
//Part 1: ✅
//Part 2: ..

let testing: Boolean = false;
const testOneAnswer: number = 4277556;
const testTwoAnswer: number = 3263827;

const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);

let dataSeparator: string = "\n";
let rawData = (await readDataset(puzzleNo, dataSeparator)) as string[];
const testData = (await readDataset(`${puzzleNo}T`, dataSeparator)) as string[];

let dataset: Array<Array<number>> = [];
let operators: Array<string> = [];

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  console.log(`Number: ${dataset}`);
  console.log(`Operator: ${operators}`);

  operators?.forEach((operator, i) => {
    let calculation: string = ``;

    dataset?.forEach((line) => {
      calculation =
        calculation != ""
          ? `${calculation} ${operator} ${line[i]}`
          : `${line[i]}`;
    });

    const answer = eval(calculation);

    console.log(`Calculation: ${calculation} = ${answer}`);

    partOneAnswer += Number(answer);
  });

  return `✅ 1: ${partOneAnswer} | ✅ 2: ${partTwoAnswer}`;
}

function structureData(): void {
  if (testing) rawData = testData;

  const dataLines: number = rawData.length - 1;

  for (let i = 0; i < dataLines; i++) {
    dataset[i] = normalize(rawData[i])
      .split(" ")
      .map((line) => Number(line.trim()));
  }

  operators = normalize(rawData[dataLines])
    .split(" ")
    .map((line) => line.trim());
}

export function test(): string {
  testing = true;
  solve();
  return tester(testOneAnswer, testTwoAnswer, partOneAnswer, partTwoAnswer);
}
