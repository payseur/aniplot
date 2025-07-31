from .line import LinePlot
import matplotlib.pyplot as plt
import numpy as np

class DototatedLinePlot(LinePlot):
    def __init__(self, ax, data, title="", colors=None, event_indices=None, tick_positions = None, tick_labels=None):
        super().__init__(ax, data, title, tick_positions= tick_positions, tick_labels=tick_labels)
        self.event_indices = event_indices if event_indices is not None else np.array([])
        self.event_colors = colors if colors is not None else np.array([])
        self.dots_drawn = set()

    def update(self, frame):
        super().update(frame)

        if frame in self.event_indices and frame not in self.dots_drawn:
            matches = np.where(self.event_indices == frame)[0]
            if matches.size > 0:
                idx = matches[0]
                color = self.event_colors[idx] if idx < len(self.event_colors) else 'black'
                self.ax.plot(frame, self.data[frame], 'o', color=color, markersize=8, markeredgecolor='white')
                self.dots_drawn.add(frame)

    def reset(self):
        super().reset()
        self.dots_drawn.clear()
