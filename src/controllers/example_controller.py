"""コントローラークラスの実装."""
from use_cases.example_interactor import ExampleInteractor


class ExampleController:
    """コントローラークラスの一例."""

    def __init__(self, use_case: ExampleInteractor):
        """コントローラークラスのコンストラクタの一例.

        Args:
            use_case (ExampleInteractor): コントローラークラスで使用するユースケース
        """
        self.__use_case = use_case
