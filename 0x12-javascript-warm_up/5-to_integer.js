#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a nnumber');
} else {
  console.log('My nnumber:', parseInt(process.argv[2]));
}
