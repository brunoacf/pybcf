
import string
import random

###########################################
# Load a file into a list
###########################################
def f2list (filename):
	L = []
	try:
		f = open (filename, "r")
		while True:
			line = f.readline()
			# if eof
			if (line == ''):
				break
			# Strips spaces, newlines, tabs
			line = line.strip()
			# Ignore empty lines 'blanked' by the previous strip() function.
			if (line==''):	# this second 'if' check is necessary.
				continue
			# Ignore comments (#)
			if (line[0]=='#'):
				continue
			L.append(line)
		f.close()
	except IOError:
		raise Exception ('f2list(): Error loading file: %s'%(filename))
	except:
		raise Exception ('f2list(): falha inesperada')
	return L

#########################################
# Removes duplicated itens from a list
#########################################
def remove_dups(L):
	U = []
	for item in L:
		if item not in U:
			U.append(item)
	return U


