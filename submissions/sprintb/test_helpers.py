
from sprintb.helpers import Vocabulary, EpithetGenerator, FileManager
import pytest
from pathlib import PurePath as Path
import os
p = Path(os.getcwd())
project_root = str(p.parent.parent)

json_path = os.path.join(project_root+'/resources', 'data.json')
csv_path = os.path.join(project_root+'/resources', 'data.csv')


def test_get_extension():
    """Tests for the appropriate file extensions from our FileManager class """
    path = 'thisstuff.txt'
    path2 = 'thisstuff.json'
    path3 = 'thisstuff.csv'
    assert FileManager.get_extension(path) == 'txt'
    assert FileManager.get_extension(path2) == 'json'
    assert FileManager.get_extension(path3) == 'csv'


def test_read_json():
    """Tests if reads json, if provided else raises error """
    returned_json = FileManager.read_json(json_path)
    print(type(returned_json))
    assert type(returned_json) == dict
    assert len(returned_json.keys()) == 3
    with pytest.raises(Exception):
        FileManager.read_json(csv_path)


def test_Vocabulary_from_file():
    """Tests json data returned by 'from_file'"""
    representation = Vocabulary.from_file(json_path)
    Vocabulary_data = representation[0]
    assert type(representation) == tuple
    assert type(Vocabulary_data) == dict
    assert len(Vocabulary_data.keys()) == 3
    with pytest.raises(Exception):
        Vocabulary.from_file(csv_path)


def test_Vocabulary_from_json():
    """Tests the from_json method in Vocabulary """
    representation = Vocabulary.from_json(json_path)
    assert type(representation) == tuple
    assert type(representation[0]) == dict
    assert len(representation[0]) == 3
    with pytest.raises(Exception):
        FileManager.read_json(csv_path)


def test_Vocabulary_strategies():
    """Tests if the vocabulary is being gathered form it's proper path"""
    json_strategy = Vocabulary.strategies('json')
    assert json_strategy.__name__ == 'from_json'
    with pytest.raises(Exception):
        FileManager.read_json(csv_path)


def test_single_epithet():
    """Tests that the epithet is served to the proper path"""
    words = EpithetGenerator.generate_epithet(json_path)
    assert type(words) == list
    assert len(words) == 3


def test_epithet_multiple():
    """tests that we're serving the proper quantity of multiple epithets """
    quantity = 2
    assert type(EpithetGenerator.generate_epithets(
        json_path, quantity)) == dict
    assert len(EpithetGenerator.generate_epithets(
        json_path, quantity)) == quantity


def test_random_num_epithets():
    """tests that we're generating a random # of epithets between 1 and 20"""
    assert type(EpithetGenerator.random_num_epithets(json_path)) == dict
