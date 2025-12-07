import { promises as fs } from "fs";
import path from "path";

export async function readDataset(
  puzzleNo: string | number,
  sep: string
): Promise<string[]> {
  const filePath: string = `./data/${puzzleNo}.txt`;
  const absolutePath = path.resolve(filePath);

  const rawData = await fs.readFile(absolutePath, "utf-8");

  return rawData
    .split(sep)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}
