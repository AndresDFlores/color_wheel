from operator import itemgetter

from matplotlib import pyplot as plt
import numpy as np
import math

class ColorPicker:


    def __init__(self):
        pass



    def get_rgb(self, theta):

        #  theta (degrees) is the angle on a color wheel - assume angles as defined on a unit circle


        #  calculate RGB values based on the theta input
        def get_blue(theta):
            return 382.5*np.sin(((math.pi/180)*theta)-(2*math.pi/3))+127.5

        def get_red(theta):
            return 382.5*np.sin(((math.pi/180)*theta)-(2*math.pi/3)+((math.pi/180)*120))+127.5
        
        def get_green(theta):
            return 382.5*np.sin(((math.pi/180)*theta)-(2*math.pi/3)-((math.pi/180)*120))+127.5
        

        #  store calculated RGB values in a tuple
        rgb_calc = (get_red(theta), get_green(theta), get_blue(theta))


        #  cap each calculated RGB value at 255, which is the maximum RGB value
        #  store RGB in a class variable
        self.rgb = ()
        for color in rgb_calc:

            if color>255:
                color = 255
            elif color<0:
                color = 0

            color = float(color)
            self.rgb = self.rgb+(color,)



    def set_color_value(self, color_val=1):

        #  color val is a numerical value (float or int) between 0 and 1 to define a color's brightness
        #  lower color values (toward 0) are darker, higher color values (toward 1) are brighter


        #  ensure that color_val is a positive value between 0 and 1
        color_val = abs(color_val)
        if color_val>1:
            color_val = 1

        #  apply desired color_val to each RGB value
        return (color*color_val for color in self.rgb)



if __name__=='__main__':

    color_picker_class = ColorPicker()

    def get_python_color(rgb):

        python_rgb = [(1/255)*rgb_val for rgb_val in rgb]
        return tuple(python_rgb)


    #  init figures
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()


    #  lower values (as low as 0)=darker, higher values (up to 1)=lighter
    color_vals = np.arange(0,1.1,0.1)


    #  iterate through each angle in the circle
    for wheel_angle in np.arange(0, 360):  
        color_picker_class.get_rgb(theta=wheel_angle)


        #  iterate through color values
        for val in color_vals:
            rgb_color = color_picker_class.set_color_value(color_val=val)

            #  convert RGB code to Python syntax values
            python_rgb = get_python_color(rgb_color)

            #  plot colors
            ax1.scatter(wheel_angle, val, color=python_rgb)

            #  plot RGB decomposition
            ax2.scatter(wheel_angle, python_rgb[0]*255, s=3, color=(1, 0, 0))
            ax2.scatter(wheel_angle, python_rgb[1]*255, s=3, color=(0, 1, 0))
            ax2.scatter(wheel_angle, python_rgb[2]*255, s=3, color=(0, 0, 1))


    #  format figure 1
    ax1.set_title('CALCULATED COLOR WHEEL')
    ax1.set_xlabel('WHEEL ANGLE')
    ax1.set_ylabel('COLOR VALUE (Darker/Lighter)')


    #  format figures 2
    ax2.set_title('DECOMPOSED RGB')
    ax2.set_xlabel('WHEEL ANGLE')
    ax2.set_ylabel('RGB VALUE')


    #  save figures
    fig1.savefig('calculated_colors_plotted.png', dpi=400)
    fig2.savefig('decomposed_rgb_plotted.png', dpi=400)

