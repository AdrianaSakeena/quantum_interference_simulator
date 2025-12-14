# import numpy to generate x values in a normal distribution
import numpy as np 

#import config for variables
import src.config as config




def hit_simulator():

     #Simulates measurement hits by sampling from a normal distribution.

    #Returns: Array of simulated hit positions

    values = np.random.normal(
    loc=0.0, # center of screen
    scale= config.width,    # this controls the smear
    size=config.num_particles
)

  
    return values


