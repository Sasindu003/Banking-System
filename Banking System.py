print(' ')

print('                                     ### BANKING SYSTEM ###')
print(' ')
print('Now you can compair your ballances ANNUAL INTEREST RATE diffrance with in the Fix Deposit Account vs Saving Account')   
print('Fill Follwing Form to Check the Blance')
print('=======================================================================')

month=int(input('type Your Balance>  Rs.'))
print(' ')

print ('If you want check Saving Account rate')

rate=int(input('type Your Monthly saving prasantage,else type zero >  %'))

print(' ')

mav1=rate/100
mav2=mav1*month
print('Monthly Interest rate Rs.', int(mav2))

maa=month+mav2
print('1st month amount with Interest Rs.', int(maa))

maa1=rate/100
maa1a=maa1*maa
maa1b=maa1a+maa
print('2nd month balance  Rs.',int(maa1b))

maa2=rate/100
maa2a=maa2*maa1b
maa2b=maa2a+maa1b
print('3rd month balance  Rs.',int(maa2b))

maa3=rate/100
maa3a=maa3*maa2b
maa3b=maa3a+maa2b
print('4th month balance  Rs.',int(maa3b))

maa4=rate/100
maa4a=maa4*maa3b
maa4b=maa4a+maa3b
print('5th month balance  Rs.',int(maa4b))

maa5=rate/100
maa5a=maa5*maa4b
maa5b=maa5a+maa4b
print('6th month balance  Rs.',int(maa5b))

maa6=rate/100
maa6a=maa6*maa5b
maa6b=maa6a+maa5b
print('7th month balance  Rs.',int(maa6b))

maa7=rate/100
maa7a=maa7*maa6b
maa7b=maa7a+maa6b
print('8th month balance  Rs.',int(maa7b))

maa8=rate/100
maa8a=maa8*maa7b
maa8b=maa8a+maa7b
print('9th month balance  Rs.',int(maa8b))

maa9=rate/100
maa9a=maa9*maa8b
maa9b=maa9a+maa8b
print('10th month balance Rs.',int(maa9b))

maa10=rate/100
maa10a=maa10*maa9b
maa10b=maa10a+maa9b
print('11th month balance Rs.',int(maa10b))

maa11=rate/100
maa11a=maa11*maa10b
maa11b=maa11a+maa10b
print('yearly  total saving balance is Rs.',int(maa11b))

print('------------------------------------------------------------------------')

print('If you want check Fix Deposit rate of Rs.',(month))
rate1=int(input('type Your yearly FD prasantage> %'))

print(' ')
 
yaa=rate1/100
yaa1=yaa*month
print('Yearly Interest rate       Rs.',  int(yaa1))

yaa1a=yaa1+month
print('Total amount with Interest Rs.', int(yaa1a))

print('........................................................................')

print('SAVING ACCOUNT ANNUAL BALANCE IS          Rs.',(maa11b))
print('FIX DEPOSITE ACCOUNT ANNUAL BALANCE IS    Rs.',(yaa1a))

pro=maa11b-yaa1a
print ('defferance of annual interest             Rs.',int(pro))

print(' ')
print('Thanking you for Join with us')
print('Programmed by SASINDU AKALANA')
print('V 1.2')





