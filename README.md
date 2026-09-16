# NUTN Agent Project

## 專案題目

**以教師範例為參考的作業規格與完成度檢查助手**

學生提供老師的作業說明、教師範例檔與自己的作業，系統逐項對照要求，引用文件證據，指出已完成、部分完成、缺漏與無法判定的內容。

LLM 的核心工作是理解不同寫法之間的語意關係，辨識「有提到」與「有充分回應」的差異；明確的作業要求是判定依據，教師範例中的額外內容僅供參考。

目前階段為題目與需求定義，尚未實作 LLM/API 或完成實際文件評測。完整內容見 [專案題目與範圍定義](docs/week2-proposal.md)。

## 團隊

| 欄位 | 內容 |
| --- | --- |
| 組別 | 01（依目前儲存庫名稱） |
| 題目 | 以教師範例為參考的作業規格與完成度檢查助手 |
| GitHub 擁有者 | `yoyo6108876` |
| 目前 Repository 名稱 | `nutn-agent-2026f-team01-campus-life` |
| 課程要求命名 | 目前名稱符合小寫 ASCII、兩位組別與連字號格式 |
| Repository URL | https://github.com/yoyo6108876/nutn-agent-2026f-team01-campus-life |
| Week 2 Driver | 建議由陳冠友擔任，待團隊確認 |

| 姓名 | 學號 | 初步分工 |
| --- | --- | --- |
| 陳冠友 | S11259039 | 隊長；建議負責環境、程式與 Git 操作 |
| 林崇偉 | S11259031 | 隊員；建議負責需求、資料來源、測試與文件審查 |

姓名、學號與隊長／隊員身分由團隊提供；具體工作分配為草案，待兩位確認。

投影片流程頁寫 3–4 人，專題說明及本週清單寫 2–3 人；本草稿依後兩者安排，實際人數以授課教師確認為準。

## 專案文件與既有工具

- [專案題目與範圍定義](docs/week2-proposal.md)：問題、使用者、LLM 必要性、輸入輸出、驗收條件與後續基準驗證規劃。
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

專案已從原本的課綱與作業要求理解方向，收斂為教師範例與學生作業的對照檢查。尚未進行學生訪談或實際 LLM 評測；需求假設與預期效果不代表已驗證的結果。
