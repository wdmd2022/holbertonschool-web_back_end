// creates a small Express server

const fs = require('fs').promises;
const express = require('express');

const port = 1245;
const database = process.argv[2];
const app = express();

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
  let returnString = '';
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
  returnString = returnString.concat(`Number of students: ${studentCount}\n`);
  for (const [field, count] of Object.entries(studentCountByField)) {
    returnString = returnString.concat(
      `Number of students in ${field}: ${count}. List: ${studentNamesByField[field].join(', ')}\n`,
    );
  }
  return returnString;
}

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const studentData = await countStudents(database);
    res.status(200).send(`This is the list of our students\n${studentData}`);
  } catch (error) {
    res.status(500).send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(port);

module.exports = app;
