# Fourier_Transform

Draw something using the Draw.py file and open the Fourier.html to see it redrawn using Discrete Fourier Transform (DFT)

Preview on pascaaaal.com/Fourier

## How is it working ?
### The Draw.py file
This python file is composed of a window in which you can draw the design you want to transform. The program get the coordinates of the mouse while drawing which are then write in a file

### The fourier.js file
To redrawn the design we are using a Descrete Fourier Transform (DFT). The DFT transform a sequence of number (in our case the coordinates of each point of the drawing) into a sequence of sinus and cosinus called fourier coefficients. The DFT is defined by:
![equation](https://latex.codecogs.com/svg.image?X_n=&space;\sum_{n=0}^{N-1}&space;x_n&space;\cdot&space;\left&space;[&space;cos\left&space;(&space;\frac{2\pi}{N}kn&space;&space;\right&space;)&space;-i&space;\cdot&space;sin\left&space;(&space;\frac{2\pi}{N}kn&space;&space;\right&space;)&space;\right&space;])

