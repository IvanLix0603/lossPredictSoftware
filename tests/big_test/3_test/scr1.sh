#!/bin/bash
#read -p "Enter N: " N
N=$1
if [ ! -x mylinpack_64 ]; then
    echo "####COMPILING .C###############"
    gcc mylinpack.c -o mylinpack_64
    echo "#######################"
    echo
fi
if [ ! -d tmp ]; then
    mkdir tmp
fi
if [ ! -d var ]; then
    mkdir var
fi
if [ ! -d pictures ]; then
    mkdir pictures
fi
if [ ! -d results ]; then
    mkdir results
fi
echo "" > tmp/tmp_timing
#if [ $N -le 100 ]; then
#    STEPX=5
#elif [ $N -le 200 ]; then
#    STEPX=10
#elif [ $N -le 500 ]; then
#    STEPX=25
#elif [ $N -le 750 ]; then
#    STEPX=50
#else 
#    STEPX=100
#fi
STEPX=1
echo "STEPX=$STEPX"

for ((i=2; i<$N+$STEPX; i+=$STEPX))
do 
    echo -n $i >> tmp/tmp_timing
    { time nice -19 ./mylinpack_64 $i; } 2>> tmp/tmp_timing
    echo >> tmp/tmp_timing

done
awk  '$1 !~ /^[\nrealusersys]/ {print $1}' tmp/tmp_timing > tmp/tmp_nov
awk  '$1 ~ /[0-9]/ {print $1}' tmp/tmp_nov > var/number_of_variables 
awk  '$1 ~ /real/ {print $2}' tmp/tmp_timing > var/real_time
echo "########################"
echo "###time:###"
cat var/real_time
echo
echo "###data:###"
cat var/number_of_variables
echo "########################"
echo "Plotting results"
python3 paint_plot.py var/real_time var/number_of_variables
rm -Rf tmp
rm -Rf var


