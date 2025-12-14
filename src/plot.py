# import matplotlib in order to generate plot of hits
from matplotlib import pyplot as plt

#import hit_simulator from simulate.py for x values for plot
import src.simulate as sim

#import config for variables
import src.config as config


#create a function that plots a graph based on the given x values from the hit simualator

def plot_maker(hits):
    # hits are x values from hit_simulator
    #the number "bins" is the amount of groups the x values will be put into
    # density = True, means were are modeling using the physics interpretation
    #we will be looking at the probability that a particle will hit a particular x value

    plt.hist(hits,bins = config.bins,density = True)
    plt.xlim(config.screen_min,config.screen_max)
    plt.xlabel("position")
    plt.ylabel("Probability Density")
    plt.show()
