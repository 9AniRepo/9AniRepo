import urllib.request

# get html and format
req = urllib.request.Request('https://github.com/Paperback-iOS/app/releases/latest')
plain = urllib.request.urlopen(req)
decoded = plain.read().decode("utf-8")

# split and parse html for link
split = decoded.split('\"')
ipaUrl = ''
for i in split:
    if 'ipa' in i:  # get first link
        ipaUrl = i
        break

# get ipa name
name = ''
for i in ipaUrl.split('/'):
    if 'ipa' in i:
        name = i

# create shell script to install ipa
with open('installer.sh', 'w') as f:
	f.write('echo \'Downloading App Archive\'\n')
	f.write('wget -q --no-check-certificate --content-disposition https://github.com%s\n' % ipaUrl)	# downloads nightly zip
	f.write('echo \'Download Complete\'\n')
	f.write('appinst %s\n' % name) # install ipa via appsync using appinst
