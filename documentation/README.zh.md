<div align="center">

![indicode 横幅](banner.png)

**为 _乐高夺宝奇兵：最初冒险_ 自动输入秘籍代码**

[English](../README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · **中文**

</div>

## indicode 是什么？

在 _乐高夺宝奇兵：最初冒险_ 中，秘籍代码需要在巴尼特学院教室的一个 6 字符转盘上输入，
每个字符逐个向上或向下滚动。手动操作既慢又容易出错。

**indicode** 替你完成。你选好想要的代码，它会计算每个字符之间的最短路径，然后模拟按键，
自动逐个输入——一个代码接一个代码。

## 演示

<a href="https://youtu.be/N4DFVwdnXN0">
    <img src="demo.gif"/>
</a>
![视频演示](https://youtu.be/N4DFVwdnXN0)

## 功能

- **一次性输入** — 选择多个代码，让它依次全部输入。
- **最短路径导航** — 为每个字符选择向上或向下，尽量减少移动。
- **自定义按键** — 自由设置 上 / 右 / 下 / 左 / 确认 的按键。
- **启动延迟与倒计时** — 给你时间切回游戏。
- **9 种语言** — 英语、法语、德语、西班牙语、意大利语、日语、韩语、俄语、中文（自动检测）。

## 环境要求

- Python 3.10+
- [`pynput`](https://pypi.org/project/pynput/) 和 [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python main.py
```

1. 选择想要的代码（`a` 全选，`v` 确认）。
2. 配置你的按键（上、右、下、左、确认）。
3. 设置启动延迟，然后切回游戏，使面板显示 `(A) A A A A A`。
4. 坐等 indicode 全部输入完成。

> 通过环境变量 `INDICODE_LANG` 强制指定语言（例如 `INDICODE_LANG=zh`）。

![end banner](./end_banner.png)
