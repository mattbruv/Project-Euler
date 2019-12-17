(defn ssort [col] (sort (mapcat str col)))

(defn canpan? [col]
  (let [freqs (frequencies (ssort col))]
    (and (every? #(= 1 (second %)) freqs)
         (not (contains? freqs \0)))))

(defn pan? [col]
  (= (ssort col) (ssort (range 1 10))))

(defn pan [n index col]
  (let [l2 (conj col (* n index))]
    (if (not (canpan? l2))
        col
        (pan n (+ 1 index) l2))))

(defn toInt [col] (Integer/parseInt (apply str col)))

(defn problem38[]
  (->> (range 1 1000000)
       (map #(pan % 1 []))
       (filter pan?)
       (map toInt)
       (apply max)))

; 932718654
; Elapsed time: 11451.150653 msecs