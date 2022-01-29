import sensor, image, time
import ustruct
from pyb import LED
from pyb import UART

low_threshold = ((29, 62, 30, 88, -24, 77))
red_led   = LED(1)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
#sensor.set_windowing([0,20,80,40])
sensor.skip_frames(time = 2000)

clock = time.clock()
uart = UART(4,115200)   #定义串口4变量
uart.init(115200, bits=8, parity=None, stop=1)  #8位数据位，无校验位，1位停止位

def sending_data(cx,cy):
    global uart;
    #frame=[0x2C,18,cx%0xff,int(cx/0xff),cy%0xff,int(cy/0xff),0x5B];
    #data = bytearray(frame)
    data = ustruct.pack("<bbhhb",              #格式为俩个字符俩个短整型(2字节)
                   0x2C,                       #帧头1
                   0x12,                       #帧头2
                   int(cx), # up sample by 4    #数据1
                   int(cy), # up sample by 4    #数据2
                   0x5B)
    uart.write(data);   #必须要传入一个字节数组

while(True):
    red_led.on()
    clock.tick()
    img = sensor.snapshot()    #保存图片
    img.binary([low_threshold])  #二值化处理
    line = img.get_regression([(100, 92, -5, 6, -3, 7)], robust = True) #线性回归
    if (line):
        img.draw_line(line.line(), color = 127)
        rho_err = abs(line.rho())-img.width()/2  #线与图像中央偏移距离
        print(rho_err)
        if line.theta()>90:
            theta_err = line.theta()-180
        else:
            theta_err = line.theta()
        #print(theta_err)
        sending_data(theta_err,rho_err)



