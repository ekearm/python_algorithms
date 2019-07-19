#
# Psuedo Code:
# Insertion-Sort(array)
#for j = 2 to array.length
# key = array[j]
# i = j - 1
# while i > 0 and array[i] > key
#   array[i+1] = array[i]
#   i = i - 1
# array[i+1] = key

def insertion_sort(array):
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
      array[i + 1] = array[i]
      i -= 1
    array[i + 1] = key

my_array = [4,7,2,1,8,9,3,5]
insertion_sort(my_array)

for i in range(len(my_array)): 
    print ("% d" % my_array[i]) 