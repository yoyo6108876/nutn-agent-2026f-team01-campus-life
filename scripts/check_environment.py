"""Generate an honest, credential-free Week 1 environment report."""

import argparse
from datetime import datetime
from pathlib import Path
import platform
import shutil
import subprocess
import sys


def run(command):
    """Return (success, output), including actionable failures without crashing."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired) as error:
        return False, f"{type(error).__name__}: {error}"
    output = (result.stdout or result.stderr).strip()
    return result.returncode == 0, output or f"exit code {result.returncode}"


def find_code():
    executable = shutil.which("code")
    if executable:
        return executable
    mac_path = Path("/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code")
    return str(mac_path) if mac_path.is_file() else None


def collect_checks():
    rows = [("Python", "通過" if sys.version_info >= (3, 10) else "版本不足",
             platform.python_version())]
    for label, command in [("Git", ["git", "--version"]),
                           ("pytest", [sys.executable, "-m", "pytest", "--version"])]:
        ok, output = run(command)
        rows.append((label, "通過" if ok else "未通過", output))
    code = find_code()
    if code:
        ok, output = run([code, "--version"])
        rows.append(("VS Code", "通過" if ok else "未通過", output))
        ok, output = run([code, "--list-extensions", "--show-versions"])
        extensions = [line for line in output.splitlines()
                      if line.lower().startswith("openai.chatgpt@")]
        rows.append(("Codex IDE Extension", "已偵測" if ok and extensions else "待確認",
                     ", ".join(extensions) if ok and extensions else
                     "未能從 VS Code CLI 確認；請在 Extensions 檢查 Codex。"))
    else:
        rows.extend([
            ("VS Code", "未偵測", "找不到 code CLI 或 macOS 標準安裝位置。"),
            ("Codex IDE Extension", "待確認", "需在 VS Code 內確認安裝與版本。"),
        ])
    rows.extend([
        ("Codex 登入", "待人工確認", "在 VS Code 的 Codex 面板確認登入並測試一次對話。"),
        ("GitHub 存取", "待人工確認", "確認正確帳號可讀寫團隊 Repository。"),
    ])
    return rows


def cell(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("|", "&#124;").replace("\r", "").replace("\n", "<br>")


def render_report(rows):
    lines = [
        "# Environment Check", "",
        f"- 檢查時間：{datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- 作業系統：{platform.system()} {platform.release()} ({platform.machine()})",
        "- 範圍：目前執行此工具的電腦與 Python 環境，不代表所有組員均已通過。",
        "- 本骨架使用 Python 3.10+；講義未指定 Python 版本。", "",
        "| 項目 | 結果 | 證據／下一步 |", "| --- | --- | --- |",
    ]
    lines += ["| " + " | ".join(cell(value) for value in row) + " |" for row in rows]
    lines += ["", "## 人工驗證", "",
              "- [ ] VS Code 可正常啟動。",
              "- [ ] Codex 擴充套件已登入，且成功回應測試對話。",
              "- [ ] Git commit 使用自己的姓名與電子郵件。",
              "- [ ] GitHub Team Repo 可讀寫，main 包含 README。",
              "- [ ] 教師已獲邀，並已確認能開啟儲存庫。", "",
              "重新執行會覆寫本報告並重設人工勾選，請完成最後一次檢查後再填寫。", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "environment_check.md")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_report(collect_checks()), encoding="utf-8")
    print(f"環境報告已產生：{args.output}")
    print("請閱讀報告；產生成功不代表所有環境要求都已通過。")


if __name__ == "__main__":
    main()
