import time
import numpy as np
import sys
import argparse
import os

def parse_args():
        parser = argparse.ArgumentParser(description="A script that helps understand speedup and efficiency")
        parser.add_argument("--threads", type=int, default=1, help="number of CPUs to divide the task")
        return parser.parse_args()

def use_one_or_more_threads(n, datos_partidos):
        # Configurar para usar 2 núcleos (hilos de OpenBLAS/MKL)
        os.environ["OMP_NUM_THREADS"] = f"{n}"
        os.environ["MKL_NUM_THREADS"] = f"{n}"
        os.environ["OPENBLAS_NUM_THREADS"] = f"{n}"
        resultado = np.sum(datos_partidos, axis=1)

def main(args):
        N = 10_000_000
        NUM_THREADS = args.threads

        datos = np.random.randint(0,10,N)
        datos_partidos = np.array_split(datos,NUM_THREADS)

        start_time_single_thread = time.perf_counter()
        use_one_or_more_threads(1, datos_partidos)
        end_time_single_thread = time.perf_counter()
        elapsed_time_single_thread = end_time_single_thread - start_time_single_thread
        print(f"Elapsed time: {elapsed_time_single_thread: 4f} seconds NUM_THREADS: 1")

        start_time_one_or_more_threads = time.perf_counter()
        use_one_or_more_threads(NUM_THREADS, datos_partidos)
        end_time_one_or_more_threads = time.perf_counter()
        elapsed_time_one_or_more_threads = end_time_one_or_more_threads - start_time_one_or_more_threads
        print(f"Elapsed time: {elapsed_time_one_or_more_threads: 4f} seconds NUM_THREADS: {NUM_THREADS}")

        speedup = elapsed_time_single_thread / elapsed_time_one_or_more_threads
        print(f"SPEEDUP: (T1/Tn) | {elapsed_time_single_thread: 4f} / {elapsed_time_one_or_more_threads: 4f}: {speedup: 4f}")
        efficiency = speedup / NUM_THREADS
        print(f"EFFICIENCY: (SPEEDUP/threads) | {speedup: 4f} / {NUM_THREADS}: {efficiency: 4f}")

if __name__ == "__main__":
        args = parse_args()
        main(args)

