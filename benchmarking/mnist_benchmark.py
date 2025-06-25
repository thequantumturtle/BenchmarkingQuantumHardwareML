from .benchmark import benchmark
from .hardware import QiskitSimulator
from .tasks import MNISTClassificationTask


def main():
    try:
        hw = [QiskitSimulator()]
    except ImportError:
        print(
            "Qiskit is required for this benchmark. "
            "Install it via pip or run using the provided Dockerfile."
        )
        return

    tasks = [MNISTClassificationTask()]
    results = benchmark(hw, tasks)
    for hw_name, task_results in results.items():
        print(f"Results for {hw_name}:")
        for task_name, metrics in task_results.items():
            metric_str = ", ".join(f"{k}={v:.3f}" for k, v in metrics.items())
            print(f"  {task_name}: {metric_str}")


if __name__ == "__main__":
    main()
