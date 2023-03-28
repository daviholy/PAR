
from pathlib import Path
import numpy as np
import h5py

def generate_signal(end:float, size:int = 100000, noise: float=0.1) ->np.ndarray:
    x = np.linspace(0,end,num = size)
    y = np.sin(x)
    nn = np.random.uniform(-noise,noise,size=len(x))
    return y+nn

def save_signal(file_name: Path, signal :np.ndarray)-> None:
    with h5py.File(f"{file_name}.hdf5","w") as f:
        ds = f.create_dataset("my_signal", data = signal)

