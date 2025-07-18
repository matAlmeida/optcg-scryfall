const { exec } = require('node:child_process');
const fs = require('fs');
const list = require('./card-collections')
const ASSETS_FOLDER = './assets/collections'

list.forEach(async collection => {
  const fileName = `${ASSETS_FOLDER}/${collection.code}.html`
  if (fs.existsSync(fileName)) {
    return
  }
  exec(`wget https://en.onepiece-cardgame.com/cardlist/\?series\=${collection.series} -O ${fileName}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });

  await new Promise(r => setTimeout(r, 5000))
});