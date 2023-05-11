export default function appendToEachArrayValue(array, appendString) {
  const llCoolArray = [];
  for (const llCoolValue of array) {
    const newVal = `${appendString}${llCoolValue}`;
    llCoolArray.push(newVal);
  }

  return llCoolArray;
}
