import streamlit as st
from streamlit.components.v1 import html

iframe_html = """<iframe frameborder="0" src="https://itch.io/embed-upload/10008023?color=2c2c2c" allowfullscreen="" width="960" height="610"><a href="https://astronautpotato.itch.io/patient73-catastrophia">Play CatastrophIA on itch.io</a></iframe>"""

html(iframe_html, width=960, height=610)