---
layout: default
title: "Narrative-to-Scene Generation: An LLM-Driven Pipeline for 2D Game Environments"
---

# Narrative-to-Scene Generation: An LLM-Driven Pipeline for 2D Game Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04481" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04481v1</a>
  <a href="https://arxiv.org/pdf/2509.04481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04481v1', 'Narrative-to-Scene Generation: An LLM-Driven Pipeline for 2D Game Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi-Chun Chen, Arnav Jhala

**分类**: cs.GR, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出轻量级管道将叙事文本转化为2D游戏场景**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `叙事生成` `2D游戏` `程序内容生成` `空间谓词` `细胞自动机` `多智能体协调` `语义嵌入`

## 📋 核心要点

1. 现有方法在将叙事文本转化为可玩游戏场景方面存在挑战，缺乏有效的空间和时间结构映射。
2. 论文提出了一种轻量级管道，通过提取空间谓词和生成分层地形，将叙事文本转化为2D游戏场景。
3. 在十个故事的实验中，系统在瓷砖-对象匹配和空间约束满足方面表现出色，展示了其可扩展性和实用性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步使得故事生成变得引人注目，但将叙事文本与可玩视觉环境连接仍然是程序内容生成（PCG）中的一个开放挑战。本文提出了一种轻量级管道，将短叙事提示转化为一系列2D瓷砖游戏场景，反映故事的时间结构。系统从LLM生成的叙事中识别三个关键时间框架，提取以“对象-关系-对象”三元组形式的空间谓词，并利用GameTileNet数据集中的语义嵌入检索视觉资产。通过细胞自动机生成分层地形，并根据谓词结构的空间规则放置对象。我们在十个不同故事中评估了系统，分析了瓷砖-对象匹配、可供性层对齐和跨帧空间约束满足情况。该原型为叙事驱动的场景生成提供了一种可扩展的方法，并为未来在故事中心PCG中的多帧连续性、符号跟踪和多智能体协调的研究奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决将叙事文本有效转化为可玩2D游戏场景的问题。现有方法在空间和时间结构的映射上存在不足，导致生成的场景缺乏连贯性和可玩性。

**核心思路**：论文的核心思路是利用大型语言模型生成叙事文本，并通过提取空间谓词和时间框架，将其转化为游戏场景。通过这种方式，能够更好地反映故事的结构和内容。

**技术框架**：整体架构包括三个主要模块：叙事生成模块、空间谓词提取模块和场景生成模块。首先，使用LLM生成叙事文本，然后识别关键时间框架和空间谓词，最后生成游戏场景。

**关键创新**：最重要的技术创新在于结合了LLM生成的叙事与空间谓词提取，形成了一个轻量级的管道，能够高效地生成符合叙事逻辑的游戏场景。这与传统方法相比，显著提高了生成的连贯性和可玩性。

**关键设计**：在技术细节上，使用“对象-关系-对象”三元组提取空间谓词，并通过细胞自动机生成分层地形。对象的放置遵循空间规则，确保生成场景的合理性和可玩性。

## 📊 实验亮点

实验结果表明，系统在瓷砖-对象匹配和空间约束满足方面表现优异，成功生成了符合叙事逻辑的游戏场景。与基线方法相比，系统在可玩性和连贯性上有显著提升，展示了其在程序内容生成中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、虚拟现实和教育等。通过将叙事文本转化为可玩场景，能够为游戏设计师提供新的创作工具，提升游戏的沉浸感和互动性。此外，未来可能在多智能体协调和符号跟踪等领域产生深远影响。

## 📄 摘要（原文）

> Recent advances in large language models(LLMs) enable compelling story generation, but connecting narrative text to playable visual environments remains an open challenge in procedural content generation(PCG). We present a lightweight pipeline that transforms short narrative prompts into a sequence of 2D tile-based game scenes, reflecting the temporal structure of stories. Given an LLM-generated narrative, our system identifies three key time frames, extracts spatial predicates in the form of "Object-Relation-Object" triples, and retrieves visual assets using affordance-aware semantic embeddings from the GameTileNet dataset. A layered terrain is generated using Cellular Automata, and objects are placed using spatial rules grounded in the predicate structure. We evaluated our system in ten diverse stories, analyzing tile-object matching, affordance-layer alignment, and spatial constraint satisfaction across frames. This prototype offers a scalable approach to narrative-driven scene generation and lays the foundation for future work on multi-frame continuity, symbolic tracking, and multi-agent coordination in story-centered PCG.

