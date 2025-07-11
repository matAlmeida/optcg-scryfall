const fs = require('fs')
const cardsFolder = './assets/parsed'

fs.readdir(cardsFolder, (err, files) => {
  if (err) {
    console.error(err)
    process.exit(1)
  }

  let cards = []
  files.forEach(file => {
    const filecards = JSON.parse(fs.readFileSync(cardsFolder + '/' + file).toString())
    cards = [...cards, ...filecards]
  })

  fs.writeFileSync('./assets/merged-cards.json', JSON.stringify(cards))
})