import sensor #引入sensor（感光元件）库

sensor.reset() #重置感光元件
sensor.set_pixformat(sensor.RGB565) #设置照片格式为RGB565
sensor.set_framesize(sensor.QVGA) #设置图像大小为QVGA
sensor.skip_frames(time = 1000) #跳过1秒内帧数

while(True):
    img = sensor.snapshot() #拍摄一张照片

    img.invert() #图像二值化

    img.set_pixel(0,0,(255,0,0)) #设置坐标（0，0）处像素为红色（255，0，0）
    print(img.get_pixel(0,0)) #获取坐标（0，0）处像素点

    print(img.width()) #获取图像宽度
    print(img.height())#获取图像高度
    print(img.format())#获取图像格式
    print(img.size())  #获取图像大小
