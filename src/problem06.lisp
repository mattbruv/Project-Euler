;; The sum of the squares of the first ten natural numbers is,
;; 1^2 + 2^2 + ... + 10^2 = 385
;; The square of the sum of the first ten natural numbers is,
;; (1 + 2 + ... + 10)^2 = 55^2 = 3025
;; Hence the difference between the sum of the squares of the
;; first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
;; Find the difference between the sum of the squares of the
;; first one hundred natural numbers and the square of the sum.

(defun range (n) (loop for i from 1 to n collect i))

(defvar 1-10 (range 10))
(defvar 1-100 (range 100))

(defun sum-of-squares (nums)
    (reduce '+ (map 'list (lambda (i) (* i i)) nums)))

(defun square-of-sum (nums)
    (let ((sum (reduce '+ nums)))
        (* sum sum)))

(defun problem06 () (- (square-of-sum 1-100) (sum-of-squares 1-100)))

;; 25164150