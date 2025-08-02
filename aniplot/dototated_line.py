from .line import LinePlot
import matplotlib.pyplot as plt
import numpy as np

class DototatedLinePlot(LinePlot):
    def __init__(self, ax, data, title="", colors=None, event_indices=None, event_y_values=None, event_overnight=None, tick_positions = None, tick_labels=None, border_color="black", border_width=2.5, color_border=False, title_size=10, label_size=8):
        super().__init__(ax, data, title, tick_positions= tick_positions, tick_labels=tick_labels,border_color=border_color, border_width=border_width, color_border=color_border, title_size=title_size, label_size=label_size)
        self.event_indices = event_indices if event_indices is not None else np.array([])
        self.event_y_values = event_y_values if event_y_values is not None else np.array([])
        self.event_overnight = event_overnight if event_overnight is not None else np.array([])
        self.event_colors = colors if colors is not None else np.array([])
        self.dots_drawn = set()

    def update(self, frame):
        super().update(frame)

        if frame < 0:
          return
        
        if frame in self.event_indices and frame not in self.dots_drawn:
            matches = np.where(self.event_indices == frame)[0]
            if matches.size > 0:
                idx = matches[0]
                color = self.event_colors[idx] if idx < len(self.event_colors) else 'black'
                if(self.event_overnight[idx]):
                  self.ax.plot(frame, self.event_y_values[idx], 'o', color='white', markersize=6, markeredgecolor=color)
                else:
                  self.ax.plot(frame, self.event_y_values[idx], 'o', color=color, markersize=8, markeredgecolor='white')
                self.dots_drawn.add(frame)

    def reset(self):
        super().reset()
        self.dots_drawn.clear()
