from jskos import get_mappings_from_jskos

# get mappings from jskos
def get_mappings(_ids: list[str]):
    jskos_ids = get_mappings_from_jskos(_ids)
    return jskos_ids
# send mappings to reasoner

# send ids to reasoner for additional mappings


# return all matching ids
