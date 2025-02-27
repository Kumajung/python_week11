# 5. การคำนวณดอทโปรดักต์ (Dot Product)
# ดอทโปรดักต์ของเวกเตอร์สองตัวสามารถคำนวณได้ดังนี้
# คำนวณดอทโปรดักต์
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# กำหนดเวกเตอร์ a และ b
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# คำนวณผลคูณดอท
dot_product = np.dot(vector_a, vector_b)
print("ผลคูณดอท:", dot_product)

# สร้างกราฟ 3 มิติ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# พล็อตเวกเตอร์ a
ax.quiver(0, 0, 0, vector_a[0], vector_a[1], vector_a[2], color='r', label='Vector a')

# พล็อตเวกเตอร์ b
ax.quiver(0, 0, 0, vector_b[0], vector_b[1], vector_b[2], color='b', label='Vector b')

# ตั้งค่าขอบเขตของกราฟ
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title("Vectors a and b along with their dot product.")
plt.show()

# สร้างกราฟผลคูณดอท
plt.figure(figsize=(6, 6))
plt.bar(["Dot product."], [dot_product])
plt.title("The dot product of vectors a and b.")
plt.xlabel("Dot product.")
plt.ylabel("Value")
plt.show()