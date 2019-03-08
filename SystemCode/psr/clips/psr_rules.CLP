(defmodule MAIN (export ?ALL))

; *************************
; Init rules engine
; *************************
(defrule MAIN::start
  (declare (salience 10000))
  =>
    (set-fact-duplication TRUE)
	(focus GET-CF SET-PLAN-CF FILTER-PLANS SET-WEIGHT RECOMMEND)
)

; *************************
; Parse form input to obtain CFs and average monthly consumption
; *************************
(defmodule GET-CF (import MAIN ?ALL) (export ?ALL))

(defrule GET-CF::parse-income
  (declare (salience 100))
  (form-input (income ?val))
  =>
    (switch ?val
      ; <2,500
      (case 1 then ; <1,500
        (assert (user-cf (name plan-is-green) (certainty 0.8)))
        (assert (user-cf (name plan-not-green) (certainty 0.2)))
      )
      (case 2 then ; 1,500-2,499
        (assert (user-cf (name plan-is-green) (certainty 0.8)))
        (assert (user-cf (name plan-not-green) (certainty 0.2)))
      )
      ; 2,500-5,999
      (case 3 then ; 2,500-3,999
        (assert (user-cf (name plan-is-green) (certainty 0.88)))
        (assert (user-cf (name plan-not-green) (certainty 0.12)))
      )
      (case 4 then ; 4,000-5,999
        (assert (user-cf (name plan-is-green) (certainty 0.88)))
        (assert (user-cf (name plan-not-green) (certainty 0.12)))
      )
      ; >=6,000
      (case 5 then ; 6,000-9,999
        (assert (user-cf (name plan-is-green) (certainty 0.68)))
        (assert (user-cf (name plan-not-green) (certainty 0.32)))
      )
      (case 6 then ; >=10,000
        (assert (user-cf (name plan-is-green) (certainty 0.68)))
        (assert (user-cf (name plan-not-green) (certainty 0.32)))
      )
    )
)

(defrule GET-CF::parse-tenancy-type
  (declare (salience 100))
  (form-input (tenancy-type ?val))
  =>
    (if (eq ?val self-owned) then
      (assert (user-cf (name short-contract) (certainty 0.48)))
      (assert (user-cf (name long-contract) (certainty 0.52)))
     else
      (assert (user-cf (name short-contract) (certainty 0.75)))
      (assert (user-cf (name long-contract) (certainty 0.25)))
    )
)

(defrule GET-CF::parse-risk-profile
  (declare (salience 100))
  (form-input (is-risk-averse ?val))
  =>
    (if (eq ?val TRUE) then
      (assert (user-cf (name fixed-plan-type) (certainty 0.8)))
      (assert (user-cf (name discount-plan-type) (certainty 0.2)))
     else
      (assert (user-cf (name fixed-plan-type) (certainty 0.2)))
      (assert (user-cf (name discount-plan-type) (certainty 0.8)))
    )
)

; Currently, oil price, tariff, and historical averages are all static, so the related rules are temporarily hard-coded
(defrule GET-CF::parse-oil-price
  (declare (salience 100))
  ; current 51.38 < 5yearAvg 66.76 is true
  (test (< 51.38 66.76))
  =>
    (assert (user-cf (name fixed-plan-type) (certainty 0.8)))
    (assert (user-cf (name discount-plan-type) (certainty 0.2)))
)

(defrule GET-CF::parse-tariff
  (declare (salience 100))
  ; current 25.52 < 1yearAvg 24.475 is false
  (test (< 25.52 24.475))
  =>
    (assert (user-cf (name fixed-plan-type) (certainty 0.7)))
    (assert (user-cf (name discount-plan-type) (certainty 0.3)))
)

(defrule GET-CF::combine-positive
  (declare (salience 90))
  ?f1 <- (user-cf (name ?rel) (certainty ?per1&:(>= ?per1 0)))
  ?f2 <- (user-cf (name ?rel) (certainty ?per2&:(>= ?per2 0)))
  (test (neq ?f1 ?f2))
  =>
    (retract ?f2)
    (modify ?f1 (certainty =(+ ?per1 (* ?per2 (- 1 ?per1)))))
)

(defrule GET-CF::combine-negative
  (declare (salience 90))
  ?f1 <- (user-cf (name ?rel) (certainty ?per1&:(<= ?per1 0)))
  ?f2 <- (user-cf (name ?rel) (certainty ?per2&:(<= ?per2 0)))
  (test (neq ?f1 ?f2))
  =>
    (retract ?f2)
    (modify ?f1 (certainty =(+ ?per1 (* ?per2 (+ 1 ?per1)))))
)

(defrule GET-CF::combine-positive-negative
  (declare (salience 90))
  ?f1 <- (user-cf (name ?rel) (certainty ?per1))
  ?f2 <- (user-cf (name ?rel) (certainty ?per2))
  (test (neq ?per1 ?per2))
  (test (< (* ?per1 ?per2) 0))
  =>
    (retract ?f2)
    (modify ?f1 (certainty =(/ (+ ?per1 ?per2) (- 1 (min (abs ?per1) (abs ?per2))))))
)

; *************************
; Combine the correct CFs for each plan based on derived user CFs
; *************************
(defmodule SET-PLAN-CF (import MAIN ?ALL) (import GET-CF ?ALL) (export ?ALL))

(defrule SET-PLAN-CF::calc-cost
  (declare (salience 80))
  ?f1 <- (plan (plan-type ?val1) (rate ?val2) (monthly-cost 0.0))
  (form-input (aptType ?val3))
  (tariff (price ?val4) (is-current TRUE))
  (estimated-consumption (aptType ?val3) (consumption ?val5))
  ?f2 <- (cost (min-cost ?val6) (max-cost ?val7))
  =>
    (if (eq ?val1 fixed) then
	   (bind ?val8 (* ?val2 ?val5))
     else
	   (bind ?val8 (* ?val5 (* ?val4 (/ (- 100 ?val2) 100))))
    )
	(modify ?f1 (monthly-cost ?val8))
	(if (and (= ?val6 0.0) (= ?val7 0.0)) then
	   (modify ?f2 (min-cost ?val8) (max-cost ?val8))
	 else
	   (if (> ?val8 ?val7) then
	      (modify ?f2 (max-cost ?val8))
		else
		  (if (< ?val8 ?val6) then
	         (modify ?f2 (min-cost ?val8))
	      )
	   )
	)
)

(defrule SET-PLAN-CF::check-consumption
  (declare (salience 70))
  (plan (id ?val1) (monthly-cost ?val2))
  (cost (min-cost ?val3) (max-cost ?val4))
  =>
    (assert (plan-cf (plan-id ?val1) (certainty (+ 1 (* -2.0 (/ (- ?val2 ?val3) (- ?val4 ?val3)))))))
)

(defrule SET-PLAN-CF::check-green
  (declare (salience 70))
  (user-cf (name plan-is-green) (certainty ?val1))
  (user-cf (name plan-not-green) (certainty ?val2))
  (plan (id ?val3) (is-green ?val4))
  =>
    (if (eq ?val4 TRUE) then
      (assert (plan-cf (plan-id ?val3) (certainty ?val1)))
     else
      (assert (plan-cf (plan-id ?val3) (certainty ?val2)))
    )
)

(defrule SET-PLAN-CF::check-length
  (declare (salience 70))
  (user-cf (name short-contract) (certainty ?val1))
  (user-cf (name long-contract) (certainty ?val2))
  (plan (id ?val3) (contract-length ?val4))
  =>
    (if (< ?val4 12) then
      (assert (plan-cf (plan-id ?val3) (certainty ?val1)))
     else
      (assert (plan-cf (plan-id ?val3) (certainty ?val2)))
    )
)

(defrule SET-PLAN-CF::check-type
  (declare (salience 70))
  (user-cf (name fixed-plan-type) (certainty ?val1))
  (user-cf (name discount-plan-type) (certainty ?val2))
  (plan (id ?val3) (plan-type ?val4))
  =>
    (if (eq ?val4 fixed) then
      (assert (plan-cf (plan-id ?val3) (certainty ?val1)))
     else
      (assert (plan-cf (plan-id ?val3) (certainty ?val2)))
    )
)

(defrule SET-PLAN-CF::combine-positive
  (declare (salience 60))
  ?f1 <- (plan-cf (plan-id ?rel) (certainty ?per1&:(>= ?per1 0)))
  ?f2 <- (plan-cf (plan-id ?rel) (certainty ?per2&:(>= ?per2 0)))
  (test (neq ?f1 ?f2))
  =>
    (retract ?f2)
    (modify ?f1 (certainty =(+ ?per1 (* ?per2 (- 1 ?per1)))))
)

(defrule SET-PLAN-CF::combine-negative
  (declare (salience 60))
  ?f1 <- (plan-cf (plan-id ?rel) (certainty ?per1&:(<= ?per1 0)))
  ?f2 <- (plan-cf (plan-id ?rel) (certainty ?per2&:(<= ?per2 0)))
  (test (neq ?f1 ?f2))
  =>
    (retract ?f2)
    (modify ?f1 (certainty =(+ ?per1 (* ?per2 (+ 1 ?per1)))))
)

(defrule SET-PLAN-CF::combine-positive-negative
  (declare (salience 60))
  ?f1 <- (plan-cf (plan-id ?rel) (certainty ?per1))
  ?f2 <- (plan-cf (plan-id ?rel) (certainty ?per2))
  (test (neq ?per1 ?per2))
  (test (< (* ?per1 ?per2) 0))
  =>
    (retract ?f2)
    (modify ?f1 (certainty =(/ (+ ?per1 ?per2) (- 1 (min (abs ?per1) (abs ?per2))))))
)

; *************************
; Set CFs to -1 for plans to be filtered out
; *************************
(defmodule FILTER-PLANS (import MAIN ?ALL) (export ?ALL))

(defrule FILTER-PLANS::filter-plan
   (declare (salience 50))
  (form-input (accept-direct-billing ?val1) (accept-sec-dep ?val2) (want-incentives ?val3) (prefer-est-brand ?val4))
  ?f1 <- (plan (id ?val5) (company ?val6) (direct-billing ?val7) (has-security-deposit ?val8) (plan-incentives $?val9) (filter-checked FALSE))
  (company (id ?val6) (is-established ?val10))
  ?f2 <- (plan-cf (plan-id ?val5))
  =>
	(if (or (and (eq ?val1 FALSE) (eq ?val7 TRUE)) (and (eq ?val2 FALSE) (eq ?val8 TRUE)) (and (eq ?val3 TRUE) (= (length$ ?val9) 0))
			(and (eq ?val4 TRUE) (eq ?val10 FALSE))) then
      (modify ?f1 (filter-checked TRUE))
	  (modify ?f2 (certainty -1.0))
    )
)

; *************************
; Set plan weightage based on plan CF
; *************************
(defmodule SET-WEIGHT (import MAIN ?ALL) (export ?ALL))

(defrule SET-WEIGHT::calc-weight
  (declare (salience 40))
  ?f1 <- (plan (id ?val1) (weightage 0.0))
  (plan-cf (plan-id ?val1) (certainty ?val2))
  =>
    (modify ?f1 (weightage ?val2))
)


; *************************
; Sort and return top 3 weighted plans
; *************************
(defmodule RECOMMEND (import MAIN ?ALL) (export ?ALL))

;(defrule RECOMMEND::find-max-value
;   (declare (salience 20))
;   (plan (id ?val1) (weightage ?value1))
;   (not (plan (weightage ?value2&:(> ?value2 ?value1))))
;   =>
;   (printout t "plan " ?val1 " is the maximum" crlf)
;   (assert (user-top (id ?val1) (rank 1) (weightage ?value1)))
;)

(defrule RECOMMEND::choose
  (declare (salience 1))
  (plan (id ?val1) (company ?val2) (plan-name ?val3) (weightage ?weightage))
  =>
  (if (> ?weightage 0) then
    (printout t ?val1 "," ?val2 "," ?val3 "," ?weightage "---" crlf)
	)
)
