import numpy as np


__all__ = ['Scatter', 'Histogram', 'LinePlot']


class Scatter:

    def __init__(self, x, y):
        """
        Constructor for Scatter.

        Args:
            x : (array type)
            y : (array type)
        """

        self.plottype = 'scatter'

        self.x = x
        self.y = y

        self.markersize = 5
        self.color = 'darkgray'
        self.marker = 'o'
        self.vmin = None
        self.vmax = None
        self.alpha = None
        self.linewidths = 1.5
        self.edgecolors = None
        self.label = f'n={np.count_nonzero(~np.isnan(x))}'
        self.linear_regression = False
        self.density = False

    def add_linear_regression(self):
        """
        Include linear regression line info as attributes.
        """
        self.linear_regression = True
        self.lr_color = 'black'
        self.lr_linewidth = 1

    def density_scatter(self):
        """
        Include density scatter plot info as attributes.
        """
        self.density = True
        self.sort = True
        self.cmap = 'magma'
        self.colorbar = True
        self.bins = [100, 100]


class Histogram:

    def __init__(self, data):
        """
        Constructor for Histogram.

        Args:
            data : (array type)
        """

        self.plottype = 'histogram'

        self.data = data

        self.bins = 10
        self.range = None
        self.density = False
        self.weights = None
        self.cumulative = False
        self.bottom = None
        self.histtype = 'bar'
        self.align = 'mid'
        self.orientation = 'vertical'
        self.rwidth = None
        self.log = False
        self.color = 'tab:blue'
        self.label = f'n={np.count_nonzero(~np.isnan(data))}'
        self.stacked = False
        self.alpha = None


class LinePlot:

    def __init__(self, x, y):
        """
        Constructor for Scatter.

        Args:
            x : (array type)
            y : (array type)
        """

        self.plottype = 'line_plot'

        self.x = x
        self.y = y

        self.color = 'tab:blue'
        self.linestyle = '-'
        self.linewidth = 1.5
        self.marker = None
        self.markersize = None
        self.alpha = None
        self.label = None


class VerticalLine:

    def __init__(self, x):
        """
        Constructor for VerticalLine

        Args:
            x : (int/float) x-value where vertical line
                is to be plotted
        """

        self.plottype = 'vertical_line'

        self.x = x

        self.color = 'black'
        self.linestyle = '-'
        self.linewidth = 1.5
        self.label = None


class HorizontalLine:

    def __init__(self, y):
        """
        Constructor for HorizontalLine

        Args:
            y : (int/float) y-value where horizontal
                line is to be plotted
        """

        self.plottype = 'horizontal_line'

        self.y = y

        self.color = 'black'
        self.linestyle = '-'
        self.linewidth = 1.5
        self.label = None
