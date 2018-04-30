(define (find s predicate)
  (cond ((null? s) #f)
  		((predicate (car s)) (car s))
  	    (else (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (if (null? s) s
  	  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
	(define (cycle-tracker so-far cur)
		(cond ((null? cur) #f)
			  ((contains so-far cur) #t)
			  (else (cycle-tracker (cons cur so-far) (cdr-stream cur))))
	)

	(define (contains lst s)
		(cond ((null? lst) #f)
			  ((eq? s (car lst)) #t)
			  (else (contains (cdr lst) s)))
	)

	(cycle-tracker nil s)
)
(define (has-cycle-constant s)
	(define (cycle-stepper slow fast)
		(cond ((or (null? fast) (null? (cdr-stream fast))) #f)
  			  ((eq? fast slow) #t)
  			  (else (cycle-stepper (cdr-stream slow) (cdr-stream (cdr-stream fast)))))
	)

	(let ((slow s)
		   (fast (cdr-stream s)))
		(cycle-stepper slow fast)
	)

)
