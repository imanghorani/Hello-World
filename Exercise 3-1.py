sh = input("Enter Hours:")
sr = input("Enter Rates:")
fh = float(sh)
fr = float(sr)
     #print(fh, fr)
if fh > 40 :
     #print("Over time")
     reg = fr * fh
     otp = (fh - 40 ) * (fr * 0.5)
     #print(reg,otp)
     xp = reg + otp
else:
     #print("Regular")
     xp = fh * fr
print("Pay:",xp)

