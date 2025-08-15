## [WIP] OPTCG-SCRYFALL

### Requirements

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
