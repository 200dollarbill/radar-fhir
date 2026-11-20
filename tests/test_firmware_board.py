"""Build and run the host test of the firmware's board identity helpers."""
import json
import pathlib
import subprocess


def test_board_helpers(tmp_path):
    exe = tmp_path / "board_test"
    src = pathlib.Path("tests/firmware/board_test.cpp")
    build = subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", "-Werror",
                            str(src), "-o", str(exe)],
                           capture_output=True, text=True)
    assert build.returncode == 0, build.stderr
    run = subprocess.run([str(exe)], capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    lines = run.stdout.splitlines()
    assert lines[-1] == "board ok"
    board = [ln for ln in lines if ln.startswith("BOARD ")]
    assert len(board) == 1
    body = json.loads(board[0][len("BOARD "):])
    assert body == {"id": "AB12CD34EF56",
                    "key": "0123456789abcdef" * 4, "fw": "radar_json"}
