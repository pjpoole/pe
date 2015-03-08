def prime?(candidate)
  # line-by-line conversion of function written in python
  candidate_root = Math.floor(Math.sqrt(candidate))

  return false if candidate <= 1
  return true if candidate < 4
  return false if candidate % 2 == 0
  return true if candidate < 9
  return false if candidate % 3 == 0

  test_factor = 5

  while test_factor <= candidate_root
    return false if candidate % test_factor == 0
                 || candidate % (test_factor + 2) == 0
    test_factor += 6
  end

  true
end
