import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

class PunkIPA:
    def __init__(self):
        self.url = os.getenv('punk_url')

    def merge_json_files(beerfiles):
        merged_beer_file = list()
        for f in beerfiles:
            with open(f, 'r') as input_beer_files:
                merged_beer_file.extend(json.load(input_beer_files))
            with open('punkbeers.json', 'w') as output_beer_file:
                json.dump(merged_beer_file, output_beer_file)

    def punk_request(self):
        beerfiles = [] # Build a list of files due to api limitations
        result = requests.get(self.url+'page=1')
        request_page = 1 # Set the request page on API
        per_page = 79 # Set max number of beers to return
        while result.text != "[]" : # We will keep sending requests for as long as the API is not returning this string
            result = requests.get(self.url+'page='+str(request_page)+'&per_page='+str(per_page))
            request_page += 1 # Keep adding pages as we go
            beerfile = 'punkbeers'+str(request_page)+'.json'
            with open(beerfile, 'w') as beeerfile:
                beer = result.json()
                json.dump(beer, beeerfile)
            beerfiles.append(beeerfile.name) # Appends the list of files created per request
        PunkIPA.merge_json_files(beerfiles) # Merge the JSON files to one file
        for file in beerfiles:
                os.remove(file) # Remove the merged files as they are no longer needed
        


if __name__ == '__main__':
    punk = PunkIPA()
    punk.punk_request()