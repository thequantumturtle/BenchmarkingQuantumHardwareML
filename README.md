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

<<<<<<< lj1txa-codex/create-benchmarking-framework-for-quantum-hardware
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
=======
## Docker

Build the Docker image and run the benchmark inside the container:

```bash
docker build -t benchmark .
docker run --rm benchmark
```

This will execute `python -m benchmarking.benchmark` in the container.
>>>>>>> main
