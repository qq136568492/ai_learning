# 练习时可先遮住实现自行编写。
"""类迭代器：从 start 起步长 step 计数 n 次。"""


class StepCount:

    def __init__(self, start: int, step: int, n: int) -> None:
        self.start = start
        self.step = step
        self.n = n
        self.current = 0

    def __iter__(self) -> 'StepCount':
        return self

    def __next__(self) -> int:
        if self.current >= self.n:
            raise StopIteration
        result = self.start + self.current * self.step
        self.current += 1
        return result

if __name__ == '__main__':
    assert list(StepCount(0, 2, 3)) == [0, 2, 4]
    print('ok')
