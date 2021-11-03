"""streamlitのメイン部の実装."""

from dependency_injector.wiring import Provide, inject

from containers import Container
from multiapps import MultiApp
from views.example_view import ExampleView
from views.plot_sample_view import PlotSampleView


@inject
def main(example_view: ExampleView = Provide[Container.view1],
         plot_sample_view: PlotSampleView = Provide[Container.view2]):
    """Set up and run application."""
    app = MultiApp()
    # ここでページの追加を行う.
    app.add_app("1st page", example_view.to_view)
    app.add_app("plot sample page", plot_sample_view.to_view)

    # アプリケーションの実行
    app.run()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()
