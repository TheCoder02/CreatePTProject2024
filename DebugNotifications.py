#MAIN FILE, IMPORTS NOTIFICATION MAKER AND LINK OPEN IN ORDER TO MAKE POPUPS

from LinkOpen import *

numbers = ['','','','','']
for i in range(5):
   number = int(input('Enter the 3 digit number to your lottery ticket to claim your prize!: '))
   numbers[i] = number
   
x = random.randint(0,4)
number = numbers[x]

if number >= 100 and number >= 0:
   print(number)
   
   popup_maker(
      'You have Viruses!', 
      'file:///C:/Users/lg255111/OneDrive%20-%20Lamar%20Consolidated%20ISD/2023-2024/Computer%20Science/CreatePT%20Ideas/info.html', 
      'Click here to run diagnostics',
      number
      )

