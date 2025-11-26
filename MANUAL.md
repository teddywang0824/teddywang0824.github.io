# 個人部落格使用手冊 (Pelican)

這份手冊將引導您如何管理、設定與發布您的個人部落格。

## 1. 環境準備

確保您已經安裝了 Python 以及必要的套件。若尚未安裝，請執行：

```bash
pip install pelican markdown ghp-import
```

## 2. 專案結構

- `content/`: 存放您的文章 (Markdown 檔案)。
- `pelicanconf.py`: **主要設定檔** (網站名稱、作者、Slogan 等)。
- `publishconf.py`: 發布時使用的設定檔。
- `output/`: 生成的靜態網頁檔案 (請勿直接修改此處，因為每次生成都會被覆蓋)。
- `themes/Wenqing/`: 部落格的主題檔案。

## 3. 新增文章

在 `content/` 資料夾中建立新的 `.md` 檔案。檔案開頭**必須**包含以下 Metadata：

```markdown
Title: 文章標題
Date: 2025-11-25 10:20
Category: Inspiration
Tags: 標籤1, 標籤2
Slug: unique-article-url
Authors: 您的名字
Summary: 這是一段簡短的文章摘要，會顯示在首頁卡片上。

# 這裡是文章標題 (H1)

這裡是文章內容...
```

> [!TIP]
> **關於分類 (Category)**
> 建議使用以下兩個分類，系統會自動套用對應的顏色主題：
> - `Inspiration`: 對應「靈感與心得」 (暖色系)。
> - `Programming`: 對應「程式相關」 (冷色系)。

## 4. 個人資訊設定 (pelicanconf.py)

您可以開啟 `pelicanconf.py` 檔案來修改部落格的基本資訊。修改後請重新啟動伺服器以查看效果。

### 基本資料
```python
AUTHOR = '您的名字'
SITENAME = '部落格名稱'
SITETITLE = '顯示在側邊欄或標題的名稱'
MOTTO = '顯示在頁尾的座右銘'
```

### 首頁 Slogan (二維結構)
Slogan 支援分組動畫顯示。外層列表代表「行」(依序顯示)，內層列表代表「段落」(同一行內並排顯示)。

```python
SLOGAN = [
    ['在此刻，'],                       # 第一組動畫
    ['世界安靜得', '只剩下呼吸。'],       # 第二組動畫 (兩個詞並排)
    ['尋找著', '存在的意義']             # 第三組動畫
]
```

### 社群連結
```python
SOCIAL = (('GitHub', 'https://github.com/yourname'),
          ('Twitter', 'https://twitter.com/yourname'),)
```

### 關於我頁面照片設定
若要在「關於我」頁面顯示您的照片：
1. 將您的照片 (例如 `profile.jpg`) 放入 `content/images/` 資料夾中 (若無此資料夾請自行建立)。
2. 開啟 `content/pages/about.md`。
3. 找到以下程式碼並修改檔名：
   ```html
   <img src="{static}/images/profile.jpg" alt="您的名字" class="about-photo">
   ```

## 5. 預覽部落格

在終端機 (Terminal) 執行以下指令來啟動開發伺服器：

```bash
pelican -r -l
```

- `-r` (autoreload): 當您修改並儲存檔案時，自動重新產生網頁。
- `-l` (listen): 在本機啟動網頁伺服器。

啟動後，打開瀏覽器前往 [http://localhost:8000](http://localhost:8000) 即可預覽。

## 6. 發布到 GitHub Pages

本專案已設定好使用 `ghp-import` 工具將生成的網頁發布到 GitHub 的 `gh-pages` 分支。

### 步驟 1: 建立 GitHub Repository
1. 在 GitHub 上建立一個新的 Repository (例如 `my-blog`)。
2. 將本機專案連結到 GitHub：
   ```bash
   git init
   git remote add origin https://github.com/您的帳號/my-blog.git
   ```

### 步驟 2: 設定 GitHub Actions 自動部署

若希望每次 Push 程式碼時自動更新部落格，請依照以下步驟設定：

1. 在專案根目錄建立資料夾 `.github/workflows/`。
2. 在該資料夾內建立檔案 `deploy.yml`，內容如下：

   ```yaml
   name: Deploy to GitHub Pages

   on:
     push:
       branches:
         - main  # 請確認您的主分支名稱是 main 還是 master

   jobs:
     deploy:
       runs-on: ubuntu-latest
       permissions:
         contents: write
       concurrency:
         group: ${{ github.workflow }}-${{ github.ref }}
       steps:
         - uses: actions/checkout@v4

         - name: Setup Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: pip install pelican markdown ghp-import

         - name: Build
           run: pelican content -s publishconf.py

         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./output
   ```

3. 將所有檔案 Push 到 GitHub：
   ```bash
   git add .
   git commit -m "Add GitHub Actions workflow"
   git push -u origin main
   ```

4. 前往 GitHub Repository 的 **Settings** > **Pages**，確認 Source 選擇 `gh-pages` 分支 (Action 執行成功後會自動建立此分支)。

完成後，每次您 Push 新文章到 `main` 分支，GitHub Actions 就會自動幫您重新生成並發布網頁。

## 7. 常見問題

### Q: 文章沒有出現？
- 檢查 `Date` 是否設為未來的時間 (預設不會顯示未來文章)。
- 檢查 `Slug` 是否與其他文章重複。
- 確保檔案已儲存在 `content/` 資料夾內。

### Q: 修改了設定檔沒生效？
- 修改 `pelicanconf.py` 後，必須重啟 `pelican -r -l` (按 `Ctrl+C` 停止，再重新輸入指令)。
