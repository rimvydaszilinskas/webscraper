from URL_parser import get_url
from bs4 import BeautifulSoup
import json
import re

def parse_vehicle(url):
    raw_html = get_url(url)
    if raw_html is None:
        return None

    html = BeautifulSoup(raw_html, 'html.parser')
    vehicle = {}
    price_str = re.findall(r'\d+', html.select('div.price')[0].getText())
    price = int(''.join(price_str))

    vehicle['price'] = price

    for item in html.select('div.param'):
        param = item.getText().strip()

        param_split = param.split('\n')

        if param_split[0] == 'Markė':
            vehicle['manufacturer'] = param_split[1]
        elif param_split[0] == 'Metai':
            vehicle['year'] = param_split[1]
        elif param_split[0] == 'Modelis':
            vehicle['model'] = param_split[1]
        elif param_split[0] == 'Metai':
            vehicle['year'] = param_split[1]
        elif param_split[0] == 'Variklis':
            vehicle['engine'] = param_split[1]
        elif param_split[0] == 'Kuro tipas':
            vehicle['fuel'] = parse_fuel(param_split[1])
        elif param_split[0] == 'Kėbulo tipas':
            vehicle['body'] = parse_body(param_split[1])
        elif param_split[0] == 'Pavarų dėžė':
            vehicle['gearbox'] = parse_gearbox(param_split[1])
        elif param_split[0] == 'Varomieji ratai':
            vehicle['drivetrain'] = parse_transmission(param_split[1])
        elif param_split[0] == 'Defektai':
            vehicle['defects'] = parse_defects(param_split[1])
        elif param_split[0] == 'Vairo padėtis':
            vehicle['driver_side'] = parse_driver_side(param_split[1])
        elif param_split[0] == 'Durų skaičius':
            vehicle['door_count'] = param_split[1]
        elif param_split[0] == 'Pavarų skaičius':
            vehicle['gear_count'] = param_split[1]
        elif param_split[0] == 'Sėdimų vietų skaičius':
            vehicle['seats'] = param_split[1]
        elif param_split[0] == 'TA iki':
            vehicle['inspection'] = param_split[1]
        elif param_split[0] == 'Pirmosios registracijos šalis':
            vehicle['first_registration_country'] = parse_country(param_split[1])

    vehicle['addons'] = {}

    for item in html.select('div.addon'):
        if item.getText().strip() == 'El. langai':
            vehicle['addons']['electric_windows'] = True
        elif item.getText().strip() == 'Odinis salonas':
            vehicle['addons']['leather_seats']= True
        elif item.getText().strip() == 'Kruizo kontrolė':
            vehicle['addons']['cruise_control'] = True
        elif item.getText().strip() == 'Klimato kontrolė':
            vehicle['addons']['climate_control'] = True
        elif item.getText().strip() == 'Navigacija / GPS':
            vehicle['addons']['gps'] = True
    
    return vehicle

def parse_fuel(fuel):
    if fuel == 'Dyzelinas':
        return 'diesel'
    elif fuel == 'Benzinas':
        return 'petrol'
    elif fuel == 'Benzinas/Dujos':
        return 'petrol/lpg'
    elif fuel == 'Benzinas/Elektra':
        return 'petrol/electricity'
    elif fuel == 'Elektra':
        return 'electricity'
    elif fuel == 'Dyzelinas/Elektra':
        return 'diesel/electricity'
    elif fuel == 'Dujos':
        return 'lpg'
    elif fuel == 'Benzinas/Gamtinės dujos':
        return 'petrol/gas'
    elif fuel == 'Etanolis':
        return 'etanol'
    else:
        return 'other'

def parse_body(body):
    if body == 'Sedanas':
        return 'sedan'
    elif body == 'Hečbekas':
        return 'hatchback'
    elif body == 'Universalas':
        return 'avant'
    elif body == 'Visureigis':
        return 'suv'
    elif body == 'Coupe':
        return 'coupe'
    elif body == 'Kabrioletas':
        return 'cabriolet'
    elif body == 'Pikapas':
        return 'pickup'
    elif body == 'Limuzinas':
        return 'limousine'
    else:
        return 'other'

def parse_gearbox(gearbox):
    if gearbox == 'Automatinė':
        return 'automatic'
    else:
        return 'manual'

def parse_transmission(transmission):
    if transmission == 'Priekiniai varantys ratai':
        return 'FWD'
    elif transmission == 'Galiniai varantys ratai':
        return 'RWD'
    elif transmission == 'Visi varantys ratai':
        return 'AWD'
    else:
        return None

def parse_defects(defects):
    if defects == 'Be defektų':
        return None
    elif defects == 'Daužta':
        return 'Damaged'
    elif defects == 'Degęs':
        return 'Burnt'
    elif defects == 'Pavarų dėžės defektas':
        return 'Gearbox'
    elif defects == 'Variklio defektas':
        return 'Engine'
    else:
        return 'Other'

def parse_driver_side(driver_side):
    if driver_side == 'Kairėje':
        return 'left'
    else:
        return 'right'

def parse_country(country):
    if country == 'Lietuva':
        return 'LT'
    elif country == 'Vokietija':
        return 'D'
    elif country == 'Latvija':
        return 'LV'
    elif country == 'Italija':
        return 'I'
    elif country == 'Prancūzija':
        return 'FR'
    else:
        return None

if __name__ == "__main__":
    url = 'https://autogidas.lt/skelbimas/audi-a6-dyzelinas--2007-m-sedanas-0131754608.html'

    print(parse_vehicle(url))