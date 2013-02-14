FILENAME='data'
NTIMES=10
FREQUENCY='0.3 0.6 0.8'
LENGTH=30
PROBZERO=0.7
PROBONE=0.8

for f in $FREQUENCY
do
    for i in 1
    do
	for j in 1
	do
	    python simulation.py $FILENAME$f".dat" $NTIMES $f $LENGTH $PROBZERO $PROBONE
	    echo python simulation.py $FILENAME$f".dat" $NTIMES $f $LENGTH $PROBZERO $PROBONE
	done
    done
done
