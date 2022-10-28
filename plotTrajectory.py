import logging
import matplotlib.pyplot as plt

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, format="%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
  trajectory = {'s':[], 'dot_s':[]}
  with open('build/trajectory.txt', 'r') as f:
    for line in f:
      vals = line.strip().split()
      if len(vals)!=2:
        logging.error("vals={}".format(vals))
      trajectory['s'].append(vals[0])
      trajectory['dot_s'].append(vals[1])

  max_velocity = {'s': [], 'dot_s1': [], 'dot_s2': []}
  with open('build/maxVelocity.txt', 'r') as f:
    for line in f:
      vals = line.strip().split()
      if len(vals)!=3:
        logging.error("vals={}".format(vals))
      max_velocity['s'].append(vals[0])
      max_velocity['dot_s1'].append(vals[1])
      max_velocity['dot_s2'].append(vals[2])
  plt.figure()
  plt.plot(trajectory['s'], trajectory['dot_s'], 'r', linewidth=1, marker='o', markersize=2, label='dot_s')
  plt.plot(max_velocity['s'], max_velocity['dot_s1'], 'g', linewidth=1, marker='o', markersize=2, label='dot_s1')
  plt.plot(max_velocity['s'], max_velocity['dot_s2'], 'b', linewidth=1, marker='o', markersize=2, label='dot_s2')
  plt.legend()
  plt.show()
