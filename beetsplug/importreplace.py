from __future__ import annotations

import re
from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from re import Pattern

    from beets.autotag import AlbumInfo, TrackInfo
    from confuse import Subview

from beets.plugins import BeetsPlugin


class ImportReplace(BeetsPlugin):
    def __init__(self) -> None:
        super().__init__()
        self._item_replacements: dict[str, list[tuple[Pattern[str], str]]] = {}
        self._album_replacements: dict[str, list[tuple[Pattern[str], str]]] = {}
        self._read_config()
        self.register_listener("trackinfo_received", self._trackinfo_received)
        self.register_listener("albuminfo_received", self._albuminfo_received)

    def _read_config(self) -> None:
        pass

    @staticmethod
    def _extract_patterns(replacement: Subview) -> list[tuple[Pattern[str], str]]:
        pass

    def _extract_item_fields(
        self, patterns: list[tuple[Pattern[str], str]], fields: list[str]
    ) -> None:
        pass

    def _extract_album_fields(
        self, patterns: list[tuple[Pattern[str], str]], fields: list[str]
    ) -> None:
        pass

    def _trackinfo_received(self, info: TrackInfo) -> None:
        pass

    def _albuminfo_received(self, info: AlbumInfo) -> None:
        pass

    def _replace_field(
        self, text: str | list[str], replacements: list[tuple[Pattern[str], str]]
    ) -> str | list[str]:
        pass

    def _replace(self, text: str, replacement: tuple[Pattern[str], str]) -> str:
        pass
