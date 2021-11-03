"""ユースケース実装の一例."""
from typing import Dict

import numpy as np

from repositories.plot_data_repository import PlotDataRepository


class LinearFunctionInteractor:
    """一次関数データの作成."""

    def __init__(self, repository: PlotDataRepository):
        """ユースケースコンストラクタの一例."""
        self.__repository = repository

    def create_data(self, gradient: float, intercept: float
                    ) -> Dict[str, np.array]:
        """一次関数のプロットデータを作成する.

        Args:
            gradient (float): 傾き
            intercept (float): 切片

        Returns:
            [type]: [description]
        """
        x_data = self.__repository.generate_data()
        data = {
            'x': x_data,
            'y': gradient * x_data + intercept
        }
        return data
