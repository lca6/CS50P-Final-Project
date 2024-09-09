from project import (
    progress,
    previous_element,
    hint,
    skipped_element,
)


def test_progress():
    assert (
        progress(0)
        == f"""
0 done
119 elements remaining\n
"""
    )
    assert (
        progress(1)
        == f"""
1 done
118 elements remaining\n
"""
    )


def test_previous_element():
    assert (
        previous_element(78)
        == f"""
Below is the previous element in the Periodic Table:

Platinum (Pt)
"""
    )


def test_hint():
    assert (
        hint(0)
        == """
Appearance: colorless gas
Category: diatomic nonmetal
Phase: Gas
Period 1
Group 1
Electron configuration: 1s1
"""
    )


def test_skipped_element():
    assert (
        skipped_element(43)
        == """
Name: Ruthenium
Summary: Ruthenium is a chemical element with symbol Ru and atomic number 44. It is a rare transition metal belonging to the platinum group of the periodic table. Like the other metals of the platinum group, ruthenium is inert to most other chemicals.
"""
    )
