#

# Import standard python modules.
import random
import sys
import time
import config

#import commandline args helper functions
from cl_args import set_aio_creds

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

from mqtt_generators import *

from math_functions import call_function

config.COMMAND_LINE_ARGS = sys.argv
print ('command line args: ', config.COMMAND_LINE_ARGS)

set_aio_creds()

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for DemoFeed changes...')
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe('test')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))


# Create an MQTT client instance.
client = MQTTClient(config.ADAFRUIT_IO_USERNAME, config.ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()




def createNormalDist(mu, sigma = 0, allow_negative = False):
	while True:
		val = random.normalvariate(mu, sigma)
		if val < 0 and not allow_negative:
			yield 0
		else:
			yield val

def setup_generator(args_array):
	while True:
		val = 0.0
		for args in args_array:
			val += call_function(**args)
		yield val

generators = {}
#generators['test'] = setup_generator({'function_name':'normal', 'mu': 50, 'sigma': 10})
generators['test'] = setup_generator([{'function_name':'sine', 'offset': 50, 'amplitude': 10, 'period': 60}])

generators['atmosphere.atmosphere-oxygen'] = setup_generator([{'function_name': 'normal', 'mu': 9.26, 'sigma': 0.089}, {'function_name': 'sine', 'offset': 10.51, 'amplitude': 0.024, 'period': 60}])

generators['atmosphere.atmosphere-carbon-dioxide'] = setup_generator([{'function_name': 'sine', 'offset': 0.011, 'amplitude': 0.0077, 'period': 60}, {'function_name': 'saw', 'offset': -0.88, 'amplitude': -.0078, 'period': -0.88}])

generators['atmosphere.atmosphere-carbon-monoxide'] = setup_generator([{'function_name': 'sine', 'offset': -.002, 'amplitude': 0.024, 'period': 60, 'allow_negative': False}])

generators['atmosphere.atmosphere-temperature'] = setup_generator([{'function_name': 'normal', 'mu': 0, 'sigma': 0.2}, {'function_name': 'sine', 'offset': 5.05, 'amplitude': 0.0011, 'period': 60}, {'function_name': 'saw', 'offset': 68.73, 'amplitude': 2.68, 'period': 7}, {'function_name': 'triangle', 'offset': -24.85, 'amplitude': -3.7, 'period': 3}])

generators['growth-chambers.growth-chambers-ph'] = setup_generator([{'function_name': 'normal', 'mu': -17.9, 'sigma': 0.01}, {'function_name': 'sine', 'offset': -0.15, 'amplitude': 0.6, 'period': 60}, {'function_name': 'saw', 'offset': 7.018, 'amplitude': 1.65, 'period': 7}, {'function_name': 'triangle', 'offset': 0.16, 'amplitude': -1.7, 'period': 3}])

generators['atmosphere.atmosphere-humidity'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 0, 		'amplitude': 1.0, 	'period': 60},
{'function_name': 'saw', 		'offset': 10, 	'amplitude': 0, 	'period': 70},
{'function_name': 'triangle', 	'offset': 0.16, 	'amplitude': 1, 	'period': 300}])

generators['regolith-cleaning.regolith-cleaning-perchlorates'] = setup_generator([{'function_name': 'normal', 'mu': 0, 'sigma': 0.005, 'allow_negative': False},
{'function_name': 'triangle', 'offset': -0.16, 'amplitude': 1, 'period': 50, 'allow_negative': False}])



#---- Start of default generators (Need to set parameters)


generators['atmosphere.atmosphere-pressure'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 1, 	'amplitude': 0.048, 	'period': 6000},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0.001, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0.001, 	'period': 3}])


generators['atmosphere.atmosphere-water'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.05},
{'function_name': 'sine', 		'offset': 40, 	'amplitude': 0, 	'period': 20},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 2, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 3, 	'period': 1}])


generators['atmosphere.atmosphere-volatiles'] = setup_generator(
[{'function_name': 'normal', 'mu': 70, 'sigma': 1},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.2, 	'period': 3},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 10, 	'period': 70},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 1, 	'period': 0.2}])


generators['by-products.by-products-duckweed'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.1},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.5, 	'period': 1},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 20, 	'period': 86400},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['by-products.by-products-food-crop-plants'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.001},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': .03, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 2, 	'period': 86400},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': .04, 	'period': 30}])


generators['by-products.by-products-algae'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.001, 'allow_negative': False},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['composting-bioreactor.composting-bioreactor-temperature'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.5},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 1, 	'period': 29},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 36, 	'period': 700},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 1, 	'period': 3}])


generators['composting-bioreactor.composting-bioreactor-ph'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 1},
{'function_name': 'sine', 		'offset': 6.5, 	'amplitude': 0.15, 	'period': 3600},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0.05, 	'period': 1}])


generators['composting-bioreactor.composting-bioreactor-influent-rate'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.1},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.05, 	'period': 21},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0.00001157407, 	'amplitude': 0.15, 	'period': 3}])


generators['composting-bioreactor.composting-bioreactor-biomass-influent-rate'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.1},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.05, 	'period': 21},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0.00001157407, 	'amplitude': 0.15, 	'period': 3}])


generators['composting-bioreactor.composting-bioreactor-compost-effluent-rate'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 0.00000462962, 	'amplitude': 0.05, 	'period': 30},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0.15, 	'period': 86400}])

#todo
generators['composting-bioreactor.composting-bioreactor-gas-production-rate'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['composting-bioreactor.composting-bioreactor-microorganism'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.001, 'allow_negative': False},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['composting-bioreactor.composting-bioreactor-pressure'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.5},
{'function_name': 'sine', 		'offset': 10, 	'amplitude': 0.1, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0.005, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 5, 	'period': 86400}])


generators['grinder.grinder-flow-meter'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.1},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.05, 	'period': 21},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0.00001157407, 	'amplitude': 0.15, 	'period': 3}])


generators['grinder.grinder-heat-monitor'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 2},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 4.5, 	'period': 29},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 37, 	'period': 700},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 1, 	'period': 0.001}])


generators['grinder.grinder-leak-detection'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.0001},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])

#todo
generators['growth-chambers.growth-chambers-nutrient-levels'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.001},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['growth-chambers.growth-chambers-dissolved-oxygen'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.1},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 2.5, 	'period': 60},
{'function_name': 'saw', 		'offset': 7.5, 	'amplitude': 1, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': .1, 	'period': .37}])


generators['growth-chambers.growth-chambers-dissolved-carbon-dioxide'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 2, 	'amplitude': .5, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': .1, 	'period': .5}])

# Not sure of value, set to zero.
generators['growth-chambers.growth-chambers-optical-density'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.0001},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['growth-chambers.growth-chambers-light-levels'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 5},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 110, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 4, 	'period': 86400}])


generators['growth-chambers.growth-chambers-pressure'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 1, 	'amplitude': 0.048, 	'period': 6000},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0.001, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0.001, 	'period': 3}])


generators['pipes-infrastructure.pipes-infrastructure-leak-detection'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.0001},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0, 	'period': 60},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['portable-water-system.portable-water-system-ph'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.25},
{'function_name': 'sine', 		'offset': 7, 	'amplitude': 0.5, 	'period': 86400},
{'function_name': 'saw', 		'offset': 0, 	'amplitude': 0, 	'period': 7},
{'function_name': 'triangle', 	'offset': 0, 	'amplitude': 0, 	'period': 3}])


generators['portable-water-system.portable-water-system-tds'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.01},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.1, 	'period': 130},
{'function_name': 'saw', 		'offset': 5, 	'amplitude': 0.5, 	'period': 130},
{'function_name': 'triangle', 	'offset': 2, 	'amplitude': 2, 	'period': 86400}])


generators['portable-water-system.portable-water-system-toc'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.5},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.1, 	'period': 130},
{'function_name': 'saw', 		'offset': 3, 	'amplitude': 0.5, 	'period': 130},
{'function_name': 'triangle', 	'offset': 1, 	'amplitude': 2, 	'period': 86400}])


generators['portable-water-system.portable-water-system-particulate-concentration'] = setup_generator(
[{'function_name': 'normal', 'mu': 0, 'sigma': 0.15},
{'function_name': 'sine', 		'offset': 0, 	'amplitude': 0.1, 	'period': 500},
{'function_name': 'saw', 		'offset': 1, 	'amplitude': 0.5, 	'period': 500},
{'function_name': 'triangle', 	'offset': 0.1, 	'amplitude': 0.1, 	'period': 86400}])

#---- End of default generators 

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()

sleep_seconds = 1.5
print('Publishing a new message every {} seconds (press Ctrl-C to quit)...'.format(sleep_seconds))
while True:
	for feed_name, feed_generator in generators.items():
		next = feed_generator.__next__()
		print('Publishing to {}: {}'.format(feed_name, next))
		client.publish(feed_name, next)
		time.sleep(sleep_seconds)

# Another option is to pump the message loop yourself by periodically calling
# the client loop function.  Notice how the loop below changes to call loop
# continuously while still sending a new message every 10 seconds.  This is a
# good option if you don't want to or can't have a thread pumping the message
# loop in the background.
#last = 0
#print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
#while True:
#   # Explicitly pump the message loop.
#   client.loop()
#   # Send a new message every 10 seconds.
#   if (time.time() - last) >= 10.0:
#       value = random.randint(0, 100)
#       print('Publishing {0} to DemoFeed.'.format(value))
#       client.publish('DemoFeed', value)
#       last = time.time()

# The last option is to just call loop_blocking.  This will run a message loop
# forever, so your program will not get past the loop_blocking call.  This is
# good for simple programs which only listen to events.  For more complex programs
# you probably need to have a background thread loop or explicit message loop like
# the two previous examples above.
#client.loop_blocking()