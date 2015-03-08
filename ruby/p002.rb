sum = 0
arr = [1, 2, 3]

until arr[1] > 4_000_000
  sum += arr[1]
  arr[0] = arr[1] + arr[2]
  arr[1] = arr[2] + arr[0]
  arr[2] = arr[0] + arr[1]
end

puts sum
