# Testing in Python example

Watch the recording of this hacky hour discussion to see the original failing test scenarios. These should all pass!

### Topics

- Static testing
- Assertions (Sanity Check)
- Unit testing

### Example task

- Load a CSV of bounding boxes ([Data from luderick-seagrass dataset](https://github.com/globalwetlands/luderick-seagrass))
- Find the center x point of each bounding box
- Calculate the mean of the center x points

![example bbox](example_bbox.png)

## To run the example code

### Install requirements

- In terminal, run `pip install -r requirements.txt`

### Run Jupyter notebook

- In terminal, run `jupyter notebook`
- Alternatively, open with VSCode with Python extension
- Open [get_bbox_center.ipynb](get_bbox_center.ipynb)

### Run unit tests

- Unit tests are written in [utils_test.py](utils_test.py)
- In terminal, run `pytest`
