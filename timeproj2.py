import arrow
from printy import printy
from datetime import datetime

#Introductory print statements
#I used Printy to make the text more defined
printy('Welcome to the Arrow Date & Time Library', 'BU')
printy('Please see below for some common [bB]date@ and [bB]time zones@:')
print('')

#Defining and assigning date & time zones variables
dt = datetime.now()
arrow_dt = arrow.Arrow.fromdate(dt)
utc = arrow.utcnow()
pst = utc.to('US/Pacific')
ist = arrow.now('Asia/Calcutta')
cest = arrow.now('Europe/Warsaw')
eat = arrow.now('Africa/Nairobi')
ast = arrow.now('Asia/Baku')

#Printing date & time zones from variables created above
print('Your Current Date & Time:', dt)
print('US/Pacific Time (PST):', pst)
print('Asia/Calcutta Time (IST):', ist)
print('Europe/Warsaw Time (CEST):', cest)
print('Africa/Nairobi Time (EAT):', eat)
print('Asia/Baku Time (AST):', ast)
