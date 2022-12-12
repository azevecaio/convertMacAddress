# MAC Address Formater

Help
convert_macaddress.py (-h/--help)

convert_macaddress.py {file} {separator} {aggregateNum} [vendor/vendoronly]

File - Mac address list with any mac address format that you want to convert
Separator - field separator in output
AggregateNum - field aggregate number in output
Vendor - show vendor in output
Vendoronly - show only vendors in output

--- file.txt ---
ff:ff:ff:ff:ff:ff
aaaa.aaaa.aaaa
cccccccc


Eg. 
convert_macaddress.py file.txt : 2 
---> ff:ff:ff:ff:ff:ff
     aa:aa:aa:aa:aa:aa
     cc:cc:cc:cc:cc:cc
     
convert_macaddress.py file.txt . 4 vendor
---> ffff.ffff.ffff - Dell Inc.
     aaaa.aaaa.aaaa - Dell Inc.
     cccc.cccc.cccc - Dell Inc.

convert_macaddress.py file.txt : 2 vendoronly
---> Dell Inc.
     Dell Inc.
     Dell Inc.
