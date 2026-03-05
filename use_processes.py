from multiprocessing import Pool
import time
import numpy as np
import sys
import argparse

def parse_args():
        parser = argparse.ArgumentParser(description="A script that helps understand speedup and efficiency")
        parser.add_argument("--CPUs", type=int, default=1, help="number of CPUs to divide the task")
        return parser.parse_args()

def mi_suma(datos):
        suma = 0
        for i in datos:
                suma = suma + i
        return suma

def use_one_or_more_processes(n, datos_partidos):
        with Pool(processes = n) as pool:
                resultados = pool.map(mi_suma, datos_partidos)

def main(args):
        N = 10_000_000
        NUM_CPUS = args.CPUs

        datos = np.random.randint(0,10,N)
        datos_partidos = np.array_split(datos, NUM_CPUS)

        start_time_single_cpu = time.perf_counter()
        use_one_or_more_processes(1,datos_partidos)
        end_time_single_cpu = time.perf_counter()
        elapsed_time_single_cpu = end_time_single_cpu - start_time_single_cpu
        print(f"Elapsed time: {elapsed_time_single_cpu: 4f} seconds NUM_CPUS: 1")

        start_time_one_or_more_cpus = time.perf_counter()
        use_one_or_more_processes(NUM_CPUS, datos_partidos)
        end_time_one_or_more_cpus = time.perf_counter()
        elapsed_time_one_or_more_cpus = end_time_one_or_more_cpus - start_time_one_or_more_cpus
        print(f"Elapsed time: {elapsed_time_one_or_more_cpus: 4f} seconds NUM_CPUS: {NUM_CPUS}")

        speedup = elapsed_time_single_cpu / elapsed_time_one_or_more_cpus
        print(f"SPEEDUP: (T1/Tn) | {elapsed_time_single_cpu: 4f} / {elapsed_time_one_or_more_cpus: 4f}: {speedup: 4f}")
        efficiency = speedup / NUM_CPUS
        print(f"EFFICIENCY: (SPEEDUP/CPUs) | {speedup: 4f} / {NUM_CPUS}: {efficiency: 4f}")

if __name__ == "__main__":
        args = parse_args()
        main(args)
