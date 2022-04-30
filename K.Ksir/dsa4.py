#building advanced data structures.
#these are the building blocks of data science and machine learning.
#dictionary can have a key which is string or integer or practically anything.
#value can be anything including a list, a dictionary or a dictionary containing list.

countries = {"in":{"India":["Mumbai","Pune","Delhi"]},"jp":{"Japan":["Tokio","Heroshima","Yakohama"]}}

for element in countries:
    print(countries[element])