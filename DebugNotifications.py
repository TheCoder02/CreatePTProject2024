import logging
import http.client
from NotificationMaker import *
from LinkOpen import *
def test_function():
   logging.basicConfig(
       filename='debugLog.txt',
       level=logging.DEBUG,
       filemode = 'w',
       format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
       datefmt='%Y-%m-%d %H:%M:%S',
      )

logging.debug(ip)
popup_maker('You have Viruses!', 'file:///C:/Users/lg255111/OneDrive%20-%20Lamar%20Consolidated%20ISD/2023-2024/Computer%20Science/CreatePT%20Ideas/info.html', 'Click here to run diagnostics')
