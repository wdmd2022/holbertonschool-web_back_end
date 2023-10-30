// reads a csv file asynchronously

const fs = require('fs').promises;

async function countStudents(csvPath) {
  let content;
  try {
    content = await fs.readFile(csvPath, 'utf-8');
  } catch (error) {
    if (error.code === 'ENOENT') {
      throw new Error('Cannot load the database');
    }
  }
  const arrayOfLines = content.split('\n').filter(Boolean); // clever bool
  arrayOfLines.shift(); // we remove the header lines
  let studentCount = 0;
  const studentCountByField = {};
  const studentNamesByField = {};
  arrayOfLines.forEach((line) => {
    const [firstName, , , field] = line.split(',');
    if (!studentCountByField[field]) {
      studentCountByField[field] = 0;
      studentNamesByField[field] = [];
    } // this is for if we haven't seen the field yet
    studentCountByField[field] += 1;
    studentNamesByField[field].push(firstName);
    studentCount += 1;
  });
  console.log(`Number of students: ${studentCount}`);
  for (const [field, count] of Object.entries(studentCountByField)) {
    console.log(
      `Number of students in ${field}: ${count}. List: ${studentNamesByField[field].join(', ')}`,
    );
  }
}
module.exports = countStudents;
