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
        self.__user_name = ""
        self.__mail_address = ""

    @property
    def user_name(self):
        """Get only property."""
        return self.__user_name

    @property
    def mail_address(self):
        """Get only property."""
        return self.__mail_address

    def get_user_info(self):
        """Try to call use case function."""
        entity = self.__use_case.get_info()
        self.__user_name = entity.name
        self.__mail_address = entity.mail_address
