简体中文 | [English](README.en.md)

# 生草翻译机

## 介绍

翻译界有“生肉”和“熟肉”一说，其中“生肉”指未翻译的东西，“熟肉”指已翻译的东西。但是，有些东西经过机器多次翻译，就会完全脱离原来的意思，我们称之为“生草”。生草翻译机借助 Google 翻译，可以帮助你把生肉变成生草。

## 安装教程

本程序无需安装，即下即用。

如果您想通过 Python 运行源代码，您需要安装 [Python 的 Google 翻译模块](https://github.com/ssut/py-googletrans)。

可以用一条命令安装它：

```bash
python -m pip install googletrans
```

或者，如果您想用 Python 3，可以用以下命令：

```bash
python3 -m pip install googletrans
```

## 使用说明

### Windows

您无需安装 Python，双击 `rawgrass.exe` 然后按照提示操作即可。

您也可以通过 Python 运行 `rawgrass.py`，但前提是您已经安装 [Python 的 Google 翻译模块](https://github.com/ssut/py-googletrans)。

### macOS/Linux

您需要运行源代码，所以需要安装 [Python 的 Google 翻译模块](https://github.com/ssut/py-googletrans)。参照[“安装教程”](#安装教程)一节。

`rawgrass-python.py` 的文件开头有 `#!/usr/bin/env python` 而且可执行，直接在终端中运行（输入 `./rawgrass-python.py`）即可。

`rawgrass-python3.py` 的文件开头有 `#!/usr/bin/env python3` 而且可执行，直接在终端中运行（输入 `./rawgrass-python3.py`）即可。

当然，直接用 Python 运行 `rawgrass.py` 也是可以的。


## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
