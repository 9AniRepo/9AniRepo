current = []

# read and write file dirs
with open('/var/mobile/Documents/JBTransfer/installed.txt', 'r') as packageList:

    # add currently installed packages to a list
    for line in packageList:
        # truncate the version numbers and save package bundleid to file
        line = line.split('/')
        for package in line:
            if '[installed' not in package and 'Listing...' not in package:
                current.append(package)

# generate log
with open('/var/mobile/Documents/JBTransfer.log', 'a') as output:
    with open('/var/mobile/Documents/JBTransfer/JBTpackages.txt', 'r') as archiveList:
        output.write('Packages that were not installed:\n')
        for line in archiveList:
            # if packages is not installed then add it to script
            line = line.strip()
            if line not in current:
                output.write(line + '\n')
        output.write('\n')
        with open('/var/mobile/Documents/JBTransfer/JBTemp.log', 'r') as aptLog:
            for line in aptLog:
                output.write(line + '\n')
