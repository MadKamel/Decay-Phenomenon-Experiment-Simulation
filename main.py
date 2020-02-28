from random import randint
from turtle import *
def randTrue(prob=1):
  return randint(0, prob) != 0
screen = Screen()
screen.bgcolor("black")

#change the variables below
graphtype = "normal" #normal graphs the trials, median shows high/low and median values (not yet though.)
sampleSize = 100 #change to get a longer or shorter test
chance = 1
outputtype = 1 #change to 0 for the old data dumps
repitions = 1 #max 6 as of now
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
dispNumbers = True #change to hide or show numbers on chart

#not these though
medianArray = []
highestArray = []
lowestArray = []
allArrays = []
arrayCalc = []
hideturtle()
penup()
goto(0, -240)
fillcolor("white")
write("Sample Decay Chart", font=('Courier', 20, 'Italic'), align='center')
for count in range(repitions):
  currentSample = sampleSize
  sampleDifference = 0
  trialsTotalSample = []
  trialsRemoved = []
  trialsKept = []
  trialsTotalRemoved = []
  iterations = 0
  while currentSample > 0:
    sampleDifference = currentSample
    iterations += 1
    for i in range(currentSample):
      if randTrue(chance):
        sampleDifference -= 1
    trialsTotalSample.append(currentSample)
    trialsRemoved.append(sampleDifference)
    currentSample -= sampleDifference
    trialsKept.append(currentSample)
    trialsTotalRemoved.append(sampleSize - currentSample)
  print(str(iterations) + " Total Iterations")
  print(str(sampleSize) + " In Sample at Start")
  print("")

  if graphtype == "normal":
    pencolor(colors[count])
    pensize(2)
    for c in range(iterations):
      if outputtype == 0:
        print("Iteration " + str(c) + ":")
        print("\t" + str(trialsTotalSample[c]) + ": Total in Sample this Iteration")
        print("\t" + str(trialsRemoved[c]) + ": Removed from Sample this Iteration")
        print("\t" + str(trialsKept[c]) + ": Kept in Sample this Iteration")
        print("\t" + str(trialsTotalRemoved[c]) + ": Total Amount removed from Sample by this Iteration")
        print("")
      else:
        print("Iteration #" + str(c) + " Results:\n")
        print("\tTotal Change:")
        print("\t\t" + str(trialsTotalSample[c]) + " Total Samples Left.")
        print("\t\t" + str(trialsTotalRemoved[c]) + " Total Samples Gone.\n")
        print("\tChange This Iteration:")
        print("\t\t" + str(trialsKept[c]) + " Samples Kept For This Iteration.")
        print("\t\t" + str(trialsRemoved[c]) + " Samples Removed For This Iteration.\n\n\n")
      if c!=0 and dispNumbers:
        pensize(1)
        pendown()
        fd(20)
        penup()
        fd(10)
        write(str(trialsTotalSample[c-1]), font=('Courier', 10, 'Italic'), align='center')
        bk(30)
      if c!= 0:
        pendown()
        pensize(2)
      goto((c-5)*40, (trialsTotalSample[c]-45)*4)
      penup()
  elif graphtype == "median":
    allArrays.append(trialsTotalSample)
    if count == range(repitions)[-1]:
      print("All Arrays Collected")
  else:
    print("\"Normal\" and \"Median\" are the only supported types as of now.")
