import numpy as np
import matplotlib.pyplot as plt

def graph(name, points, bar_color):
  plt.plot(40)
  plt.bar(name, points, color=bar_color)
  plt.title(f'Fantasy Points Earned for {name}') # remove f-string for name when overlay is available [TODO]

  plt.savefig(f'{name}.png') # remove f-string for name when overlay is available [TODO]

  plt.show()