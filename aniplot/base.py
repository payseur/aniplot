from abc import ABC, abstractmethod
import numpy as np

class BasePlot(ABC):
    def __init__(self, ax, data=None, title=None, border_color="black", border_width=2.5, color_border=False, title_size=10, label_size=8):
        self.ax = ax
        self.data = data
        self.title = title
        self.border_color = border_color
        self.color_border = color_border
        self.border_width = border_width
        self.title_size = title_size
        self.label_size = label_size
        self._initialized = False
        

    def setup(self, visible=True):
        """Initial setup for the plot (axes, titles, limits, etc)."""
        self.ax.set_visible(visible)
        if self.title:
            self.ax.set_title(self.title, fontsize=self.title_size)
        self.ax.set_xlim(0, self.data.shape[0])
        
        buffer = (np.nanmax(self.data) - np.nanmin(self.data)) * .1
       # print(buffer)
      #  print(np.floor(np.nanmin(self.data)))
       # print(np.floor(np.nanmax(self.data)))
      #  self.ax.set_ylim(np.floor(np.nanmin(self.data))-buffer, np.floor(np.nanmax(self.data))+buffer)
        self.ax.set_ylim(np.nanmin(self.data)-buffer, np.nanmax(self.data)+buffer)
       
        self.ax.tick_params(axis='both', labelsize=self.label_size)
        if self.color_border:
          for spine in self.ax.spines.values():
            spine.set_edgecolor(self.border_color)
            spine.set_linewidth(self.border_width)
        
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
