export default function cleanSet(set, startString) {
  let returnString = '';
  if ((startString === '') || (typeof startString !== 'string') || (!startString)) {
    return returnString;
  }
  for (const element of set) {
    if (element.startsWith(startString)) {
      if (returnString === '') {
        returnString += element.slice(startString.length);
      } else {
        returnString += '-';
        returnString += element.slice(startString.length);
      }
    }
  }
  return returnString;
}
