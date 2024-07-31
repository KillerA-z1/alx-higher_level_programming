#!/usr/bin/node

const request = require('request');

const [apiUrl] = process.argv.slice(2);

function countUserTasksCompleted () { // Added space before function parentheses
  request(apiUrl, (error, response, body) => {
    if (error) {
      return console.error(error);
    }
    const users = JSON.parse(body);
    const taskCountByUserId = {};

    for (const user of users) {
      if (user.completed) {
        if (taskCountByUserId[user.userId] === undefined) {
          taskCountByUserId[user.userId] = 1;
        } else {
          taskCountByUserId[user.userId] += 1;
        }
      }
    }
    console.log(taskCountByUserId);
  });
}

countUserTasksCompleted();
