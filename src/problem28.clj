(defn x [n]
  (+ 1 (* n 2)))

(defn y [n]
  (reduce + (map x (range 0 (+ n 1)))))

(defn corners [n]
  (if (= n 0)
    '(1)
    (map #(- (y n) (* n %)) (range 0 4))))

(defn spiral [n]
  (map corners (filter even? (range 0 (+ n 1)))))

(defn sum [s]
  (reduce + (map #(reduce + %) s)))

(defn problem28 [] (sum (spiral 1001)))