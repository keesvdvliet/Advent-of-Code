import { readDataset } from "../helpers/read-dataset";
import { fileURLToPath } from "url";
import { basename } from "path";

/* Status */
//Part 1: ✅
//Part 2: ✅

const testing: Boolean = false;
const puzzleNo: string = basename(fileURLToPath(import.meta.url)).replace(
  /\.[^/.]+$/,
  ""
);
const rawData: Array<string> = await readDataset(
  testing ? `${puzzleNo}T` : puzzleNo,
  ","
);
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

  console.log(`Part 1: ${partOneAnswer}`);
  console.log(`Part 2: ${partTwoAnswer}`);
  return "✅";
}

function structureData(): void {
  rawData?.forEach((datapoint, i) => {
    dataset[i] = datapoint.split("-").map((line) => Number(line.trim()));
  });
}

function checkRepeat(pattern: number, input: string | number): boolean {
  const regex = pattern === 1 ? /^(\d+)\1$/ : /^(\d+)\1+$/;
  const str = input as string;
  return regex.test(str);
}
