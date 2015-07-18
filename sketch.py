try:
	data = open('sketchds.txt')

	for each_line in data:
		try:
			(role, words) = each_line.split(':', 1)
			print(role)
			print(words)
		except:
			pass

	data.close()
except:
	print("no data file")