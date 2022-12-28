#! /usr/bin/python3.9

from tests.common_vars import caa
from tests.source_files import cat_part_measurable


def test_application():
    assert 'Application(name="CNEXT")' in caa.__repr__()


def test_refresh():
    documents = caa.documents
    documents.open(str(cat_part_measurable))
    document = caa.active_document

    caa.refresh_display = False
    assert caa.refresh_display is False

    caa.refresh_display = True
    assert caa.refresh_display is True

    document.close()


def test_visible():
    documents = caa.documents
    documents.open(str(cat_part_measurable))
    document = caa.active_document

    caa.visible = False
    assert caa.visible is False

    caa.visible = True
    assert caa.visible is True

    document.close()
