# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.

# What is the 10 001st prime number?

num_primes = 1
prime_arr = [2]
i = 3

curr_sqrt = 1
next_sqrt = 2
sqrt_cap  = 3

until num_primes == 10001
  # # This code takes 2x as long as the following code
  # if prime_arr.all? { |prime| i % prime != 0 }
  #   prime_arr << i
  #   num_primes += 1
  # end
  #
  # i += 1


  # Still takes 3.3s though.
  prime_arr.each do |j|
    break if i % j == 0
    if j > curr_sqrt
      prime_arr << i
      num_primes += 1
      break
    end
  end

  i += 1
  next_sqrt += 1

  if next_sqrt == sqrt_cap
    curr_sqrt += 1
    sqrt_cap += 2
  end
end

puts prime_arr.last
