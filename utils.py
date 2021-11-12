def get_bbox_center_x(bbox_x, bbox_w):
    assert bbox_x >= 0, "bbox_x should be >= 0"
    assert bbox_w >= 0, "bbox_w should be >= 0"

    center_x = bbox_x + divide_by_two(bbox_w)
    return center_x


def divide_by_two(num):
    return num / 2