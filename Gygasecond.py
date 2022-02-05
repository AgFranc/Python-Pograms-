import datetime as dt #importing datetime module
def add(moment): #defining the function to get the value after a moment
    return moment + dt.timedelta(seconds=10**9) # using timedelta with parameter second= 10**9 because 10**9 == "gigasecond"