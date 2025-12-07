const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("❌ No puzzle number provided (example: npm run solve -- 1)");
  process.exit(1);
}

const puzzleNumber = args[0];
const filePath = `../puzzles/${puzzleNumber}.ts`;

async function run() {
  try {
    const module = await import(filePath);
    const solve = module.default;

    if (typeof solve !== "function") {
      throw new Error(`⚠️ No export function found`);
    }

    const result = await solve();
    console.log("➡️ ", result);
  } catch (err) {
    console.error("❌ Error ", err);
  }
}

run();
