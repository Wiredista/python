import numpy
import time
import matplotlib.pyplot as plt

arraysize = int(input("Array size     : "))
delaytime = float(input("Delay time (ms): "))
animetype = raw_input("Animation type (f)aster / (s)low: ")

if(delaytime == 0):
	delaytime = 1

if animetype != "f" and animetype != "s":
	animetype = "f"


array = numpy.random.random(arraysize)

print("Original array: ")



numpy.random.shuffle(array)
print(array)

plt.show()
while True:
	notready = False
	for a in range(len(array)-1):
		before = array[a]
		after  = array[a+1]
		if before > after:
			if(animetype == "s"):
				plt.plot(array, "o")
				plt.pause(delaytime / 1000)
				plt.gcf().clear()
			array[a] = after
			array[a+1]  = before
			notready = True
			
	if notready == False:
		break

	if(animetype == "f"):
		plt.plot(array, "o")
		plt.pause(delaytime / 1000)
		plt.gcf().clear()

print("RESULT: ")
print(array)

raw_input("Press enter to close.")
