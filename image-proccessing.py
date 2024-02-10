import numpy as np
import itertools
from matplotlib import pyplot as plt
import PIL.Image

#generate a random image of 64*64 pixels
img = np.zeros((64,64,3), np.uint8)
for i, j in itertools.product(range(64), range(64)):
    img[i,j] = [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]
plt.imshow(img)
plt.show()

#The frequency model - The Fourier transform
#The Fourier transform is a mathematical technique that transforms a function of time or space into a function of frequency.
#The Fourier transform of an image is a representation of the image in the frequency domain. It is used to analyze the frequency characteristics of an image.
#The Fourier transform of an image is calculated using the following formula:
#F(u,v) = ∑∑f(x,y) * e^(-j2π(ux/M + vy/N))
#where:
#F(u,v) is the Fourier transform of the image
#f(x,y) is the image
#e is the base of the natural logarithm
#j is the imaginary number
#2π is the circumference of a circle
#u is the horizontal frequency
#v is the vertical frequency
#M is the width of the image
#N is the height of the image
#x is the horizontal coordinate of the pixel
#y is the vertical coordinate of the pixel

#The Fourier transform of an image is a complex number. It has a magnitude and a phase. The magnitude is the amplitude of the frequency component, and the phase is the phase of the frequency component.
#The magnitude of the Fourier transform is called the magnitude spectrum. The phase of the Fourier transform is called the phase spectrum.
#The magnitude spectrum is a representation of the amplitude of the frequency components of the image. The phase spectrum is a representation of the phase of the frequency components of the image.
#The magnitude spectrum is used to analyze the frequency characteristics of an image. The phase spectrum is used to analyze the phase characteristics of an image.
#The magnitude spectrum is calculated using the following formula:
#|F(u,v)| = ∑∑|f(x,y)|
#where:
#F(u,v) is the Fourier transform of the image
#f(x,y) is the image
#|f(x,y)| is the magnitude of the pixel at (x,y)

#The Fourier transform
#f(x,y) (image)
Image = PIL.Image.open('_images/image_00018.jpg')
plt.imshow(Image)
plt.title('Image')
plt.show()

#F(u,v)
img = PIL.Image.open('_images/image_00018.jpg').convert('L') #convert image to greyscale
plt.imshow(img)
plt.title('Image greyscale')
plt.show()
FourierTransform = np.fft.fft2(np.array(img))
FourierTransform = np.fft.fftshift(FourierTransform)
magnitude_spectrum = 20*np.log(1+np.abs(FourierTransform))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.xlabel('u')
plt.ylabel('v')
plt.title('Magnitude Spectrum')
plt.show()

phase = np.angle(FourierTransform)
plt.imshow(phase, cmap = 'gray')
plt.xlabel('u')
plt.ylabel('v')
plt.title('Phase Spectrum')
plt.show()
