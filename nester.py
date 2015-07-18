def print_lol(the_list, is_tab = False, level=0) :
	for each_element in the_list:
		if isinstance(each_element, list):
			print_lol(each_element, is_tab,level+1)
		else:
			if is_tab:
				print("\t"*level, end="")
			print(each_element)
