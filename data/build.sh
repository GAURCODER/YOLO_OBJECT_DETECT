#!/bin/bash
echo "###############################"
echo "# Build data from classes.txt #"
echo "###############################"

# Build data.yaml
classes=($(cat classes.txt))
data=$(printf ", '%s'" "${classes[@]}")
data=${data:2}
nc="${#classes[@]}"


echo $'path: ../data\ntrain: images\nval: images\n\nnc: '${nc} $'\n\nnames: ['"${data}]" > ./data.yaml

cat ./data.yaml