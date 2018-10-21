
import random
import time
import math

def normal(args, allow_negative):
        mu = 0
        if args['mu']:
            mu = args['mu']

        sigma = 0
        if args['sigma']:
            sigma = args['sigma']

        val = random.normalvariate(args['mu'], args['sigma'])

        if val < 0 and not allow_negative:
            return 0
        else:
            return val

def sine(args, allow_negative):
        offset = 0
        if args['offset']:
            offset = args['offset']

        amplitude = 0
        if args['amplitude']:
            amplitude = args['amplitude']

        period = 0
        if args['period']:
            period = args['period']

        seconds = time.time()
        cycle = math.fmod(seconds, period) / period
        radians = cycle * 2 * math.pi

        val = (math.sin(radians) * amplitude / 2) + offset

        if val < 0 and not allow_negative:
            return 0
        else:
            return val
    
def saw(args, allow_negative):
        offset = 0
        if args['offset']:
            offset = args['offset']

        amplitude = 0
        if args['amplitude']:
            amplitude = args['amplitude']

        period = 0
        if args['period']:
            period = args['period']

        seconds = time.time()

        cycle = 2 * math.fmod(seconds, period) / period
        val = (cycle * amplitude) - (amplitude / 2) + offset

        if val < 0 and not allow_negative:
            return 0
        else:
            return val

def triangle(args, allow_negative):
        offset = 0
        if args['offset']:
            offset = args['offset']

        amplitude = 0
        if args['amplitude']:
            amplitude = args['amplitude']

        period = 0
        if args['period']:
            period = args['period']

        seconds = time.time()

        cycle = 2 * math.fmod(seconds, period) / period
        if cycle < 1:
            tricycle = cycle * amplitude
        else:
            tricycle = amplitude - ((cycle-1) * amplitude)

        val = offset + tricycle - (amplitude /2)

        if val < 0 and not allow_negative:
            return 0
        else:
            return val

def call_function(**args):
    funcname = args['function_name']
    functions = {
        'normal': normal,
        'sine': sine,
        'saw': saw,
        'triangle': triangle}

    func = functions.get(funcname, lambda: 'Invalid function')

    #since allow_negative is common to all functions...
    allow_negative = False
    if 'allow_negative' in args:
        allow_negative = args['allow_negative']

    return_val = func(args, allow_negative)
    return return_val