#importing wx files
import wx
 
import gui
import SwerleinFreq as alg
import numpy as np
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar
from openpyxl import Workbook
from openpyxl import load_workbook
import time
import datetime
import winsound
import visa
#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class CalcFrame(gui.Swerlein):
    
    #constructor
    def __init__(self,parent):
        #initialize parent class
        self.row_inc=2 #Always start at 2. The 1 row has the column titles
        try:
            alg.OnStart(self,self.Port.GetValue())
        except Exception:
            pass
        gui.Swerlein.__init__(self,parent)

    def RunFunc(self,event):
        #Create a new workbook in Excel.
        self.date=str(datetime.date.today())
        filename='data'+str(self.date)+str(self.Excel_Filename.GetValue())+'.xlsx'
        #Comment out following three lines if wanting to continue working in an existing Excel file.
        #Remember to change the filename parameter initialized previously to the existing filename
        #As well as changing self.row_inc to the last+1 elemt in the existing file
        wb = Workbook()
        wb.template=False
        wb.save(filename)
        self.filename=filename
        remote = visa.ResourceManager() #Gets remote access of the 5730A Calibrator 
        supply = remote.open_resource('GPIB0::16::INSTR')
        
        Acdc = self.ACDC.GetValue()
        Ac = self.AC.GetValue()
        Mean = self.MEAN.GetValue()
##         Mem = self.memory.GetValue()
        
        alg.OnStart(self,self.Port.GetValue())
        n = int(self.NumReadings.GetValue())
        wb=load_workbook(self.filename) #Open Excel file
        ws=wb.active #Make it active to work in
        #Add tiles to the columns
        ws.cell(row=1,column=1,value="Voltage")
        ws.cell(row=1,column=2,value="Bw_corr")
        ws.cell(row=1,column=3,value="Frequency")
        ws.cell(row=1,column=4,value="# of Samples")
        ws.cell(row=1,column=5,value="Sample Spacing")
        ws.cell(row=1,column=6,value="# of 1/Freq to Sample")
        ws.cell(row=1,column=7,value="# of bursts")
        ws.cell(row=1,column=8,value="Parameters Forced?")
        ws.cell(row=1,column=9,value="Time")
        wb.template=False #Make sure Excel file is saved as document not template
        wb.save(self.filename) #Save file with same name
        
        voltage_list=[0.65,0.512,0.001,1.0,0.023]
        #[0.11,0.179,0.201,0.250,0.293,0.001,0.023,0.041,0.065,0.084,0.321,0.369,0.444,0.512,0.583,0.607,0.722,0.821,0.908,0.937,1.00,1.102,1.142]
        for v in voltage_list:
            if self.CodeValidation.GetValue()==True:
                query_file = open("Code_Validation"+self.Version+str(self.date)+".txt","a") #Create code_validation in txt file.
                query_file.write("\n ---------------------"+str(v)+"V "+str(self.date)+"---------------------\n")
                query_file.close()
            supply.write("OUT "+str(v)+"V,200.0HZ")
            for i in range (0,n):
                alg.run(self,float(self.Harmonics.GetValue()),float(self.Bursts.GetValue()),Acdc,Ac,Mean,self.row_inc,self.filename )
                i = i+1
                self.row_inc = self.row_inc + 1
        
        winsound.Beep(2500,1000)
        self.row_inc=2 #Reset to Row 2 for next Excel file.
        print("\n DONE-----DONE-----DONE-----DONE-----DONE")

    def StopFunc(self,event):
        alg.reset(self)
            
 
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)

#create an object of CalcFrame
frame = CalcFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
