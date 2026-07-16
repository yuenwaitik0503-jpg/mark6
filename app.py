
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="攪珠模擬器", layout="centered")

st.title("攪珠動畫模擬器")

# 這裡放入我們之前的 HTML 程式碼（包含 Matter.js）
html_code = """
<!-- 貼上你剛剛那個完整的 HTML 檔案內容，從 <!DOCTYPE html> 到 </html> -->
<!-- 記得要把 <script> 區塊內原本的 HTML 結構保留 -->
<div id="canvas-container"></div>
<div class="controls">
    <button id="btn-mix">開始攪珠</button>
    <button id="btn-draw">抽取號碼</button>
    <button id="btn-reset">重設</button>
</div>
<div id="drawn-container"></div>
<style>
    /* 這裡放入剛剛的 CSS */
</style>
<script>
    /* 這裡放入剛剛的 JavaScript */
</script>
"""

# 在 Streamlit 中渲染
components.html(html_code, height=700)
