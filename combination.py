import numpy as np 

# implement your function to combine two numpy arrays 

def combination(numpy_array_1, numpy_array_2, axis = 0):

    numpy_array_1 = numpy_array_1.squeeze()
    numpy_array_2 = numpy_array_2.squeeze()
    
    try:
        combined_array = np.concatenate((numpy_array_1, numpy_array_2), axis=axis)
        return combined_array
    except ValueError as e:
        raise ValueError(f'{e}')
    

if __name__ == "__main__":
    # use this for your own testing!
    numpy_array_1 = np.arange(12).reshape((3,4))
    numpy_array_2 = np.arange(4).reshape((1,4))
    arr = combination(numpy_array_1, numpy_array_2, axis = 0)
    print(arr)
