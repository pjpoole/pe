def palindrome?(num)
  num_s = num.to_s
  length = num_s.length

  (length / 2).times do |i|
    return false if num_s[i] != num_s[length - i - 1]
  end

  true
end

largest = 0

1000.times do |i|
  1000.times do |j|
    prod = i * j
    largest = prod if prod > largest && palindrome?(prod)
  end
end

puts largest
