# First puzzle

I was too lazy to interpret the horrible way the crates are setup, at the beginning of the input, so you have to specify it as an `ALLBOXES` variable on the command line…

```
cat sample.txt | awk -v ALLBOXES="ZN MCD P" -f 1.awk
cat input.txt | awk -v ALLBOXES="JHPMSFNV SRLMJDQ NQDHCSWB RSCL MVTPFB TRQNC GVR CZSPDLR DSJVGPBF" -f 1.awk | tail
```

# Second puzzle

```
cat sample.txt | awk -v ALLBOXES="ZN MCD P" -f 2.awk
cat input.txt | awk -v ALLBOXES="JHPMSFNV SRLMJDQ NQDHCSWB RSCL MVTPFB TRQNC GVR CZSPDLR DSJVGPBF" -f 2.awk | tail
```
