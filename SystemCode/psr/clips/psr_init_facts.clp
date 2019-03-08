; deffacts that are not plans

(deffacts MAIN::starting-CFs
  ; All CFs initialise to default starting value 0.0
  (user-cf (name plan-is-green))
  (user-cf (name plan-not-green))
  (user-cf (name short-contract))
  (user-cf (name long-contract))
  (user-cf (name fixed-plan-type))
  (user-cf (name discount-plan-type))
)

(deffacts MAIN::oil-price-history
  ; TO-DO
  (oil-price (date 2019 01) (price 51.38) (is-current TRUE))
  (oil-price (date 2018 12) (price 49.52) (is-current FALSE))
)

(deffacts MAIN::tariff-history
  ; TO-DO
  (tariff (date 2019 1) (price 25.52) (is-current TRUE))
  (tariff (date 2018 4) (price 25.82) (is-current FALSE))
)

(deffacts MAIN::estimated-consumption-list
  ; Based on 2017 average
  (estimated-consumption (aptType hdb-1-room) (consumption 168.9))
  (estimated-consumption (aptType hdb-2-room) (consumption 168.9))
  (estimated-consumption (aptType hdb-3-room) (consumption 275.8))
  (estimated-consumption (aptType hdb-4-room) (consumption 372.9))
  (estimated-consumption (aptType hdb-5-room) (consumption 453.9))
  (estimated-consumption (aptType exec-apt-condo) (consumption 533.5))
  (estimated-consumption (aptType landed) (consumption 1204.5))
)

(deffacts MAIN::company-list
  ; Established companies are those which have generated or retailed electricity for at least 10 years
  (company (id best) (display-name "Best Electricity Supply Pte Ltd") (is-established FALSE))
  (company (id diamond) (display-name "Diamond Energy Merchants Pte Ltd") (is-established TRUE))
  (company (id espower) (display-name "ES Power (by Environmental Solutions (Asia) Pte Ltd)") (is-established FALSE))
  (company (id geneco) (display-name "Geneco (by Seraya Energy Pte Ltd)") (is-established TRUE))
  (company (id iswitch) (display-name "iSwitch Pte Ltd") (is-established FALSE))
  (company (id keppel) (display-name "Keppel Electric Pte Ltd") (is-established TRUE))
  (company (id ohm) (display-name "Ohm Energy Pte Ltd") (is-established FALSE))
  (company (id pacificlight) (display-name "PacificLight Energy Pte Ltd") (is-established FALSE))
  (company (id sembcorp) (display-name "Sembcorp Power Pte Ltd") (is-established TRUE))
  (company (id senoko) (display-name "Senoko Energy Supply Pte Ltd") (is-established TRUE))
  (company (id sunseap) (display-name "Sunseap Energy Pte Ltd") (is-established FALSE))
  (company (id tuas) (display-name "Tuas Power Supply Pte Ltd") (is-established TRUE))
  (company (id union) (display-name "Union Power Pte Ltd") (is-established FALSE))
)

(deffacts MAIN::min-max-cost
  (cost (min-cost 0.0) (max-cost 0.0))
)