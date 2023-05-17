export default function createInt8TypedArray(length, position, value) {
  if ((position < 0) || (position >= length)) {
    throw new Error('Position outside range');
  }
  const buffy = new ArrayBuffer(length);
  const llCoolView = new Int8Array(buffy);
  llCoolView[position] = value;
  return buffy;
}
