import math
import random
import time
name = ["Sachin", "Ganguly", "Rahul", "Dhoni", "Ashwin"]
no_ball_score = 0
wide_score = 0
i = 0
total_score = 0


class Batsman:
    def __init__(self):
        self.score = 0
        self.name = name[i]

    def updatescore(self, total_score, i):
        print(self.name + ' is bating......... ')
        time.sleep(4)
        status = random.random()
        if status <= 0.2:
            print(self.name + ' is out..... ')
            active.remove(self)
            current = 1
            return False, total_score, current
        else:
            hit = random.randint(0, 6)
            print(self.name + " has hit " + str(hit) + "  runs")
            self.score = self.score + hit
            print(self.name + ' has scored ' + str(self.score) + ' ... ')
            time.sleep(4)
            if hit % 2 == 0:
                for ip in range(len(active)):
                    if (active[ip] == self):
                        current = ip
            else:
                for ip in range(len(active)):
                    if (active[ip] != self):
                        current = ip
            total_score = total_score + hit
            print('Total score is.... ' + str(total_score))
            return (True, total_score, current)


p = 0
balls = 0
total_score = 0
l = []
active = []
b = Batsman()
l.append(b)
active.append(b)
i = i + 1
b = Batsman()
active.append(b)
l.append(b)
current = 0
while (balls <= 300 and i <= len(name) - 1):
    print(str(math.floor(balls / 6) + 1) + " Over ," + str(balls % 6 + 1) + ", Ball......")
    bl = random.random()
    if (bl <= .2):
        print("Wide ball or No ball .....")
        total_score = total_score + 1
        wide_score = wide_score + 1
    else:
        balls = balls + 1
        z = active[current].updatescore(total_score, i)
        total_score = total_score + z[1]
        current = z[2]
    if not z[0]:
        i = i + 1
        b = Batsman()
        l.append(b)
        active.append(b)