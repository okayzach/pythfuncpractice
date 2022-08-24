def max_num(num1, num2, num3):
    list = [ num1, num2, num3 ]
    print(max(list))

max_num(3, 5, 7)


def mult_list(*num):
    numbers = [ *num ]
    product = 1
    for i in numbers:
        product = product * i
    print(product)
    
mult_list(3, 5, 7, 10)


def rev_string(string):
    print(string[::-1])

rev_string('salmon')


def num_within(num, rfrom, rto):
    numrange = list(range(rfrom, (rto + 1)))
    print(bool(numrange.count(num)))
        
num_within(4, 2, 10)
num_within(10, 2, 7)


triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate numbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(7)