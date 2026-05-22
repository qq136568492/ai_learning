# 练习时可先遮住实现自行编写。
"""无 Streamlit 运行时：仿真 session_state 列表追加。"""

class MiniSession(dict):

    def append_msg(self, role: str, text: str) -> None:
        pass
if __name__ == '__main__':
    st = MiniSession()
    st.append_msg('user', 'hello')
    st.append_msg('assistant', 'hi')
    assert st['msgs'][0]['content'] == 'hello'
    print('ok')
