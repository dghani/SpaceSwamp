
class MQTTVars :
    def __init__(self, function, min, max):
        self.function = function
        self.min = min
        self.max = max

def mqtt_gen(aio, feedname, function_vars):
    #aio - reference to adafruit.io library to call publish function
    #feedname - text, name of adafruit.io feed to publish value to 
    #range - array[2] to define min/max values for values
    #function - set of functions to use to generate the value (rand, sin, cos, saw)
    print('test')