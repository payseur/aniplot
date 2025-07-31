from abc import ABC, abstractmethod
import numpy as np

class BasePlot(ABC):
    def __init__(self, ax, data=None, title=None):
        self.ax = ax
        self.data = data
        self.title = title
        self._initialized = False

    def setup(self):
        """Initial setup for the plot (axes, titles, limits, etc)."""
        if self.title:
            self.ax.set_title(self.title)
        self.ax.set_xlim(0, self.data.shape[0])
        
        
        self.ax.set_ylim(np.floor(np.nanmin(self.data)), np.floor(np.nanmax(self.data)))

        self._initialized = True

    @abstractmethod
    def update(self, frame):
        """Update the plot for a given frame."""
        pass

    def reset(self):
        # Optional default behavior: clear axis title and lines if needed
        self.ax.cla()
        self.ax.set_title(self.title)

    def plot(self):
      for i in range(len(self.data)): self.update(i)
