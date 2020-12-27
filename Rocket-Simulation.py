
#Modeling and simulation

#physical constans
airDensity=1.293
cdFins=0.01
cdBody=0.45
bodyArea=0.506E-3
finsArea=0.00496
dt=0.1
mass=(0.0340+0.0242)
gravity=9.80665

#variables 
time=0
height=0
velocity=0
acceleration=0
totalForce=0
index=1

#measured values of thrust
thrust=[0,6,14,4.9,4.5,4.3,4.4,4.3,4.4,4.3,4.3,4.3,4.3,4.3,4.4,4.3,4.3,4.3,4.4,0.0]

while(velocity >= 0):
    #force of drag of fins in newtons in opposite direction of velocity
    forceFinsDrag=(cdFins*airDensity*(finsArea)*(abs(velocity)**2))/2
    #force of drag of body in newtons in opposite direction of velocity
    forceBodyDrag=(cdBody*airDensity*(bodyArea)*(velocity**2))/2
    #force of gravity toward center of Earth
    forceGravity=mass*gravity
    #value from thrust curve array at this time
    if(index < 19):
        thrustCurveVal=thrust[index]
    else:
        thrustCurveVal=0

    #resolve forces
    totalForce=thrustCurveVal-(forceBodyDrag+forceFinsDrag+forceGravity)
    #acceleration
    acceleration=(totalForce/mass)
    #velocity change in meters per second in time dt
    velocityChange=(acceleration*dt)
    #new velocity after the dt time step
    velocity+=velocityChange
    #distance in meters moved in time dt
    distanceMoved=(velocity*dt)
    #new position after the dt time step
    height+=distanceMoved;
    #mass in each step
    mass=mass-(0.0001644*thrustCurveVal)
    #time advances
    time+=dt
    index+=1
    
    #print the time in seconds, height in meters, velocity in meters per second, acceleration in meters per second squared, force in newtons and mass in kilograms
    if (velocity > 0):
        print(format(time,'.2f'),', ',format(height,'.2f'),', ',format(velocity,'.4f'),', ',format(acceleration,'.4f'),', ',format(totalForce,'.4f'),', ',format(mass,'.4f'))

    
        
    
    
