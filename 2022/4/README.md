# First puzzle

```
cat input.txt | awk -F '[,-]' '{if ( ($1<=$3 && $2>=$4) || ($1>=$3 && $2<=$4) ) S++ } END {print S}'
```

# Second puzzle

Even simpler... but I counted the other way round, so need to substract the result from the number of records in the end!

```
cat input.txt | awk -F '[,-]' '{if ( ($2<$3) || ($4<$1) ) S++ } END {print NR-S}'
```
