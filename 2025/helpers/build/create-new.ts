import { promises as fs } from "fs";
import path from "path";

const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("❌ No puzzle number provided (example: npm run create -- 1)");
  process.exit(1);
}

const puzzleName = args[0];

const templatePath = path.resolve("helpers/build/puzzle.template.ts");
const puzzlesDir = path.resolve("puzzles");
const dataDir = path.resolve("data");

const newPuzzlePath = path.join(puzzlesDir, `${puzzleName}.ts`);
const newDataPath = path.join(dataDir, `${puzzleName}.txt`);
const newTestDataPath = path.join(dataDir, `${puzzleName}T.txt`);

async function createPuzzle() {
  try {
    await fs.mkdir(puzzlesDir, { recursive: true });
    await fs.mkdir(dataDir, { recursive: true });

    await fs.copyFile(templatePath, newPuzzlePath);
    console.log(`✅ Created puzzle file`);

    await fs.writeFile(newDataPath, "");
    await fs.writeFile(newTestDataPath, "");
    console.log(`✅ Created data & test data files`);
  } catch (err) {
    console.error("❌ Error ", err);
  }
}

createPuzzle();
