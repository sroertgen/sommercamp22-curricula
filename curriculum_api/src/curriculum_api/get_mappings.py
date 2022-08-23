from jskos import get_mappings_from_jskos
from insert_data import insert_data

# get mappings from jskos
def get_mappings(_ids: list[str]):
    jskos_ids = get_mappings_from_jskos(_ids)
    insert_data(jskos_ids)
    return jskos_ids

# send mappings to triple store
def insert_mappings_to_triple_store(jskos_ids: list[str]):
    pass

# send mappings to reasoner

# send ids to reasoner for additional mappings


# return all matching ids
