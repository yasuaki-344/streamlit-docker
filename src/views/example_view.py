"""ビュークラスの実装."""
from controllers.example_controller import ExampleController
import streamlit as st


class ExampleView:
    """ビュークラスの一例."""

    def __init__(self, controller: ExampleController):
        """ビュークラスのコンストラクタの一例.

        Args:
            controller (ExampleController): ビューに1対1対応したコントローラー.
        """
        self.__controller = controller


def app1():
    st.title('APP1')
    st.write('Welcome to app1')
