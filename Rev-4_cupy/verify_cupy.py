#!/home/drnorris/venv/bin/python
'''Simple tests to ensure that CuPy is installed correctly and is working as expected.'''

import gc
import time
import cupy as cp
import numpy as np

start_time = time.time()
# Create a sample array
gpu_array = cp.random.uniform(0, 1, (100000000,))
cp.cuda.Stream.null.synchronize()  # Synchronize to ensure the transfer completes
gpu_time = time.time()

# Transfer to CPU and back to GPU
cpu_array = cp.asnumpy(gpu_array)
cp.cuda.Stream.null.synchronize()  # Synchronize to ensure the transfer completes
cpu_time = time.time()

gpu_array_back = cp.array(cpu_array)
cp.cuda.Stream.null.synchronize()
gpu_back_time = time.time()

print(f"Time to init in GUP: {gpu_time - start_time:.6f} seconds")
print(f"Time to transfer from GPU to CPU: {cpu_time - gpu_time:.6f} seconds")
print(f"Time to transfer from CPU to GPU: {gpu_back_time - cpu_time:.6f} seconds")

# Compare values
is_consistent = np.allclose(gpu_array.get(), gpu_array_back.get())
print(f"Data transfer consistency: {is_consistent}")  # Should print True

# Get the free and total memory on the GPU
mempool = cp.get_default_memory_pool()
pinned_mempool = cp.get_default_pinned_memory_pool()

# Using CuPy's memory pool API
free_bytes, total_bytes = cp.cuda.runtime.memGetInfo()
print(f"Free memory: {free_bytes / (1024 ** 2):.2f} MB")
print(f"Total memory: {total_bytes / (1024 ** 2):.2f} MB")

# Free up CuPy memory
del gpu_array, cpu_array, gpu_array_back
gc.collect()
cp.get_default_memory_pool().free_all_blocks()

# Using CuPy's memory pool API
free_bytes, total_bytes = cp.cuda.runtime.memGetInfo()
print(f"Free memory after cleanup: {free_bytes / (1024 ** 2):.2f} MB")
print(f"Total memory after cleanup: {total_bytes / (1024 ** 2):.2f} MB")
