from app import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    # Check that the header is present
    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Soul Foods - Pink Morsel Sales Visualizer"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    # Check that the graph is present
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    # Check that the region picker is present
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None
