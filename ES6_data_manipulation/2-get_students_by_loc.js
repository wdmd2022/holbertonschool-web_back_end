export default function getStudentsByLocation(list, city) {
  const arr = list.filter((obj) => (obj.location === city));
  return arr;
}
