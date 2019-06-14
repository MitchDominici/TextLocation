import json
import requests
from html.parser import HTMLParser
"""
json_string = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyDzw5cBZKsSp7dABBYcvggSct9hOhtv6kY"

parsed_json = json.loads(json_string)
print(parsed_json['steps'])

"""
response = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyDzw5cBZKsSp7dABBYcvggSct9hOhtv6kY")
data = response.json()

print (data["routes"][0]["legs"][0]['steps']['html_instructions'])

class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        print(data)
        
parser = MyHTMLParser()
parser.feed(data["routes"][0]["legs"][0]["steps"][0]["html_instructions"])

#print(data["routes"][0]["legs"][0]["steps"][0]["html_instructions"])