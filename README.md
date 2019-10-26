# PropertyAnalysis
![Sample picture](https://github.com/Zafirmk/PropertyAnalysis/blob/master/SampleTestTrain.png)  

**Project duration**: 1 day  
**IDE**: Pycharm 2019.2.1 (Community Edition)  
**Python Version**: Python 3.7  


## Description
A machine learning model that uses a regression line to fit data relating to house prices and area of house in sqft. All data obtained for this project is from webscraping [Bayut](https://www.bayut.com/to-rent/property/dubai/). Webscraping project used to get the data can be found in the [PropertyFinder](https://github.com/Zafirmk/PropertyFinder) repository.


## .csv Files Used  
* **properties.csv**: Contains each property with its attributes. 

## How it works
1. Data from the properties.csv file is sectioned off for use. (ie: the price and sqft data)  

2. Once data is ready to be used for ML purposes, it is split into a test and train set.  

3. Using poly1d and polyfit a line is fit against the data in the training set and testing set.  
The degree of the line is set to 1 by default since the relationship is assumed to be linear. 
```
coefficients = np.polyfit(x_train, y_train, 1)
p4 = np.poly1d(coefficients)
```  

4. The R2 Score is calculated for each graph, which is a measure of how well the line fits the data.

5. Finally, the data is displayed on two graphs. 


## Getting Started

1. Clone this repo using the following command  
```
$ git clone https://github.com/Zafirmk/PropertyAnalysis.git
$ cd PropertyAnalysis
```
2. Open the project in your preferred IDE  

3. Set the directory of the project to where the repo is saved. Or simply edit the following lines of code to read
```
data = pd.read_csv("<YOUR PATH HERE>/properties.csv", thousands=",")
```

### Prerequisites
Things you need to install before running:
*  [Python](https://www.python.org/)
*  [Pandas](https://pandas.pydata.org/)
*  [Matplotlib](https://matplotlib.org/)
*  [Sklearn](https://scikit-learn.org/stable/)

#### Additional Notes
*  All data used in this project is obtained from [Bayut](https://www.bayut.com/to-rent/property/dubai/)
