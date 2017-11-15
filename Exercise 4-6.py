"""
Created on Wed Nov 15 14:21:14 2017

@author: eghoima
"""
def computepay(hours, rate) :
     #print("In computepaye", hours, rate)
    if hours > 40 :
     #print("Over time")
     reg = rate * hours
     otp = (hours - 40.0 ) * (rate * 0.5)
     #print(reg,otp)
     pay = reg + otp
    else:
       
     pay = hours * rate
    #print("Returning",pay)
    return pay
sh = input("Enter Hours:")
sr = input("Enter Rates:")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:",xp)
