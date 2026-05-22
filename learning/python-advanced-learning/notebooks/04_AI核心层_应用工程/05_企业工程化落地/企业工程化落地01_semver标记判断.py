# 练习时可先遮住实现自行编写。
"""CI/CD 语义：给定 git tag 是否 semver 前缀 v。"""

def is_semver_git_tag(tag: str) -> bool:
    pass
if __name__ == '__main__':
    assert is_semver_git_tag('v1.2.3')
    assert not is_semver_git_tag('dev')
    print('ok')
