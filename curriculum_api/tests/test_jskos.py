from curriculum_api import jskos


def test_get_ids_from_jskos():
    test_ids = ["http://uri.gbv.de/terminology/bk/0"]
    res = jskos.get_ids_from_jskos(test_ids)
    assert res != None

if __name__ == "__main__":
    test_get_ids_from_jskos()
