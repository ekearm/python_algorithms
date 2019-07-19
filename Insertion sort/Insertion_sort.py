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

my_array = [31,41,59,26,41,58]
insertion_sort(my_array)

for i in range(len(my_array)): 
   print ("% d" % my_array[i]) 

#desertion_sort
def desertion_sort(array):
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] < key:
      array[i + 1] = array[i]
      i -= 1
    array[i + 1] = key

#my_array = [31,41,59,26,41,58]
desertion_sort(my_array)

for i in range(len(my_array)): 
    print ("% d" % my_array[i]) 