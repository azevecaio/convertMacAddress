'''
Help options:

convert_macaddress.py (file) (separator) (field) [vendor/vendoronly]

Form options:
: (00:80:41:ae:fd:7e)
.. (0080.41ae.fd7e)
- (0080-41ae-fd7e)

Eg. 
convert_macaddress.py file.txt : 2 
---> 00:80:41:ae:fd:7e

convert_macaddress.py file.txt . 4 vendor
---> 0080.41ae.fd7e - Dell Inc.

convert_macaddress.py file.txt : 2 vendoronly
---> Dell Inc.

'''

import re, sys
import pandas as pd

#Args
try:
    for arg in sys.argv:
        if arg in 'h':
            print(__doc__)
            sys.exit(1)
        mac_file = sys.argv[1]
        separator = sys.argv[2]
        fields = sys.argv[3]
        fields = int(fields)
        try:
            input_vendor = sys.argv[4]
        except Exception as e:
            pass
except Exception as e:
    print(__doc__)
    sys.exit(1)

#Source file with mac values
content = open(mac_file, 'r')
macs = content.readlines()

def format_mac(mac, separator, fields):
    '''Returns mac address formated'''
    sep = separator
    mac = re.sub('[.:-]', '', mac).upper()  # remove delimiters and convert to lower case
    mac = ''.join(mac.split())  # remove whitespaces
    assert len(mac) == 12  # length should be now exactly 12 (eg. 008041aefd7e)
    assert mac.isalnum()  # should only contain letters and numbers
    # convert mac in separator (eg. 00:80:41:ae:fd:7e)
    mac = sep.join(["%s" % (mac[i:i+fields]) for i in range(0, 12, fields)])
    return mac

def get_vendor(mac):
    '''Get vendor from IANA csv file'''
    iana_csv = 'macaddress-io-db.csv'
    mac = format_mac(mac, ':', 2)
    mac = mac.upper()
    data_frame = pd.read_csv(iana_csv, sep=';' )
    count = 0
    while True:
        if not data_frame[data_frame['oui'].isin([mac[:count]])].empty:
            vendor = pd.array(data_frame.loc[data_frame['oui'].isin([mac[:count]]), 'companyName'])
            return vendor[0]
            break
        if count == -12:
            return 'Not Found'
            break
        count -= 1

for mac in macs:
    mac = format_mac(mac, separator, fields)
    try:
        vendor = get_vendor(mac)
        if input_vendor == 'vendoronly':
            print(vendor)
        elif vendor:
            print(mac + ' - ' + vendor)
    except Exception as e:
        print(mac)        