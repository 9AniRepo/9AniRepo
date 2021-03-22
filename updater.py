import urllib.request
from html.parser import HTMLParser

# nightly url -> html -> string
webUrl  = urllib.request.urlopen('https://nightly.link/SuperMarcus/NineAnimator/workflows/nightly/master')	# url to html
html = webUrl.read().decode("utf-8")	# html to string

# html parser
class Parser(HTMLParser):
	# method to append the data between the tags to the list all_data.
	def handle_data(self, data):
		global all_data
		all_data.append(data)
all_data = []
# creating an instance of our class.
parser = Parser()
# providing the input.
parser.feed(html)

# filter the parsed html
list1 = ['iOS']	# filter
list2 = all_data	# input for filter

filtered = [n for n in list2 if	# the actual filtering
			any(m in n for m in list1)]
name = filtered[0]	# name of file
url = filtered[1]	# dl link for the file

# create shell script to install NineAnimator
with open('installer.sh', 'w') as f:	# create shell script and sets f to write mode
	f.write('echo \'downloading app archive\'\n')
	f.write('wget -q --no-check-certificate --content-disposition %s\n' % url)	# downloads nightly zip
	f.write('echo \'download complete\'\n')
	f.write('echo \'unzipping archive\'\n')
	f.write('unzip -q %s.zip\n' % name)	# unzip which outpus the ipa
	f.write('echo \'unzip complete\'\n')
	f.write('echo \'rename zip to ipa\'\n')
	f.write('mv %s.ipa app.zip\n' % name) # rename ipa
	f.write('echo \'unziping app\'\n')
	f.write('unzip -q app.zip\n')	# unzip which outputs the Payload
	f.write('echo \'unzipping complete\'\n')
	f.write('echo \'resigning app with ldid\'\n')
	f.write('ldid Payload/*.app\n') # run ldid on the Payload and .app folder
	f.write('echo \'resign complete\'\n')
	f.write('echo \'rezipping app into ipa\'\n')
	f.write('zip -qr output.ipa Payload\n') # rezip the Payload folder into ipa
	f.write('echo \'rezip complete\'\n')
	f.write('appinst output.ipa\n') # install ipa via appsync using appinst
