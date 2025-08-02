from .base import BasePlot

class BarPlot(BasePlot):
    def __init__(self, ax, data=None, title=None, color='gray', tick_positions=None, tick_labels=None, border_color="black", border_width=2.5, color_border=False, title_size=10, label_size=8):
        super().__init__(ax, data, title, border_color=border_color, border_width=border_width, color_border=color_border, title_size=title_size, label_size=label_size)
        self.color = color
        self.bars = []
        self.x_data = []
        self.y_data = []
        self.tick_positions = tick_positions
        self.tick_labels = tick_labels

    def setup(self, visible=True):
        super().setup(visible=visible)
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
            bar = self.ax.bar(frame, self.data[frame], color=self.color)
            self.bars.append(bar)

        return self.bars[-1] if self.bars else []

    def reset(self):
        self.x_data.clear()
        self.y_data.clear()
        for bar_group in self.bars:
            for bar in bar_group:
                bar.remove()
        self.bars.clear()
