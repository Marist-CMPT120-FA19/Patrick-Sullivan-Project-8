def main():
    print('Enter the daily average temperatures or leave an empty space when finished.')
    
    hdd,cdd = 0,0
    date = 1
    temp = input('Day #{} :'.format(date))
    while temp != '':
        temp = int(temp)
        
        if temp > 80:
            cdd = ((temp-80)+cdd)
        if temp < 60:
            hdd = ((60-temp)+hdd)
        date = date + 1
        temp = input('Day #{} :'.format(date))
    print('In {} days, there are a total of {} HDD.'.format(date-1,hdd))
    print ('In {} days, there are a total of {} CDD.'.format(date-1,cdd))
        
main()
