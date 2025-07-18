#!/usr/bin/env bash

# improve error handling
set -euo pipefail

# User input
echo "What is your name?"
read -r name

if [ "$name" == "" ]; then
  echo "your name is unknow"
else
  echo "Hello, $name"
fi

# User input
read -p "Do you want to continue? (y/n) " resp

if [ $resp != "y" ]; then
  exit 1
fi
echo "Continuing..."

# Subshell
(
 echo "Ich bin in einer Subshell"
 cd /tmp
 echo "Aktuelles Verzeichnis: $PWD"
)

echo $(( 3 + 4 ))

# if-else
number=7

if [ "$number" -gt 6 ]; then
  echo "$number is greater than 6"
elif [ "$numer" -eq 6 ]; then
  echo "$number is equal to 6"
else
  echo "$number is smaller than 6"
fi

# Arrays
my_arr=(1 2 3 4 5)

echo ${my_arr[@]}
echo ${#my_arr[@]}

# for-loop
for item in "${my_arr[@]}"; do
  echo $item
done

for i in range {5..10}; do
  echo "$i"
done

# functions
function hello() {
  echo "Hello World"
}

hello

# while-loop (does not work somehow)
counter=0
while [[ "$counter" -lt 5 ]]; do
  echo "$counter"
  ((counter++))
done

