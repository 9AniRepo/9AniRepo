# files to read and write
with open('/JBTemp/prefs.txt', 'r') as prefs:
    with open('/JBTemp/cpprefs.sh', 'a') as output:

        # filter out prefs
        for line in prefs:
            if 'apple' not in line and 'google' not in line and 'SuiteName' not in line and ('com' in line or 'love' in line or 'me' in line or 'net' in line or 'org' in line):
                # shell script to move package pref files to JBTransfer dir
                path = '/var/mobile/Library/Preferences/' + line.strip()
                output.write('cp %s /var/mobile/Documents/JBTransfer/preferences/\n' % path)
