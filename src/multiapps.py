"""Frameworks for running multiple Streamlit applications as a single app."""
import streamlit as st


class MultiApp:
    """Framework for combining multiple streamlit applications."""

    def __init__(self):
        """Initialize a new instance of MultiApp."""
        self.pages = {}

    def add_app(self, title, func):
        """Add a new application.

        Args:
            title ([type]): the python function to render this app.
            func ([type]): title of the app. Appears in the dropdown in the
                           sidebar.
        """
        self.pages[title] = func

    def run(self):
        """Run application."""
        selection = st.sidebar.radio("Go To", list(self.pages.keys()))

        app = self.pages[selection]
        app()
