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

def simple_vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

# imagine a robot that starts from some known position and heading
# it does the following motions
# 1) drives forward 1 unit and up 1 unit (y, z)
# 2) turns 90 deg to the right
# 3) drives forward another 2 units (x)

# we get the position as
robot_position = (2, 1, 1)
print(f"robot_position: {robot_position}")

# we get the orientation as the quaternion x, y, z, w
z_axis_unit = (0, 0, 1)
robot_orientation = axisangle_to_q(z_axis_unit, -numpy.pi / 2)
print(f"robot_orientation: {robot_orientation}")

# if there is a laser mounted 1 unit above the pose center
laser_mount_position = (0, 0, 1)
# with an orientation pointed left with the quaternion x, y, z, w
laser_orientation = axisangle_to_q(z_axis_unit, numpy.pi / 2)
print(f"laser_orientation: {laser_orientation}")
# the points that the robot detects are in a 3x3 grid of points that form a square 1 unit apart
point_list = []
# first row
point_list.append((-1, 1, 1))
point_list.append((0, 1, 1))
point_list.append((1, 1, 1))
# second row
point_list.append((-1, 1, 0))
point_list.append((0, 1, 0))
point_list.append((1, 1, 0))
# third row
point_list.append((-1, 1, -1))
point_list.append((0, 1, -1))
point_list.append((1, 1, -1))

laser_position = simple_vec_add(robot_position, laser_mount_position)
print(f"laser_position: {laser_position}")

# translate the laser points to the local global pose by rotating the reverse of the orientations of the laser then robot
for point in point_list:
    laser_conj = q_conjugate(laser_orientation)
    robot_conj = q_conjugate(robot_orientation)
    reverse_laser_reverse_robot_pt = qv_mult(robot_conj, qv_mult(laser_conj, point))
    print(simple_vec_add(reverse_laser_reverse_robot_pt, laser_position))


top_left_point = (1, 2, 3)
(2, 2, 3)
(3, 2, 3)

(1, 2, 2)
middle_point = (2, 2, 2)
(3, 2, 2)

(1, 2, 1)
(2, 2, 1)
bottom_right_point = (3, 2, 1)
