# for reading file system
import os

# read each line, split, filter, and write to output file also add to list of currentSources
def addSource(listPath, currentSources):
    with open(listPath, 'r') as repoList:
        for line in repoList:
            line = line.split(' ')
            for url in line:
                if '://' in url:
                    url = url.strip()
                    if url[-1]!= '/':
                        url = url + '/'
                    if url not in currentSources and 'thebigboss' not in url:  # get rid of trash and bootstrap sources
                        currentSources.append(url)
        return currentSources

# empty array to store current sources
currentSources = []

# read all source lists from apt sources dir
for path in os.listdir('/etc/apt/sources.list.d/'):
    currentSources = addSource('/etc/apt/sources.list.d/%s' % path, currentSources)

# save missing sources to apt source dir
with open('/var/mobile/Documents/JBTransfer/JBTsources.list', 'r') as jbtsource:

    # determine path to write sources
    if os.path.exists('/etc/apt/sources.list.d/sileo.sources'):  # sileo
        with open('/etc/apt/sources.list.d/sileo.sources', 'a') as finalSources:
            for line in jbtsource:
                line = line.strip()
                if line not in currentSources:
                    finalSources.write('Types: deb\n')
                    finalSources.write('URIs: %s\n' % line)
                    finalSources.write("Suites: ./\n")
                    finalSources.write("Components:\n\n")

    else:   # cydia
        with open('/etc/apt/sources.list.d/cydia.list', 'a') as finalSources:
            for line in jbtsource:
                line = line.strip()
                if line not in currentSources:
                    finalSources.write('deb %s ./\n' % line)
