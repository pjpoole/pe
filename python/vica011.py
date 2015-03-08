from math import sqrt

"""Multiplies all elements of a list."""
def product(list):
   product = 1
   for k in range(len(list)):
      product *= list[k]
   return product

"""
Given a list, this function creates a new list
containing all (running) sublists of length m.
"""
def sublists(list, m):
   if m > len(list):
      return 'Sublist length too long.'
   sublists = []
   start = 0
   
   while start + m < len(list) + 1:
      sublist = [list[k] for k in range(start, start + m)]
      sublists.append(sublist)
      start += 1
   
   return sublists

"""
Consider an NxN matrix as a list of length N**2. 
This function creates a new list of all forward
diagonal (as in '\') sublists of length m.
"""
def diag(list, m):
   diagonals = []
   N = sqrt(len(list))
   N = int(N)
   if m > N:
      return 'Diagonal length too long.'
   
   for row in xrange(0, N*(N-m+1), N) :
      for column in range(N - m + 1):
         diagonal = [list[row + column + (N + 1)*i] for i in range(m)]
         diagonals.append(diagonal)
   
   return diagonals

"""
Returns maximum of all products of all running sublists 
of length m of rows of a square matrix, thought of as a list.
"""
def row_products(list, m):
   N = sqrt(len(list))
   N = int(N)
   max_prod = 0
   
   for row in xrange(0, N**2, N):
      rowlist = [list[row + column] for column in range(N)]
      for sublist in sublists(rowlist, m):
         max_prod = max(product(sublist), max_prod)
   
   return max_prod

"""
Returns maximum of all products of all "\" diagonals 
of length m of a square matrix, thought of as a list.
"""
def diag_products(list, m):
   N = sqrt(len(list))
   N = int(N)
   max_prod = 0
   
   for diagonal in diag(list, m):
      max_prod = max(product(diagonal), max_prod)
   
   return max_prod

"""
Consider an NxN matrix as a list of length N**2. 
This function transposes the matrix.
"""
def transpose(list):
   N = sqrt(len(list))
   N = int(N)
   transpose = []
   
   for row in xrange(0, N**2, N) :
      for column in range(N):
         transpose.append(list[N*column + row/N])
         
   return transpose

"""
Takes square matrix (thought of as a list) and
returns the same matrix with rows reversed.
"""
def reverse_rows(list):
   N = sqrt(len(list))
   N = int(N)
   reversed = []
   
   for row in xrange(0, N**2, N):
      reversed_row = [list[row + column] for column in range(N)[::-1]]
      reversed.extend(reversed_row)

   return reversed
   
if __name__ == '__main__':

   string = ('08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 '
             '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 '
             '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 '
             '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 '
             '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 '
             '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 '
             '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 '
             '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 '
             '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 '
             '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 '
             '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 '
             '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 '
             '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 '
             '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 '
             '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 '
             '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 '
             '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 '
             '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 '
             '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 '
             '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48')

   list = [int(string[k:k+2]) for k in xrange(0, len(string), 3)]
   m = 4
   
   max_prod = row_products(list, m)
   list = transpose(list)
   max_prod = max(row_products(list, m), max_prod)
   
   max_prod = max(diag_products(list, m), max_prod)
   list = reverse_rows(list)	
   max_prod = max(diag_products(list, m), max_prod)

   print max_prod