from abc import ABC, abstractmethod
from typing import List
import math
import random

try:
    from qiskit import QuantumCircuit, execute, Aer
except Exception:  # pragma: no cover - used when qiskit isn't installed
    QuantumCircuit = None
    execute = None
    Aer = None

class QuantumHardware(ABC):
    """Abstract base class for quantum hardware backends."""

    @abstractmethod
    def run_circuit(self, circuit: List[str]) -> int:
        """Execute a simple single-qubit circuit.

        The circuit is represented as a list of gate names. Supported gates:
        "H" for Hadamard, "X" for Pauli-X, "Z" for Pauli-Z.
        Returns a classical measurement result (0 or 1).
        """
        raise NotImplementedError


class SimpleSimulator(QuantumHardware):
    """Very small single-qubit simulator using Python complex numbers."""

    def run_circuit(self, circuit: List[str]) -> int:
        # Start in |0>
        state = [1+0j, 0+0j]
        for gate in circuit:
            if gate == "H":
                s0 = (state[0] + state[1]) / math.sqrt(2)
                s1 = (state[0] - state[1]) / math.sqrt(2)
                state = [s0, s1]
            elif gate == "X":
                state = [state[1], state[0]]
            elif gate == "Z":
                state = [state[0], -state[1]]
            else:
                raise ValueError(f"Unsupported gate: {gate}")
        prob1 = abs(state[1]) ** 2
        return 1 if random.random() < prob1 else 0


class QiskitSimulator(QuantumHardware):
    """Backend that executes circuits using Qiskit's Aer simulator."""

    def __init__(self):
        if QuantumCircuit is None:
            raise ImportError("qiskit is required for QiskitSimulator")
        self.backend = Aer.get_backend("qasm_simulator")

    def run_circuit(self, circuit: List[str]) -> int:
        qc = QuantumCircuit(1, 1)
        for gate in circuit:
            if gate == "H":
                qc.h(0)
            elif gate == "X":
                qc.x(0)
            elif gate == "Z":
                qc.z(0)
            else:
                raise ValueError(f"Unsupported gate: {gate}")
        qc.measure(0, 0)
        job = execute(qc, self.backend, shots=1)
        result = job.result()
        counts = result.get_counts(qc)
        return 1 if counts.get("1", 0) > 0 else 0

