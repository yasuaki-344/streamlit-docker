"""Containers module."""

from dependency_injector import containers, providers
from views.another_view import AnotherView

from views.example_view import app1


class Container(containers.DeclarativeContainer):
    """依存性の解決を行うためのコンテナの実装."""
    view1 = providers.Factory(app1)
    view2 = providers.Factory(AnotherView)
