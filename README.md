# **DSP-Tasks**
  - Implementing Digital Signal Processing tasks for different signals
  - Use Python as programming language
  - Gui by tkinter library
  - Dealing with .txt files 

## Every Task's details
### **Task 1**
  ⦁ Read samples of a signal from a txt file and display it in both continuous and discrete representations.
  ⦁ Generate sinusoidal or cosinusoidal signals, the user should choose whether he wants cosine or sine, the amplitude A, the phase shift theta, the   
    analog frequency, and the sampling frequency needed. 
    
### **Task 2**
  ⦁	Addition: add input signals (any number) and display the resulting signal.
  ⦁	Subtraction: subtract input signals and display the resulting signal. 
  ⦁	Multiplication: multiply a signal by a constant value to amplify or reduce the signal amplitude. (If constant equals -1, then signal will be 
    inverted
  ⦁	Squaring: squaring a signal and displaying the resulting signal. 
  ⦁	Shifting: add to the signal a (+ve) or (-ve) constant. 
  ⦁	Normalization: normalize the signal from -1 to 1 or 0 to 1 depending on user choice. 
  ⦁	Accumulation of input signal    

### **Task 3**
  quantize an input signal (its samples), the application should ask the user for the needed levels or number of bits available (in case of number of 
  bits the application should compute from it the appropriate number of levels). Thereafter, the application should display the quantized signal and 
  quantization error besides the encoded signal
  
### **Task 4**
  ⦁	Apply Fourier transform to any input signal then display frequency versus amplitude and frequency versus phase relations after asking the user to 
    enter the sampling frequency in HZ.
  ⦁	Allow modification of the amplitude and phase of the signal components.
  ⦁	Allow signal reconstruction using IDFT. 
  ⦁	The frequency components should be saved in txt file in polar form (amplitude and phase). 
  ⦁	Read a txt file that contains frequency components in polar form and reconstructing the signal by IDFT. 
  
### **Task 5**
  ⦁	Computing DCT for a given input, display the result and the user can choose the first m coefficients to be saved in txt file. 
  ⦁	Remove DC component in time domain. 

### **Task 6**
⦁ Smoothing: Compute moving average y(n) for signal x(n) let the user enter the number of points included in averaging.
⦁ Sharpening: Compute and display y (n) which represents:
    - First Derivative of input signal  Y(n) = x(n)-x(n-1)
    - Second derivative of input signal Y(n)= x(n+1)-2x(n)+x(n-1) 
⦁ Delaying or advancing a signal by k steps. 
⦁ Folding a signal.
⦁ Delaying or advancing a folded signal.
⦁ Remove the DC component in frequency domain.

### **Task 7**
  convolve two signals.
  
### **Task 8**
  Correlation: compute normalized cross-correlation of two signals.
  
### **Practical Task**
  ⦁ Fast convolution. 
  ⦁ Fast correlation.


