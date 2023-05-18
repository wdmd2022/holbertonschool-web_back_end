export default function cleanSet(set, startString) {
  let returnString = '';
  const sliceIndex = startString.length;
  set.forEach((stringElement) => {
    if (stringElement.startsWith(startString)) {
      if (returnString = '') {
        returnString = returnString + stringElement.slice(sliceIndex);
      } else {
        returnString = returnString + '-' + stringElement.slice(sliceIndex);
      }
    }
  })
  return returnString;
}
