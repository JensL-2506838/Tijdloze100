from tijdloze100_types import *
import os


def lees_tijdloze100(root_folder: str) -> Edities:
    result: Edities = dict()

    path: str = os.path.join(os.getcwd(), root_folder)
    edities: list[str] = os.listdir(path)
    for editie in edities:
        cur_path: str = os.path.join(path, editie)
        nummers: list[str] = os.listdir(cur_path)
        cur_editie: Editie = []
        for nummer in nummers:
            num_path: str = os.path.join(cur_path, nummer)
            files: list[str] = ["artiest.txt", "titel.txt", "release_jaar.txt"]
            with open(os.path.join(num_path, files[0])) as data:
                the_artist: str = data.readline().rstrip("\n")

            with open(os.path.join(num_path, files[1])) as data:
                the_title: str = data.readline().rstrip("\n")

            with open(os.path.join(num_path, files[2])) as data:
                release_year: int = int(data.readline().rstrip("\n"))

            cur_editie.append((the_artist, the_title, release_year))
        
        result[int(editie)] = cur_editie

    return result



def schrijf_tijdloze100(edities: Edities, csv_out: str) -> None:
    # TODO: voeg gepaste docstring toe.
    # TODO: vervolledig deze functie.
    pass


a = lees_tijdloze100("tijdloze")
for edition in a.values():
    print(edition)