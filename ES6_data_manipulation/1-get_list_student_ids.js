export default function getListStudentIds(list) {
  let arr = [];
  if (Array.isArray(list)) {
    arr = list.map((obj) => obj.id);
  }
  return arr;
}
