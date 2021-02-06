from spreadsheet import Spreadsheet

sheet = Spreadsheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms')
print(sheet.get_range("a", "b"))

def process(tags):
    if "Action" not in tags:
        return None
    elif tags["Action"] == "make":
        return make_graph(tags)
    elif tags["Action"] == "change":
        pass

 
def make_graph(tags):
    pass



    
    
    
