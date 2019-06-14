import location


def main():
	coordinates = location.get_location()
	fullAddress = location.reverse_geocode(coordinates)
	
	street = fullAddress[0]['Street']
	zip = fullAddress[0]['ZIP']
	city = fullAddress[0]['City']
	state = fullAddress[0]['State']
	
	address = 'Your location is' + ' ' + street + ' ' + ' ' + zip + ' ' + city + ' ' + state
	
	
	return address
	
	
	
	
if __name__=='__main__':
	main()
