
import sys
import config

def set_aio_creds():
    #global ADAFRUIT_IO_USERNAME
    #global ADAFRUIT_IO_KEY
    #get adafruit.io username and key from environment variables to avoid
    #exposing them on github
    if len(config.COMMAND_LINE_ARGS) < 3 :
        print ('insufficient command line variables')
        print ('Adafruit.IO username and key must be first and 2nd command line args')
        exit()

    # Set your Adafruit IO username.
    # (go to https://accounts.adafruit.com to find your username)
    config.ADAFRUIT_IO_USERNAME = config.COMMAND_LINE_ARGS[1]

    if config.ADAFRUIT_IO_USERNAME == 'YOUR_AIO_USERNAME' :
        print ('invalid Adafruit.IO username')
        exit()
    else:
        print ('Adafruit.IO username: ', config.ADAFRUIT_IO_USERNAME)

    # Set to your Adafruit IO key.
    # Remember, your key is a secret,
    # so make sure not to publish it when you publish this code!
    config.ADAFRUIT_IO_KEY = config.COMMAND_LINE_ARGS[2]
    if config.ADAFRUIT_IO_KEY == 'YOUR_AIO_KEY' :
        print ('Invalid Adafruit.IO key')
        exit()
    else:
        print ('Adafruit.IO key: ', config.ADAFRUIT_IO_KEY)