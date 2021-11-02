"""Containers module."""

from dependency_injector import containers, providers

from business_logic.example_business_logic import ExampleBusinessLogic
from controllers.example_controller import ExampleController
from repositories.example_repository import ExampleRepository
from use_cases.example_interactor import ExampleInteractor
from views.another_view import AnotherView
from views.example_view import ExampleView


class Container(containers.DeclarativeContainer):
    """依存性の解決を行うためのコンテナの実装."""

    # repository の依存性の解決
    example_repository = providers.Singleton(ExampleRepository)

    # business logic の依存性の解決
    example_business_logic = providers.Factory(ExampleBusinessLogic)

    # use case の依存性の解決
    example_use_case = providers.Factory(
        ExampleInteractor,
        logic=example_business_logic,
        repository=example_repository)

    # controller の依存性の解決
    example_contoller = providers.Factory(
        ExampleController, use_case=example_use_case)

    # view の依存性の解決
    view1 = providers.Singleton(ExampleView, controller=example_contoller)
    view2 = providers.Singleton(AnotherView)