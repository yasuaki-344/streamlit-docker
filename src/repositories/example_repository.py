"""データアクセスオブジェクトのサンプル."""
from entities.example_data_class import ExampleDataClass


class ExampleRepository:
    """データアクセスオブジェクトの一例."""

    def __init__(self):
        """Initialize a new instance of ExampleRepository."""
        pass

    def get_entity(self) -> ExampleDataClass:
        """データ取得の一例.

        Returns:
            ExampleDataClass: データクラスで関連データを集約して返す
        """
        entity = ExampleDataClass("user", "xxx@xxx")
        return entity
