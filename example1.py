# ตัวอย่างที่ 1 การสร้างเวกเตอร์ใน Python
# เราสามารถสร้างเวกเตอร์ใน Python โดยใช้ list หรือ numpy array
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_2d_vector(vector):
    fig, ax = plt.subplots()
    ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid()
    plt.title("2D Vector")
    plt.show()

def plot_3d_vector(vector):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title("3D Vector")
    plt.show()

# สร้างเวกเตอร์ 2D และ 3D
vector_2d = np.array([3, 4])
vector_3d = np.array([1, 2, 3])

# แสดงผลลัพธ์
print("2D Vector:", vector_2d)
plot_2d_vector(vector_2d)

print("3D Vector:", vector_3d)
plot_3d_vector(vector_3d)
