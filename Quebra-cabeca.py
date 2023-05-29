
def list_to_int(row):
  new = []
  for i in row:
    new.append(int(i))
  return new
  
def get_collumn(arr, index):
  collumn = []
  for coll in arr:
    collumn.append(coll[index])
  return collumn

def get_line(arr, index):
  return arr[index]
 
def list_is_equals(arr):
  for i in arr:
    if i != arr[0]:
      return False
  return True

f_to_int = lambda el: int(el)

# Começa o código main
l, c  = list_to_int(input().split(" "))
 
matrix_var = []
right_values = []
var_know = {}

# Pega os valores e verifica se a linha da matriz são todos iguais 
for i in range(l):
  row = input().split(" ")
  matrix_var.append(row[:c])
  right_values.append(list_to_int(row[c:])[0])
  if list_is_equals(row[:c]):
    var_know[matrix_var[i][0]] = right_values[i] / len(row)


bottom_values = list(map(f_to_int, input().split(" ")))

#Verifica as colunas com valores iguais 

if var_know == []:
  for i in range(c):
    tamp = get_collumn(matrix_var,i)
    if list_is_equals(tamp):
      var_know[matrix_var[1][i]] = bottom_values[1][i] / len(tamp)

