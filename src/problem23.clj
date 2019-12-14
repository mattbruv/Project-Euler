(defn divisors [n]
  (if (= n 1)
    []
    (filter #(= 0 (rem n %)) (range 1 n))))

(defn is-abundant [n] (< n (reduce + (divisors n))))

(def abundants (set (filter is-abundant (range 1 28123))))

(defn is-non-abundant-sum [n]
  (not-any? #(contains? abundants (- n %)) abundants))

(defn problem23 [] (reduce + (filter is-non-abundant-sum (range 1 28123))))