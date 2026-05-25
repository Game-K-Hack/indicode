<div align="center">

![indicode バナー](banner.png)

**_レゴ インディ・ジョーンズ オリジナル・アドベンチャー_ のチートコードを自動入力**

[English](../README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Italiano](README.it.md) · **日本語** · [한국어](README.ko.md) · [Русский](README.ru.md) · [中文](README.zh.md)

</div>

## indicode とは？

_レゴ インディ・ジョーンズ オリジナル・アドベンチャー_ では、チートコードはバーネット大学
の教室にある 6 文字のホイールで、各文字を 1 つずつ上下にスクロールして入力します。
手作業では時間がかかり、ミスも起こりがちです。

**indicode** がそれを代わりに行います。入力したいコードを選ぶと、各文字間の最短経路を
計算し、キー入力をシミュレートして自動的に — 1 つずつ順番に入力します。

## デモ

<a href="https://youtu.be/N4DFVwdnXN0">
    <img src="demo.gif"/>
</a>

![デモ動画](https://youtu.be/N4DFVwdnXN0)

## 機能

- **一括入力** — 複数のコードを選択すれば、まとめて順番に入力します。
- **最短経路ナビゲーション** — 各文字で上か下かを選び、移動を最小化します。
- **キー割り当てのカスタマイズ** — 上 / 右 / 下 / 左 / 決定 のキーを自由に設定できます。
- **開始ディレイとカウントダウン** — ゲームに戻る時間を確保できます。
- **9 言語対応** — 英語・フランス語・ドイツ語・スペイン語・イタリア語・日本語・韓国語・ロシア語・中国語（自動検出）。

## 必要環境

- Python 3.10 以上
- [`pynput`](https://pypi.org/project/pynput/) と [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## 使い方

```bash
python main.py
```

1. 入力したいコードを選びます（`a` ですべて選択、`v` で確定）。
2. キーを設定します（上、右、下、左、決定）。
3. 開始ディレイを設定し、盤面が `(A) A A A A A` の状態でゲームに戻ります。
4. あとは indicode がすべて入力するのを待つだけです。

> 環境変数 `INDICODE_LANG` で言語を指定できます（例：`INDICODE_LANG=ja`）。

![end banner](./end_banner.png)
