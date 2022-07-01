import time

for x in range (0, 101):

    bars = '|' * x + ' ' * (100 - x)
    percent =  str(x) + '%'

    print("Loading:", bars, percent, end="\r")

    time.sleep(0.02) 