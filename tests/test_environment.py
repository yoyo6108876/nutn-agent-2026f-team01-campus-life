import subprocess

from scripts import check_environment as check


def test_missing_command_does_not_crash(monkeypatch):
    def missing(*args, **kwargs):
        raise FileNotFoundError("tool missing")
    monkeypatch.setattr(check.subprocess, "run", missing)
    ok, output = check.run(["missing-tool"])
    assert not ok
    assert "FileNotFoundError" in output


def test_timeout_is_reported(monkeypatch):
    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired("tool", 15)
    monkeypatch.setattr(check.subprocess, "run", timeout)
    ok, output = check.run(["tool"])
    assert not ok
    assert "TimeoutExpired" in output


def test_failed_command_is_not_reported_as_success(monkeypatch):
    monkeypatch.setattr(check.subprocess, "run", lambda *args, **kwargs:
                        subprocess.CompletedProcess(args[0], 1, "", "missing module"))
    assert check.run(["python", "-m", "pytest"]) == (False, "missing module")


def test_report_preserves_table_and_marks_manual_checks():
    report = check.render_report([("Tool", "未通過", "first|second\n<error>")])
    assert "first&#124;second<br>&lt;error&gt;" in report
    assert "- [ ] Codex" in report
    assert "不代表所有組員均已通過" in report


def test_missing_vscode_leaves_extension_unverified(monkeypatch):
    monkeypatch.setattr(check, "find_code", lambda: None)
    monkeypatch.setattr(check, "run", lambda command: (True, "test version"))
    rows = {name: status for name, status, detail in check.collect_checks()}
    assert rows["VS Code"] == "未偵測"
    assert rows["Codex IDE Extension"] == "待確認"
    assert rows["Codex 登入"] == "待人工確認"
