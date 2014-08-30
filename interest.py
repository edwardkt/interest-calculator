import datetime

print '***********************************************************************'
print '******************EDWARDS INTEREST CALCULATOR**************************'
print '***********************************************************************'

# Get todays date
today = datetime.date.today()

# Figure out how many days have passed
unsub_2011 = datetime.date(2011, 8, 15)
diff_2011 = today - unsub_2011
unsub_2012 = datetime.date(2012, 8, 17)
diff_2012 = today - unsub_2012
unsub_2013 = datetime.date(2013, 8, 16)
diff_2013 = today - unsub_2013 

# Print outputs
print 'Interest rate for Unsub loan is 6.8% taken on 8/15/2011'
print 'Interest rate for Unsub loan is 6.8% taken on 8/17/2012'
print 'Interest rate for Unsub loan is 3.86% taken on 8/16/2013'

interest = 2000 * (0.068 / 365)
days_2011 = diff_2011.days
days_2012 = diff_2012.days
unsub_2011_amount = 2000 + (interest * days_2011)
print unsub_2011_amount
