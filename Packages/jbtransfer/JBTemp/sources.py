# for reading file system
import os

# output file path
savePath = '/JBTemp/JBTsources.list'
archivePath = '/var/mobile/Documents/JBTransfer/JBTsources.list'

# read each line, split, filter, and write to output file also add to list of currentSources
def addSource(listPath, currentSources):
    with open(listPath, 'r') as repoList:
        with open(savePath, 'a') as output:
            with open(archivePath, 'a') as archive:
                for line in repoList:
                    line = line.split(' ')
                    for url in line:
                        if '://' in url:
                            url = url.strip()
                            if url[-1]!= '/':
                                url = url + '/'
                            if 'bigboss' not in url and 'zodttd' not in url and 'bingner' not in url and 'modmyi' not in url and 'procurs' not in url and 'theodyssey' not in url and url not in currentSources:  # get rid of trash and bootstrap sources
                                output.write('deb %s ./\n' % url)
                                archive.write(url + '\n')
                                currentSources.append(url)
                return currentSources

# empty array to store current sources
currentSources = []

# read all source lists from apt sources dir
for path in os.listdir('/etc/apt/sources.list.d/'):
    currentSources = addSource('/etc/apt/sources.list.d/%s' % path, currentSources)

# check and read source from zebra and installer
zebraPath = '/var/mobile/Library/Application Support/xyz.willy.Zebra/sources.list'
installerPath = '/var/mobile/Library/Application Support/Installer/APT/sources.list'
if os.path.exists(zebraPath):  # zebra
    currentSources = addSource(zebraPath, currentSources)
if os.path.exists(installerPath):  # installer
    currentSources = addSource(installerPath, currentSources)
