from time import strptime
from datetime import datetime

#test = datetime.strftime("April",)

#test = datetime.datetime.strptime('Mon Feb 15 2010', '%a %b %d %Y').strftime('%d/%-m/%Y')
#'15/02/2010'

test = datetime.strptime('April 4, 2020', '%B %d, %Y').strftime('%d/%m/%Y')

print(test)