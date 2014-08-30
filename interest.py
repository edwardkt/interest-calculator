import datetime

print 'EDWARDS INTEREST CALCULATOR!'
print '*******************************'

today = datetime.date.today()
someday = datetime.date(2011, 8, 15)
diff = today - someday
print diff.days
