import re
from typing import Optional

from icontract import require, ensure

ENTRY_RE = re.compile(
    r"^(?P<min_count>0|[1-9][0-9]*)-(?P<max_count>0|[1-9][0-9]*) "
    r"(?P<character>[a-z]): (?P<password>[a-z]+)$"
)


@require(lambda line: ENTRY_RE.match(line))
def verify_line(line: str) -> Optional[bool]:
    mtch = ENTRY_RE.match(line)
    if mtch is None:
        return None

    return verify(
        min_count=int(mtch.group("min_count")),
        max_count=int(mtch.group("max_count")),
        character=mtch.group("character"),
        password=mtch.group("password"),
    )


@require(lambda min_count: min_count > 0)
@require(lambda max_count: max_count > 0)
@require(lambda min_count, max_count: min_count <= max_count)
@require(lambda character: len(character) == 1)
@ensure(lambda password, result: not (len(password) == 0) or not result)
def verify(min_count: int, max_count: int, character: str, password: str) -> bool:
    # crosshair: on
    answer = min_count <= password.count(character) <= max_count
    return answer