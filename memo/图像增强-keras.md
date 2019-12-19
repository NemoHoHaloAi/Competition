# 使用keras进行图像增强

https://blog.csdn.net/jacke121/article/details/79245732

基本流程：
```python
from keras.preprocessing.image import ImageDataGenerator
from keras.datasets import mnist
from keras.utils import np_utils

datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=10,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range = 0.1, # Randomly zoom image 
        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=False,  # randomly flip images
        vertical_flip=False)  # randomly flip images

datagen.fit(X_train)

times = 5
bs = 10

ims = np.zeros(shape=(len(train_data)*times,28,28,1))
iml = [0]*(len(train_data)*times)

idx=0
for label in range(0,11):
    X_train_part = train_data[train_data.label==label].drop(["label"],axis = 1) 
    X_train_part = X_train_part / 255.0
    X_train_part = X_train_part.values.reshape(-1,28,28,1)
    Y_train_part = train_data[train_data.label==label].label.copy()
    print(len(X_train_part))
    
    data_iter = datagen.flow(X_train_part, Y_train_part, batch_size=bs)

    print(int(len(X_train_part)*times))
    for i in range(int(len(X_train_part)*times/bs)):
        x_batch, y_batch = data_iter.next()
        for j in range(len(x_batch)): # 注意batch的size不总是等于初始化时传入的bs
            ims[idx] = x_batch[j]
            iml[idx] = y_batch[j]
            idx += 1
#             plt.subplot(2,5,j+1)
#             plt.imshow(x_batch[j].reshape(28,28))
# plt.show()

ims = ims.reshape(-1,784) # ims中可能存在全为空的情况需要剔除，如果没有产生理想的batch size的话
print(idx,ims[0],iml[0])
```
