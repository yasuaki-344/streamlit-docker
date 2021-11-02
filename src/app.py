"""streamlitのメイン部の実装."""

from dependency_injector.wiring import Provide, inject

from containers import Container
from multiapps import MultiApp
from views.another_view import AnotherView
from views.example_view import ExampleView


@inject
def main(app1: ExampleView = Provide[Container.view1],
         app2: AnotherView = Provide[Container.view2]):
    """Set up and run application."""
    app = MultiApp()
    # ここでページの追加を行う.
    app.add_app("1st page", app1.to_view)
    app.add_app("2nd page", app2.to_view)

    # アプリケーションの実行
    app.run()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()
