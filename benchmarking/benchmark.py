from typing import Iterable, Dict, Any

from .hardware import QuantumHardware, SimpleSimulator
from .tasks import MLTask, ParityClassificationTask

def benchmark(hardwares: Iterable[QuantumHardware], tasks: Iterable[MLTask]) -> Dict[str, Dict[str, Any]]:
    """Run all tasks on all hardware backends."""
    results: Dict[str, Dict[str, Any]] = {}
    for hw in hardwares:
        hw_name = hw.__class__.__name__
        results[hw_name] = {}
        for task in tasks:
            results[hw_name][task.name] = task.run(hw)
    return results


def main():
    hardware = [SimpleSimulator()]
    tasks = [ParityClassificationTask()]
    results = benchmark(hardware, tasks)
    for hw_name, task_results in results.items():
        print(f"Results for {hw_name}:")
        for task_name, metrics in task_results.items():
            metric_str = ", ".join(f"{k}={v:.3f}" for k, v in metrics.items())
            print(f"  {task_name}: {metric_str}")


if __name__ == "__main__":
    main()

