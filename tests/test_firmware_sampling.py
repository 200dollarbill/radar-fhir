"""Build and run the host test of the firmware's sample clock."""
import pathlib
import subprocess


def test_sampling_logic(tmp_path):
    exe = tmp_path / "sampling_test"
    src = pathlib.Path("tests/firmware/sampling_test.cpp")
    build = subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", "-Werror",
                            str(src), "-o", str(exe)],
                           capture_output=True, text=True)
    assert build.returncode == 0, build.stderr
    run = subprocess.run([str(exe)], capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    assert "sampling ok" in run.stdout
