import time
import RPi.GPIO as GPIO
from crontab import CronTab

t = time.localtime()
curHr = int(time.strftime('%H',t))
curMin = int(time.strftime('%M',t))

cron = CronTab(user = True)
for job in cron: 
    if job.comment != 'weigh':
        if (job.minute) == curMin and (job.hour) == curHr:
            calories = int(job.comment)
            break

feedtime = calories #DO SOMETHING HERE DUMMY!

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)

GPIO.output(38,1)
time.sleep(feedtime)
GPIO.output(38,0)
    
GPIO.cleanup()