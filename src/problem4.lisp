;; A palindromic number reads the same both ways.
;; The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
;; Find the largest palindrome made from the product of two 3-digit numbers.

(defparameter *top-palindrome* 0)

(defun number-to-list (n)
  (loop for c across (write-to-string n) collect (digit-char-p c)))

(defun pal? (n)
  (let ((n-list (number-to-list n)))
    (equal n-list (reverse n-list))))

(defun nested-loop ()
  (loop for i from 100 to 999 doing
        (loop for j from 100 to 999 doing
              (let ((product (* i j)))
                  (if (and (pal? product) (> product *top-palindrome*))
                      (defparameter *top-palindrome* product)
                      NIL)))))

(defun problem4 () (progn (nested-loop) *top-palindrome*))

;; 906609