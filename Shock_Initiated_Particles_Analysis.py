"""
Created on Tue May  3 15:40:30 2022

Edit-I on Fri June 24 17:17:00 2022
-Error handling for user input
-User input for handling image sequences from old camera and new
-Camera aquisition delays and exposures handled via user inputs
-Shock duration time entred by user
-Reacted particles during shock identified

@author: Siva Kumar Valluri
Requires VSK_ChipsII imageJMacro code generated data (in the form of csv files) as input.
"""

#Libraries_used####################################################################################################################################################
import os
import glob
import io 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\sivak\\.spyder-py3') #Spyder folder containing all codes 
print("Revelant libraries imported")

###################################################################################################################################################################
#User input: Fill in csv files location and camera aquisition settings

address1 = input("Enter address of folder with SIMX images (copy paste address): ")
while True:
    numberofimages = input("Enter number of SIMX images captured in a single shot (8 for older data or 16 new SIMX data): ")
    try:
        if numberofimages in  ["8","16"]:
            print("Noted.")
        else:
            raise Exception("Invalid input! Answer can only be '8' or '16'")
    except Exception as e:
        print(e)    
    else:
        break

while True:
    choice=input("Is the exposure same for all instances captured? (Y/N): ").lower() # So that user input is not case-senitive
    try:
        if choice.lower() in  ["y","yes","yippee ki yay","alright","alrighty"]:
            print("Consider changing exposure next time based on sampling instances!")
        elif choice.lower() in ["n","no","nope"]:
            print("Get ready to enter the exposures used for each instance")
        else:
            raise Exception("Invalid input! Answer can only be 'Yes' or 'No'")
    except Exception as e:
        print(e)    
    else:
        break

while True:
    choice2=input("Is the capture contiguous? (Y/N): ").lower() # So that user input is not case-senitive
    try:
        if choice2.lower() in  ["y","yes","yippee ki yay","alright","alrighty"]:
            print("Noted.")
        elif choice2.lower() in ["n","no","nope"]:
            print("Get ready to enter the delays used for each instance sampling")
        else:
            raise Exception("Invalid input! Answer can only be 'Yes' or 'No'")
    except Exception as e:
        print(e)    
    else:
        break
while True:
    choice3=input("Do you want to plot Intensity within every particle as a function of time for each well analyzed? (Y/N): ").lower() # So that user input is not case-senitive
    try:
        if choice3.lower() in  ["y","yes","yippee ki yay","alright","alrighty"]:
            print("Consider changing exposure next time based on sampling instances!")
        elif choice3.lower() in ["n","no","nope"]:
            print("Get ready to enter the exposures used for each instance")
        else:
            raise Exception("Invalid input! Answer can only be 'Yes' or 'No'")
    except Exception as e:
        print(e)    
    else:
        break  

shock_passtime = int(input("Enter duration shock lasts in sample: ") or "42")
    
csv_Particlesinchip = glob.glob(os.path.join(address1, "Particle*"))      #Gets information on particles identified by imageJ
csv_Intensityinparticles = glob.glob(os.path.join(address1, "Trial*"))    #Gets intensities at 4/8 instances of observation after its shocked for each particle 

###################################################################################################################################################################
#User input: Fill in delay for SIMX sampling and their corresponding exposure details
#units in nano seconds (ns)


exposures=[]
if choice.lower() in  ["n","no","nope"]:
    for instance in range(0,int(int(numberofimages)/2),1):           
        exp=int(input("Enter exposure for instance "+str(instance+1)+": ") or "50") #default value for exposure is 50ns 
        exposures.append(exp)
else:
    exp = int(input("What is the chosen exposure? (Only positive integers): "))
    for instance in range(0,int(int(numberofimages)/2),1):           
        exposures.append(exp)
 
delays=[]
if choice2.lower() in  ["n","no","nope"]:
    for instance in range(0,int(int(numberofimages)/2),1):           
        delay=int(input("Enter delay for instance "+str(instance+1)+": ") or "50") 
        delays.append(delay)
else:
    delay=int(input("Enter when the instance of capture began? :" or "0"))
    delays.append(delay)
    for number in exposures:
        delay=delay+number
        delays.append(delay)
    delays.pop(-1)
    
time_scale=[]
for i in range(0,len(delays),1):
    number=delays[i]+exposures[0]/2
    time_scale.append(number)


#Body##############################################################################################################################################################

time=np.array(time_scale) #Unit nano-seconds

folder_name=address1.rpartition('\\')[2]
Excelwriter = pd.ExcelWriter(str(folder_name)+'-Shock Initiated Ignition Analysis.xlsx', engine='xlsxwriter')
Ignited_particles=pd.DataFrame(columns=['Particlesize','ignition instance'])

Surveyed_Particlesizes=[]
Shock_Initiated_Particlesizes=[]

for t in range(len(csv_Particlesinchip)):
    sheetname=str(t)+"-Well"
    Particles_df = pd.read_csv(str(csv_Particlesinchip[t]))
    Particles_df = Particles_df.drop(Particles_df.columns[[0]], axis=1)
    Particles_df["Particle size"]=(Particles_df['Major']+Particles_df['Minor'])/2
    size=Particles_df['Particle size'].to_numpy()
    Particle_size=Particles_df['Particle size'].values.tolist()
    
    Surveyed_Particlesizes.append(Particle_size)
    
    Dmean = pd.DataFrame(columns = ['1','2','3','4','5','6','7','8'])
    Dmode = pd.DataFrame(columns = ['1','2','3','4','5','6','7','8'])
    Dmin = pd.DataFrame(columns = ['1','2','3','4','5','6','7','8'])
    Dmax = pd.DataFrame(columns = ['1','2','3','4','5','6','7','8'])
    for y in range(len(size)):
        Instance_df = pd.read_csv(str(csv_Intensityinparticles[y]))
        Instance_df = Instance_df.drop(Instance_df.columns[[0]], axis=1)
        Instance_df = Instance_df.transpose()
        x=Instance_df.iloc[[0]].to_numpy()
        X = pd.DataFrame(x,columns = ['1','2','3','4','5','6','7','8'])
        Dmean=Dmean.append(X)
        x=Instance_df.iloc[[1]].to_numpy()
        X = pd.DataFrame(x,columns = ['1','2','3','4','5','6','7','8'])
        Dmode=Dmode.append(X)
        x=Instance_df.iloc[[2]].to_numpy()
        X = pd.DataFrame(x,columns = ['1','2','3','4','5','6','7','8'])
        Dmin=Dmin.append(X)
        x=Instance_df.iloc[[3]].to_numpy()
        X = pd.DataFrame(x,columns = ['1','2','3','4','5','6','7','8'])
        Dmax=Dmax.append(X)
    Dmean = Dmean.transpose()
    Dmean.columns = size
    Dmean.set_index(time,inplace=True)
    Dmode = Dmode.transpose()
    Dmode.columns = size
    Dmode.set_index(time,inplace=True)
    Dmin = Dmin.transpose()
    Dmin.columns = size
    Dmin.set_index(time,inplace=True)
    Dmax = Dmax.transpose()
    Dmax.columns = size
    Dmax.set_index(time,inplace=True)
    
    Dmean.to_excel(Excelwriter, sheet_name=sheetname,index=False) 
    
    #Identifying shock initiated particles##########################################################
    shock_zone=Dmax[Dmean.index < shock_passtime]
    outlier=pd.DataFrame() 
    for row in range(0,shock_zone.shape[0],1):
        #Dmean.iloc[row].describe()
        Q1=shock_zone.iloc[row].quantile(0.25)
        Q3=shock_zone.iloc[row].quantile(0.75)
        IQR=Q3-Q1
        limit=Q3+1.5*IQR
        entry=shock_zone.iloc[row]>limit
        outlier[str(row+1)] = entry 
    #Index_label = outlier[(outlier['1']==True)&(outlier['2']==True)&(outlier['3']==True)].index.tolist()
    Index_label = outlier.index.tolist()    
    outlier=outlier.values.tolist()
    for i in range(0,len(outlier),1):
        if str(all(str(element) == "True" for element in outlier[i]))=="True":
            Shock_Initiated_Particlesizes.append(Index_label[i])
    #################################################################################################
    
    
    #Plotting gray values in particles as a function of time
    if choice3.lower() in  ["y","yes","yippee ki yay","alright","alrighty"]: 
        ax = Dmean.plot(lw=2, colormap='jet', marker='.', markersize=10, title='Average Gray value in each Particle inside PBX Chip no. '+str(t+1),legend=False,logx=True)
        ax.set_xlabel("time, ns")
        ax.set_ylabel("Mean Gray Value")
        ax.set_xlim([min(time), max(time)])
        ax.set_ylim([0, 5000])
        #ax.set_xlim([0, 2000])
         
        ax2 = Dmin.plot(lw=2, colormap='jet', marker='.', markersize=10, title='Minimum Gray value in each Particle inside PBX Chip no. '+str(t+1),legend=False,logx=True)
        ax2.set_xlabel("time, ns")
        ax2.set_ylabel("Min Gray Value")
        ax2.set_xlim([min(time), max(time)])
        ax2.set_ylim([0, 5000])
        #ax2.set_xlim([0, 2000]) 
        
        ax3 = Dmax.plot(lw=2, colormap='jet', marker='.', markersize=10, title='Maximum Gray value in each Particle inside PBX Chip no. '+str(t+1),legend=False,logx=True)
        ax3.set_xlabel("time, ns")
        ax3.set_ylabel("Max Gray Value")
        ax3.set_xlim([min(time), max(time)])
        ax3.set_ylim([0, 5000])
        #ax3.set_xlim([0, 2000])

Surveyed_Particlesizes=np.array(Surveyed_Particlesizes).T
Surveyed_Particlesizes=pd.DataFrame(Surveyed_Particlesizes,columns = ['Surveyed_Particlesizes'])
Shock_Initiated_Particlesizes=pd.DataFrame(Shock_Initiated_Particlesizes,columns = ['Shock_Initiated_Particlesizes'])

Surveyed_Particlesizes.to_excel(Excelwriter, sheet_name="Surveyed_Particlesizes",index=False)
Shock_Initiated_Particlesizes.to_excel(Excelwriter, sheet_name="Shock_Initiated_Particlesizes",index=False)
Excelwriter.save()
Excelwriter.close()
####################################################################################################################################################################







"""
Backup Plotting code
"""
"""
    #Plotting particle sizes in PBX
    _ = plt.hist(size, bins='auto')  # arguments are passed to np.histogram
    plt.title("Particle sizes in PBX")
    plt.xlabel("Particle size, micron")
    plt.ylabel("Number frequency")
    plt.show()
  
"""
            