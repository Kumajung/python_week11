# 10. การคำนวณดีเทอร์มิแนนต์ของเมทริกซ์
# ดีเทอร์มิแนนต์ของเมทริกซ์สามารถคำนวณได้โดยใช้ np.linalg.det
# คำนวณดีเทอร์มิแนนต์
import numpy as np
import matplotlib.pyplot as plt

# สร้างเมทริกซ์ A
matrix_a = np.array([[1, 2], [3, 4]])

# คำนวณดีเทอร์มิแนนต์
determinant = np.linalg.det(matrix_a)
print("ดีเทอร์มิแนนต์ของเมทริกซ์ A:", determinant)

# สร้างเวกเตอร์ฐานมาตรฐาน
i_hat = np.array([1, 0])  # เวกเตอร์ i
j_hat = np.array([0, 1])  # เวกเตอร์ j

# แปลงเวกเตอร์โดยใช้เมทริกซ์ A
transformed_i = matrix_a @ i_hat
transformed_j = matrix_a @ j_hat

# พล็อตเวกเตอร์
fig, ax = plt.subplots()
ax.quiver(0, 0, i_hat[0], i_hat[1], color='r', angles='xy', scale_units='xy', scale=1, label='i-hat')
ax.quiver(0, 0, j_hat[0], j_hat[1], color='b', angles='xy', scale_units='xy', scale=1, label='j-hat')
ax.quiver(0, 0, transformed_i[0], transformed_i[1], color='r', angles='xy', scale_units='xy', scale=1, alpha=0.5, label='Transformed i-hat')
ax.quiver(0, 0, transformed_j[0], transformed_j[1], color='b', angles='xy', scale_units='xy', scale=1, alpha=0.5, label='Transformed j-hat')

# ตั้งค่าขอบเขตของกราฟ
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend()

plt.title("Vector transformation by a matrices. A")
plt.show()

# สร้างกราฟเมทริกซ์ A
plt.figure(figsize=(6, 6))
plt.imshow(matrix_a, cmap='Blues', interpolation='nearest')
plt.title("matrices A")
plt.colorbar()
plt.show()

# สร้างกราฟดีเทอร์มิแนนต์
plt.figure(figsize=(6, 6))
plt.bar(["Determinant."], [determinant])
plt.title("The determinant of a matrices. A")
plt.ylabel("Value")
plt.show()