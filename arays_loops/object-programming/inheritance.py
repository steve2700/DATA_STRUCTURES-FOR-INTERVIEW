#inheriting attributes
class Date:
    def get_date(self):
        return'2016-08-09'
    
class Time(Date):
    def get_time(self):
        return'09:00:00'
    
dt = Date()
print('What was the date:', dt.get_date())
tm = Time()
print('what was the time:',tm.get_date())
# this following line this is what we mean by inheritance
print('get date by using the  time:' , tm.get_date())


