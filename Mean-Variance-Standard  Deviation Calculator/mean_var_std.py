import numpy as np

def calculate(list):

    if (len(list)<9):
      # print("lenght = ",len(array))
      raise ValueError("List must contain nine numbers.")
    else:
      arr = np.array(list).reshape((3,3))

      mean = [(np.mean(arr, axis=0)).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]

      var = [(np.var(arr, axis=0)).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]

      std = [(np.std(arr, axis=0)).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]

      maxx = [(np.max(arr, axis=0)).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)]

      minn = [(np.min(arr, axis=0)).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)]

      summ = [(np.sum(arr, axis=0)).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]

      calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': maxx,
        'min': minn,
        'sum': summ
      }

      return calculations