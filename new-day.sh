#!/bin/bash

DAY=$(date +'%d')
YEAR=$(date +'%y')
DAY_DIR="$PWD/AOC_$YEAR/day_$DAY"

[ -d "$DAY_DIR" ] || mkdir "$DAY_DIR"

cp -r day_template/* $DAY_DIR
