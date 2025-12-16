# create a function skeleteon that will return a grid and probability density
# should take in x_min, x_max, num_points, l, d,wavelegnth
import numpy as np # import numpy in order to make array
import src.config as config # import config for variables


def slit_y_positions(y_center,slit_width,num_points):
    #creating an array of y values within 
    y_min = y_center - slit_width/2
    y_max = y_center + slit_width/2
    grid = np.linspace(y_min,y_max, num_points)
    return grid

def make_screen(x_min,x_max,num_points):
    grid = np.linspace(x_min,x_max,num_points) #returns ordered x values within the specified range

    return grid

#produce a 2d array where each entry is the distance from the slit_point to the screen point

def non_finite_path_lengths(screen_points,slit):
    if slit == 1:
        path = np.sqrt((config.L**2)+((screen_points)-config.d_1)**2)
    elif slit == 2:
        path =  np.sqrt((config.L**2)+((screen_points)-config.d_2)**2)

    return path


def path_length(screen_points, slit_points):

    #compute paths using each x value in screen_point and each y value in slit_points
    path = np.sqrt((config.L**2)+((screen_points[:,None]-slit_points[None,:])**2))
    #[:,None] = ensures proper shape of graph
        
    #return an array of paths to be used by the next function to calculate phase
    return path


def compute_phase(path_grid,wavelength):
    #calculates phase and returns grid of phases to calculate complex amplitude probability
    pi = np.pi
    k = (2*pi)/wavelength
    phase = path_grid *k

    return phase

def nonfinite_amplitude(phase_grid):
    amplitude = np.exp(1j*phase_grid)
    return amplitude


def complex_probability_amplitude(phase_grid,path_grid):
    #creating complex probability amplitude
    amplitude = np.exp(1j*phase_grid)/path_grid
    return amplitude


def non_finite_probability_distribution():
    #creating a probability distribution for points on graph will non-finite slit width

    #make screen of x values
    screen = make_screen(config.screen_min,config.screen_max,config.resolution)

    #make path lengths for each x value on the screen
    path_legnths_slit1 = non_finite_path_lengths(screen,1)
    path_legnths_slit2 = non_finite_path_lengths(screen,2)

    #find phases for each of the paths
    phase_1 = compute_phase(path_legnths_slit1,config.wavelength)
    phase_2 = compute_phase(path_legnths_slit2,config.wavelength)

    #compute amplitudes
    a1 = nonfinite_amplitude(phase_1)
    a2 = nonfinite_amplitude(phase_2)


    a = a1 + a2
    #compute probability using Born rule
    p = np.abs(a)**2

    if np.sum(p) != 0:
        p = p / np.sum(p) # the probabilities will add to equal 1, ensuring the particles land somewhere on the screen
    else:
        p = p

    return p




def probability_distribution():
   
    #Computes the normalized probability distribution on the detection screen
    #for a finite slit width,two-slit experiment using free particle propagation.

    #create an array of screen points
    screen_points = make_screen(config.screen_min,config.screen_max,config.resolution)

    #create arrays of points within the width of the slits
    slit1_points = slit_y_positions(config.d_1,config.slit_width,config.slit_samples)
    slit2_points = slit_y_positions(config.d_2,config.slit_width,config.slit_samples)
   
    #calculate path legnths for both slits
    path_lengths_slit1 = path_length(screen_points,slit1_points)
    path_lengths_slit2 = path_length(screen_points,slit2_points)


    #compute phase for both slits
    wavelength = config.wavelength
    phase_1 = compute_phase(path_lengths_slit1,wavelength)
    phase_2 = compute_phase(path_lengths_slit2,wavelength)

    #compute complex probability amplitude for each slit
    a1 = complex_probability_amplitude(phase_1,path_lengths_slit1)
    a2 = complex_probability_amplitude(phase_2,path_lengths_slit2)

    #The probability distribution is obtained by summing the complex probability amplitudes 
    # from each slit and then applying the Born rule, after which normalization ensures the 
    # total detection probability equals one.

    # sum across columns to get amplitude per screen point
    a1 = np.sum(a1,axis = 1)
    a2 = np.sum(a2,axis =1)

    #add amplitudes from both slits
    a = a1 + a2
    #compute probability using Born rule
    p = np.abs(a)**2

    if np.sum(p) != 0:
        p = p / np.sum(p) # the probabilities will add to equal 1, ensuring the particles land somewhere on the screen
    else:
        p = p


    # return probability distribution and the screen 
    return screen_points,p


    



