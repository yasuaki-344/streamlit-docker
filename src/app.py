"""streamlitのメイン部の実装."""

from multiapps import MultiApp
from views.another_view import app2
from views.example_view import app1


def main():
    """Set up and run application."""
    app = MultiApp()
    app.add_app("1st page", app1)
    app.add_app("2nd page", app2)

    app.run()


if __name__ == "__main__":
    main()
