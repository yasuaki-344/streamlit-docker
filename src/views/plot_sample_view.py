"""複数ページ検証用に用意した簡易的なビュークラス."""
import streamlit as st

from controllers.plot_sample_controller import PlotSampleController


class PlotSampleView:
    """単純なビュークラス."""

    def __init__(self, controller: PlotSampleController):
        """Initialize a new instance of PlotSampleView class.

        Args:
            controller (PlotSampleController): 対応するコントローラオブジェクト
        """
        self.__controller = controller

    def to_view(self):
        """実際に表示するページ要素の作成."""
        st.title('Plot sample page')
        st.write('1次関数を描画するためサンプルページ')
        self.__controller.view_model.gradient = \
            st.number_input("傾き", -100.0, 100.0, 1.0)
        self.__controller.view_model.intercept = \
            st.number_input("切片", -100.0, 100.0, 0.0)

        is_pressed = st.button("描画")

        st.subheader('Line Chart')
        if is_pressed:
            df = self.__controller.create_plot_data()
            st.line_chart(df)
