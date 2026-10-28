import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.metrics import mean_squared_error

#step 1: Load image and convert to grayscale
img = io.imread('images.jpg')
gray = color.rgb2gray(img) # values between 0-1

plt.imshow(gray, cmap='gray')
plt.title("Original GrayScale Image")
plt.axis('off')
plt.show()

# step 2: Apply SVD
U, S , Vt = np.linalg.svd(gray, full_matrices=False)
# returns U and Vt with shapes (m,k) and (k,n) instead of full sq sizes(m,m) and

#step 3 : Function to reconstruct with top r values
def reconstruct(U, S, Vt, r):
    return U[:, :r] @ np.diag(S[:r]) @ Vt[:r, :]

#step 4: Choose r values
r1,r2,r3,r4,r5,r6,r7,r8,r9 = 5,20,50,100,150,200,500,800,1100

#Step 5 : Reconstruct images
img_r1 = reconstruct(U, S, Vt, r1)
img_r2 = reconstruct(U, S, Vt, r2)
img_r3 = reconstruct(U, S, Vt, r3)
img_r4 = reconstruct(U, S, Vt, r4)
img_r5 = reconstruct(U, S, Vt, r5)
img_r6 = reconstruct(U, S, Vt, r6)
img_r7 = reconstruct(U, S, Vt, r7)
img_r8 = reconstruct(U, S, Vt, r8)
img_r9 = reconstruct(U, S, Vt, r9)

plt.close('all')
plt.figure(figsize=(18, 12))

plt.subplot(3, 3, 1)
plt.imshow(img_r1, cmap='gray')
plt.title(f"r={r1}")
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(img_r2, cmap='gray')
plt.title(f"r={r2}")
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(img_r3, cmap='gray')
plt.title(f"r={r3}")
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(img_r4, cmap='gray')
plt.title(f"r={r4}")
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(img_r5, cmap='gray')
plt.title(f"r={r5}")
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(img_r6, cmap='gray')
plt.title(f"r={r6}")
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(img_r7, cmap='gray')
plt.title(f"r={r7}")
plt.axis('off')

plt.subplot(3, 3, 8)
plt.imshow(img_r8, cmap='gray')
plt.title(f"r={r8}")
plt.axis('off')

plt.subplot(3, 3, 9)
plt.imshow(img_r9, cmap='gray')
plt.title(f"r={r9}")
plt.axis('off')

plt.tight_layout()
plt.show()

#Step 6: Compute mse
mse_r1 = mean_squared_error(gray, img_r1)
mse_r2 = mean_squared_error(gray, img_r2)
mse_r3 = mean_squared_error(gray, img_r3)
mse_r4 = mean_squared_error(gray, img_r4)
mse_r5 = mean_squared_error(gray, img_r5)
mse_r6 = mean_squared_error(gray, img_r6)
mse_r7 = mean_squared_error(gray, img_r7)
mse_r8 = mean_squared_error(gray, img_r8)
mse_r9 = mean_squared_error(gray, img_r9)

print(mse_r1)
print(mse_r2)
print(mse_r3)
print(mse_r4)
print(mse_r5)
print(mse_r6)
print(mse_r7)
print(mse_r8)
print(mse_r9)
