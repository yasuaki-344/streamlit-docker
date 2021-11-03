"""プロットサンプルページの管理データと挙動を実装するクラス."""
import numpy as np
import pandas as pd

from use_cases.linear_function_interactor import LinearFunctionInteractor
from view_models.plot_sample_view_model import PlotSampleViewModel


class PlotSampleController:
    """サンプルプロットページ制御クラス."""

    def __init__(self, use_case: LinearFunctionInteractor):
        """コントローラークラスのコンストラクタの一例.

        Args:
            use_case (ExampleInteractor): コントローラークラスで使用するユースケース
        """
        self.view_model = PlotSampleViewModel(gradient=0.0, intercept=0.0)
        self.__use_case = use_case

    def create_plot_data(self) -> pd.DataFrame:
        """サンプルデータを作成する."""
        data = self.__use_case.create_data(
            self.view_model.gradient, self.view_model.intercept)
        df = pd.DataFrame(data).set_index('x')
        return df
