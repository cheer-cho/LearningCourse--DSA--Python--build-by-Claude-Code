from checkpoint_11 import (
    OrgNode,
    chain_of_command,
    common_manager,
    headcount,
    management_depth,
    meetings_by_level,
)


def _sample_org() -> OrgNode:
    #            Ava
    #           /    \
    #         Bo      Cy
    #        /  \        \
    #      Dee  Eli       Fay
    dee = OrgNode("Dee")
    eli = OrgNode("Eli")
    fay = OrgNode("Fay")
    bo = OrgNode("Bo", left=dee, right=eli)
    cy = OrgNode("Cy", right=fay)
    return OrgNode("Ava", left=bo, right=cy)


def test_headcount_typical():
    assert headcount(_sample_org()) == 6


def test_headcount_empty():
    assert headcount(None) == 0


def test_headcount_single_person():
    assert headcount(OrgNode("Ava")) == 1


def test_management_depth_typical():
    assert management_depth(_sample_org()) == 3


def test_management_depth_empty():
    assert management_depth(None) == 0


def test_management_depth_single_person():
    assert management_depth(OrgNode("Ava")) == 1


def test_chain_of_command_finds_leaf():
    assert chain_of_command(_sample_org(), "Fay") == ["Ava", "Cy", "Fay"]


def test_chain_of_command_root_is_itself():
    assert chain_of_command(_sample_org(), "Ava") == ["Ava"]


def test_chain_of_command_missing_name():
    assert chain_of_command(_sample_org(), "Zed") == []


def test_chain_of_command_empty_org():
    assert chain_of_command(None, "Ava") == []


def test_meetings_by_level_groups_left_to_right():
    assert meetings_by_level(_sample_org()) == [
        ["Ava"],
        ["Bo", "Cy"],
        ["Dee", "Eli", "Fay"],
    ]


def test_meetings_by_level_empty():
    assert meetings_by_level(None) == []


def test_common_manager_siblings():
    assert common_manager(_sample_org(), "Dee", "Eli") == "Bo"


def test_common_manager_across_branches():
    assert common_manager(_sample_org(), "Dee", "Fay") == "Ava"


def test_common_manager_ancestor_and_descendant():
    assert common_manager(_sample_org(), "Bo", "Dee") == "Bo"


def test_common_manager_missing_name_returns_none():
    assert common_manager(_sample_org(), "Dee", "Zed") is None


def test_common_manager_same_person_twice():
    assert common_manager(_sample_org(), "Fay", "Fay") == "Fay"
