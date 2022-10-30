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
      trajectory['s'].append(float(vals[0]))
      trajectory['dot_s'].append(float(vals[1]))

  max_velocity = {'s': [], 'dot_s_max_vel': [], 'dot_s_max_acc': []}
  with open('build/maxVelocity.txt', 'r') as f:
    for line in f:
      vals = line.strip().split()
      if len(vals)!=3:
        logging.error("vals={}".format(vals))
      max_velocity['s'].append(float(vals[0]))
      max_velocity['dot_s_max_acc'].append(float(vals[1]))
      max_velocity['dot_s_max_vel'].append(float(vals[2]))
  plt.figure()
  plt.plot(max_velocity['s'], max_velocity['dot_s_max_acc'], 'b', linewidth=0.5, marker='o', markersize=1, label='Acceleration Limit Curve')
  plt.plot(max_velocity['s'], max_velocity['dot_s_max_vel'], 'g', linewidth=0.5, marker='o', markersize=1, label='Volicity Limit Curve')
  plt.plot(trajectory['s'], trajectory['dot_s'], 'r', linewidth=0.5, marker='o', markersize=1, label='Trajectory')
  plt.legend()
  plt.show()
