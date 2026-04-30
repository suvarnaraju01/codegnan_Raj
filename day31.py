'''
Data Analysis :
-------------------
    Y it is needed :
    -----------------
    it covert raw data into  actionable insights enablibg information to decision
    making, easy and improve operational efficiency...
        
    1.Decision-making
    2.Improved Operational Efficiency
    3.Customer Understanding
    4.Market Insight
    5.Risk Management
    6.Data Driven Strategies
    
import matplotlib.pyplot as Raj
X = [1,2,3,4,5]
Y = [10,20,15,30,5]
Raj.plot(X,Y)
Raj.show( )

Numpy:
---------
Numerical python is the foundational open source library
for  scientific  computing in python providing high performance.
N - dimensional array objects(ndarray)
 This enables efficient  numerical computing linear algebra and data manipulation,serving
 as the basis for tools  like  tensor flow and scipy

import numpy as Raj
arr = Raj.array([1,2,3])
print(arr - 1)

Pandas :
----------
 used for handling structured  data in table format


import pandas as pd
data = {"S.No":[1,2],"Name" : ["Raju","SarathLaxmi"],"marks":[99,99.9]}
any = pd.DataFrame(data)
print(any)

import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.title("Very Long Title Example 1")

plt.subplot(2,2,2)
plt.title("Very Long Title Example 2")

plt.subplot(2,2,3)
plt.title("Very Long Title Example 3")

plt.subplot(2,2,4)
plt.title("Very Long Title Example 4")

# Uncomment this to fix overlap
plt.tight_layout()

plt.show()'''
import matplotlib.pyplot as plt

# Data
weeks = [1, 2, 3, 4, 5]
marks = [9, 9, 5, 11, 4]

# 1. Line Plot
plt.subplot(2,3,1)
plt.plot(weeks, marks, marker='o')
plt.title("Line Plot")

# 2. Bar Graph
plt.subplot(2,3,2)
plt.bar(weeks, marks)
plt.title("Bar Graph")

# 3. Pie Chart
plt.subplot(2,3,3)
plt.pie(marks, labels=weeks, autopct='%1.1f%%')
plt.title("Pie Chart")

# 4. Scatter Plot
plt.subplot(2,3,4)
plt.scatter(weeks, marks)
plt.title("Scatter Plot")

# 5. Histogram
plt.subplot(2,3,5)
plt.hist(marks)
plt.title("Histogram")

# Layout fix
plt.tight_layout()

# Show all graphs
plt.show()
    
