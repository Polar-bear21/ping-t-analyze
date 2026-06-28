# Ping-t Result Analyzer

## 概要

Ping-tの模擬試験結果HTMLを解析し、
JSONとして保存・蓄積し、
分野別の正答率を分析するCLIアプリです。

## 必要環境

Docker
Docker Compose

## ディレクトリ構成

app/
data/
 ├── raw_html
 ├── json
 └── csv

## ビルド

docker compose build

## HTMLを解析

docker compose run --rm app python app/main.py parse data/raw_html/result.html

## 分析

docker compose run --rm app python app/main.py analyze

## 出力

・JSON保存
・分野別正答率表示

## 使用ライブラリ

BeautifulSoup4
lxml