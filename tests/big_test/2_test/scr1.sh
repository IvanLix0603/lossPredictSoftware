#!/bin/bash
#read -p "Enter N: " N
N=$1
if [ ! -x mylinpack_64_0 ]; then
    echo "####COMPILING .C###############"
    gcc mylinpack.c -O0 -o mylinpack_64_0
    echo "#######################"
    echo
fi
if [ ! -x mylinpack_64_1 ]; then
    echo "####COMPILING .C###############"
    gcc mylinpack.c -O1 -o mylinpack_64_1
    echo "#######################"
    echo
fi
if [ ! -x mylinpack_64_2 ]; then
    echo "####COMPILING .C###############"
    gcc mylinpack.c -O2 -o mylinpack_64_2
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
 #   STEPX=25
#elif [ $N -le 750 ]; then
#    STEPX=50
#else 
#    STEPX=100
#fi
STEPX=1
echo "STEPX=$STEPX"

for ((i=2; i<$N+$STEPX; i+=$STEPX))
do 
    echo -n $i >> tmp/tmp_timing_0
    echo -n $i >> tmp/tmp_timing_1
    echo -n $i >> tmp/tmp_timing_2
    echo -n $i >> tmp/tmp_timing_3
    { time ./mylinpack_64_0 $i; } 2>> tmp/tmp_timing_0
    { time ./mylinpack_64_1 $i; } 2>> tmp/tmp_timing_1
    { time ./mylinpack_64_2 $i; } 2>> tmp/tmp_timing_2
    echo >> tmp/tmp_timing_0
    echo >> tmp/tmp_timing_1
    echo >> tmp/tmp_timing_2
done

echo "Просчет с уровнем оптимизации 0"
awk  '$1 !~ /^[\nrealusersys]/ {print $1}' tmp/tmp_timing_0 > tmp/tmp_nov_0
awk  '$1 ~ /[0-9]/ {print $1}' tmp/tmp_nov_0 > var/number_of_variables_0 
awk  '$1 ~ /real/ {print $2}' tmp/tmp_timing_0 > var/real_time_0
echo "########################"
echo "###time:###"
cat var/real_time_0
echo
echo "###data:###"
cat var/number_of_variables_0
echo "########################"

echo "Просчет с уровнем оптимизации 1"
awk  '$1 !~ /^[\nrealusersys]/ {print $1}' tmp/tmp_timing_1 > tmp/tmp_nov_1
awk  '$1 ~ /[0-9]/ {print $1}' tmp/tmp_nov_1 > var/number_of_variables_1 
awk  '$1 ~ /real/ {print $2}' tmp/tmp_timing_1 > var/real_time_1
echo "########################"
echo "###time:###"
cat var/real_time_1
echo
echo "###data:###"
cat var/number_of_variables_1
echo "########################"

echo "Просчет с уровнем оптимизации 2"
awk  '$1 !~ /^[\nrealusersys]/ {print $1}' tmp/tmp_timing_2 > tmp/tmp_nov_2
awk  '$1 ~ /[0-9]/ {print $1}' tmp/tmp_nov_2 > var/number_of_variables_2 
awk  '$1 ~ /real/ {print $2}' tmp/tmp_timing_2 > var/real_time_2
echo "########################"
echo "###time:###"
cat var/real_time_2
echo
echo "###data:###"
cat var/number_of_variables_2


echo "Plotting results"
python3 paint_plot.py var/real_time_0 var/number_of_variables_0 var/real_time_1 var/number_of_variables_1 var/real_time_2 var/number_of_variables_2
#./paint_plot.py var/real_time_1 var/number_of_variables_1
#./paint_plot.py var/real_time_2 var/number_of_variables_2
#./paint_plot.py var/real_time_3 var/number_of_variables_3

rm -Rf tmp
rm -Rf var


