import { readDataset } from "../helpers/read-dataset";
import { tester } from "../helpers/tester";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ✅
//Part 2: ✅

let testing: Boolean = false;
const testOneAnswer: number = 3;
const testTwoAnswer: number = 14;

const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);

let dataSeparator: string = "\n";
let setSeparator: string = "\n\n";
let rawData = (await readDataset(
  puzzleNo,
  dataSeparator,
  setSeparator
)) as string[][];
const testData = (await readDataset(
  `${puzzleNo}T`,
  dataSeparator,
  setSeparator
)) as string[][];

let ranges: Array<number[]> = [];
let ingredients: Array<number> = [];
let uniqueIngredients = new Set<number>();

let partOneAnswer: number = 0;
let partTwoAnswer: number = 0;

export default function solve(): string {
  structureData();

  const sortedRanges: Array<number[]> = [...ranges].sort((a, b) => a[0] - b[0]);
  let mergedRanges: [number, number][] = [];

  ingredients?.forEach((ingredient) => {
    let isInRange: boolean = false;

    for (const [start, end] of sortedRanges) {
      //Merging ranges for part 2
      if (
        !mergedRanges.length ||
        mergedRanges[mergedRanges.length - 1][1] < start - 1
      ) {
        mergedRanges.push([start, end]);
      } else {
        mergedRanges[mergedRanges.length - 1][1] = Math.max(
          mergedRanges[mergedRanges.length - 1][1],
          end
        );
      }

      //Also checking part 1 here
      if (start <= ingredient && end >= ingredient && !isInRange) {
        partOneAnswer++;
        isInRange = true;
      }
    }

    partTwoAnswer = mergedRanges.reduce(
      (sum, [start, end]) => sum + (end - start + 1),
      0
    );
  });

  return `✅ 1: ${partOneAnswer} | ✅ 2: ${partTwoAnswer}`;
}

function structureData(): void {
  if (testing) rawData = testData;

  rawData[0]?.forEach((datapoint, i) => {
    ranges[i] = datapoint.split("-").map((line) => Number(line.trim()));
  });

  ingredients = rawData[1].map(Number);
}

export function test(): string {
  testing = true;
  solve();
  return tester(testOneAnswer, testTwoAnswer, partOneAnswer, partTwoAnswer);
}
