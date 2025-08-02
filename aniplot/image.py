from .base import BasePlot
import matplotlib.pyplot as plt

class ImagePlot(BasePlot):
    def __init__(self, ax, image_data, title=None, border_color="black", border_width=2.5, color_border=False, title_size=10):
        super().__init__(ax, data=image_data, title=title,border_color=border_color, border_width=border_width, color_border=color_border, title_size=title_size)
        self.image_drawn = False
        self.image_obj = None

    def setup(self, visible=True):
        super().setup(visible = visible)
       # if self.title:
      #      self.ax.set_title(self.title)

        # Disable axes ticks for a cleaner image panel
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        # Optionally set limits depending on the image shape
        if self.data is not None:
            height, width = self.data.shape[:2]
            self.ax.set_xlim(0, width)
            self.ax.set_ylim(height, 0)  # Top-left origin for images

        self._initialized = True

    def update(self, frame):
        if frame < 0:
          return
        
        if not self.ax.get_visible():
          self.ax.set_visible(True)
        
        if not self.image_drawn:
            self.image_obj = self.ax.imshow(self.data, aspect='auto')
            self.image_drawn = True

    def reset(self):
        super().reset()
        self.image_drawn = False
        self.image_obj = None
