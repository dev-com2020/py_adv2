from functools import lru_cache
from typing import Any, Iterable


@lru_cache(maxsize=100)
def exp(*args, **kwargs):
    pass


UNSET = object()


def repr_instance(instance: object, attrs: Iterable[str]) -> str:
    attr_values: dict[str, Any] = {
        attr: getattr(instance, attr, UNSET) for attr in attrs
    }
    sub_repr = ", ".join(
        f"{attr}={repr(val) if val is not UNSET else 'UNSET'}"
        for attr, val in attr_values.items()
    )
    return f"<{instance.__class__.__qualname__}: {sub_repr}>"


print(repr_instance(1 + 10j, ['real', 'imag']))
