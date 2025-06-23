import pandas
import matplotlib.pyplot as plt 
import numpy as np

# locating the files:
excel_Data = pandas.read_excel(r"D:\linear regresion\house.xlsx")  
print(excel_Data)

#multipling the datas for computation:

excel_Data["x"] = excel_Data["x(size Sq.ft)"]
excel_Data["y"] = excel_Data["y(price)"]

excel_Data = excel_Data.drop(columns=["x(size Sq.ft)", "y(price)"])

excel_Data["xy"] = excel_Data["x"] * excel_Data["y"]

excel_Data["x_square"] = excel_Data["x"] * excel_Data["x"] 

print (excel_Data)
# saving the file:
excel_Data.to_excel(r"D:\linear_regression.xlsx")

#adding the columns for summation values:
summation = excel_Data.sum()
print(summation)
summation_row = pandas.DataFrame([summation])
summation_row.index = ["Total"]
data_with_sum = pandas.concat([excel_Data, summation_row])

count=  len(excel_Data)
print("n: " ,count)

# slope =  [n * Σ(xy) - Σx * Σy] / [n * Σ(x²) - (Σx)²]

slope=((count*summation.xy)-(summation.x * summation.y)) /((count*summation.x_square) -(summation.x * summation.x))
 
print("slope: " ,slope)

# c = ( ∑y - m ∑x) / n

C = (summation.y-(slope * summation.x))/ count
print("C : ",C)

y=f'{slope} x +{C}'
print("y = ",y)


try:
    X = int(input("Enter the Independent variable = "))
    Y = slope*X + C
    print("Y=",Y)


except ValueError:
    print("Please enter a valid number for the independent variable.")

prediction_row = pandas.DataFrame([{
    'x': X,
    'y': Y,
    'xy': '',
    'x_square': '',
}], index=["Predicted Y"])
final_df = pandas.concat([data_with_sum, prediction_row])

#Save all data to Excel
final_df.to_excel(r"D:\linear_regression_house.xlsx", index=True)

# plotting the graph:

x=excel_Data['x']
y=excel_Data['y']

#fixing the values for graph view

x_min = x.min()
x_max = x.max()
x_range = x_max - x_min
x_line = np.linspace(x_min - 0.1 * x_range, x_max + 0.1 * x_range, 100)
y_line = slope * x_line + C


print("Now plotting...")

plt.plot(x_line , y_line, label=f'y = {slope}(x) + {C}')

plt.scatter(x, y)
plt.scatter(X,Y,color= 'red')
plt.grid(True)
plt.legend()
plt.xlabel('Independent variables( size_sq.ft )')
plt.ylabel('Dependent variables( Price )')
plt.title('Linear_regression')


plt.savefig(r'D:\linear regresion\my_plot.png')
plt.show()




