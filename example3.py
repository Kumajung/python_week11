# ตัวอย่างที่ 3 การบวกเวกเตอร์
# การบวกเวกเตอร์สามารถทำได้โดยการบวกองค์ประกอบที่ตรงกัน
# สร้างเวกเตอร์สองตัว
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# บวกเวกเตอร์
vector_sum = vector_a + vector_b
print("Vector Sum:", vector_sum)

# สร้างกราฟ 3 มิติ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# พล็อตเวกเตอร์ a
ax.quiver(0, 0, 0, vector_a[0], vector_a[1], vector_a[2], color='r', label='Vector a')

# พล็อตเวกเตอร์ b
ax.quiver(0, 0, 0, vector_b[0], vector_b[1], vector_b[2], color='b', label='Vector b')

# พล็อตผลรวมของเวกเตอร์ a และ b
ax.quiver(0, 0, 0, vector_sum[0], vector_sum[1], vector_sum[2], color='g', label='Vector Sum')

# ตั้งค่าขอบเขตของกราฟ
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title("Vector **a**, vector **b**, and the sum of vectors **a** and **b**.")
plt.show()