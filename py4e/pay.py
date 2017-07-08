__author__ = 'Merlin'
int=input("enter the hours:")
hours=float(int)
int=input("enter the rate:")
rate=float(int)
if hours <= 40:
 pay=hours*rate
if hours > 40:
    pay=hours*(rate*1.5)
print(pay)
          