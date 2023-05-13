import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):

    numeric_types = (int,float)
    values = [loc, scale, lower_bound, upper_bound]
    for val in values:    
        if not isinstance(val, numeric_types):
            raise ValueError('All parameter values have to be of type int or float')
    
    if not lower_bound < upper_bound:
        raise ValueError('The value of lower_bound has to be larger that the value of upper_bound')
    
    gaussian_array = np.random.normal(loc, scale, size = 100)
    mask_gaussian_array = (gaussian_array <= upper_bound) & (gaussian_array >= lower_bound)
    gaussian_array = gaussian_array[mask_gaussian_array]
    
    mean = 0
    std = 0
    if len(gaussian_array) > 0:
        mean = np.mean(gaussian_array)
        std = np.std(gaussian_array)

    return (mean, std)


if __name__ == "__main__":
    print(gaussian_analysis(7,4,0,1))

