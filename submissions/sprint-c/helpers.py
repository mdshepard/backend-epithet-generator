import os
import json
import random
from secrets import randbelow


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    """Returns a random Bardly quip!"""
    vernacular = Vocabulary()

    @classmethod
    def generate_epithet(cls, path):
        """Returns but one verbose tongue lashing!"""
        dict_columns = cls.vernacular.from_file(path)[0]
        epithet = []
        for Columns in dict_columns:
            epithet.append(random.choice(dict_columns[Columns]))
        return epithet

    @classmethod
    def generate_epithets(cls, path, quantity):
        """Returns as many obscure verbal attacks as you see fit."""
        epithets = {}
        for i in range(quantity):
            epithets[i+1] = cls.generate_epithet(path)
        return epithets

    @classmethod
    def random_num_epithets(cls, path):
        """Returns a random quantity of generated epithets"""
        epithets = {}
        random_num = randbelow(20)+1
        for i in range(random_num):
            epithets[i+1] = cls.generate_epithet(path)
        return epithets
