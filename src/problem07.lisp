;; By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
;; we can see that the 6th prime is 13.
;; What is the 10 001st prime number?

(defparameter *primes* '(2 3))

(defun is-prime (test)
    (notany (lambda (p) (= 0 (mod test p))) *primes*))

(defun next-prime (test)
    (if (is-prime test)
        (defparameter *primes* (cons test *primes*))
        NIL))

(defun gen-primes (start amount)
    (if (/= amount (length *primes*))
        (progn (next-prime start)
               (gen-primes (+ 1 start) amount))
        NIL))

(defun problem07 ()
    (progn (gen-primes 2 10001)
           (car *primes*)))

;; 104743