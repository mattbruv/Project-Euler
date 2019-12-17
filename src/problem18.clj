

(def ex1
"3
7 4
2 4 6
8 5 9 3")

(def ex2
"75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

(defn toInt [coll] (map #(Integer/parseInt %) coll))

(defn tri [tstr]
  (->> (clojure.string/split tstr #"\n")
       (map #(clojure.string/split % #" "))
       (map toInt)))

(defn search [t layer offset]
  ; (print (nth t layer))
  (if (= layer (count t))
      0
      (let [candidates (take 2 (drop offset (nth t layer)))]
        (let [maxN (apply max candidates)]
            (print maxN)))))

(def foo (tri ex1))
(def bar (search (tri ex1) 0 0))