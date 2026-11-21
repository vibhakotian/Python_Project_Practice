import time
import os
print('This is screen')
screen_width=100
screen_height=10
x_axis_for_dvd=5
y_axis_for_dvd=2
dvd_direction=1
dvd_direction1=1
max_x=screen_width-5
max_y=screen_height-1
counter=0
x=0
while x<100:
  os.system('cls')
  print('-'*screen_width)
  for i in range(screen_height):
      if i==y_axis_for_dvd:
              print('|'+' '*x_axis_for_dvd+'DVD'+' '*(screen_width-5-x_axis_for_dvd)+'|')
        
             
      else:
           print('|'+' '*(screen_width-2)+'|')

  y_axis_for_dvd+=dvd_direction1*3
  x_axis_for_dvd+=dvd_direction*3        
  if x_axis_for_dvd>=max_x:
        x_axis_for_dvd=max_x
        dvd_direction=-1
  elif x_axis_for_dvd<=0:
       dvd_direction=1
       x_axis_for_dvd=0
  if y_axis_for_dvd>=max_y:
       y_axis_for_dvd=max_y
       dvd_direction1=-1
  elif y_axis_for_dvd<=0:
       dvd_direction1=1
  
 

  print('-'*screen_width)
  time.sleep(0.2)
  
     
  
  x=x+1


  