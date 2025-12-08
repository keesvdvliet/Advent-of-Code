const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("❌ No puzzle number provided (example: npm run solve -- 1)");
  process.exit(1);
}

const puzzleNumber = args[0];
const runMode = args[1] || "default";
const filePath = `../../puzzles/${puzzleNumber}.ts`;

async function run() {
  try {
    const module = await import(filePath);
    let fn: any;

    if (runMode === "default") {
      fn = module.default;
    } else {
      fn = module[runMode];
    }

    if (typeof fn !== "function") {
      throw new Error(`❌ Error`);
    }

    const result = await fn();
    console.log("➡️ ", result);
  } catch (err) {
    console.error("❌ Error ", err);
  }
}

run();
