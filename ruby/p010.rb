# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

require 'set'

CAP = 2_000_000
primes = Array.new(CAP) { |idx| idx }
primes[1] = 0

CAP.times do |i|
  next if primes[i] < 2
  interval = j = i
  j += interval
  until j > CAP
    primes[j] = 0
    j += interval
  end
end

sum = primes.inject(&:+)

puts sum
