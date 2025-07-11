const { exec } = require('node:child_process');
const list = require('./card-collections')

list.forEach(async collection => {
  exec(`python3 ./src/scripts/fetch_collection.py ./assets/collections/${collection.code}.html ./assets/parsed/${collection.code}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
});