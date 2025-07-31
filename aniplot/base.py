from abc import ABC, abstractmethod

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
        self._initialized = True

    @abstractmethod
    def update(self, frame):
        """Update the plot for a given frame."""
        pass

    def reset(self):
        # Optional default behavior: clear axis title and lines if needed
        self.ax.cla()
        self.ax.set_title(self.title)
