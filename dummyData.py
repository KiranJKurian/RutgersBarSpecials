data = [{ "name": "Old Queens", "monday": ["$2 LITs", "$4 Yeunglings"] }]
data.append({ 'name': "Knight Club", 'monday': ["$999 shot of vodka"] })

for bar in data:
	print "Name: %s, Monday Specials: %s" % (bar['name'], bar['monday'])
