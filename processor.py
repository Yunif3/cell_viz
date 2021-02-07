from spreadsheet import Spreadsheet
from visualize import *

sheet = Spreadsheet('1cH4OGCXdfq_3CNAec6hWsXUtXJ9-4PPBUBEbMPg5XRc')
# test_tags = {"Action": "make", "Graph": "line graph", "Range": "range from A1 to D4"}

def process(tags):
    if "Action" not in tags:
        print("ERROR: Action is not in tags")
    
    # TODO: think of better ways to store data since this is a singleton
    action_type = tags["Action"][0]
    if action_type == "make":
        graph = get_graph(tags)
        data = get_data(tags)
        kwargs = {"color": "red"} # TODO: come back to this
        graph(data, kwargs=kwargs)
    elif tags["Action"] == "change":
        pass


def get_graph(tags):
    if "Graph" not in tags:
        print("ERROR: Graph is not in tags")
    
    # TODO: think of better ways to store data since this is a singleton
    graph_type = tags["Graph"][0]
    if graph_type == "line graph":
        return line_plot


def get_data(tags):
    if "Range" in tags:
        # TODO: assume that the range list always has one element at the moment
        range_start, range_end = extract_cell_range(tags["Range"][0])
        print(range_start, range_end)
        return sheet.get_range(range_start, range_end)
    else:
        print("ERROR: There is no data")


# will be given the form "range from X to Y"
def extract_cell_range(range_text):
    tokens = range_text.split()
    return (tokens[2], tokens[4])

    
    
    
