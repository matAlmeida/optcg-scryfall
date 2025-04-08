const { exec } = require('node:child_process');
const list = require('./card-collections')

list.forEach(async collection => {
  exec(`wget https://en.onepiece-cardgame.com/cardlist/\?series\=${collection.series} -O ./assets/collections/${collection.code}.html`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });

  await new Promise(r => setTimeout(r, 5000))
});