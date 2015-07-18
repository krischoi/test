try:
	data = open('sketchds.txt')

	for each_line in data:
		try:
			(role, words) = each_line.split(':', 1)
			print(role)
			print(words)
		except ValueError:
			pass
	data.close();fasdsdfsdfsfsfaasfssfsd

except IOError:
	print("no data file")