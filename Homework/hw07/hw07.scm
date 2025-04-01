(define (square n) (* n n))

(define (pow base exp)
  (cond
    ((= exp 0) 1)                     ; 终止条件：base^0 = 1
    ((even? exp) (square (pow base (/ exp 2))))  ; exp 是偶数：(base^(exp/2))^2
    (else (* base (pow base (- exp 1))))))       ; exp 是奇数：base * (base^(exp-1))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))
