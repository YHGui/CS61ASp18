; Q4
(define (rle s)
  (define (track-run elem st len)
    (cond ((null? st) (cons-stream (list elem len) nil))
          ((= elem (car st)) (track-run elem (cdr-stream st) (+ len 1)))
          (else (cons-stream (list elem len) (rle st))))
  )

  (if (null? s)
      nil
      (track-run (car s) (cdr-stream s) 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (helper s so-far)
    (cond ((null? s) (append so-far (cons n s)))
          ((< n (car s)) (append so-far (cons n s)))
          (else (helper (cdr s) (append so-far (list (car s))))))
  )
  
  (helper s nil)
)

; Q6
(define (deep-map fn s)
  (cond ((null? s) nil)
        ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
        (else (cons (fn (car s)) (deep-map fn (cdr s)))))
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (if (null? s) nil
      (cons (car s)
            (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)

(define (count name s)
  (if (null? s) 0
       (+ (if (eq? name (car s)) 1 0)
          (count name (cdr s))))
)

(define (tally names)
  (map (lambda (name) (cons name (count name names))) (unique names))
)