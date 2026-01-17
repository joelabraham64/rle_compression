# rle_compression

A simple **Run-Length Encoding (RLE)** compression program written in C.  
RLE reduces file size by replacing consecutive repeated characters (or values) with a single value and a count (e.g., `AAAAA` → `A5`). This approach is most effective on inputs with long runs of repeated data.
pl/plt is used to generate plots for analyzing and visualizing behavior related to the RLE compression algorithm. It uses NumPy and Matplotlib to produce PDF output for reporting purposes.

## Files
- main.c
- file.c
- pl.py

## How to Compile (Linux / WSL)
```bash
gcc *.c -o compress
./compress

python pl.py

