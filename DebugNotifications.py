import logging
import http.client
from NotificationMaker import *
from LinkOpen import *
def test_function():
   logging.basicConfig(
       filename='debugLog.txt',
       level=logging.DEBUG,
           filemode = 'w',
       format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
       datefmt='%Y-%m-%d %H:%M:%S',
   )
   logging.debug('This is a debug log')
   


ip()
popup_maker()