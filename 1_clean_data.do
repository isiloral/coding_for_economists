*Load data
import delimited using "data/raw/european_commission/ted-sample.csv", clear

*only keep relevant variables
keep iso_country_code win_country_code award_value_euro

*summarize award_value_euro
summarize award_value_euro, detail
display "Number of observation" `r(N)'
display "Mean" `r(Mean)'

*drop outliers
drop if award_value_euro > `r(p95)'

*plot the histogram
hist award_value_euro

*lets generate an indicator: 1 (above mean), 0 (otherwise)
generate above_mean = (award_value_euro > `r(p50)')

*little excursion: looping in stata

******
*recall python loop syntax
* for i in rage(10):
*	print(i)
*********

* forvalues looping
forvalues i = 0/10 {
	display `i'
}

* foreach loop (1)
foreach vegetables in paprika aubergine carrot {
	di "`vegetables'"
}

* foreach loop (2)
foreach var of varlist iso_country_code win_country_code {
	count if strlen(`var') > 2
}



