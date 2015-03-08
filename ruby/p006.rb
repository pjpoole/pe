# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

CAP = 100

sq_sum = (((CAP) * (CAP + 1))/2)**2
sum_sq = 0

(CAP + 1).times do |i|
  sum_sq += i**2
end

puts sq_sum - sum_sq
