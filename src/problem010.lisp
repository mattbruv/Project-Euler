;; The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
;; Find the sum of all the primes below two million.


(defparameter *primes* '(2 3))

(defun prime? (number)
    (notany (lambda (p) (= 0 (mod number p))) *primes*))

(defun add-if-prime (test)
    (if (prime? test)
        (defparameter *primes* (append *primes* (list test)))))

(defun find-primes (start limit)
    (if (< start limit)
        (progn (add-if-prime start)
               (find-primes (+ 1 start) limit))))

(defun problem10 ()
    (let ((biggest (reduce #'max *primes*)))
        (progn (find-primes biggest 2000000)
               (reduce '+ *primes*))))

;; 142913828922
;; Pretty slow, but it finds it nonetheless.