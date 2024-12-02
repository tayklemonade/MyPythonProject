import tkinter as tk
from tkinter import messagebox, PhotoImage

class MainInterface:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title('Weather Data Program')
        self.mainWin.geometry('400x400')

        self.titleLabel = tk.Label(self.mainWin, text='Weather Data Anaylsis', font=('Helvetica', 16, 'bold'))
        self.titleLabel.place(x=100, y=10)
        
        self.image = PhotoImage(file='Weather_image.png')
        self.imageLabel = tk.Label(self.mainWin, image=self.image)
        self.imageLabel.place(x=100, y=40)

        #Temp label and input
        self.tempLabel = tk.Label(self.mainWin, text='Enter the temperature in degrees Fahrenheit:')
        self.tempLabel.place(x=20, y=160)

        self.inputTemp = tk.Entry(self.mainWin, width=5)
        self.inputTemp.place(x=300, y=160)

        #Wind label and input
        self.windLabel = tk.Label(self.mainWin, text='Enter wind speed in mph:')
        self.windLabel.place(x=20, y=200)
        
        self.inputWind = tk.Entry(self.mainWin, width=5)
        self.inputWind.place(x=300, y=200)

        #Dew label and input
        self.dewLabel = tk.Label(self.mainWin, text='Enter the dew point in degrees Fahrenheit:')
        self.dewLabel.place(x=20, y=240)
    
        self.inputDew = tk.Entry(self.mainWin, width=5)
        self.inputDew.place(x=300, y=240)

        #Chill factor and cloud base altitude
        self.windChill = tk.Label(self.mainWin, text='')
        self.windChill.place(x=20, y=280)
        
        self.cloudBase = tk.Label(self.mainWin, text='')
        self.cloudBase.place(x=20, y=300)

        #Show Data and Compute Buttons
        self.showData = tk.Button(self.mainWin, text='Show File Data', font=('Helvetica', 8), \
                                  width = 12, command = self.displayData)
        self.showData.place(x=50, y=360)

        self.compute = tk.Button(self.mainWin, text='Compute', font=('Helvetica', 8), \
                                 width = 8, command = self.dataCompute)
        self.compute.place(x=300, y=360)

        self.dataComputed = None
        self.dataWin = None

    def dataCompute(self):
        try:
            ws = int(self.inputWind.get())
            temp = int(self.inputTemp.get())
            dewPoint = int(self.inputDew.get())
        except ValueError:
            messagebox.showerror('Invalid Input', 'Must be numerical values.')
            return

        if (temp > 50 or ws <= 3):
            self.windChill.config(text = 'The wind chill facotr in degrees is: ERROR')
            self.cloudBase.config(text = 'The wind chill factor in degrees is: ERROR')
            messagebox.showerror('Compute Failed', 'Invalid Temperature or Wind Speed')
            self.inputWind.delete(0, tk.END)
            self.inputTemp.delete(0, tk.END)
            self.inputDew.delete(0, tk.END)
            return
        else:
            if not self.dataWin:
                self.compute.config(state='disabled')
            wc = 35.74 + (0.6215 * temp) - (35.75 * (ws**0.16)) + 0.4275 * temp * (ws**0.16)

        tempSpread = temp - dewPoint
        cloudBase = tempSpread / 4.4 * 1000

        self.windChill.config(text = f'The wind chill factor in degrees is:  {wc:.2f}')
        self.cloudBase.config(text = f'The cloud base altitude in feet is: {cloudBase:.2f}')

        self.dataComputed = (temp, ws, dewPoint, wc, cloudBase)
        
        if self.dataWin:
            self.dataWin.updateData(self.dataComputed)
            
    def displayData(self):

        self.showData.config(state='disabled')
        self.compute.config(state='normal')
        if self.dataComputed:
            if  not self.dataWin:
                self.dataWin = DataWindow(self.mainWin, self.dataComputed)
            else:
                self.dataWin.updateData(self.dataComputed)
        else:
            messagebox.showerror('Data Missing', 'Please compute first.')
        

class DataWindow:
    def __init__(self, parent, data):
        self.dataWin = tk.Toplevel(parent)
        self.dataWin.title('Weather Data Program')
        self.dataWin.minsize(width=500,height=400)
        self.dataWin.configure(bg = 'white')
        self.dataWin.rowconfigure(0,minsize=50)
        self.newRow = 4

        for c in range(6):
            self.dataWin.columnconfigure(c, minsize=50)

        for r in range(1,10):
            self.dataWin.rowconfigure(r, minsize=15)

        self.dataWin.header = tk.Label(self.dataWin, width=20, text='Weather Output Data', bg='white', font = ('Helvetica', 14))
        self.dataWin.header.place(x=150, y=25)

        self.dataWin.line = tk.Label(self.dataWin, width=70, \
                                     text='-'*200, bg='white')
        self.dataWin.line.place(x=50,y=50)

        #Labels for temp, windspeed, dewpoint,  windchill, cloudbase
        self.dataWin.temperatureHeader = tk.Label(self.dataWin, width=10, text='Temperature', bg='white', font = ('Helvetica', 11))
        self.dataWin.temperatureHeader.grid(row = 3, column = 1)

        self.dataWin.windspeedHeader = tk.Label(self.dataWin, width=10, text='Wind Speed', bg='white', font = ('Helvetica', 11))
        self.dataWin.windspeedHeader.grid(row = 3, column = 2)

        self.dataWin.dewpointHeader = tk.Label(self.dataWin, width=10, text='Dew Point', bg='white', font = ('Helvetica', 11))
        self.dataWin.dewpointHeader.grid(row = 3, column = 3)

        self.dataWin.windchillHeader = tk.Label(self.dataWin, width=10, text='Wind Chill', bg='white', font = ('Helvetica', 11))
        self.dataWin.windchillHeader.grid(row = 3, column = 4)

        self.dataWin.cloudbaseHeader = tk.Label(self.dataWin, width=10, text='Cloud Base', bg='white', font = ('Helvetica', 11))
        self.dataWin.cloudbaseHeader.grid(row = 3, column = 5)

        self.updateData(data)

    def addData(self, temp, ws, dewPoint, wc, cloudBase):

        fltT = float(temp)
        fltWS = float(ws)
        fltDP = float(dewPoint)
        fltWC = float(wc)
        fltCB = float(cloudBase)

        tempLabel = tk.Label(self.dataWin, width=15, text=f'{fltT:.2f} °F', bg='white', font=('Helvetica', 10))
        tempLabel.grid(row=self.newRow, column=1)

        windSpeedLabel = tk.Label(self.dataWin, width=15, text=f'{fltWS:.2f} mph', bg='white', font=('Helvetica', 10))
        windSpeedLabel.grid(row=self.newRow, column=2)

        dewPointLabel = tk.Label(self.dataWin, width=15, text=f'{fltDP:.2f} °F', bg='white', font=('Helvetica', 10))
        dewPointLabel.grid(row=self.newRow, column=3)

        windChillLabel = tk.Label(self.dataWin, width=15, text=f'{fltWC:.2f} °F', bg='white', font=('Helvetica', 10))
        windChillLabel.grid(row=self.newRow, column=4)

        cloudBaseLabel = tk.Label(self.dataWin, width=15, text=f'{fltCB:.2f} ft', bg='white', font=('Helvetica', 10))
        cloudBaseLabel.grid(row=self.newRow, column=5)

        self.newRow += 1

    def updateData(self, data):
        temp, ws, dewPoint, wc, cloudBase = data
        self.addData(temp, ws, dewPoint, wc, cloudBase)
