from pathlib import Path, PurePath
import tarfile, gzip, os, sys, json, zipfile
from glob import glob


def writetestdata(*args):
    "Attempt to write test data to the corresponding files"
    for file in args:
        with open(file, "w", encoding="utf8") as my_file:
            my_file.write("here is some content")


writetestdata("testfileone.txt", "testfiletwo.txt", "testfilethree.txt")

# Add demo files to tarfile

fdtar = tarfile.open("mynewtarfile.tar.gz", "w:gz")
fdtar.add("testfileone.txt")
fdtar.add("testfiletwo.txt")
fdtar.add("testfilethree.txt")
fdtar.close()

os.listdir(".")
