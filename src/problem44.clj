

(defn pent [n] (* n (/ (- (* 3 n) 1) 2)))

(def foo (map pent (range 1 11)))

(defn problem44 [] 44)