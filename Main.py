from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size):
    
    min = i
    
    for j in range(1, size):
      
      if data[min] > data[j]:
        
        min = j
      
    temp = data[min]
    data[min] = data[i]
    data[i] = temp
  

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
