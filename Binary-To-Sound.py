import time
import winsound

binary = input("Binary input: \n")
for i in binary:
	if i == "0":
		winsound.Beep(2000, 100)
	if i == "1":
		winsound.Beep(4000, 100)
	time.sleep(0.1)
exit()