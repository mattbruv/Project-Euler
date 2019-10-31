;; 2520 is the smallest number that can be divided by
;; each of the numbers from 1 to 10 without any remainder.
;; What is the smallest positive number that is evenly
;; divisible by all of the numbers from 1 to 20?

(defun is-div (n div)
    (= 0 (mod n div)))

(defun range () (loop for n from 2 to 20 collect n))

(defun test (n)
    (every (lambda (div) (is-div n div)) (range)))

(defun smolest (num)
    (if (test num)
        num
        (smolest (+ 1 num))))

(defun problem5 () (smolest 20))

;; 232792560