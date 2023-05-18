export default function hasValuesFromArray(set, array) {
  const gottem = array.every((item) => set.has(item));
  return gottem;
}
