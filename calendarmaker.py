import datetime


DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February','March', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December') 

while True:
    print('Enter the yeat for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True:
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month like 3 for march')
        continue

    month = int(response)
    if 1<= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarFor(year, month):
    calText ='' #will contain the string of our calendar

    #put month and year at the top of the calendar
    calText += (' ' *34) +MONTHS[month - 1] + str(year) + '\n'

    #add the days of the week label to the calendar
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    #the horizontal line string separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    #the blank rows have ten spaces in between the | day separaors:
    blankRow = ('|          '* 7) + '|\n'

    #get the first date in the month
    currentDate = datetime.date(year, month, 1)

    #roll back currentdate until it is sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator

        #dayNumberRow is the row with the day number ;abe;s:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n' #add vertical line after ssaturday

        #ass the day number row and 3 blank rows to the calendar text
        calText += dayNumberRow
        for i in range(3):
            calText+= blankRow

        #check if we're done with the month:
        if currentDate.month != month:
            break

    #add the horizontal line at the bottom of the callendar
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)

#save the calendar to a txt file:
# calendarFilename = 'calendar_{}_{}.txt'.format(year,month)
# with open(calendarFilename, 'w') as fileObj:
#     fileObj.write(calText)

# print('saved to' + calendarFilename)