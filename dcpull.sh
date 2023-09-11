#!/bin/bash
DIR=$(pwd)
DCHOME=/home/pnppl/Pictures/dc1500; # REMEMBER TO UPDATE
DATETIME=$(date +%F_%T);

cd $DCHOME/.PULLED;
gphoto2 -P;

# get lists of high res and low res pics
find $DCHOME/.PULLED -size +150k -name "*.pnm" > Hr.list;
find $DCHOME/.PULLED -size -150k -name "*.pnm" > Lr.list;

# directories to hold them
mkdir $DCHOME/$DATETIME
mkdir $DCHOME/$DATETIME/HrRaw
mkdir $DCHOME/$DATETIME/LrRaw

 # sort them
for i in $(cat Hr.list);
do
	mv $i $DCHOME/$DATETIME/HrRaw;
done;

for i in $(cat Lr.list);
do
	mv $i $DCHOME/$DATETIME/LrRaw;
done;

# do the thing
mogrify -path $DCHOME/$DATETIME -shave 2x2 -resize 384x288\! $DCHOME/$DATETIME/HrRaw/*.pnm;
mogrify -path $DCHOME/$DATETIME -shave 2x2 -resize 192x144\! $DCHOME/$DATETIME/LrRaw/*.pnm;

rm Hr.list; # clean up
rm Lr.list;
cd $DIR;
echo -e "\nAll done! If you got an error it was probably because you only took photos in one resolution.\nImages saved in $DCHOME/$DATETIME";