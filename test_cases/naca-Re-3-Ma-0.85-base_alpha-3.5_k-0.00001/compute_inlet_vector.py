#!/usr/bin/python

import numpy as np

U_in = 291.97
angle_rad = 3.5 * np.pi / 180.0
inlet_dir = np.asarray([1.0, np.tan(angle_rad)])
inlet_dir /= np.linalg.norm(inlet_dir)
inlet_vel = inlet_dir * U_in
print(inlet_vel)

# consistency check
U_ref = np.asarray([U_in, 0])
prod = inlet_vel.dot(U_ref) / np.linalg.norm(U_ref) / np.linalg.norm(inlet_vel)
print(np.arccos(prod)*180/np.pi)
