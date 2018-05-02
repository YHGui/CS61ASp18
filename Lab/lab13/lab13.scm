; Q1
(define (compose-all funcs)
  (lambda (x)
  	(if (null? funcs)
  		x
  		((compose-all (cdr funcs)) ((car funcs) x))))
)

; Q2
(define (tail-replicate x n)
	(define (helper n so-far)
		(if (= n 0)
			so-far
			(helper (- n 1) (cons x so-far)))
	)
	(helper n '())
)