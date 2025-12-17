---
layout: default
title: MuseCPBench: an Empirical Study of Music Editing Methods through Music Context Preservation
---

# MuseCPBench: an Empirical Study of Music Editing Methods through Music Context Preservation

**arXiv**: [2512.14629v1](https://arxiv.org/abs/2512.14629) | [PDF](https://arxiv.org/pdf/2512.14629.pdf)

**作者**: Yash Vishe, Eric Xue, Xunyi Jiang, Zachary Novack, Junda Wu, Julian McAuley, Xin Xu

**分类**: cs.SD, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出MuseCPBench基准以解决音乐编辑中音乐上下文保存评估不一致的问题。**

**关键词**: `音乐编辑` `音乐上下文保存` `评估基准` `音乐生成模型` `多任务比较` `音乐制作` `标准化评估`

## 📋 核心要点

1. 现有音乐编辑方法在评估音乐上下文保存（MCP）时缺乏统一标准，导致比较不可靠。
2. 论文提出首个MCP评估基准MuseCPBench，涵盖四类音乐方面，支持对五种基线方法的全面比较。
3. 通过系统分析，识别出当前方法的保存差距，为改进编辑策略提供实用指导。

## 📝 摘要（中文）

音乐编辑在现代音乐制作中扮演着关键角色，应用于电影、广播和游戏开发等领域。近年来，音乐生成模型的进步使得音色转换、乐器替换和风格变换等多样化编辑任务成为可能。然而，许多现有工作忽视了评估编辑过程中应保持不变的音乐方面——我们将其定义为音乐上下文保存（MCP）。尽管一些研究考虑了MCP，但它们采用了不一致的评估协议和指标，导致不可靠和不公平的比较。为填补这一空白，我们引入了首个MCP评估基准MuseCPBench，涵盖四类音乐方面，并支持对五种代表性音乐编辑基线方法进行全面比较。通过对音乐方面、方法和模型的系统分析，我们识别出当前音乐编辑方法中一致的保存差距，并提供深入解释。我们希望这些发现能为开发具有强大MCP能力的更有效和可靠音乐编辑策略提供实用指导。

## 🔬 方法详解

论文的核心方法是构建MuseCPBench基准，整体框架包括定义音乐上下文保存（MCP）概念、设计四类音乐方面（如旋律、节奏、和声和音色）的评估指标，并集成五种代表性音乐编辑基线方法（如基于生成模型的编辑技术）。关键技术创新点在于首次系统化MCP评估，通过标准化协议确保公平比较。与现有方法的主要区别在于，现有工作多关注编辑效果本身，而MuseCPBench强调保存不变属性的评估，填补了评估空白。

## 📊 实验亮点

实验结果显示，MuseCPBench基准能有效识别当前音乐编辑方法在保存音乐上下文方面的差距，例如在特定音乐方面（如和声）的保存性能普遍较低，为未来方法优化提供了明确方向。

## 🎯 应用场景

该研究可应用于音乐制作、电影配乐、游戏音频和广播编辑等领域，帮助开发者评估和改进音乐编辑模型的上下文保存能力，提升编辑质量和可靠性。

## 📄 摘要（原文）

> Music editing plays a vital role in modern music production, with applications in film, broadcasting, and game development. Recent advances in music generation models have enabled diverse editing tasks such as timbre transfer, instrument substitution, and genre transformation. However, many existing works overlook the evaluation of their ability to preserve musical facets that should remain unchanged during editing a property we define as Music Context Preservation (MCP). While some studies do consider MCP, they adopt inconsistent evaluation protocols and metrics, leading to unreliable and unfair comparisons. To address this gap, we introduce the first MCP evaluation benchmark, MuseCPBench, which covers four categories of musical facets and enables comprehensive comparisons across five representative music editing baselines. Through systematic analysis along musical facets, methods, and models, we identify consistent preservation gaps in current music editing methods and provide insightful explanations. We hope our findings offer practical guidance for developing more effective and reliable music editing strategies with strong MCP capability

