import src.simulate as sim # import simulate to use hit_simulator()
import src.config as config # import config to use variables
import src.plot as plot # impot plot to display plot of values
import numpy as np # important numpy to create random seed to ensure reproducability


def main():
    np.random.seed(config.random_seed)
    
    values = sim.hit_simulator()
    values_plot = plot.plot_maker(values)

if __name__ == "__main__":
    main()