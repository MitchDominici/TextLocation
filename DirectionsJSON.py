import json
import objectpath

with open("https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyDzw5cBZKsSp7dABBYcvggSct9hOhtv6kY") as datafile:    data = json.load(datafile)

jsonnn_tree = objectpath.Tree(data['steps'])  

result_tuple = tuple(jsonnn_tree.execute('$..html_instructions'))

println(result_tuple)