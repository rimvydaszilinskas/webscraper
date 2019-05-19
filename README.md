# webscaper

webscraper for autogidas.lt car ads.

## How to run:

First parse all the URLS to the seperate ads using file ```link_parser.py```, then run ```main.py``` to parse all the ads in batches of 100 to the output. Then run ```join_files.py``` get a single ```vehicles.json``` file to work with.