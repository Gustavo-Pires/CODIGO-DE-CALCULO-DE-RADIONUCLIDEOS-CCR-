#Gamma-Precision-Balance-GPB


The code written in python named Gamma Precision Balance (GPB), takes this .csv file, im- ports/extracts its necessary data, and using repetition structures it finds the determined peak of the 2 elements with a margin of 2 keV of variation for more or less, so as the characteristic peak of is 57Co is 122.06 keV, it searches between 121.06 and 123.06keV and for 60Co with characteristic peak of 1332, 5 keV, between 1331.5 and 1333.5 keV. This is the first check that the program makes, if the energy peak is not within this range, the program does not continue if there is no energy peak within this check, it informs the user and asks to call someone responsible. To avoid data with incorrect precision
When finding a value among these limiting parameters, it takes this value, which in this case is energy, extracts the position of this data in the variable, with this position it takes the other relevant data in the other variables, such as the resolution that will be useful for the next step. 
Prompts the user to select the month’s sheet to store. After storing the calibration data for this day, it imports/extracts all the calibration data for the specific month present in the spreadsheet and starts the second check, if the resolution is not within the 20% variation used for the .57Co and 30% for 60Co he again does not continue the calibration, informs which parameter is wrong and also requests the presence of the person responsible. If the resolution is normal, it starts to plot the graph with the quality control subplots, images 2 and 3, with the same parameters/requirements used to save the calibration program, which are later automatically saved as a .png file in the directory.
The code was divided into two parts, the first which searches for the energy peak of 57Co and 60Co and saves it in the spreadsheet, and the second part which imports this data from the spreadsheet and that plots the graphs. As previously mentioned, both parts have a check stage, which are the quality control criteria.
These two pieces of codes are executed using the subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This in order to guarantee computational efficiency, considering that if the calibration does not go beyond the first arrival of the energy peak, it is unnecessary to import graph plotting libraries from the second part as the code will break thus not executing the graphs, since the energy is very displaced.
For the first part, searching for the energy peak of 57Co and 60Co, there was little data used to test which prevented us from ensuring that the code works in all the different circumstances envisaged, due to the fact that the calibration files were never saved, and storing them is important to correct the equipment’s efficiency in the future if there is an error. In this case, the lack of these files prevented testing the program.
