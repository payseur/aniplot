from .line import LinePlot
import matplotlib.pyplot as plt

class DototatedLinePlot(LinePlot):
    def __init__(self, ax, data, title="", colors=None, event_indices=None):
        super().__init__(ax, data, title)
        self.event_indices = event_indices or []
        self.event_colors = colors or []
        self.dots_drawn = {} 

    def update(self, frame):
        super().update(frame)

        if frame in self.event_indices and frame not in self.dots_drawn:
            idx = self.event_indices.index(frame)
            color = self.event_colors[idx] if idx < len(self.event_colors) else 'black'
            self.ax.plot(frame, self.data[frame], 'o', color=color, markersize=8, markeredgecolor='white')
            self.dots_drawn.add(frame)

    def reset(self):
      super().reset()
      for dot in self.dots_drawn.values():
        try:
          dot.remove()
        except Exception:
          dot.set_visible(False)
      self.dots_drawn.clear()

