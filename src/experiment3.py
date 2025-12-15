# create a function skeleteon that will return a grid and probability density
# should take in x_min, x_max, num_points, l, d,wavelegnth
import numpy as np # import numpy in order to make array
import src.config as config # import config for variables


def make_screen(x_min,x_max,num_points):
    grid = np.linspace(x_min,x_max,num_points) #returns ordered x values within the specified range

    return grid

def compute_path(grid,slit):

    #y coordinate should be the slit location!!
    # slit 1 = config.d_1
    # slit 2 = config.d2
    if slit == 1:
        y = config.d_1
    elif slit == 2:
        y = config.d_2
    
    #compute paths using each x value in grid
    path = np.sqrt((config.L**2)+((grid-y)**2))
        
    #return an array of path to be used by the next function to calculate phase
    return path
    
def compute_phase(path_grid,wavelength):
    #calculates phase and returns grid of phases to calculate complex amplitude probability
    pi = np.pi
    k = (2*pi)/wavelength
    phase = path_grid *k

    return phase

def complex_probability_amplitude(phase_grid):
    #creating complex probability amplitude
    amplitude = np.exp(1j*phase_grid)
    return amplitude

def probability_distribution():
   
    #Computes the normalized probability distribution on the detection screen
    #for a two-slit experiment using free particle propagation.


    screen = make_screen(config.screen_min,config.screen_max,config.resolution)

   
    #take the screen and compute possible paths for both slits
    path_1 = compute_path(screen,1)

    path_2 = compute_path(screen,2)

    #compute phase for both slits
    wavelength = config.wavelength
    phase_1 = compute_phase(path_1,wavelength)
    phase_2 = compute_phase(path_2,wavelength)

    #compute complex probability amplitude for each slit
    a1 = complex_probability_amplitude(phase_1)
    a2 = complex_probability_amplitude(phase_2)

    #The probability distribution is obtained by summing the complex probability amplitudes 
    # from each slit and then applying the Born rule, after which normalization ensures the 
    # total detection probability equals one.
    a = a1 + a2
    p = np.abs(a)**2
    if np.sum(p) != 0:
        p = p / np.sum(p) # the probabilities will add to equal 1, ensuring the particles land somewhere on the screen
    else:
        p = p


    # return probability distribution and the screen 
    return screen,p


    



