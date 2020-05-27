from pygame import *
from datetime import *
import time


def play_alarm(_file, *stopper):
	"""  To play notification tone  """

	mixer.init()
	mixer.music.load(_file)
	mixer.music.play(-1)
	while True:
		get_input = input()
		if get_input in stopper:
			mixer.music.stop()
			break
	return get_input

#######################################################################

def get_time():
	""" To get current date """

	duration = datetime.now()
	return duration

#######################################################################

def add_logs(_data):
	"""  To add logs of carried out events """

	with open("Daily_Health_Logs.csv", "a") as f:
		f.write(_data)

print("\n\n\t\t****************************************************************************************************")
print(f"\t\t\t\tHello Shanthveer Good Morning. \n\t\t\t\tDate is :{get_time().date()} and Clock is ticking at : {get_time().time()}")
print("\t\t****************************************************************************************************")

start_hour, start_min = 9,0
end_hour, end_min = 18,0
check_alarm = ("water","eyes","physical")
check_water = ""
check_eye = ""
check_physical = ""

if get_time().hour >= start_hour and get_time().minute >= start_min:
	initial_time = get_time().time()
	initial_time1 = time.time()
	start_session = True
else:
	start_session = False

try:
	while start_session:
		while True:
			current_time = get_time()
			start_time = time.time()
			diff_min = current_time.minute - initial_time.minute
			diff = start_time - initial_time1

			if diff >= 50 and diff <= 100 and check_water == "":
				output_result = play_alarm("sound/water.ogg", *check_alarm)
				check_water = output_result
				if check_water in check_alarm:
					insert_log = check_water.upper() + "," + str(current_time.date()) + ',' + str(current_time.time()) + "," + "Water Drunk" + "\n"
					add_logs(insert_log)
					check_physical = ""
				else:
					pass
			else:
				pass

			if diff >= 150 and diff <= 200 and check_eye == "":
				output_result = play_alarm("sound/eye.ogg", *check_alarm)
				check_eye = output_result
				if check_eye in check_alarm:
					insert_log = check_eye.upper() + "," + str(current_time.date()) + ',' + str(current_time.time()) + "," + "Eyes Relaxed" + "\n"
					add_logs(insert_log)
					check_water = ""
				else:
					pass
			else:
				pass

			if diff >= 250 and diff <= 300 and check_physical == "":
				output_result = play_alarm("sound/physical.ogg", *check_alarm)
				check_physical = output_result
				if check_physical in check_alarm:
					insert_log = check_physical.upper() + "," + str(current_time.date()) + ',' + str(current_time.time()) + "," + "Had a Round" + "\n"
					add_logs(insert_log)
					check_eye = ""
					break
				else:
					pass
			else:
				pass
			if current_time.hour >= end_hour and current_time.minute >= end_min:
				break
			else:
				continue
		if current_time.hour >= end_hour and current_time.minute >= end_min:
			break
		else:
			initial_time1 = start_time
			continue
except Exception as e:
	print(e)