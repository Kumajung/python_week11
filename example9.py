# 9. การคูณเมทริกซ์
# การคูณเมทริกซ์ทำได้โดยใช้ฟังก์ชัน np.dot หรือ @
# คูณเมทริกซ์
import numpy as np
import matplotlib.pyplot as plt

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Product:")
print(matrix_product)

# สร้างกราฟ
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# กราฟเมทริกซ์ A
axs[0].imshow(matrix_a, cmap='Blues', interpolation='nearest')
axs[0].set_title("matrices A")

# กราฟเมทริกซ์ B
axs[1].imshow(matrix_b, cmap='Blues', interpolation='nearest')
axs[1].set_title("matrices B")

# กราฟผลคูณของเมทริกซ์ A และ B
axs[2].imshow(matrix_product, cmap='Blues', interpolation='nearest')
axs[2].set_title("The product of matrices A and B.")

plt.show()