export function tester(
  checkOne: number,
  checkTwo: number,
  inputOne: number,
  inputTwo: number
) {
  let testOneStatus: string = "";
  let testTwoStatus: string = "";

  console.log(`Answer 1: ${inputOne} | Correct 1: ${checkOne}`);
  console.log(`Answer 2: ${inputTwo} | Correct 2: ${checkTwo}`);

  testOneStatus =
    inputOne === checkOne ? "✅ Test 1 succeeded" : "⚠️ Test 1 failed";
  testTwoStatus =
    inputOne === checkOne ? "✅ Test 2 succeeded" : "⚠️ Test 2 failed";

  return `${testOneStatus} | ${testTwoStatus}`;
}
