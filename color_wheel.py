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


    fig, ax = plt.subplots()

    color_vals = np.arange(0,1.1,0.1)

    for wheel_angle in np.arange(0, 360):  
        color_picker_class.get_rgb(theta=wheel_angle)

        for val in color_vals:
            rgb_color = color_picker_class.set_color_value(color_val=val)

            python_rgb = get_python_color(rgb_color)
            ax.scatter(wheel_angle, val, c = python_rgb)


    ax.set_title('CALCULATED COLOR WHEEL')
    ax.set_xlabel('WHEEL ANGLE')
    ax.set_ylabel('COLOR VALUE')

    plt.savefig('calculated_colors_plotted.png', dpi=400)
