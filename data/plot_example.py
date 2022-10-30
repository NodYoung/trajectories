import os
import sys
import logging
import matplotlib.pyplot as plt
import json

PLOT_COLOR = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

def read_json_file(file_path):
  if not os.path.exists(file_path):
    raise ValueError("json file doesn't exist.")
  content = None
  with open(file_path, 'r') as f:
    content = json.load(f)
  return content

def plot_phase_plane(data, data_marker=True, linewidth=1, markersize=2):
  if not isinstance(data, dict):
    raise ValueError("data must be dict")
  plt.figure()
  i=-1
  for key in data:
    i += 1
    s = [d['s'] for d in data[key]]
    sdot = [d['sdot'] for d in data[key]]
    plt.plot(s, sdot, color=PLOT_COLOR[i], linewidth=linewidth, 
        marker='o' if data_marker else '', markersize=markersize, 
        label=key)
  plt.legend()
  plt.show()

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, format="%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
  content = read_json_file('example.json')
  plot_phase_plane({'Trajectory': content['trajectory'], 
                    'AccLimitCurve': content['max_acc'],
                    'VelLimitCurve': content['max_vel']})