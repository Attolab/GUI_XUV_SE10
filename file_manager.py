from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget,QFileDialog)
import pathlib
import h5py
from numpy import array as npa
import sys, traceback
import numpy as np
import os
import re


class FileManager:
    def __init__(self, filename = None):
        self.filename = filename
        self.dataset_list= []
        # if filename:
        #     with h5py.File(self.filename, 'r') as file:
        #         self.keys = self.extractKeys(file)
        
        
    def print_grp_name(self,grp_name, object):        
        # print ('object = ' , object)
        # print ('Group =', object.name)
        dataset_list = []
        try:
            n_subgroups = len(object.keys())
            print ('Object is a Group')
        except:
            n_subgroups = 0
            print ('Object is a Dataset')
            dataset_list.append (object.name)            

    def get_keys(self,f):
        return [key for key in f.keys()]

    def list_keys(self,group):
        return group.keys()
# Create a list containing all the keys

    def list_keys(self,group):
        return group.keys()

    def get_dataset_keys(self,f):
        keys = []
        f.visit(lambda key: keys.append(key) if isinstance(f[key], h5py.Dataset) else None)
        return keys

    def get_values(self, f, keys):
        return [npa(f[key][0]) if len(f[key].shape) > 1 else npa(f[key]) for key in keys]        

    def get_type(self, value):
        return value.dtype

    def get_shape(self, value):
            return value.shape

    def extractValues(self,filename,keys):
        with h5py.File(filename, 'r') as file:
            return [self.get_values(file,key) for key in keys]  
        
    def extractType(self,filename,keys):
        with h5py.File(filename, 'r') as file:
            return [self.get_type(self.get_values(file,key)) for key in keys]    

    def extractShape(self,filename,keys):
        with h5py.File(filename, 'r') as file:
            return [self.get_shape(self.get_values(file,key)) for key in keys]    

    def extractKeys(self,filename):
        with h5py.File(filename, 'r') as file:
            return self.get_dataset_keys(file)

    def extractAll(self):
        with h5py.File(self.filename, 'r') as file:
            keys = self.extractKeys(file)
            values = get_values(self, file, keys)
            shape = values.shape
            dtype = values.dtype
        return keys,values,shape,dtype        
    def convertInput(self,inputs):
        return [input.decode('ISO-8859-1)') if input[0] == 80 else input for input in inputs]

    def Read_h5(self):
        with h5py.File(self.filename, 'r') as file:
            keys = self.get_dataset_keys(file)
            keys = self.convertInput(keys)
            data = npa(self.get_values(file, get_key_data(keys)))
            position = self.get_values(file, get_key_position(keys))[0]
            parameters = self.get_values(file, get_key_parameters(keys))
        return self.convert_h5(data,position,parameters)

    def convert_h5(self,data,position,parameters):
        delay = position * 0.635 / ( 2 * np.pi * 0.299792458)        
        t_vol = parameters[-2] * np.arange(data.shape[1])*1e9
        indexing = np.argsort(delay)
        delay = delay[indexing]
        data = data[indexing,:]
        return data.T,delay,t_vol



    def readCalibration(self):
        with open(self.filename, "r") as f:  
            file_content = f.read().split()
            if len(file_content) != 8:
                print('File non valid')
                return None
            else:
                headers = file_content[0:4]
                coeffs = file_content[4:8]
                [print(f'{headers[i]}: {coeffs[i]}') for i in range(3)]
                return [float(coeff) for coeff in coeffs]

    def writeCalibration(self,calibration_inputs):
        if self.filename == '':
            print('Filename is empty')
            return
        else:         
            with open(self.filename, "w") as f:       
                [f.write(letter+'\t') for letter in ['A','B','t0']]
                f.write('\n') 
                [f.write(item.text()+'\t') for item in calibration_inputs]
                # [f.write(str(coeff)) for coeff in self.getCalibration()]
            print(f'Calibration saved as {self.filename}')


    # Get key for data array
def get_key_data(keys):
    # Extract key data and associated index 
    key_data, key_data_index = zip(
        *[(key, int(re.search('(\d+)$', key)[0])) for key in keys if "Data/Y_axis/Averaged_data" in key])
    # List is not sorted so we sort it using the index
    ordering_index = np.argsort(key_data_index)
    # Return sorted key_data array
    return npa(key_data)[ordering_index]

# Get key for position array
def get_key_position(keys):
    return npa([key for key in keys if "StagePosition" in key])

# Get key for parameters
def get_key_parameters(keys):
    return npa([key for key in keys if "Scan_parameters" in key])

# def get_values(f, keys):
#     return [npa(f[key][0]) if len(f[key].shape) > 1 else npa(f[key]) for key in keys]
   



def main():
    from file_manager import FileReader as F
    import matplotlib.pyplot as plt
    p = F()
    folder = "/mnt/Q_drive/LIDyL/Atto/ATTOLAB/SE1/Data_Experiments/SE1_2022/2022-03-24/"
    filename = "scan_Neon_Neon_voltage_Voltage 1950V.h5"
    folder ='/home/cs268225/Documents/Python/GUI/FourierGUI/TestData/Dataset_20220415_002/'
    filename = 'Dataset_20220415_002.h5'
    folder = '/home/cs268225/Atto/ATTOLAB/SE1/Data_Experiments/SE1_2022/2022-04-20/'
    filename = 'test phase scan_2.h5'
    # fileReader = F(folder + filename).Read_h5()
    signal, position, parameters = F(folder + filename).Read_h5()
    delay = 2 * (position / 0.299792458)
    t_vol = parameters[-2] * np.arange(signal.shape[1])*1e6    
    # data, position, parameters = F(folder + filename)
    delay = 2 * (position / 0.299792458)
    t_vol = parameters[-1] * np.arange(signal.shape[1])
    plt.imshow(np.transpose(signal), aspect='auto')
    plt.show()


if __name__ == "__main__":
    main()