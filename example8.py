# 8. การคูณเมทริกซ์ด้วยสเกลาร์
# การคูณเมทริกซ์ด้วยสเกลาร์ทำได้โดยการคูณแต่ละองค์ประกอบของเมทริกซ์ด้วยสเกลาร์
# คูณเมทริกซ์ด้วยสเกลาร์

# สร้างเมทริกซ์สองตัว
import numpy as np
import matplotlib.pyplot as plt

# กำหนดเมทริกซ์ A
matrix_a = np.array([[1, 2], [3, 4]])

# กำหนดสเกลาร์
scalar = 2

# ปรับขนาดเมทริกซ์
scaled_matrix = scalar * matrix_a
print("A scaled matrix.:")
print(scaled_matrix)

# สร้างกราฟ
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# กราฟเมทริกซ์ A
axs[0].imshow(matrix_a, cmap='Blues', interpolation='nearest')
axs[0].set_title("Matrix A")

# กราฟเมทริกซ์ที่ถูกปรับขนาด
axs[1].imshow(scaled_matrix, cmap='Blues', interpolation='nearest')
axs[1].set_title("A scaled matrix.")

plt.show()