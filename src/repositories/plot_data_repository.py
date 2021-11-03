"""プロットデータアクセスオブジェクトのサンプル."""
import numpy as np


class PlotDataRepository:
    """データアクセスオブジェクトの一例."""

    def __init__(self):
        """Initialize a new instance of ExampleRepository."""
        pass

    def generate_data(self) -> np.array:
        """データ取得の一例."""
        x_data = np.random.random(20)
        return x_data
