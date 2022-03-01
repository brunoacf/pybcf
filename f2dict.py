
import string
import random

###########################################
# Load a file into a Dictionary
###########################################
def f2dict (filename):
	D = dict()
	lnum=0
	try:
		f = open (filename, "r")
		while True:
			line = f.readline()
			# if eof
			if (line == ''):
				break
			# Strips spaces, newlines, tabs
			line = line.strip()
			# Ignores comments (#) and empty lines 'blanked' by the previous strip() function.
			#if (re.search ('^#', line)) or (line == ''):
			if (line[0]=='#') or (line == ''):
				continue
			lnum+=1
			D[lnum]=line
		f.close()
	except IOError:
		raise Exception ('f2list(): Error loading file: %s'%(filename))
	except:
		raise Exception ('f2list(): falha inesperada')
	return D

#########################################
# Removes duplicated itens from a list
#########################################
#def remove_dups(D):
#	U = []
#	for item in D:
#		if item not in U:
#			U.append(item)
#	return U


