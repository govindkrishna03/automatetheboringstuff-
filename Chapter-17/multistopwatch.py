import time,pyperclip

print('Press ENTER to begin. Afterwards,press ENTER to "click" the stopwatch. print Ctrl-c to quit.')

input()
print('Started.')
start = time.time()
end = start
lapNum = 1


try:
    while True:
        input()
        lapTime = round(time.time() - end, 2)
        totalTime = round(time.time() - start, 2)
        print('Lap #' + str(lapNum).rjust(3) + str(totalTime).rjust(8) + ' (' + str(lapTime).rjust(6) + ')')
        outPutTxt = 'Lap # ' + str(lapNum).rjust(3) + str(totalTime).rjust(8) + ' (' + str(lapTime).rjust(6) + ')'
        lapNum += 1
        end = time.time()
except KeyboardInterrupt:

    print('\nDone')


pyperclip.copy(outPutTxt)