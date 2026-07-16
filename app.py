import streamlit as st
import streamlit.components.v1 as components

st.title("手動攪珠機")

# 讀取外部 HTML 檔案
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 載入並顯示
html_content = load_html("simulator.html")
components.html(html_content, height=600)
