# import numpy to generate x values in a normal distribution
import numpy as np 

#import config for variables
import src.config as config

num = config.num_particles
sigma = config.width
left_slit_center = config.d_1
right_slit_center = config.d_2


def hit_simulator():

     #Simulates measurement hits by sampling from a normal distribution.
     # create two distributions corresponding to two slits

    #Returns: Array of simulated hit positions with two slits (two distributions)

    #creating first distribution corresponding to slit 1 on the left side of the screen
    #using floor division to ensure particles split evenly between two slits
    #half of the particles go through each slit because a particle has equal probability of going through each slit
    #... since we know nothing about the path each indivdual particle took
    values1 = np.random.normal(loc= left_slit_center,scale = sigma, size = num//2)
    values2 = np.random.normal(loc = right_slit_center,scale= sigma, size = num //2)

    #combine the two distributions into a single one to simulate the experiment
    values = np.concatenate([values1,values2])
    



  
    return values


