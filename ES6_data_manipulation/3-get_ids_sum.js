export default function getStudentIdsSum(list) {
  const idSum = list.reduce(
    (accumulator, currentObject) => accumulator + currentObject.id, 0,
  );
  return idSum;
}
