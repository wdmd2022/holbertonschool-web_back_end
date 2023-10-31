// creates a more complex server using the http module

const http = require('http');

const coolDataBase = process.argv[2];
const hostname = '127.0.0.1';
const port = 1245;
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
  let returnString = "";
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

const server = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      res.statusCode = 200;
      const coolStudents = await countStudents(coolDataBase);
      res.end(`This is the list of our students\n${coolStudents}`);
    } catch (error) {
      res.statusCode = 200;
      res.end(`This is the list of our students\n${error.message}`);
    }
  }
});

const app = server.listen(port, hostname);

module.exports = app;
