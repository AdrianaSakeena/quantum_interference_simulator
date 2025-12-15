# the number of particles controls statistical noise
num_particles = 5000

#width should control how spread out the particle impacts are on the screen
#small width = tight cluster near center
#large width = broad smeard distribution
# width - controls a classical probability distribution
#essentially the standard deviation
#smaller standard deviation corresponds to smaller distrubution
#larger standard deviation corresponds to larger smaller distribution
width = .5

#minimum x-value of the screen
screen_min = -5.0

#maximum x-value of the screen
screen_max = 5.0

#random number associated to run to make it reproducable
#affects reproduceability, not outcomes
random_seed = 42


#pixel size
#larger dx = coarse measurement
#samller dx = more precise measurement

dx = .05

#the detector resolution
#Your detector screen is divided into pixels of width dx, and you cannot distinguish
#... two particle hits whose positions differ by less than dx
bins = int((screen_max - screen_min)/dx)

# distance between slit centers
half_screen = (screen_max - screen_min)/2

d = 1.0
#the center of the left slit (negative side of screen)
d_1 = (d/2)*-1

#the center of the right slit (positive side of screen)
d_2 = (d/2)

# distance between slit and screen 
L = 10

#resolution
resolution = 4000

# wavelegnth
wavelength = 0.2