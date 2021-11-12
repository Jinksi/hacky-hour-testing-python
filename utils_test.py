from utils import get_bbox_center_x


def test_get_bbox_center_x():
    assert get_bbox_center_x(0, 50) == 25
    assert get_bbox_center_x(100, 200) == 200
    assert get_bbox_center_x(500, 1) == 500.5
