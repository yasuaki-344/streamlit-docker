"""複数ページ検証用に用意した簡易的なビュークラス."""
import streamlit as st


class AnotherView:
    """単純なビュークラス."""

    def to_view(self):
        """実際に表示するページ要素の作成."""
        st.title('another page')
        st.write('Welcome to another page')
