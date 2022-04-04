from main import Data
import matplotlib.pyplot as plt




a = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
     {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
     {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
     {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

test1 = Data(a)
#
print(test1.see_data())
# print(test1.check_cat_in_col())
# print(final)
b = [{"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
     {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
test2 = Data(b)

final = test2.see_data()

print(test2.check_cat_in_col())

print(final)
##### graphical interpretation of data

final.plot()
plt.show()
### statistical interpretation of data
print(final.describe())

