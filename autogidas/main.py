import json

from link_parser import parse_ad_links
from vehicle_parser import parse_vehicle

def do_links_exist():
    # TODO change this to check the directory if the links are ready
    return True

BASE_URL = 'https://autogidas.lt'

with open('./output/urls.json', 'r') as urls:
    urls = json.load(urls)
    vehicles = []
    current = 0
    batch_current = 0
    batch_size = 100
    batch = 0

    for url in urls:
        current += 1
        batch_current += 1

        print(f'Scraping {current}/{len(urls)} at: {BASE_URL}{url}')

        vehicle = parse_vehicle(BASE_URL + url)
        
        if vehicle is not None:
            vehicles.append(vehicle)

        if batch_current == batch_size:
            with open(f'./output/vehicles_{batch}.json', 'w') as batch_file:
                print(f'writing out batch {batch}')

                json.dump(vehicles, batch_file, indent=4)

                batch_current = 0
                batch += 1
                vehicles = []

    with open('./output/vehicles.json', 'w') as output_file:
        json.dump(vehicles, output_file, indent=4)

# with open('./output/urls.json', 'w') as output_file:
#         json.dump(names, output_file, indent=4)