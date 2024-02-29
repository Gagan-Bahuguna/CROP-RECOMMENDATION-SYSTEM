                                                            
import pandas as pd
from sklearn import preprocessing                                         
from sklearn.neighbors import KNeighborsClassifier                        
import numpy as np                                                        
import PySimpleGUI as sg                                                  
import warnings
warnings.filterwarnings("ignore")
excel = pd.read_excel(r"C:\Users\HP\Downloads\crop.xlsx" , header = 0)   
print(excel) 
print(excel.shape) 
excel.duplicated().sum()
excel.isnull().sum()
excel['CROP'].unique()
X=excel.drop('CROP',axis=1)
y=excel["CROP"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size =0.30,shuffle=True,random_state=0)


model = KNeighborsClassifier(n_neighbors=3)  
model.fit(X_train, y_train)       
                                                                       # fit your model on the train set using fit() and perform prediction on the test set using predict().
layout = [[sg.Text('                      Crop Recommendation SYSTEM', font=("italic", 30), text_color = 'black')],                                                    # Defining the layout of the Graphical User Interface. It consist of some text, Buttons, and blanks to take Input.                                                        
         [sg.Text('Please enter the following details :-', font=("Helvetica", 20))],                                                                                          
         [sg.Text('Enter ratio of Nitrogen in the soil                                  :', font=("italic", 20)), sg.Input(font=("Helvetica",20), size = (20,1) )],
         [sg.Text('Enter ratio of Phosphorous in the soil                           :', font=("italic", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter ratio of Potassium in the soil                               :', font=("italic", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter average Temperature value around the field        :', font=("italic", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('*C', font=("Helvetica", 20))], 
         [sg.Text('Enter average percentage of Humidity around the field :', font=("italic", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('%', font=("Helvetica", 20))], 
         [sg.Text('Enter PH value of the soil                                            :', font=("italic", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))], 
         [sg.Text('Enter average amount of Rainfall around the field        :', font=("italic", 20) ), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text('mm', font=("Helvetica", 20))],
         [sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'red', key='-OUTPUT1-' )],
         [sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Quit', font=("italic", 20))] ]
window = sg.Window('Crop Recommendation system', layout) 

while True: 
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':                                                                                            
		break
	print(values[0])
	nitrogen_content =         values[0]                                                                                                        
	phosphorus_content =       values[1]                                                                                                        
	potassium_content =        values[2]                                                                                                        
	temperature_content =      values[3]                                                                                                        
	humidity_content =         values[4]                                                                                                        
	ph_content =               values[5]                                                                                                        
	rainfall =                 values[6]                                                                                                        
	X_test = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall])
	print(X_test)                                                                                                                             
	X_test = X_test.reshape(1,-1)                                                                              
	print(X_test)                                                                                                
	result = model.predict(X_test)                                                                             # Applying the user input data into the model. 
	print(result)
	window['-OUTPUT1-'].update('The best crop that you can grow : ' + result )  
    
           