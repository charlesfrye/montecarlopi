import os
import subprocess
from pathlib import Path

lib_base_name = "libmontecarlo3pi"
mod_base_name = lib_base_name[3:]  # drop lib prefix
extensions = [".so", ".dylib", ".dll"]


def build(setup_kwargs):

    root = Path(os.getcwd())

    extension_path = root / "src" / "rust" / "pyo3_monte_carlo_pi"
    module_path = root / "src" / "python" / "montecarlopi"

    os.chdir(extension_path)

    subprocess.run(["cargo", "build", "--release"], check=True)

    os.chdir(root)

    build_path = extension_path / Path("target") / "release"

    library_file = get_library_file(build_path)
    library_path = build_path / library_file

    submodule_file = get_submodule_file(library_file)
    submodule_path = module_path / submodule_file

    subprocess.run(["cp",  # FIXME: not windows compatible
                    str(library_path), str(submodule_path)])


def get_library_file(build_path):
    contents = os.listdir(build_path)
    for extension in extensions:
        possible_library_file = lib_base_name + extension
        if possible_library_file in contents:
            return possible_library_file
    err_msg = (f"could not find {lib_base_name} in {build_path} "
               f"with extension from {extensions}.")
    raise FileNotFoundError(err_msg)


def get_submodule_file(library_file):
    if library_file.endswith(".dll"):
        return mod_base_name + ".pyd"
    else:
        return mod_base_name + ".so"


if __name__ == "__main__":
    build({})
