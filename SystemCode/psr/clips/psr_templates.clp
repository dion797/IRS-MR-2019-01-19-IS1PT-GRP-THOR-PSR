(deftemplate MAIN::form-input
  (slot aptType (allowed-symbols
    hdb-1-room hdb-2-room hdb-3-room hdb-4-room hdb-5-room
    exec-apt-condo landed))
  ; Form input enum:
  ; 1: <1,500   2: 1,500-2,499   3: 2,500-3,999
  ; 4: 4,000-5,999   5: 6,000-9,999   6: >=10,000
  (slot income (type INTEGER) (range 1 6))
  (slot tenancy-type (allowed-symbols self-owned rented))
  (slot is-risk-averse (allowed-symbols TRUE FALSE))
  (slot accept-direct-billing (allowed-symbols TRUE FALSE))
  (slot accept-sec-dep (allowed-symbols TRUE FALSE))
  (slot want-incentives (allowed-symbols TRUE FALSE))
  (slot prefer-est-brand (allowed-symbols TRUE FALSE))
)

(deftemplate MAIN::plan
  (slot id (type INTEGER) (range 1 ?VARIABLE))
  (slot company (allowed-symbols
    best diamond espower geneco iswitch
    keppel ohm pacificlight sembcorp senoko
    sunseap tuas union seraya)
  )
  (slot plan-name (type STRING))
  (slot plan-type (allowed-symbols fixed discounted))
  ; Rate: The fixed rate or the discount percentage
  (slot rate (type FLOAT))
  ; Contract length: Number of months
  (slot contract-length (type INTEGER))
  (slot is-green (allowed-symbols TRUE FALSE))
  ; Direct Billing: Separate bill
  (slot direct-billing (allowed-symbols TRUE FALSE))
  (slot has-security-deposit (allowed-symbols TRUE FALSE))
  ; Each incentive is one string
  (multislot plan-incentives (type STRING))
  (slot is-standard (allowed-symbols TRUE FALSE))
  (slot monthly-cost (type FLOAT) (default 0.0))
  (slot filter-checked (allowed-symbols TRUE FALSE) (default FALSE))
  (slot weightage (type FLOAT) (default 0.0))
)

(deftemplate MAIN::company
  (slot id (allowed-symbols
    best diamond espower geneco iswitch
    keppel ohm pacificlight sembcorp senoko
    sunseap tuas union)
  )
  (slot display-name (type STRING))
  (slot is-established (allowed-symbols TRUE FALSE))
)

(deftemplate MAIN::oil-price
  ; Year & Month
  (multislot date (type INTEGER))
  (slot price (type FLOAT))
  (slot is-current (allowed-symbols TRUE FALSE))
)

(deftemplate MAIN::tariff
  ; Year & Quarter
  (multislot date (type INTEGER))
  (slot price (type FLOAT))
  (slot is-current (allowed-symbols TRUE FALSE))
)

(deftemplate MAIN::estimated-consumption
  (slot aptType (allowed-symbols
    hdb-1-room hdb-2-room hdb-3-room hdb-4-room hdb-5-room
    exec-apt-condo landed)
  )
  (slot consumption (type FLOAT))
)

(deftemplate MAIN::user-cf
  (slot name (type SYMBOL))
  (slot certainty (type FLOAT) (range -1.0 1.0) (default 0.0))
)

(deftemplate MAIN::plan-cf
  (slot plan-id (type INTEGER) (range 1 ?VARIABLE))
  (slot certainty (type FLOAT) (range -1.0 1.0) (default 0.0))
)

(deftemplate MAIN::cost
  (slot min-cost (type FLOAT) (default 0.0))
  (slot max-cost (type FLOAT) (default 0.0))
)

(deftemplate MAIN::user-top
  (slot id (type INTEGER) (range 1 ?VARIABLE))
  (slot rank (type INTEGER))
  (slot weightage (type FLOAT) (default 0.0))
)