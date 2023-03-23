#!/bin/bash

# set the path to the directory containing the files
dir_path="/Users/devin/Pictures/wallpapers"

# get the list of files in the directory
files=($dir_path/*)

# get the number of files in the directory
num_files=${#files[@]}

# generate a random index between 0 and num_files-1
index=$((RANDOM % num_files))

# get the random file from the list
random_file=${files[$index]}

osascript changewallpaper.applescript "$random_file"
