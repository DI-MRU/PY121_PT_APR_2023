let x = 10;
let y = 20;
console.warn(x + y);

let greeting = "Hello Naiza, Dhivyesh, Safidy, Melanie";
console.log(greeting);
// Create a webserver on port 3000

// Import the http module

const http = require("http");

// Create a server object

const server = http.createServer((req, res) => {
  res.write(`<style>`);
  res.write(`h1 {color: blue;text-align: center;}`);
  res.write(`</style>`);
  res.write("<h1>Extra NodeJS Example</h1>");
  res.write(`<div>${greeting}</div>`);
  res.end();
});

// Listen on port 3000

server.listen(3000, () => {
  console.log("Server is listening on port 3000");
});
