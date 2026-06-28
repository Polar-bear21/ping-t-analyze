# Ping-t Result Analyzer

Ping-tの模擬試験結果HTMLを解析し、JSONとして保存・集計するCLIツールです。

## 機能

- 模擬試験結果HTMLの解析
- JSONへの保存
- 分野別正答率の集計
- 複数回受験結果の集計

## ディレクトリ構成

```text
.
├── app/
├── data/
│   ├── raw_html/
│   ├── json/
│   └── csv/
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md
```

## Dockerで実行する

### ビルド

```bash
docker compose build
```

### HTMLを解析

解析したいHTMLを配置します。

```text
data/raw_html/result.html
```

実行します。

```bash
docker compose run --rm app python app/main.py parse data/raw_html/result.html
```

JSONが `data/json` に保存されます。

### 分析

```bash
docker compose run --rm app python app/main.py analyze
```

---

## Pythonのみで実行する

### リポジトリを取得

```bash
git clone <repository-url>
cd <repository-name>
```

### 仮想環境を作成

Windows

```powershell
python -m venv .venv
```

Linux

```bash
python3 -m venv .venv
```

### 仮想環境を有効化

Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

Linux

```bash
source .venv/bin/activate
```

### ライブラリをインストール

```bash
pip install -r requirements.txt
```

### HTMLを解析

解析したいHTMLを配置します。

```text
data/raw_html/result.html
```

実行します。

```bash
python app/main.py parse data/raw_html/result.html
```

Linuxでは

```bash
python3 app/main.py parse data/raw_html/result.html
```

でも実行できます。

### 分析

```bash
python app/main.py analyze
```

Linuxでは

```bash
python3 app/main.py analyze
```

でも実行できます。

---

## 出力

### JSON

解析結果は以下へ保存されます。

```text
data/json/
```

### コンソール出力

```text
分野別成績
======================================================================
仮想マシン・コンテナの概念と利用                     0/2 (0.0%)
ブートプロセスとsystemd                            1/4 (25.0%)
...
```

## 使用ライブラリ

- BeautifulSoup4
- lxml
- wcwidth

## 今後追加予定

- CSV出力
- 問題別分析
- グラフ表示
- Web UI