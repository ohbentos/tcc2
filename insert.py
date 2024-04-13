import numpy as np
from tqdm import tqdm

from db.postgres import PGDatabase


def main():
    insert_data([PGDatabase(8000)], restart=False)


def insert_data(curs: list[PGDatabase], restart=False):
    for x in curs:
        pass


if __name__ == "__main__":
    main()
