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

<<<<<<< lj1txa-codex/create-benchmarking-framework-for-quantum-hardware

class MNISTClassificationTask(MLTask):
    """Simple MNIST parity task using pixel intensity threshold."""

    def __init__(self, samples: int = 100):
        self.name = "MNISTClassification"
        self.samples = samples

    def run(self, hardware: QuantumHardware) -> Dict[str, float]:
        try:
            from tensorflow.keras.datasets import mnist
        except Exception as exc:  # pragma: no cover - dataset import may fail
            raise RuntimeError("TensorFlow is required for MNIST task") from exc

        (x_train, y_train), _ = mnist.load_data()
        x_train = x_train[: self.samples]
        y_train = y_train[: self.samples]

        correct = 0
        for img, label in zip(x_train, y_train):
            avg_intensity = img.mean()
            bit = 1 if avg_intensity > 127 else 0
            circuit = ["X"] if bit == 1 else []
            result = hardware.run_circuit(circuit)
            if result == (label % 2):
                correct += 1

        accuracy = correct / len(x_train)
        return {"accuracy": accuracy}

=======
>>>>>>> main
