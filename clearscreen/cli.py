import argparse
import pathlib
import random
import sys
import typing as t

from . import art as art_module


class InvalidChoice(BaseException):
    def __init__(self, arg: t.Union[int, str]) -> None:
        self.arg = arg

def format_vertical_lines(lines: t.List[str]) -> t.List[str]:
    is_empty = [l.strip() == '' for l in lines]
    try:
        first_non_empty = is_empty.index(False)
    except ValueError:
        first_non_empty = 0

    is_empty.reverse()
    try:
        last_non_empty = len(lines) - is_empty.index(False)
    except ValueError:
        last_non_empty = len(lines)

    return [''] + lines[first_non_empty: last_non_empty] + ['']


class Screens:
    def __init__(self, path: pathlib.Path) -> None:
        self._path = path
        self._files = [f for f in path.iterdir() if f.is_file() and f.suffix == '.txt']

    def get_by_index(self, index: int) -> t.List[str]:
        if index > len(self._files) - 1:
            raise InvalidChoice(index)
        with open(self._files[index]) as f:
            lines = list(l.rstrip() for l in f.readlines())
            return format_vertical_lines(lines)

    def get_by_name(self, name: str) -> t.List[str]:
        for index, f in enumerate(self._files):
            if name == f.stem:
                return self.get_by_index(index)
        raise InvalidChoice(name)

    @property
    def length(self):
        return len(self._files)

    @property
    def names(self):
        return [(index, f.stem) for index, f in enumerate(self._files)]

    def random(self) -> t.List[str]:
        r = random.random()
        max = len(self._files)
        choice = int(r * max)
        return self.get_by_index(choice)



def main()-> None:
    screens = Screens(pathlib.Path(art_module.__file__).parent)
    parser = argparse.ArgumentParser("cls", description="Shows random art to clear the screen.")
    parser.add_argument("--index", help=f"Index of art to pick (max {screens.length - 1}", required=False, default=None, type=int)
    parser.add_argument("--name", required=False, default=None, help="Name of art")
    parser.add_argument("--ls", help="List all the screens", action="store_true")
    args = parser.parse_args()

    if args.ls:
        print("Selections:")
        for index, name in screens.names:
            print(f"\t{index: < 3} {name}")
        sys.exit(0)
    try:
        if args.name is not None:
            art = screens.get_by_name(args.name)
        elif args.index is not None:
            art = screens.get_by_index(args.index)
        else:
            art = screens.random()
    except InvalidChoice as ic:
        print('Invalid selection "{}". Pick a number from 0 - {}.'
              .format(ic.arg, screens.length))
        sys.exit(1)

    for index, line in enumerate(art):
        if index == 0 and line.strip() != '':
            print()  # add an extra line
        print(line)
        if index == len(art) - 1 and line.strip() != '':
            print()  # add one last line for spacing



if __name__=='__main__':
    main()