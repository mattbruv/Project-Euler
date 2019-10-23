;; If we list all the natural numbers below 10 that are
;; multiples of 3 or 5, we get 3, 5, 6 and 9.
;; The sum of these multiples is 23.
;; Find the sum of all the multiples of 3 or 5 below 1000.

(defun multiple? (x)
  (or (= (mod x 3) 0)
      (= (mod x 5) 0)))

(defun range (number) (loop :for n :below number :collect n))

(defun problem1 ()
  (reduce '+ (remove-if-not 'multiple? (range 1000))))

;; 233168