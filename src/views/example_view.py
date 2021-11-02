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
        st.title("Example view")
        st.write('Clean architecture based example view')
        is_pressed = st.button("execute sample process")
        if is_pressed:
            self.__controller.get_user_info()

        st.write(self.__controller.user_name)
        st.write(self.__controller.mail_address)
