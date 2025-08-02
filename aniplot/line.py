from .base import BasePlot

class LinePlot(BasePlot):
    def __init__(self, ax, data=None, title=None, color='gray', marker='o', tick_positions=None, tick_labels=None, border_color="black", border_width=2.5, color_border=False, title_size=10, label_size=8):
        super().__init__(ax, data, title, border_color=border_color, border_width=border_width, color_border=color_border, title_size=title_size, label_size=label_size)
        self.color = color
        self.marker = marker
        self.line = None
        self.marker_obj = None
        self.x_data = []
        self.y_data = []
        self.tick_positions = tick_positions
        self.tick_labels = tick_labels

    def setup(self, visible=True):
        super().setup(visible = visible)
        self.line, = self.ax.plot([], [], lw=2, color=self.color)
        self.marker_obj, = self.ax.plot([], [], self.marker, color=self.color)
        if self.tick_positions is not None and self.tick_labels is not None:
          self.ax.set_xticks(self.tick_positions)
          self.ax.set_xticklabels(self.tick_labels)


    def update(self, frame):
        if frame < 0:
          return
        
        if not self.ax.get_visible():
          self.ax.set_visible(True)
        
        if not self._initialized:
            self.setup()

        if self.data is not None and frame < len(self.data):
            self.x_data.append(frame)
            self.y_data.append(self.data[frame])
            
            if len(self.x_data) == 1:
                # Show the first point as a marker
                #self.marker_obj.set_data(self.x_data, self.y_data)
                self.line.set_data(self.x_data, self.y_data)
            else:
                # Show the rest as a line
                self.line.set_data(self.x_data, self.y_data)
  
        return [self.line, self.marker_obj]
      
    def reset(self):
        self.x_data.clear()
        self.y_data.clear()
        self.line.set_data([], [])


