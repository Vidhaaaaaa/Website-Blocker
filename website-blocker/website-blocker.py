
import time
from datetime import datetime as dt


end_time = dt(2022,5,5,15)     # (2022,may,05,3pm)

# Change the 'end time' above for sites being blocked as per your requirement in the format given below:
# end_time = dt(year, month, day, hour, minutes, seconds)
# Put the 'Hour' in 24 hour clock
# Hour, Minutes and Seconds are optional


path = r'C:\Windows\System32\drivers\etc\hosts' # for windows
# If you are on Mac/Linux, then use this instead of above 'path' object:
# path = '/etc/hosts'

redirect = '127.0.0.1'

weblist = ['www.site1.com' , 'site1.com', 'www.site2.in' , 'site2.in']
# Add any number of sites in the given format above
# Use any domain - .com / .in / .tk / .ml / .co / .me  etc.


 
# --------------------DO NOT CHANGE ANYTHING AFTER THIS---------------------- #

# Main Code
def block_the_sites():
    if dt.now() < end_time: # Running until the given time
        with open(path,'r+') as hostsfile:
            cont_hosts = hostsfile.read()
            for site in weblist:
                if site not in cont_hosts:
                    hostsfile.write(f'{redirect} {site} \n')
                else:
                    pass
        print('Hurray , Sites have been blocked!!')

    else: # To unblock the sites after the given time is over
        with open(path,'r+') as hostsfile:
            cont_hosts = hostsfile.readlines()
            hostsfile.seek(0)
            for line in cont_hosts:
                if not any(site in line for site in weblist):
                    hostsfile.write(line)
            hostsfile.truncate() # Deleting the added lines in the file to unblock sites

        print('Hurray, sites have been unblocked!!')

if __name__ == '__main__':
    block_the_sites() # Calling the function out to block the sites

