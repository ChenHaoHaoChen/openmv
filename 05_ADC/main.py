from pyb import Pin,ADC,delay  #从pyb模块中引入Pin,ADC,delay

adc_p6 = ADC('P6')  #P6引脚设置为模数转换引脚
                    #注：只有P6引脚可作模数，数模转换引脚
while(True):
    value = adc_p6.read()  #读取P6引脚电压，并转换为数字量，范围0~4095
    voltage = round((value*3.3)/4095,2)  #电压保留小数点后两位
    print('ADC = %fV'%voltage)  #输出电压
    delay(500)
