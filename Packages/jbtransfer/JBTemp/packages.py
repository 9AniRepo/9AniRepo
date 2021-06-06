# read and write file dirs
with open('/JBTemp/packages.txt', 'r') as packageList:
    with open('/var/mobile/Documents/JBTransfer/JBTpackages.txt', 'a') as output:

        # filter out auto installed and local packages
        for line in packageList:
            if 'local]' not in line and 'automatic]' not in line and 'com.asianman.jbtransfer' not in line:

                # truncate the version numbers and save package bundleid to file
                line = line.split('/')
                for package in line:
                    if '[installed' not in package and 'Listing...' not in package:
                        output.write(package + '\n')
