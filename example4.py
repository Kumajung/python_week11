# ตัวอย่างที่ 4. การคูณเวกเตอร์ด้วยสเกลาร์
# การคูณเวกเตอร์ด้วยสเกลาร์ทำได้โดยการคูณแต่ละองค์ประกอบของเวกเตอร์ด้วยสเกลาร์
# คูณเวกเตอร์ด้วยสเกลาร์
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vector_a = np.array([1, 2, 3])
scalar = 2

# ปรับขนาดเวกเตอร์
scaled_vector = scalar * vector_a
print("Scaled Vector:", scaled_vector)

# สร้างกราฟ 3 มิติ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# พล็อตเวกเตอร์ a
ax.quiver(0, 0, 0, vector_a[0], vector_a[1], vector_a[2], color='r', label='Vector a')

# พล็อตเวกเตอร์ที่ถูกปรับขนาด
ax.quiver(0, 0, 0, scaled_vector[0], scaled_vector[1], scaled_vector[2], color='b', label='Scaled Vector')

# ตั้งค่าขอบเขตของกราฟ
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title("Vector a and the scaled vector.")
plt.show()