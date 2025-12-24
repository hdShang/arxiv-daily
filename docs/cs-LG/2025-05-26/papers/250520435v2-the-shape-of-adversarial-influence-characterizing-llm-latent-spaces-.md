---
layout: default
title: The Shape of Adversarial Influence: Characterizing LLM Latent Spaces with Persistent Homology
---

# The Shape of Adversarial Influence: Characterizing LLM Latent Spaces with Persistent Homology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20435" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20435v2</a>
  <a href="https://arxiv.org/pdf/2505.20435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20435v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20435v2', 'The Shape of Adversarial Influence: Characterizing LLM Latent Spaces with Persistent Homology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aideen Fay, Inés García-Redondo, Qiquan Wang, Haim Dubossarsky, Anthea Monod

**分类**: cs.LG, cs.AI, cs.CG, math.AT

**发布日期**: 2025-05-26 (更新: 2025-10-09)

---

## 💡 一句话要点

**利用持久同调分析LLM的对抗影响特征**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗样本` `持久同调` `可解释性` `大型语言模型` `拓扑数据分析` `模型安全性` `激活分析`

## 📋 核心要点

1. 现有的可解释性方法未能充分捕捉LLM内部表示的复杂几何结构，导致对抗影响的理解不足。
2. 本研究提出持久同调作为分析工具，系统性地表征LLM激活中的多尺度动态，揭示对抗输入的拓扑特征。
3. 实验结果显示，对抗输入导致的拓扑压缩现象在不同模型和层次中具有统计稳健性，提供了新的可解释性视角。

## 📝 摘要（中文）

现有的大型语言模型（LLM）可解释性方法往往局限于线性方向或孤立特征，忽视了模型表示中的高维、非线性和关系几何。本研究聚焦于对抗输入如何系统性地影响LLM的内部表示空间，提出使用持久同调（PH）作为框架来表征LLM激活中的多尺度动态。通过对六种先进模型在两种对抗条件下的系统分析，识别出对抗影响的一致拓扑特征，揭示了对抗输入导致的“拓扑压缩”现象，提供了对对抗效应的可解释性见解。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有可解释性方法无法有效捕捉LLM内部高维、非线性结构的问题，尤其是在对抗输入影响下的表现变化。

**核心思路**：通过引入持久同调（PH），我们能够从拓扑数据分析的角度系统性地分析LLM的激活，识别出对抗输入对模型表示的影响。

**技术框架**：研究首先定义对抗条件，包括间接提示注入和后门微调，然后应用PH分析六种先进模型的激活，提取拓扑特征并进行比较。

**关键创新**：本研究的主要创新在于使用持久同调作为分析工具，揭示了对抗输入导致的拓扑压缩现象，这一特征在不同模型和层次中具有一致性和可解释性。

**关键设计**：在实验中，设置了多种对抗输入条件，采用了标准的PH算法来提取拓扑特征，并通过统计方法验证其稳健性和区分能力。具体参数设置和损失函数设计在论文中详细描述。

## 📊 实验亮点

实验结果表明，所有分析的模型在对抗输入下均表现出显著的拓扑压缩现象，拓扑特征在不同层次间具有高度一致性。这一发现为理解对抗影响提供了新的视角，且在统计上具有显著性，展示了持久同调在模型可解释性中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括对抗样本检测、模型安全性评估和LLM的可解释性提升。通过深入理解对抗输入对模型内部表示的影响，可以为未来的模型设计和优化提供重要参考，增强AI系统的鲁棒性和透明度。

## 📄 摘要（原文）

> Existing interpretability methods for Large Language Models (LLMs) often fall short by focusing on linear directions or isolated features, overlooking the high-dimensional, nonlinear, and relational geometry within model representations. This study focuses on how adversarial inputs systematically affect the internal representation spaces of LLMs, a topic which remains poorly understood. We propose persistent homology (PH), a tool from topological data analysis, as a principled framework to characterize the multi-scale dynamics within LLM activations. Using PH, we systematically analyze six state-of-the-art models under two distinct adversarial conditions, indirect prompt injection and backdoor fine-tuning, and identify a consistent topological signature of adversarial influence. Across architectures and model sizes, adversarial inputs induce ``topological compression'', where the latent space becomes structurally simpler, collapsing from varied, compact, small-scale features into fewer, dominant, and more dispersed large-scale ones. This topological signature is statistically robust across layers, highly discriminative, and provides interpretable insights into how adversarial effects emerge and propagate. By quantifying the shape of activations and neuronal information flow, our architecture-agnostic framework reveals fundamental invariants of representational change, offering a complementary perspective to existing interpretability methods.

