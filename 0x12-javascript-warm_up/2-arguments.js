#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('No Arguments');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
