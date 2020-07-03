;; A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
;; a^2 + b^2 = c^2
;; For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
;; There exists exactly one Pythagorean triplet for which a + b + c = 1000.
;; Find the product abc.

(defun triple? (a b c)
    (let ((a2 (* a a))
          (b2 (* b b))
          (c2 (* c c)))
        (= c2 (+ a2 b2))))

(defun find-triple ()
    (loop for a from 1 to 1000 do
        (loop for b from 1 to 1000 do
            (loop for c from 1 to 1000 do
                (if (and (triple? a b c)
                         (= (+ a b c) 1000))
                    (return-from find-triple (* a b c)))))))

(defun problem09 () (find-triple))

;; 31875000