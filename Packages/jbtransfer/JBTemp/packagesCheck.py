import os

current = []

# read and write file dirs
with open('/JBTemp/packages.txt', 'r') as packageList:

    # add currently installed packages to a list
    for line in packageList:
        # truncate the version numbers and save package bundleid to file
        line = line.split('/')
        for package in line:
            if '[installed' not in package and 'Listing...' not in package:
                current.append(package)

# generate shell script
with open('/var/mobile/Documents/JBTinstall.sh', 'a') as output:
    output.write('unzip -q /var/mobile/Documents/JBTransfer.zip\n')
    output.write('echo \'Installing packages...(this may take a while)\'\n')
    output.write('echo \'After packages are installed a log will be left behind stating what packages did not get installed as well as the console output for installing the packages. Also the device the will ldrestart after install the packages.\'\n')
    with open('/var/mobile/Documents/JBTransfer/JBTpackages.txt', 'r') as archiveList:
        for line in archiveList:
            # if packages is not installed then add it to script
            line = line.strip()
            if line not in current:
                output.write('apt-get install -y --allow-unauthenticated %s >> /var/mobile/Documents/JBTransfer/JBTemp.log\n' % line)
    # genereate log
    output.write('cd /var/mobile/Documents/JBTransfer/\n')
    output.write('apt list --installed > ./installed.txt\n')
    if os.path.exists('/var/mobile/Documents/JBTransfer.log'): # remove old log file
        output.write('rm /var/mobile/Documents/JBTransfer.log\n')
    output.write('python3 log.py\n')
    output.write('rm /var/mobile/Documents/JBTinstall.sh\n')
    output.write('rm -rf /var/mobile/Documents/JBTransfer/\n')
    output.write('ldrestart\n')