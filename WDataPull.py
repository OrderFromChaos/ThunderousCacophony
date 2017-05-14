import numpy as np



def pull_Data(weatherdata):
    for i in range(len(weatherdata)):
        for j in range(len(weatherdata[i])):
            name = weatherdata[i,j]
            data = name.replace('\'','')
            if(data.isalpha() == False):     
                number = data.replace('b','')
                weatherdata[i,j] = float(number)
            else:
                weatherdata[i,j] = "N/A"

def pull_time(weatherdata):
    time_list=[]
    for i in range(1,len(weatherdata)):
        time_list.append(i)
        
    return time_list
                
def pull_Precip(weatherdata):
    precip_list=[]
    for i in range(0,len(weatherdata)):
        precip_list.append(weatherdata[i,13])
    
    return precip_list

def pull_Humi(weatherdata):
    humid_list=[]
    for i in range(0,len(weatherdata)):
        humid_list.append(weatherdata[i,27])
    
    return humid_list
                            
def pull_Avghumid(weatherdata):
    avghumid_list=[]
    for i in range(0,len(weatherdata)):
        avghumid_list.append(weatherdata[i,28])
    
    return avghumid_list

def pull_Station(weatherdata):
    station_list = []
    for i in range(0,len(weatherdata)):
        station_list.append(weatherdata[i,0])
    
    return station_list

def pull_TempHrCalc(weatherdata):
    temp_list = []
    for i in range(0,len(weatherdata)):
        temp_list.append(weatherdata[i,8])
    
    return temp_list

def pull_TempHrAvg(weatherdata):
    temp_list = []
    for i in range(0,len(weatherdata)):
        temp_list.append(weatherdata[i,9])
    
    return temp_list

def pull_TempHrMax(weatherdata):
    temp_list = []
    for i in range(0,len(weatherdata)):
        temp_list.append(weatherdata[i,10])
    
    return temp_list

def pull_TempHrMin(weatherdata):
    temp_list = []
    for i in range(0,len(weatherdata)):
        temp_list.append(weatherdata[i,11])
    
    return temp_list
            
def load_Data(input_w):
    data_name = input_w + ".txt"
    weather_data = np.loadtxt(data_name,dtype=str)
    pull_Data(weather_data)
    
    return weather_data
    