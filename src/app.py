"""streamlitのメイン部の実装."""

from dependency_injector import containers
from containers import Container
from multiapps import MultiApp

from dependency_injector.wiring import Provide, inject

from views.another_view import AnotherView


@inject
def main(app1=Provide[Container.view1],
         app2: AnotherView = Provide[Container.view2]):
    """Set up and run application."""
    app = MultiApp()
    # ここでページの追加を行う.
    app.add_app("1st page", app1)
    app.add_app("2nd page", app2.to_view)

    # アプリケーションの実
    app.run()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()
