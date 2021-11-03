"""プロットサンプルページの管理データと挙動を実装するクラス."""
from view_models.plot_sample_view_model import PlotSampleViewModel


class PlotSampleController:
    """サンプルプロットページ制御クラス."""

    def __init__(self):
        """コントローラークラスのコンストラクタの一例.

        Args:
            use_case (ExampleInteractor): コントローラークラスで使用するユースケース
        """
        self.view_model = PlotSampleViewModel(gradient=0.0, intercept=0.0)

    def create_plot_data(self):
        """サンプルデータを作成する."""
        pass
