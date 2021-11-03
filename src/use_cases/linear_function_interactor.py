"""ユースケース実装の一例."""

import numpy as np
from typing import Dict


class LinearFunctionInteractor:
    """一次関数データの作成."""

    def __init__(self):
        """ユースケースコンストラクタの一例.
        """
        pass

    def create_data(self, gradient: float, intercept: float
                    ) -> Dict[str, np.array]:
        """一次関数のプロットデータを作成する.

        Args:
            gradient (float): 傾き
            intercept (float): 切片

        Returns:
            [type]: [description]
        """
        x_data = np.random.random(20)
        data = {
            'x': x_data,
            'y': gradient * x_data + intercept
        }
        return data
