export default function updateUniqueItems(mappyDay) {
  if (!(mappyDay instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [k, v] of mappyDay) {
    if (v === 1) {
      mappyDay.set(k, 100);
    }
  }
  return mappyDay;
}
