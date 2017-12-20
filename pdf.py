#! /usr/bin/python3

import requests, sys
fileName = 'newFile.pdf'
# Error check for an argument using if-else
if len(sys.argv)>1:

	if len(sys.argv) == 2:

		url  = sys.argv[1]

	elif len(sys.argv) >= 3:

		url = sys.argv[1]
		fileName = sys.argv[2]

else:
	print('Error: Please enter URL of PDF to download')
	sys.exit()

pdf = requests.get(url)

pdf.raise_for_status()

newFile = open(fileName, 'wb')

newFile.write(pdf.content)

newFile.close()
print('\n')
if len(sys.argv) == 2:
	print('File downloaded as newFile.pdf.')
	print('Change file name before running PDF again')
else:
	print('File downloaded as %s' % fileName)
