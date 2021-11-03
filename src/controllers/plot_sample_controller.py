"""プロットサンプルページの管理データと挙動を実装するクラス."""
from view_models.plot_sample_view_model import PlotSampleViewModel
import pandas as pd
import numpy as np


class PlotSampleController:
    """サンプルプロットページ制御クラス."""

    def __init__(self):
        """コントローラークラスのコンストラクタの一例.

        Args:
            use_case (ExampleInteractor): コントローラークラスで使用するユースケース
        """
        self.view_model = PlotSampleViewModel(gradient=0.0, intercept=0.0)

    def create_plot_data(self) -> pd.DataFrame:
        """サンプルデータを作成する."""
        x_data = np.random.random(20)
        data = {
            'x': x_data,
            'y': self.view_model.gradient * x_data + self.view_model.intercept
        }
        df = pd.DataFrame(data).set_index('x')
        return df
