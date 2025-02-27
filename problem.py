import numpy as np
import matplotlib.pyplot as plt

# กำหนดเวกเตอร์ u และ v
u = np.array([7, 6])
v = np.array([2, 9])

# คำนวณผลรวมของเวกเตอร์
result = u + v
print("ผลคูณของเวกเตอร์ u ด้วยสเกลาร์ v คือ ", result)

# ตั้งค่ากราฟ
fig, ax = plt.subplots()
ax.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r', label='u')
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='v')
ax.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1, color='g', label='u + v')

# ตั้งค่าขอบเขตของกราฟ
ax.set_xlim(-2, 5)
ax.set_ylim(-1, 10)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle='--', linewidth=0.5)

# เพิ่มคำอธิบาย
ax.legend()
plt.title("Vector Addition: u + v")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# แสดงกราฟ
plt.show()