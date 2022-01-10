from dataclasses import dataclass


@dataclass
class ParticleData:

    @property
    def edges(self):
        pass

    @property
    def pmu(self):
        pass

    @property
    def pdg(self):
        pass

    @property
    def final(self):
        pass

    @property
    def color(self):
        pass

    @classmethod
    def empty(cls):
        return cls(
            edges = np.array([[0, 1]], dtype=TYPE['int']),
            pmu=np.array([[0.0, 0.0, 0.0, 0.0]], dtype=REAL_TYPE),
            pdg=np.array([1], dtype=TYPE['int']),
            final=np.array([False], dtype=TYPE['bool'])
            )
