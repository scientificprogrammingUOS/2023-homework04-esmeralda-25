import numpy as np

def strange_pattern(shape):
    # your code, delete pass
    n ,m = shape
    sp = np.zeros(shape=(n,m), dtype=bool)
    sp[::3,::3]=True
    sp[1::3,2::3]=True
    sp[2::3,1::3]=True
    
    return sp

if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern(8,8))
