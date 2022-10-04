(head -n 1 ../ex01/hh.csv;
tail -n +2 ../ex01/hh.csv | sort --field-separator="," -k2 -k4) > hh_sorted.csv
