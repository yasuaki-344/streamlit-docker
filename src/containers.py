"""Containers module."""

from dependency_injector import containers, providers

from business_logic.example_business_logic import ExampleBusinessLogic
from controllers.example_controller import ExampleController
from controllers.plot_sample_controller import PlotSampleController
from repositories.example_repository import ExampleRepository
from use_cases.example_interactor import ExampleInteractor
from use_cases.linear_function_interactor import LinearFunctionInteractor
from views.example_view import ExampleView
from views.plot_sample_view import PlotSampleView


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
    linear_function_interactor = providers.Factory(LinearFunctionInteractor)

    # controller の依存性の解決
    example_contoller = providers.Factory(
        ExampleController, use_case=example_use_case)
    plot_sample_contoller = providers.Factory(
        PlotSampleController, use_case=linear_function_interactor)

    # view の依存性の解決
    view1 = providers.Singleton(ExampleView, controller=example_contoller)
    view2 = providers.Singleton(
        PlotSampleView, controller=plot_sample_contoller)
