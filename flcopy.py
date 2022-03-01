# Fixed lenght copy
def flcopy (s, fl, pad=' '):
	s2=''
	for i in range (fl):
		try:
			s2 += s[i]
		except IndexError:
			s2 += pad
	return s2


