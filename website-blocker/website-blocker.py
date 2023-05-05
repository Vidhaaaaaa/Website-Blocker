
import time
from datetime import datetime as dt


end_time = dt(2022,5,5,15)     # (2022,may,05,3pm)

# change the 'end time' above for sites being blocked as per your requirement in the formal given below:
# end_time = dt(year, month, day, hour, minutes, seconds)
# put the 'hour' in 24 hour clock
# hour, minutes and seconds are optional


path = r'C:\Windows\System32\drivers\etc\hosts' # for windows
# if you are on Mac/Linux, then use:
# path = '/etc/hosts'

redirect = '127.0.0.1'

weblist = ['www.site1.com' , 'site1.com', 'www.site2.in' , 'site2.in']
# add any number of sites in the given format
# use any domain - .com / .in / .tk / .ml / .co / .me  etc.


 
# --------------------DO NOT CHANGE ANYTHING AFTER THIS---------------------- #

# main code
def block_the_sites():
    if dt.now() < end_time: #running until the given time
        with open(path,'r+') as hostsfile:
            cont_hosts = hostsfile.read()
            for site in weblist:
                if site not in cont_hosts:
                    hostsfile.write(f'{redirect} {site} \n')
                else:
                    pass
        print('Hurray , Sites have been blocked!!')

    else:
        with open(path,'r+') as hostsfile:
            cont_hosts = hostsfile.readlines()
            hostsfile.seek(0)
            for line in cont_hosts:
                if not any(site in line for site in weblist):
                    hostsfile.write(line)
            hostsfile.truncate()

        print('Hurray, sites have been unblocked!!')

if __name__ == '__main__':
    block_the_sites() #calling the function

