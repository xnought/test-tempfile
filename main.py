import tempfile
from pathlib import Path
import os
import shutil


def test_mkdtemp():
    p = Path(tempfile.mkdtemp())
    print(p)
    print(os.listdir(p))
    shutil.rmtree(p)


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


def main():
    # test_mkdtemp() # cons is that have to manually delete temporary dir
    test_Temporary()
    # test_TempFile()


if __name__ == "__main__":
    main()
