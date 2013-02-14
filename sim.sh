FILENAME='data'#name of the .dats to be plot
NTIMES=10 #number of times that the word will be transmitted
FREQUENCY='0.3 0.6 0.8' #frequencies that a 0 will be added to the new word
LENGTH=30 #max length of the words
PROBZERO=0.7 #probability that a 0 will be transmitted as a 0
PROBONE=0.8 #probability that a 1 will be transmitted as a 1

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
PLOTFILE="graph"$f".plot" #name of the .plot file 
>$PLOTFILE #access to the .plot file
echo set term png >>$PLOTFILE
echo set xlabel \""Length"\" >>$PLOTFILE
echo set ylabel \""Average"\">>$PLOTFILE
echo set output \""chart"$f".png"\">>$PLOTFILE
echo plot \"$FILENAME$f".dat"\" with lines>>$PLOTFILE

gnuplot *.plot
rm *.plot
done
