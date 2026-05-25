<div align="center">

![indicode 배너](banner.png)

**_레고 인디아나 존스: 오리지널 어드벤처_ 치트 코드 자동 입력**

[English](../README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · **한국어** · [Русский](README.ru.md) · [中文](README.zh.md)

</div>

## indicode란?

_레고 인디아나 존스: 오리지널 어드벤처_ 에서는 바넷 대학 교실의 6글자 휠에서 각 글자를
하나씩 위아래로 굴려 치트 코드를 입력합니다. 손으로 하면 느리고 실수하기 쉽습니다.

**indicode** 가 대신 해 줍니다. 원하는 코드를 고르면 각 글자 사이의 최단 경로를 계산한 뒤,
키 입력을 시뮬레이션하여 자동으로 — 하나씩 차례대로 입력합니다.

## 데모

<video src="demo.mp4"></video>

## 기능

- **한 번에 입력** — 여러 코드를 선택하면 모두 연달아 입력합니다.
- **최단 경로 탐색** — 각 글자마다 위/아래를 선택해 이동을 최소화합니다.
- **키 매핑 커스터마이즈** — 위 / 오른쪽 / 아래 / 왼쪽 / 확인 키를 직접 설정합니다.
- **시작 딜레이 & 카운트다운** — 게임으로 돌아갈 시간을 줍니다.
- **9개 언어 지원** — 영어, 프랑스어, 독일어, 스페인어, 이탈리아어, 일본어, 한국어, 러시아어, 중국어 (자동 감지).

## 요구 사항

- Python 3.10 이상
- [`pynput`](https://pypi.org/project/pynput/) 와 [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## 사용법

```bash
python main.py
```

1. 원하는 코드를 선택합니다 (`a` 전체 선택, `v` 확정).
2. 키를 설정합니다 (위, 오른쪽, 아래, 왼쪽, 확인).
3. 시작 딜레이를 정한 뒤, 보드가 `(A) A A A A A` 인 상태로 게임에 돌아갑니다.
4. indicode가 모두 입력하는 동안 기다리기만 하면 됩니다.

> 환경 변수 `INDICODE_LANG` 로 언어를 지정할 수 있습니다 (예: `INDICODE_LANG=ko`).

![end banner](./end_banner.png)
