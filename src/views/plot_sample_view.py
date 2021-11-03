"""複数ページ検証用に用意した簡易的なビュークラス."""
import streamlit as st
import pandas as pd
import numpy as np


class PlotSampleView:
    """単純なビュークラス."""

    def to_view(self):
        """実際に表示するページ要素の作成."""
        st.title('Plot sample page')
        st.write('1次関数を描画するためサンプルページ')
        st.number_input("傾き", -100, 100, 1)
        st.number_input("切片", -100, 100, 0)
        st.button("描画")
        data = {
            'x': np.random.random(20),
            'y': np.random.random(20) - 0.5,
            'z': np.random.random(20) - 1.0,
        }
        df = pd.DataFrame(data).set_index('x')
        st.subheader('Line Chart')
        st.line_chart(df)
