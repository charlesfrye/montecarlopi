import os
import subprocess
from pathlib import Path


def build(setup_kwargs):

    root = Path(os.getcwd())

    extension_path = root / "src" / "rust" / "pyo3_monte_carlo_pi"
    module_path = root / "src" / "python" / "montecarlopi"

    os.chdir(extension_path)

    subprocess.run(["cargo", "build", "--release"])
    # FIXME: error handling here

    os.chdir(root)

    build_path = extension_path / Path("target") / "release"

    library_file = "libmontecarlo3pi.so"
    library_path = build_path / library_file

    submodule_file = "montecarlo3pi.so"  # FIXME: OS-dependent
    submodule_path = module_path / submodule_file

    subprocess.run(["cp", str(library_path), str(submodule_path)])


if __name__ == "__main__":
    build({})
