# import matplotlib in order to generate plot of hits
from matplotlib import pyplot as plt

#import hit_simulator from simulate.py for x values for plot
import src.simulate as sim

#import config for variables
import src.config as config


#create a function that plots a graph based on the given x values from the hit simualator

def classical_plot_maker(hits):
    # hits are x values from hit_simulator
    #the number "bins" is the amount of groups the x values will be put into
    # density = True, means were are modeling using the physics interpretation
    #we will be looking at the probability that a particle will hit a particular x value

    plt.hist(hits,bins = config.bins,density = True)
    plt.xlim(config.screen_min,config.screen_max)
    plt.xlabel("Screen Position X")
    plt.ylabel("Estimated Probability Density")
    plt.title("Double Slit Experiment (Classical Expected Result)")
    plt.show()
   

def plot_probability_distribution(screen,p):
    plt.figure() #start a new plotting window
    plt.plot(screen,p)#plot the probability distribution to the correct x values
    plt.xlabel("Screen Position x") 
    plt.ylabel("Probability P(x)")
    plt.title("Double Slit Interference (Which-Path Dectection)(Finite Slit-Width)")
    plt.grid(True) #add grid lines to the background so it is easier to see peaks and spacing
    plt.tight_layout() #improve spacing/presentation cleanup
    plt.show() #show the plot

def plot_overlay(screen,p1,p2):
    

    plt.figure()
    plt.plot(screen,p1,label = "Point-slit (slit width → 0)")
    plt.plot(screen,p2,label = "Finite-slit (width > 0)", alpha=0.85)
    #plotting difference between points on graph
    plt.plot(screen, p2 - p1, label="Finite Slit - Point Slit", linestyle="--")

    plt.xlabel("Screen Position X")
    plt.ylabel("Probability P(x)")
    plt.title("Point-Slit vs Finite-Slit")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()



              

    
