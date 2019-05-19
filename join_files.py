import json
import os

def join_batches():
    data = []

    for (dirpath, dirnames, filenames) in os.walk('./files/'):
        for filename in filenames:
            if filename.startswith('vehicles_'):
                with open(dirpath + filename, 'r') as file_input:
                    file_data = json.load(file_input)

                    data += file_data

    with open('./files/output.json', 'w') as output:
        json.dump(data, output, indent=4)