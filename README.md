# BenchmarkingQuantumHardwareML

This repository contains a simple framework for benchmarking different quantum
hardware backends on machine learning tasks. The goal is to provide a minimal
interface for integrating hardware providers and ML tasks so they can be
evaluated in a uniform way.

## Structure

- `benchmarking/hardware.py` – abstractions and a tiny single-qubit simulator.
- `benchmarking/tasks.py` – task definitions. Includes a toy parity
  classification task.
- `benchmarking/benchmark.py` – orchestration utilities and a CLI for running
  benchmarks.

## Running

Execute the default benchmark using the simple simulator:

```bash
python -m benchmarking.benchmark
```

This will run all tasks on the simulator and print the resulting metrics.

To run the MNIST benchmark using the Qiskit simulator (requires Qiskit and
TensorFlow):

```bash
python -m benchmarking.mnist_benchmark
```

### Docker

If you don't have the dependencies installed locally, build the provided Docker
image which includes Qiskit and TensorFlow:

```bash
docker build -t qhw-bench .
docker run --rm qhw-bench python -m benchmarking.mnist_benchmark
```
