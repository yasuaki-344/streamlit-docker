"""データアクセスオブジェクトのサンプル."""


class ExampleBusinessLogic:
    """データアクセスオブジェクトの一例."""

    def __init__(self):
        """Initialize a new instance of ExampleBusinessLogic."""
        pass

    def to_upper(self, name: str) -> str:
        """ビジネスロジック実装の一例.

        Args:
            name (str): 変換元の文字列

        Returns:
            str: 大文字に変換した文字列
        """
        upper_str = name.upper()
        return upper_str
