import numpy as np
class Convertinator:

    def str2float(string):
        return float(string.replace(',','.'))

    def float2str(number):
        return str(number)

    def isStringElementEmpty(elements):    
        return any([element == '' for element in elements])


    def wavelength2frequency(wavelength):
        c = 299.792458
        return c/wavelength

    def frequency2wavelength(frequency):        
        c = 299.792458
        return c/frequency

    def wavelength2omega(wavelength):
        return Convertinator.wavelength2frequency(wavelength)*2*np.pi

    def omega2wavelength(omega):        
        return Convertinator.frequency2wavelength(omega)/(2*np.pi)

    def energy2wavelength(energy):        
        h = 4.135667696 #eV.fs
        return Convertinator.frequency2wavelength(h/energy)

    def wavelength2energy(wavelength):
        h = 4.135667696 #eV.fs
        return Convertinator.wavelength2frequency(wavelength)*h

    def omega2energy(omega): 
        hbar = 6.582119569e-1 #eV.fs  
        return hbar*omega
    def energy2omega(energy): 
        hbar = 6.582119569e-1 #eV.fs  
        return energy/hbar