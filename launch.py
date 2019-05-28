# coding: utf-8

import sys
import time
import math
import os
import sched
import argparse
from scrapy import cmdline


parser = argparse.ArgumentParser(description="EasyGoSpider")
group = parser.add_mutually_exclusive_group()
group.add_argument("--now", action="store_true",
                   help="Launch right now and only once.")
group.add_argument("--loop", action="store_true",
                   help="Launch once every two hours from next even o'clock on.")
args = parser.parse_args()
schedule = sched.scheduler(time.time, time.sleep)
cmd = 'scrapy crawl yogaga'

def next_time(t):
    next_t = list(t)
    if math.fmod(next_t[3], 2) == 0:
        next_t[3] += 2
    else:
        next_t[3] += 1
    next_t = next_t[:4] + [0 for i in range(5)]
    print(next_t)
    return next_t




#demo
# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     print "Doing stuff..."
#     # do your stuff
#     s.enter(60, 1, do_something, (sc,))
#
# s.enter(60, 1, do_something, (s,))
# s.run()



def perform_command(cmd, inc):
    os.system(cmd)
    schedule.enter(inc, 0, perform_command, (cmd, inc))  #scheduler.enter(delay, priority, action, argument=(), kwargs={})


def loop():
    os.system('scrapy crawl yogaga')   #先运行爬虫

    schedule.enter(86400, 0, perform_command,   #等待一天
                   (cmd, 86400))  # scheduler.enter(delay, priority, action, argument=(), kwargs={})
    schedule.run()


if __name__ == '__main__':
    # # cmdline.execute('scrapy crawl proc'.split())
    # if len(sys.argv) == 1:
    #     parser.print_help()
    # elif args.now:
    #     cmdline.execute('scrapy crawl proc'.split())
    # elif args.loop:
    #     loop()
    loop()