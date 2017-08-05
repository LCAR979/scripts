# ! /bin/bash

index=1
max_index=30

while [ $index -lt $max_index ]
do
  if [ -e "*2017_lecture${index}.pdfi*" ]; then
    index=$(( index+1 ))
    continue
  fi

  addr="http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture${index}.pdf"
  wget ${addr} -q --show-progress
  result=$?
 
  if [ ${result} -eq 0 ]; then
    index=$(( index+1 ))
  else
    echo "Downloading finished. ${index} file(s) downloaded"
    break
  fi
done

