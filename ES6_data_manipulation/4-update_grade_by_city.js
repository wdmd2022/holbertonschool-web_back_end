export default function updateStudentGradeByCity(list, city, newGrades) {
  return list
    .filter((obj) => obj.location === city)
    .map((obj) => {
      const matchingObject = newGrades.find((item) => item.studentId === obj.id);
      const record = { ...obj };
      record.grade = matchingObject ? matchingObject.grade : 'N/A';
      return record;
    });
}
