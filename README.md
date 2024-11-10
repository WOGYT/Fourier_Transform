# Fourier_Transform

![Language](https://img.shields.io/badge/Language-JavaScript-ffcc14)
![Open Source](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

<br/>


Draw something using the Draw.py file and open the Fourier.html to see it redrawn using Discrete Fourier Transform (DFT)


## How is it working ?
### The Draw.py file:
This python file is composed of a window in which you can draw the design you want to transform. The program get the coordinates of the mouse while drawing which are then write in a file

### The fourier.js file:
To redrawn the design we are using a Descrete Fourier Transform (DFT). The DFT transform a sequence of number (in our case the coordinates of each point of the drawing) into a sequence of sinus and cosinus called Fourier Coefficients (FC). The DFT is defined by:

![equation](https://latex.codecogs.com/svg.image?X_n=&space;\sum_{n=0}^{N-1}&space;x_n&space;\cdot&space;\left&space;[&space;cos\left&space;(&space;\frac{2\pi}{N}kn&space;&space;\right&space;)&space;-i&space;\cdot&space;sin\left&space;(&space;\frac{2\pi}{N}kn&space;&space;\right&space;)&space;\right&space;])

### The sketch.js file:
As we can see, each FC is a complexe number, a + bi, where a and b are real number and where a is called the real part and bi the imaginary part. In our program, the real part is noted "re" and the imaginary part is noted "im". The real and imagninary parts are defined by:

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D%20re_n=%20x_n%20%5Ccdot%20cos%5Cleft%20(%20%5Cfrac%7B2%5Cpi%7D%7BN%7Dkn%20%20%5Cright%20))

![equation](https://latex.codecogs.com/gif.image?\dpi{110}&space;im_n=&space;x_n&space;\cdot&space;sin\left&space;(&space;\frac{2\pi}{N}kn&space;&space;\right&space;))

In order to avoid doing calculations with real numbers, we are drawing the x and y separately. 
To visualize the path of the design we are using circles. There are as many circles as there are fourier coefficients. 
To draw those circles, we need the frequency, which is the speed at which the circle will turn, noted "freq". 

![equation](https://latex.codecogs.com/gif.image?\dpi{110}&space;freq&space;=&space;k)

We also need the amplitude, which is the radius of the circle. The amplitude is defined by:

![equation](https://latex.codecogs.com/gif.image?\dpi{110}&space;amplitude&space;=&space;\sqrt{re^{2}&plus;im^{2}})

Finally, we need the phase, which is the angle at which the circle wil started drawing. The phase is defined by:

![equation](https://latex.codecogs.com/gif.image?\dpi{110}&space;phase&space;=&space;atan2(im,&space;re))

## Installation
