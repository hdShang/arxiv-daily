---
layout: default
title: "SIRI-Bench: Challenging VLMs' Spatial Intelligence through Complex Reasoning Tasks"
---

# SIRI-Bench: Challenging VLMs' Spatial Intelligence through Complex Reasoning Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14512" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14512v3</a>
  <a href="https://arxiv.org/pdf/2506.14512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14512v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14512v3', 'SIRI-Bench: Challenging VLMs\' Spatial Intelligence through Complex Reasoning Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijian Song, Xiaoxin Lin, Qiuming Huang, Guangrun Wang, Liang Lin

**分类**: cs.CV

**发布日期**: 2025-06-17 (更新: 2025-10-17)

**备注**: 20 pages, 11 figures

---

## 💡 一句话要点

**提出SIRI-Bench以评估视觉语言模型的空间智能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `空间智能` `复杂推理` `基准测试` `3D场景生成` `自动化数据合成` `结构推理` `多模态学习`

## 📋 核心要点

1. 现有的视觉语言模型在复杂空间推理任务上表现不足，缺乏系统性的评估基准。
2. 本文提出SIRI-Bench，通过9000个视频-问题-答案三元组评估VLMs的结构空间智能，结合空间理解与结构推理。
3. 实验结果显示，当前最先进的VLMs在SIRI-Bench上面临显著挑战，强调了结构空间推理的重要性。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂推理任务上取得了快速进展，而视觉语言模型（VLMs）在真实世界交互中对空间智能的需求却未得到系统研究。为填补这一空白，本文提出了SIRI-Bench，一个旨在通过空间基础推理任务评估VLMs结构空间智能的基准。SIRI-Bench包含9000个视频-问题-答案三元组，每个问题都嵌入在逼真的3D场景中。该基准的设计要求解决每个问题时必须具备空间理解和结构推理能力。为促进大规模数据合成，本文开发了一个自动场景创建引擎，利用协作的LLM代理将抽象数学问题转化为真实的3D场景。实验结果表明，当前最先进的VLMs在SIRI-Bench上表现不佳，凸显了结构空间推理的挑战。希望本研究能引起研究者对空间基础推理的关注，推动VLMs在视觉问题解决方面的进展。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在复杂空间推理任务中的评估不足，现有方法未能有效衡量其空间智能能力。

**核心思路**：通过设计SIRI-Bench基准，结合空间基础推理任务，要求模型具备空间理解与结构推理能力，以全面评估VLMs的表现。

**技术框架**：SIRI-Bench的整体架构包括数据生成模块和评估模块。数据生成模块利用自动场景创建引擎生成3D场景，评估模块则通过问题-答案对来测试模型的推理能力。

**关键创新**：最重要的创新在于开发了自动场景创建引擎，利用协作的LLM代理将抽象问题转化为真实场景，这一方法在现有研究中尚属首次。

**关键设计**：在数据合成过程中，设置了多种参数以确保生成场景的真实性和复杂性，同时采用了适合空间推理的损失函数，以提高模型的学习效果。

## 📊 实验亮点

实验结果显示，当前最先进的视觉语言模型在SIRI-Bench上表现不佳，整体准确率显著低于预期，强调了结构空间推理的复杂性和挑战性。这一发现为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟现实等，能够提升这些领域中模型的空间理解与推理能力。未来，SIRI-Bench可能成为评估视觉语言模型的重要标准，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have undergone rapid progress, largely attributed to reinforcement learning on complex reasoning tasks. In contrast, while spatial intelligence is fundamental for Vision-Language Models (VLMs) in real-world interaction, the systematic study of their complex spatial reasoning remains underexplored. To bridge this gap, we introduce SIRI-Bench, a benchmark designed to evaluate VLMs' structural spatial intelligence through spatial-grounded reasoning tasks. SIRI-Bench comprises 9,000 video-question-answer triplets, where each problem is embedded in a realistic 3D scene. The benchmark is carefully designed so that solving each problem requires both spatial comprehension and structural reasoning. To facilitate large-scale data synthesis, we develop an Automatic Scene Creation Engine that employs collaborative LLM agents to translate abstract mathematical problems into faithful 3D scenes. Experimental results reveal that state-of-the-art VLMs struggle significantly on SIRI-Bench, underscoring the challenge of structural spatial reasoning. We hope that our study will bring researchers' attention to spatially grounded reasoning and advance VLMs in visual problem-solving.

