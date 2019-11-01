;; The prime factors of 13195 are 5, 7, 13 and 29.
;; What is the largest prime factor of the number 600851475143 ?

;; trial division
;; returns a list of prime factors
(defun factor (n &optional (f 2) (result '()))
  (if (> n 1)
    (if (= 0 (mod n f))
        ;; append f to list, and divide n by f
        (factor (/ n f) f (cons f result))
        (factor n (+ f 1) result))
    result))

(defun problem03 () (first (factor 600851475143)))

;; 6857