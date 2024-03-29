# from: https://stackoverflow.com/questions/4870393/rotating-coordinate-system-via-a-quaternion

import math
import numpy
import quaternion

def q_mult(q1, q2):
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2

    return x, y, z, w

def q_conjugate(q):
    x, y, z, w = q
    return (-x, -y, -z, w)

def qv_mult(q1, v1):
    q2 = v1 + (0.0,)
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[:-1]

def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = math.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v

def axisangle_to_q(v, theta):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = math.cos(theta)
    x = x * math.sin(theta)
    y = y * math.sin(theta)
    z = z * math.sin(theta)
    return x, y, z, w

def q_to_axisangle(q):
    v, w = q[:-1], q[3]
    theta = math.acos(w) * 2.0
    return normalize(v), theta

q1 = -0.007, -0.015, -0.432, 0.902
v1 = -675, 423.318, 17.850

print(qv_mult(q1, v1))

q2 = -0.013868643555168, 0.006892854307608, 0.901973760745189, 0.431513017431241
v2 = -675, 423.318, 17.850

print(qv_mult(q2, v2))

v3 = -675.0, 423.3, 17.7
q3 = -0.013869, 0.006893, 0.901974, 0.431513

v4 = 0.05069, -0.01712, 0.139
q4 = 0.000698, 0.000437, 1.000000, 0.000437

p1 = -10, 0, 0
print(f"1) {qv_mult(q4, p1)}")

# A sequence of 90-degree rotations about the x, y, and z axes will return a vector on the y axis to its original position.
x_axis_unit = (1, 0, 0)
y_axis_unit = (0, 1, 0)
z_axis_unit = (0, 0, 1)
r1 = axisangle_to_q(x_axis_unit, numpy.pi / 2)
r2 = axisangle_to_q(y_axis_unit, numpy.pi / 2)
r3 = axisangle_to_q(z_axis_unit, numpy.pi / 2)

print(f"r1: {r1}")
print(f"r2: {r2}")
print(f"r3: {r3}")

v = qv_mult(r1, (0, 1, 0,))
print(v)
v = qv_mult(r2, v)
print(v)
v = qv_mult(r3, v)
print(v)

assert int(v[0]) == 0
assert int(v[1]) == 1
assert int(v[2]) == 0

# A sequence of 90-degree rotations about the y, x, and z axes will return a vector on the x axis to its original position.
r1 = axisangle_to_q(x_axis_unit, numpy.pi / 2)
r2 = axisangle_to_q(y_axis_unit, numpy.pi / 2)
r3 = axisangle_to_q(z_axis_unit, -numpy.pi / 2)

print(f"r1: {r1}")
print(f"r2: {r2}")
print(f"r3: {r3}")

v = qv_mult(r2, (1, 0, 0,))
print(v)
v = qv_mult(r1, v)
print(v)
v = qv_mult(r3, v)
print(v)

assert int(v[0]) == 1
assert int(v[1]) == 0
assert int(v[2]) == 0

# A sequence of 90-degree rotations about the z axis
r1 = axisangle_to_q(z_axis_unit, numpy.pi / 2)
r2 = axisangle_to_q(z_axis_unit, numpy.pi / 2)

print(f"r1: {r1}")
print(f"r2: {r2}")

v = qv_mult(r2, (1, 0, 0,))
print(v)
v = qv_mult(r1, v)
print(v)
