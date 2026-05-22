# 练习时可先遮住实现自行编写。
"""Pydantic：校验 + 预处理。"""
from pydantic import BaseModel, Field, field_validator

class Item(BaseModel):
    name: str = Field(min_length=1)

    @field_validator('name')
    @classmethod
    def normalize(cls, v: str) -> str:
        pass
if __name__ == '__main__':
    i = Item(name='  Ada ')
    assert i.name == 'ada'
    print('ok')
