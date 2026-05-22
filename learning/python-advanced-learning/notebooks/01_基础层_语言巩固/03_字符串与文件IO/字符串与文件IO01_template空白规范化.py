# 练习时可先遮住实现自行编写。
"""字符串：规范化空白并做模板填充。"""
from string import Template

def format_greeting(name: str, mood: str) -> str:
    who = " ".join(name.split())
    feel = mood.strip()
    t = Template("Hello, $who — feeling $feel today.")
    return t.substitute(who=who, feel=feel)

if __name__ == '__main__':
    assert format_greeting('  Ada\tLovelace ', ' curious ') == 'Hello, Ada Lovelace — feeling curious today.'
    print('ok')
