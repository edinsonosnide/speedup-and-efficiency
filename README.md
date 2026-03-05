# Parallel Speedup Experiment (Processes vs Threads)

This project contains two Python scripts that demonstrate **parallel
computing concepts** such as **speedup** and **efficiency**.

## Scripts

### Multiprocessing (processes.py)

Uses Python's `multiprocessing.Pool` to divide a large array into chunks
and compute the sum in parallel using multiple **CPU processes**.

Run:

python processes.py --CPUs 4

### Multithreading / BLAS (threads.py)

Uses **NumPy + BLAS threading** by controlling environment variables:

-   OMP_NUM_THREADS
-   MKL_NUM_THREADS
-   OPENBLAS_NUM_THREADS

Run:

python threads.py --threads 4

## What the scripts measure

Both programs:

-   Generate an array of **10 million random integers**
-   Run the computation with **1 CPU/thread**
-   Run the computation with **N CPUs/threads**
-   Calculate:

Speedup:

S = T1 / Tn

Efficiency:

E = Speedup / N

Where: - T1 = execution time with 1 CPU/thread - Tn = execution time
with N CPUs/threads

## Requirements

Python 3\
numpy

Install dependencies:

pip install numpy

## Goal

Understand how **parallelism impacts performance** and compare:

-   Multiprocessing (true parallelism)
-   Thread-based parallelism using BLAS
