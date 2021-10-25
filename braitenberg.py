"""braitenberg controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


TIMESTEP = 64
MAX_SPEED = 10


def run_robot(robot):
   
   #Enable motors
    wheels = []
    wheelsName = ['wheel1','wheel2','wheel3','wheel4']
    for ind in range(4):
        wheels.append(robot.getMotor (wheelsName[ind]))
        wheels[ind].setPosition (float('inf'))
        wheels[ind].setVelocity(0.0)
    
    #Enable light sensors
    light_sensors = []
    light_sensors_names = ['ls_left', 'ls_right']
    for ind in range (2):
        light_sensors.append(robot.getLightSensor(light_sensors_names[ind]))
        light sensors[ind].enable(TIMESTEP)
    
    
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:
        # Read the sensors:
        left_light_val = light_sensors[0].getValue()
        right_light_val = light_sensors[1].getValue()
        
    
        # Process sensor data here.
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED
        # Enter here functions to send actuator commands, like:
        # wheel1 and wheel3 -> left speed
        wheels[0].setVelocity (left_speed)
        wheels[2].setVelocity (left_speed)
        # wheel2 and wheel 4 -> right speed

        wheels[1].setVelocity (right_speed)
        wheels[3].setVelocity (right_speed)
    

if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)
