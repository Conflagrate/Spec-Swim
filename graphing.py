import numpy as np
import matplotlib.pyplot as plt

def graph_results(name, points, bar_color):
  plt.plot(40)
  plt.bar(name, points, color=bar_color)
  plt.title(f'Fantasy Points Earned for {name}')

  plt.savefig(f'{name} PLOT.png')

  plt.show()

  return 'Finished graphing.'