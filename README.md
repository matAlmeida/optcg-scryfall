## [WIP] OPTCG-SCRYFALL

### Dependencies

`Python3.x` or greater<br/>
`Node20.x` or greater

### Parsing new collections

#### Starting virtual env

```sh
$ python3 -m venv .
$ source ./bin/activate
$ python3 -m pip install -r requirements.txt
```

#### Adding new collections

`Note: the script will only work in collection that already appears in the OPTCG English site (https://en.onepiece-cardgame.com)`

Go to the file `card-collections.js` and add a new object in the list with the following pattern:

```json
{
  "series": "569202",
  "code": "eb02"
}
```

##### Code
In the `code` field add the code of the collection you want to add.

##### Series
In the `series` field you need to specify the correct coleection serie (It will be used to download the cards information).

If you notice each kind of collection has the same starting numbers:

| Collection | Series |
|------------|--------|
|STx         |`5690xx`|
|OPx         |`5691xx`|
|EBx         |`5692xx`|
|PRBx        |`5693xx`|

#### Download the collections

Run the following command

```sh
$ npm run download
```

#### Parse the collections

Run the following command

```sh
$ npm run parse
```

#### Merge the collections into a single file

Run the following command

```sh
$ npm run merge
```

After that the new collection will be available as a new file in `assets/parsed` as well inside the `assets/merged-cards.json`

### Card object sctucture

|Field              |Type                 |Description                                                                                            |Example|
|-------------------|---------------------|-------------------------------------------------------------------------------------------------------|---------|
|`code`             |`string`             |Unique code of the card (Can appear more then once if has AltArt)                                      |`"EB01-001"`
|`rarity`           |`string`             |Rarity of the card                                                                                     |`"L"`
|`card_type`        |`string`             |Type of the card                                                                                       |`"LEADER"`
|`card_name`        |`string`             |Card name                                                                                              |`"Kouzuki Oden"`
|`cost`             |`number` `nullable`  |Cost to play the card (If isn't a Leader)                                                              |`null` if Leader, `5` if "EB01-002 Izo"
|`life`             |`number` `nullable`  |Life of the card (If is a Leader)                                                                      |`null` if non Leader, `4` if "EB01-001 Kouzuki Oden"
|`power`            |`number` `nullable`  |Power of the card (Events and Stages does not has power)                                               |`5000`
|`counter`          |`number` `nullable`  |Counter of the card                                                                                    |`1000` 
|`color`            |`string[]`           |Colors of the card (Leader can be multicolor)                                                          |`["Red","Green"]`
|`attribute`        |`string` `nullable`  |Attribute of the card (Events does not has attribute)                                                  |`"Slash"` or `"Slash/Special"` if multiple attribute
|`feature`          |`string[]`           |Types of the card                                                                                      |`["Land of Wano","Kouzuki Clan"]`
|`card_image_link`  |`string[]`           |List with the card image link (Need concatenate with `https://en.onepiece-cardgame.com/` at the start) |`["images/cardlist/card/EB01-001.png?250701"]`
|`text`             |`string` `nullable`  |Effects and Abilities of the card                                                                      |`"All of your {Land of Wano} type Character cards without a Counter have a +1000 Counter, according to the rules.[DON!! x1] [When Attacking] If you have a {Land of Wano} type Character with a cost of 5 or more, this Leader gains +1000 power until the start of your next turn."`
|`trigger`          |`string` `nullable`  |Trigger text of the card                                                                               |`"[Trigger] K.O. up to 1 of your opponent's Characters with 5000 base power or less."`
|`card_sets`        |`string`             |The full name of the collection                                                                        |`"Card Set(s)-Memorial Collection- [EB-01]"`

### TODO

- [ ] Merge all cards with same `code` into a single object with `card_image_link` link containing all the images
- [ ] Convert the `fetch_collection.py` to Node script to remove Python dependency
