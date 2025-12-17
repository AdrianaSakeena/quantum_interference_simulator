# # import simulate to use hit_simulator()
import src.config as config # import config to use variables
import src.plot as plot # impot plot to display plot of values
from matplotlib import pyplot as plt
import numpy as np # important numpy to create random seed to ensure reproducability
import src.experiment4 as exp4

def main():
    #np.random.seed(config.random_seed)
    #showing probability distribution plot
    screen,p_finite = exp4.probability_distribution()
    plot.plot_probability_distribution(screen,p_finite)
    





    
    #plot.plot_probability_distribution(screen,p)
    
    
              
    

   
    


if __name__ == "__main__":
    main()