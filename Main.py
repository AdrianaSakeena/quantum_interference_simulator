# # import simulate to use hit_simulator()
import src.config as config # import config to use variables
import src.plot as plot # impot plot to display plot of values
from matplotlib import pyplot as plt
import numpy as np # important numpy to create random seed to ensure reproducability
import src.experiment3 as exp3

def main():
    #np.random.seed(config.random_seed)
    #showing probability distribution plot
    nonfinite_p = exp3.non_finite_probability_distribution()
    screen,p_finite = exp3.probability_distribution()

    #p1 = nonfinite probability distribution 
    #p2 = finite probability distribution

    #print overlay plot
    plot.plot_overlay(screen,nonfinite_p,p_finite)



    
    #plot.plot_probability_distribution(screen,p)
    
    
              
    

   
    


if __name__ == "__main__":
    main()