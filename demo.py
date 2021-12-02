import json
from typing import Dict, List
from pydantic import BaseModel, Extra


class GlossEntry(BaseModel, extra=Extra.ignore):
    ID: str
    Acronym: str


class GlossDiv(BaseModel, extra=Extra.ignore):
    title: str
    GlossList: Dict[str, GlossEntry]


class Glossary(BaseModel, extra=Extra.ignore):
    title: str
    GlossDiv: GlossDiv


class Thing(BaseModel, extra=Extra.ignore):
    glossary: Glossary


def main():
    with open("demo.json", "r") as jin:
        inpt = json.load(jin)
        mdel = Thing.parse_obj(inpt)
        print(mdel)


if __name__ == "__main__":
    main()
