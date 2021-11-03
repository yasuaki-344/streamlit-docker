"""ユースケース実装の一例."""

from business_logic.example_business_logic import ExampleBusinessLogic
from dto.example_data_class import ExampleDataClass
from repositories.example_repository import ExampleRepository


class ExampleInteractor:
    """ユースケースクラス実装の一例."""

    def __init__(self,
                 logic: ExampleBusinessLogic,
                 repository: ExampleRepository):
        """ユースケースコンストラクタの一例.

        Args:
            logic (ExampleBusinessLogic): ユースケースで使用するビジネスロジック
            repository (ExampleRepository): ユースケースで使用するリポジトリ
        """
        self.__logic = logic
        self.__repository = repository

    def get_info(self) -> ExampleDataClass:
        """ビジネスロジックとリポジトリを組み合わせて実現するユースケースの一例.

        Returns:
            ExampleDataClass: 返却するデータクラス
        """
        entity = self.__repository.get_entity()
        entity.name = self.__logic.to_upper(entity.name)
        return entity
