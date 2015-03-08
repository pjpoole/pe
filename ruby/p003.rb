a = 600_851_475_143
sqrt_a = Math.sqrt(a)
factor_arr = []
i = 1

until a < sqrt_a
  if a % i == 0
    a /= i
    factor_arr << i
  end
  i += 1
end

p a
