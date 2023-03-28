import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import h5py

def generate_signal(end:float, size:int = 100000, noise: float=0.1) ->np.ndarray:
    x = np.linspace(0,end,num = size)
    y = np.sin(x)
    nn = np.random.uniform(-noise,noise,size=len(x))
    return y+nn

def save_signal(file_name: Path, signal :np.ndarray)-> None:
    with h5py.File(f"{file_name}.hdf5","w") as f:
        ds = f.create_dataset("my_signal", data = signal)

def smooth_signal(signal:np.ndarray) -> None:
    tmp = np.empty(signal.shape[0] + 2, dtype=signal.dtype)
    tmp[1:-1] = signal
    tmp[0] = signal[0]
    tmp[-1] = signal[-1]
    signal += tmp[0:-2] + tmp[2:]
    signal /= 3.0

def der_signal(y:np.ndarray) -> np.ndarray:
    tmp = np.append(y,y[-1])
    y = tmp[1:] - tmp[:-1]
    return y

def sign_change(y: np.ndarray) :
    tmp = np.append(y,y[-1])
    y = tmp[1:] * tmp[:-1]
    return np.where(y < 0,1,0)

def peak_indexes(y: np.ndarray):
    return np.argwhere(y).flatten()

# y = np.array([1,2,1,2,1,2])
y =generate_signal(5,size=50, noise = 0.1)
# sns.lineplot(y)
smooth_signal(y)
sns.lineplot(y)
# plt.show()
y = der_signal(y)
# sns.lineplot(y)
y = sign_change(y)
sns.lineplot(y)
plt.show()
print(peak_indexes(y))
# save_signal(Path("signal"),y)
