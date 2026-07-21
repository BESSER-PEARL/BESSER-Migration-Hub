"""Pydantic request/response models for the Migration Hub API."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class PlatformsResponse(BaseModel):
    sources: list[dict]
    targets: list[dict]


class ModulesResponse(BaseModel):
    modules: list[str]


class ModelSummary(BaseModel):
    # Structural (domain) counts
    classes: Optional[int] = None
    attributes: Optional[int] = None
    associations: Optional[int] = None
    enumerations: Optional[int] = None
    class_names: list[str] = []
    # GUI counts
    modules: Optional[int] = None
    screens: Optional[int] = None
    widgets: Optional[int] = None
    screen_names: list[str] = []


class DownloadInfo(BaseModel):
    artifact: str          # domain | gui
    filename: str
    available: bool
    note: Optional[str] = None


class PivotResponse(BaseModel):
    session_id: str
    source_lcp: str
    scope: str
    summary: ModelSummary
    downloads: list[DownloadInfo]
    warnings: list[str] = []


class GenerateRequest(BaseModel):
    target_lcp: str


class ArtifactInfo(BaseModel):
    name: str
    description: str


class GenerateResponse(BaseModel):
    session_id: str
    target_lcp: str
    artifacts: list[ArtifactInfo]
    tutorial: str
    warnings: list[str] = []
