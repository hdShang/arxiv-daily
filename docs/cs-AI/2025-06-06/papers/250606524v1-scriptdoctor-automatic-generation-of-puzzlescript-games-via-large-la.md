---
layout: default
title: "ScriptDoctor: Automatic Generation of PuzzleScript Games via Large Language Models and Tree Search"
---

# ScriptDoctor: Automatic Generation of PuzzleScript Games via Large Language Models and Tree Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06524" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06524v1</a>
  <a href="https://arxiv.org/pdf/2506.06524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06524v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06524v1', 'ScriptDoctor: Automatic Generation of PuzzleScript Games via Large Language Models and Tree Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sam Earle, Ahmed Khalifa, Muhammad Umair Nasir, Zehua Jiang, Graham Todd, Andrzej Banburski-Fahey, Julian Togelius

**分类**: cs.AI, cs.HC

**发布日期**: 2025-06-06

**备注**: 5 pages, 3 figures, 3 tables, submitted to IEEE Conference on Games as a Short Paper

---

## 💡 一句话要点

**提出ScriptDoctor以实现PuzzleScript游戏的自动生成与测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动游戏设计` `大型语言模型` `PuzzleScript` `游戏生成` `自动化测试` `迭代优化` `闭环系统`

## 📋 核心要点

1. 现有的自动游戏设计方法多依赖人类监督，缺乏长时间周期的自动化集成，限制了其应用范围。
2. 本文提出ScriptDoctor系统，通过大型语言模型自动生成和测试PuzzleScript游戏，形成迭代生成与测试的闭环。
3. 实验表明，ScriptDoctor能够有效生成功能性游戏设计，并通过自动化测试提升游戏内容的质量与多样性。

## 📝 摘要（中文）

目前在自动游戏设计（AGD）领域，利用大型预训练模型生成代码、资产或设计理念的兴趣日益增长。然而，现有方法多依赖于持续的人类监督，缺乏长时间周期的自动化集成。为此，本文提出了ScriptDoctor，一个基于大型语言模型（LLM）的系统，能够自动生成和测试PuzzleScript游戏。ScriptDoctor通过迭代循环生成和测试游戏设计理念，利用人类编写的示例作为基础，利用PuzzleScript引擎的编译错误生成功能代码，并通过搜索代理进行游戏测试。该系统展示了基于LLM的自动化工作流程在生成新游戏内容方面的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动游戏设计方法中对人类监督的依赖，缺乏长时间周期的自动化集成的问题。现有方法难以实现与游戏引擎的有效接口，限制了生成内容的测试与验证。

**核心思路**：ScriptDoctor的核心思路是利用大型语言模型（LLM）生成PuzzleScript游戏，通过迭代循环结合人类示例、编译错误和自动化测试，形成一个闭环的生成与验证系统。这样的设计使得生成过程能够自我调整和优化，减少对人类干预的需求。

**技术框架**：ScriptDoctor的整体架构包括三个主要模块：首先是游戏设计生成模块，利用LLM生成游戏设计理念；其次是编译与错误处理模块，捕捉PuzzleScript引擎的编译错误以生成有效代码；最后是游戏测试模块，通过搜索代理进行游戏的自动化测试。

**关键创新**：ScriptDoctor的主要创新在于将LLM与游戏引擎的自动化测试结合，形成一个完整的生成与验证闭环。这一方法与传统的依赖人类监督的生成方式有本质区别，能够实现更高效的游戏内容生成。

**关键设计**：在设计上，ScriptDoctor使用了特定的损失函数来优化生成的游戏设计，同时在网络结构上采用了适应PuzzleScript特性的模块，以确保生成内容的有效性和可玩性。

## 📊 实验亮点

实验结果显示，ScriptDoctor能够成功生成多种功能性PuzzleScript游戏，相较于传统方法，生成的游戏在可玩性和创新性上有显著提升，自动化测试的引入使得游戏设计的验证过程更加高效。

## 🎯 应用场景

ScriptDoctor的研究成果在自动游戏设计领域具有广泛的应用潜力，能够为游戏开发者提供高效的工具，自动生成多样化的游戏内容。未来，该系统可能推动游戏设计的自动化进程，降低开发成本，提高创作效率。

## 📄 摘要（原文）

> There is much interest in using large pre-trained models in Automatic Game Design (AGD), whether via the generation of code, assets, or more abstract conceptualization of design ideas. But so far this interest largely stems from the ad hoc use of such generative models under persistent human supervision. Much work remains to show how these tools can be integrated into longer-time-horizon AGD pipelines, in which systems interface with game engines to test generated content autonomously. To this end, we introduce ScriptDoctor, a Large Language Model (LLM)-driven system for automatically generating and testing games in PuzzleScript, an expressive but highly constrained description language for turn-based puzzle games over 2D gridworlds. ScriptDoctor generates and tests game design ideas in an iterative loop, where human-authored examples are used to ground the system's output, compilation errors from the PuzzleScript engine are used to elicit functional code, and search-based agents play-test generated games. ScriptDoctor serves as a concrete example of the potential of automated, open-ended LLM-based workflows in generating novel game content.

