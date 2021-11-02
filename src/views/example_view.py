"""ビュークラスの実装."""
import streamlit as st

from controllers.example_controller import ExampleController


class ExampleView:
    """ビュークラスの一例."""

    def __init__(self, controller: ExampleController):
        """ビュークラスのコンストラクタの一例.

        Args:
            controller (ExampleController): ビューに1対1対応したコントローラー.
        """
        self.__controller = controller

    def to_view(self):
        """streamlitで表示するためのページを作成."""
        st.title('APP1')
        st.write('Welcome to app1')
