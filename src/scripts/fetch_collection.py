import codecs
import json
import sys
from bs4 import BeautifulSoup

filepath = sys.argv[1]
output = sys.argv[2]

html = codecs.open(filepath, 'r')
parsed_html = BeautifulSoup(html, features="html.parser")
cards = parsed_html.body.find_all('dl', attrs={'class':'modalCol'})
print(len(cards))

cards_json = []

for card in cards:
    (code, rarity, card_type) = [info.text for info in card.find('div', attrs={'class':'infoCol'}).find_all('span')]
    card_name = card.find('div', attrs={'class':'cardName'}).text
    card_image_link = card.find('div', attrs={'class':'frontCol'}).find('img').get_attribute_list('data-src')
    card_image_link = [link.replace("../", "") for link in card_image_link]

    # Card Infos
    card_infos = card.find('div', attrs={'class':'backCol'})
    life = None
    cost = None
    if card_type == "LEADER":
        life = card_infos.find('div', attrs={'class':'cost'}).text.replace("Life", "")
    else:
        cost = card_infos.find('div', attrs={'class':'cost'}).text.replace("Cost", "")
        if cost == "-":
            cost = "0"
    attribute = card_infos.find('div', attrs={'class':'attribute'}).find('i').text
    if not attribute:
        attribute = None
    power = card_infos.find('div', attrs={'class':'power'}).text
    if power == "Power-":
        power = None
    else:
        power = str.replace(power, "Power",  "")
    counter = card_infos.find('div', attrs={'class':'counter'}).text
    if counter == "Counter-":
        counter = None
    else:
        counter = str.replace(counter, "Counter",  "")
    color = card_infos.find('div', attrs={'class':'color'}).text
    color = str.replace(color, "Color", "").split("/")
    feature = card_infos.find('div', attrs={'class':'feature'}).text
    feature = str.replace(feature, "Type",  "").split("/")
    text = card_infos.find('div', attrs={'class':'text'}).text
    if text == "Effect-":
        text = None
    else:
        text = text[len("Effect"):]
    trigger = None
    try:
        trigger = card_infos.find('div', attrs={'class':'trigger'}).text[len("Trigger"):]
    except:
        pass
    card_sets = card_infos.find('div', attrs={'class':'getInfo'}).text
    
    card = {
        'code': code,
        'rarity': rarity,
        'card_type': card_type,
        'card_name': card_name,
        'cost': int(cost) if cost else None,
        'life': int(life) if life else None,
        'power': int(power) if power else None,
        'counter': int(counter) if counter else None,
        'color': color,
        'attribute': attribute,
        'feature': feature,
        'card_image_link': card_image_link,
        'text': text,
        'trigger': trigger,
        'card_sets': card_sets,
    }

    print(card)
    cards_json.append(card)

with open(f'./{output}.json', 'w') as file:
    file.write(json.dumps(cards_json))