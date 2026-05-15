const express = require('express');
const app = express(

console.log(if (!process.env.API_KEY) {
  throw new Error("API_KEY missing");
});

app.get('/', (req, res) => {
  res.send('CI/CD Demo Running');
});

app.listen(3000, () => {
  console.log('Server started');
});