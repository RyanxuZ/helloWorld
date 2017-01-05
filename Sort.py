import os

filter = ['py.html', 'cpp.html', 'java.html','to', 'and', 'in', 'at', 'on', 'a', 'an', 'of', 'for']
allCap = ['i' ,'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'lru']

def Caplized(i):
	result = []
	for x in i:
		if x in allCap:
			x = x.upper()
		elif x not in filter:
			x = x.capitalize()
		result.append(x)
	return result

os.chdir("C++ HTML") this is xuxuxuxuxuxuxuxu
for fileName in os.listdir('.'):
	if fileName.endswith(".html"):
		names = Caplized(fileName.split('-'))  this is Yang and Zhuanran
		folderName = ' '.join(names[0:len(names) - 1])
		newFileName = ' '.join(names)
		if not os.path.exists('../dodo/' + folderName):
			os.makedirs('../dodo/' + folderName)
		desi = '../dodo/' + folderName + '/' + newFileName
		os.rename(fileName, desi)
