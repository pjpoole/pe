# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which,

# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c =
# 1000.

# Find the product abc.

def triplet
  (1..1000).each do |a|
    (a..1000).each do |b|
      (b..1000).each do |c|
        next unless a + b + c == 1000
        return (a * b * c) if a**2 + b**2 == c**2
      end
    end
  end
end

if __FILE__ == $0
  puts triplet
end
