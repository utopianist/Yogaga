# coding: utf-8

import sys
import time
import datetime
import math
import os
import sched
import argparse  #Parser for command-line options, arguments and sub-commands
from scrapy import cmdline


parser = argparse.ArgumentParser(description="Yogaga")
group = parser.add_mutually_exclusive_group()
group.add_argument("--now", action="store_true",
                   help="Launch right now and only once.")
group.add_argument("--loop", action="store_true",
                   help="Launch once every two hours from next even o'clock on.")
args = parser.parse_args()
schedule = sched.scheduler(time.time, time.sleep)


def next_time(t):  # t = time.struct_time(tm_year=2019, tm_mon=5, tm_mday=28, tm_hour=23, tm_min=15, tm_sec=32, tm_wday=1, tm_yday=148, tm_isdst=0)
    print(t)
    # next_t =
    # if math.fmod(next_t[3], 2) == 0:
    #     next_t[3] += 2
    # else:
    #     next_t[3] += 1
    # next_t = next_t[:4] + [0 for i in range(5)]
    # print(next_t)
    # return next_t


def perform_command(cmd, inc):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)


def timming_exe(cmd, inc):
    schedule.enter(inc, 0, perform_command, (cmd, 7200))
    schedule.run()


def loop():
    now = datetime.datetime.now()
    next_t = now + datetime.timedelta(days=1)  #

    interval = time.mktime(next_t) - time.mktime(now) + 10
    # logger.info("...wait for %s seconds" % interval)
    timming_exe('scrapy crawl yogaga', interval)


if __name__ == '__main__':
    # cmdline.execute('scrapy crawl yogaga'.split())
    # if len(sys.argv) == 1:
    #     parser.print_help()
    # elif args.now:
    #     cmdline.execute('scrapy crawl yogaga'.split())
    # elif args.loop:
    #     loop()
    now = datetime.datetime.now()
    next_t = now + datetime.timedelta(days=1)
    print(now, next_t)