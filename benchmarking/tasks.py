from abc import ABC, abstractmethod
from typing import Dict

from .hardware import QuantumHardware

class MLTask(ABC):
    """Base class for ML tasks."""

    name: str

    @abstractmethod
    def run(self, hardware: QuantumHardware) -> Dict[str, float]:
        """Execute the task using the provided hardware and return metrics."""
        raise NotImplementedError


class ParityClassificationTask(MLTask):
    """Toy task that measures whether the hardware can flip a qubit."""

    def __init__(self):
        self.name = "ParityClassification"

    def run(self, hardware: QuantumHardware) -> Dict[str, float]:
        correct = 0
        for bit in (0, 1):
            circuit = ["X"] if bit == 1 else []
            result = hardware.run_circuit(circuit)
            if result == bit:
                correct += 1
        accuracy = correct / 2
        return {"accuracy": accuracy}

