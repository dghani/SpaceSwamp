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

from mqtt_generators import MQTTVars
from mqtt_generators import mqtt_gen

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

generators = {}
generators['atmosphere.atmosphere-oxygen'] = createNormalDist(21, 0.1)
generators['atmosphere.atmosphere-carbon-dioxide'] = createNormalDist(0.04, 0.05)
generators['atmosphere.atmosphere-carbon-monoxide'] = createNormalDist(0.1, 0.1)
generators['atmosphere.atmosphere-water'] = createNormalDist(0)
generators['atmosphere.atmosphere-pressure'] = createNormalDist(0)
generators['atmosphere.atmosphere-temperature'] = createNormalDist(70, 0.1)
generators['atmosphere.atmosphere-volatiles'] = createNormalDist(0)
generators['atmosphere.atmosphere-humidity'] = createNormalDist(0)
generators['by-products.by-products-duckweed'] = createNormalDist(0)
generators['by-products.by-products-food-crop-plants'] = createNormalDist(0)
generators['by-products.by-products-algae'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-temperature'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-ph'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-influent-rate'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-biomass-influent-rate'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-compost-effluent-rate'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-gas-production-rate'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-microorganism'] = createNormalDist(0)
generators['composting-bioreactor.composting-bioreactor-pressure'] = createNormalDist(0)
generators['oxygen'] = createNormalDist(0)
generators['test'] = createNormalDist(0)
generators['grinder.grinder-flow-meter'] = createNormalDist(0)
generators['grinder.grinder-heat-monitor'] = createNormalDist(0)
generators['grinder.grinder-leak-detection'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-nutrient-levels'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-ph'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-dissolved-oxygen'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-dissolved-carbon-dioxide'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-optical-density'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-light-levels'] = createNormalDist(0)
generators['growth-chambers.growth-chambers-pressure'] = createNormalDist(0)
generators['pipes-infrastructure.pipes-infrastructure-leak-detection'] = createNormalDist(0)
generators['portable-water-system.portable-water-system-ph'] = createNormalDist(0)
generators['portable-water-system.portable-water-system-tds'] = createNormalDist(0)
generators['portable-water-system.portable-water-system-toc'] = createNormalDist(0)
generators['portable-water-system.portable-water-system-particulate-concentration'] = createNormalDist(0)
generators['regolith-cleaning.regolith-cleaning-perchlorates'] = createNormalDist(0)

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()

sleep_seconds = 6
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