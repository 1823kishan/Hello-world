from datetime import datetime
now = datetime.now()
time = now.strftime("%H,%M,%S")
date = now.day
print(time)
print(date)
