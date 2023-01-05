from collections import UserDict
from typing import Any, Hashable


class SubclassDict(UserDict):
    def __getitem__(self, value: Hashable) -> Any:
        try:
            return self.data[value]
        except:
            for key in self.data:
                if issubclass(type(value), key):
                    return self.data[key]