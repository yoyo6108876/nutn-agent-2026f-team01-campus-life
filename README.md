# NUTN Agent Project

## 團隊

| 欄位 | 內容 |
| --- | --- |
| 組別 | 待填（兩位數） |
| 暫定題目 | 南大校園生活 Agent：問題探索 |
| GitHub 擁有者 | `yoyo6108876` |
| 目前 Repository 名稱 | `nutn` |
| 課程要求命名 | `nutn-agent-2026f-teamNN-campus-life`（NN 待提供；現有名稱尚不符合講義格式） |
| Repository URL | https://github.com/yoyo6108876/nutn |
| Week 2 Driver | 建議由陳冠友擔任，待團隊確認 |

| 姓名 | 學號 | 初步分工 |
| --- | --- | --- |
| 陳冠友 | S11259039 | 隊長；建議負責環境、程式與 Git 操作 |
| 林崇偉 | S11259031 | 隊員；建議負責需求、資料來源、測試與文件審查 |

姓名、學號與隊長／隊員身分由團隊提供；具體工作分配為草案，待兩位確認。

投影片流程頁寫 3–4 人，專題說明及本週清單寫 2–3 人；本草稿依後兩者安排，實際人數以授課教師確認為準。

## 本週成果

- [環境驗證紀錄](environment_check.md)：實際偵測結果及待人工確認項目。
- [三個候選問題](docs/candidate_problems.md)：對象、痛點、資料工具及 Agent Necessity Test。
- [Git 操作與繳交步驟](docs/submission.md)：本機 commit、GitHub 建立、推送與教師權限確認。
- `scripts/check_environment.py`：可重複執行的環境檢查工具。
- `tests/test_environment.py`：檢查工具的失敗處理與報告格式測試。

## 執行環境驗證

使用 Python 3.10 以上（這是本骨架的需求；講義未指定版本）。目前電腦是 macOS；講義的示範環境為 Windows，以下也提供 PowerShell 操作。

macOS / Linux：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/check_environment.py
.venv/bin/python -m pytest
```

Windows PowerShell：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts/check_environment.py
.\.venv\Scripts\python.exe -m pytest
```

檢查指令預設更新根目錄的 `environment_check.md`；也可使用 `--output 路徑` 保存各組員的紀錄。指令成功只代表報告已產生；請閱讀表格中的缺少工具與待確認項目。

VS Code 的 Codex 擴充套件登入、GitHub 存取與教師權限須人工確認，程式不讀取憑證。Cursor 或 Codex 桌面版的存在不代表已完成 VS Code + Codex IDE 要求。

## 完成交付前

- [ ] 填妥組別、組員姓名、學號與分工，指定 Week 2 Driver。
- [ ] 每位組員完成環境驗證及 Codex 擴充套件登入。
- [ ] 團隊討論並修改候選問題草稿。
- [ ] 建立符合命名規則的 GitHub Team Repo，將本機 main 推送上去。
- [ ] 依講義邀請教師並確認存取權限，再提交 Repository URL。

候選問題是提案草稿，尚未進行學生訪談或驗證校方資料來源；不要將假設當作調查結果。
