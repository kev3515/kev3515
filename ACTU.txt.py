#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:09:27 2022

@author: kevinzhang
"""

import xlwt

import numpy as np

f = open('actu_0907.txt','r')

data_raw = f.readlines()

block = []

for i in range(len(data_raw)):
   
    if '+CGPSINFO' in data_raw[i]:
       
        block.append(i)
        
block.append(len(data_raw))    
        
len_piece = len(block) - 1

piece = []

for i in range(0, len(block) - 1):
   
    piece.append( data_raw[block[i]:block[i+1]] )
    

    
X_total = []
Y_total = []
Z_total = []
IMU_logic_total = []
Noise_total = []
Noise_logic_total = []    

for block in range(len(piece)):
    
    data = piece[block]
    
    print('******' + str(block))
    
    X = []
    Y = []
    Z = []
    IMU_logic = []
    Noise = []
    Noise_logic = []  
    
    for i in range(len(data)):
        
        if 'Acceleration_long[sample-01]:' in data[i]:
            
            x = []
            y = []
            z = []
            
            # print(i)
            
            for count in range(i,i+5):
                
                x.append(float(data[count].split('x = ')[1].split(' y = ')[0]))
                y.append(float(data[count].split('y = ')[1].split(' z = ')[0]))
                z.append(float(data[count].split('z = ')[1]))
                
            flag = 0
            
            for j in range(1,5):
                
                if x[j] >= 0.00001 * 1 or y[j] >= 0.00001 * 1 or z[j] >= 0.00001 * 1:
                    
                    flag = 1
                    
                    break
                    
                else:
                    flag = 0
                    
                    
                    
            if flag == 1:
                
                IMU_logic.append(flag)
                
            else:
                
                IMU_logic.append(flag)

                
            X.extend(x)
            Y.extend(y)
            Z.extend(z)
            
            # print(len(X))
            # print(x_period)
            # print('*****')
            # print(x[j:j+20])
            print(len(X))
            
        if 'noise[sample-01][data-01]' in data[i]:
            
            noise_max = []
            
            for count in range(i,i+10):
                
                noise_array = data[i].split('= ')
                del(noise_array[0])
                
                for j in range(len(noise_array)):
                    
                    noise_array[j] = abs(float(noise_array[j].split(' ')[0]) - 2000)
                    
                noise_max.append(max(noise_array))
                
                noise_mean = sum(noise_max)/len(noise_max)
            
            Noise.append(noise_mean)
            
            if noise_mean >= 30:
                
                Noise_logic.append(1)
                
            else:
                
                Noise_logic.append(0)
                
                
    X_total.append(X)
    Y_total.append(Y)
    Z_total.append(Z)
    IMU_logic_total.append(IMU_logic)
    Noise_total.append(Noise)
    Noise_logic_total.append(Noise_logic)
            
            
                
            
            
            
                
                
#             # Xa = np.array(x)                
#             # sb = np.var(Xa)
               

workbook = xlwt.Workbook(encoding= 'ascii')

for i in range(len(X_total)):
    
    worksheet = workbook.add_sheet("Result"+str(i))
    
    worksheet.write(0,0, 'X_acc')
    worksheet.write(0,1, 'Yacc')
    worksheet.write(0,2, 'Zacc')
    worksheet.write(0,3, 'Noise')
    worksheet.write(0,4, 'Motion')
    worksheet.write(0,5, 'Noisy')
    
    
    for j in range(len(X_total[i])):
        
        worksheet.write(j+1,0, float(X_total[i][j]))
        
        worksheet.write(j+1,1, float(Y_total[i][j]))
        
        worksheet.write(j+1,2, float(Z_total[i][j]))
        
    for j in range(len(IMU_logic_total[i])):
        
        worksheet.write(j+1,3, float(Noise_total[i][j]))
        
        worksheet.write(j+1,4, float(IMU_logic_total[i][j]))
        
        worksheet.write(j+1,5, float(Noise_logic_total[i][j]))
    
# for i in range(len(IMU_logic)):
    
#     worksheet.write(i,3, float(IMU_logic[i]))
    

    
# for i in range(len(Noise_logic)):
    
#     worksheet.write(i,5, float(Noise_logic[i]))

workbook.save("ACTU_0907-2.xls")       

       
# acc_list = []
# noise_list = []
# flight_status = []
       
# for item in clean_data:
   
#     if 'Motion' in item:
       
#         if 'NOT Motion' in item:
#             acc_list.append(0)
#         else:
#             acc_list.append(1)
       
       
#     elif 'average_noise' in item:
       
#         noise = item.split('[')[1]
       
#         noise = noise.split(']')[0]
       
#         if float(noise) >= 30:
           
#             noise_list.append(1)
           
#         else:
           
#             noise_list.append(0)
       
#     elif 'Aircraft' in item:
       
#         if 'OFF' in item:
           
#             flight_status.append(0)
           
#         else:
           
#             flight_status.append(1)


# # import matplotlib.pyplot as plt

# # plt.plot(noise_list,label='Acceleration')

# # plt.show()           


           