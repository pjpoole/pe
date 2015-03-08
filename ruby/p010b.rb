
CAP = 2_000_000

sieve_bound = (CAP - 1)/2
max_idx = ((Math.sqrt(CAP)-1).floor/2).to_i

sieve = Array.new(sieve_bound) { true }

(1..max_idx).each do |idx|
  if sieve[idx]
    ((2 * idx * (idx + 1))..sieve_bound).step(2 * idx + 1) do |j|
      sieve[j] = false
    end
  end
end

aggregator = 2

(1..sieve_bound).each do |i|
  aggregator += (2 * i + 1) if sieve[i]
end

puts aggregator
