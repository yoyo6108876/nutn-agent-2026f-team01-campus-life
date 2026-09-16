# Git 操作與提交

## 本機狀態與作者

此資料夾作為獨立 Git 儲存庫，分支為 `main`。初始骨架若由 Codex 建立 commit，作者會明確標記為 Codex；這不代表學生已完成個人的 Git 實作。每位組員仍應用自己的帳號完成一次修改與提交。

先將以下示意值改為自己的真實資訊；設定僅作用於本儲存庫：

```sh
git config user.name "你的姓名"
git config user.email "你的 GitHub 提交電子郵件"
```

修改 README 的組員資料與本週分工後：

```sh
git status
git diff
git add README.md
git diff --cached
git commit -m "docs: add team members and week 2 driver"
```

## GitHub Team Repo

團隊已提供現有儲存庫：https://github.com/yoyo6108876/nutn 。首次檢查時為空的公開儲存庫；本機 origin 使用此網址。以下建立步驟供課程核對，無須重複建立。名稱 `nutn` 尚不符合講義格式，取得組別後再由團隊決定改名。

### 此次執行結果

- 已建立本機 `main`、環境報告、候選問題與初始 commit。
- 已執行測試：5 項通過。
- 已設定 `origin` 為 `https://github.com/yoyo6108876/nutn.git`。
- 推送未完成：本機 Git 未取得 GitHub 登入憑證（`could not read Username`）；檢查用的 Codex 內建瀏覽器也尚未登入。
- 尚未邀請教師或提交課程 URL。

完成 Git 的 GitHub 驗證後，可在本專案資料夾執行以下指令續傳現有 commit：

```sh
git push -u origin main
```

1. 使用團隊決定的擁有者帳號建立 Repository。
2. 名稱使用 `nutn-agent-2026f-teamNN-campus-life`，將 NN 改成兩位組別。若團隊決定其他主題，可修改最後一段；所有字元使用小寫 ASCII 與連字號。
3. 選擇團隊需要的可見性；不要預先產生 README，避免與本機初始歷史衝突。
4. 將以下 OWNER 與 REPO 改為剛建立的帳號及完整名稱，再執行：

```sh
git remote add origin https://github.com/OWNER/REPO.git
git push -u origin main
```

若已有 `origin`，先用 `git remote -v` 確認網址，不要直接覆蓋或強制推送。若遠端已有檔案，先協調或整合歷史。

## clone 練習

遠端建立並成功 push 後，其他組員使用新資料夾練習講義流程：

```sh
git clone https://github.com/OWNER/REPO.git
cd REPO
```

修改 README 後依序執行 `git status`、`git diff`、`git add README.md`、`git commit` 與 `git push`。本機初始化不等於已完成 clone 或 push。

## 教師權限與繳交

講義指定：Settings → Collaborators → Add people，邀請 `wcchiang0627@gmail.com`（江維鈞）。這是待由團隊執行的課程要求；本專案未自動寄出邀請。

- [ ] README 已填姓名、學號、題目與分工。
- [ ] 已指定 Week 2 Driver，並討論三個候選問題。
- [ ] `environment_check.md` 真實記錄版本、工具與登入驗證。
- [ ] GitHub 上的 `main` 可看到 README、環境紀錄與問題探索文件。
- [ ] 教師已獲得存取權限，並確認可以開啟。
- [ ] 將實際 URL 填回 README，再提交 `https://github.com/OWNER/REPO`。

目前已提供兩位組員與 GitHub 擁有者；組別、符合課程格式的名稱、Week 2 Driver 確認、教師邀請與 URL 提交仍待完成。
