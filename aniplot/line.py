from .base import BasePlot

class LinePlot(BasePlot):
    def __init__(self, ax, data=None, title=None, color='gray', marker='o', tick_positions=None, tick_labels=None):
        super().__init__(ax, data, title)
        self.color = color
        self.marker = marker
        self.line = None
        self.marker_obj = None
        self.x_data = []
        self.y_data = []
        self.tick_positions = tick_positions
        self.tick_labels = tick_labels

    def setup(self):
        super().setup()
        self.line, = self.ax.plot([], [], lw=2, color=self.color)
        self.marker_obj, = self.ax.plot([], [], self.marker, color=self.color)
        if self.tick_positions is not None and self.tick_labels is not None:
          self.ax.set_xticks(self.tick_positions)
          self.ax.set_xticklabels(self.tick_labels)


    def update(self, frame):
        if not self._initialized:
            self.setup()

        if self.data is not None and frame < len(self.data):
            self.x_data.append(frame)
            self.y_data.append(self.data[frame])
            
            if len(self.x_data) == 1:
                # Show the first point as a marker
                self.marker_obj.set_data(self.x_data, self.y_data)
            else:
                # Show the rest as a line
                self.line.set_data(self.x_data, self.y_data)

        return [self.line, self.marker_obj]
      
    def reset(self):
        self.x_data.clear()
        self.y_data.clear()
        self.line.set_data([], [])


