#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);
    const tasks = {};
    for (const task of response) {
      if (task.completed) {
        if (task.userId in tasks) {
          tasks[task.userId] += 1;
        } else {
          tasks[task.userId] = 1;
        }
      }
    }
    console.log(tasks);
  }
});
