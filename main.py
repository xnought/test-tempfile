import tempfile
from pathlib import Path
import os
import shutil


def test_mkdtemp():
    p = Path(tempfile.mkdtemp())
    print(p)
    print(os.listdir(p))
    shutil.rmtree(p)


class TemporaryDirectoryPath(tempfile.TemporaryDirectory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __enter__(self, *args, **kwargs):
        return Path(super().__enter__(*args, **kwargs))  # gota love Path

    def __exit__(self, *args, **kwargs):
        super().__exit__(*args, **kwargs)


def test_Temporary():
    with tempfile.TemporaryDirectory() as path_str:
        tempdir = Path(path_str)  # i prefer to use pathlib instead of str

        with open(tempdir / "test.txt", "w") as f:
            f.write("Hi there!")

        print(os.listdir(tempdir))

    print("Dir was deleted?", not os.path.exists(tempdir))


def test_TempFile():
    with tempfile.NamedTemporaryFile("r+", dir=".cache") as f:
        f.write("Hi")
        f.seek(0)
        d = f.read()
        print(d)


def test_TemporaryPath():
    with TemporaryDirectoryPath(dir=".cache", prefix="test") as tempdir:
        with open(tempdir / "test.txt", "w") as f:
            f.write("Hi there!")

        print(os.listdir(tempdir))
        while True:
            continue

    print("Dir was deleted?", not os.path.exists(tempdir))


def main():
    # test_mkdtemp() # cons is that have to manually delete temporary dir
    # test_Temporary()
    # test_TempFile()
    test_TemporaryPath()


if __name__ == "__main__":
    main()
