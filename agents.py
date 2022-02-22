class Agent():
    def __init__(self,name = "",env = "",act = [],sens = [],metrics = []):
        self.name = name
        self.environment = env
        self.actuators = act
        self.sensors = sens
        self.metrics = metrics
    def printInfo(self):
        print("Name: " + str(self.name))
        print("Environment: " + str(self.environment))
        print("Actuators: " + str(self.actuators))
        print("Sensor: " + str(self.sensors))
        print("Metrics: " + str(self.metrics))
# Dog
my_dog = Agent("Dog","Real World",["Mouth","Paws"],["Eyes","Ears","Nose","Skin"],["Ability to Follow Commands","Finding an object based on smell","Successfully protects owner"])
# Phone Camera
my_camera = Agent("Phone Camera","Phone",["Filter", "Flash","Resolution adjusting"],["Lens","What the user wants to take picture of"],["Quality of image","Lighting of the image"])
# Voice Recognition System
voice_recognition_system = Agent("Intelligent AI System","The Program",["Speaker","Program Screen"],["Microphone"],["Sucessfully recognizes users voice"])
# Led Light Strip
my_led = Agent("LED_Light Strip","Room",["LED's"],["Music Frequency","User Input"],["Color based on music frequency"])
# Calculator
calculator_program = Agent("Calculator Program","The Device Itself",["Calcualtor Screen"],["Calculator Buttons"],["Speed of Calculation","Accuracy of Calculation"])

my_dog.printInfo()
my_camera.printInfo()
voice_recognition_system.printInfo()
my_led.printInfo()
calculator_program.printInfo()
