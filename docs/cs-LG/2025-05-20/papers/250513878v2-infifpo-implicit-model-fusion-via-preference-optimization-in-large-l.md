---
layout: default
title: InfiFPO: Implicit Model Fusion via Preference Optimization in Large Language Models
---

# InfiFPO: Implicit Model Fusion via Preference Optimization in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13878" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13878v2</a>
  <a href="https://arxiv.org/pdf/2505.13878.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13878v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13878v2', 'InfiFPO: Implicit Model Fusion via Preference Optimization in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanggan Gu, Yuanyi Wang, Zhaoyi Yan, Yiming Zhang, Qi Zhou, Fei Wu, Hongxia Yang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-22)

**期刊**: NeurIPS 2025

---

## 💡 一句话要点

**提出InfiFPO以解决大语言模型融合中的偏好对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `模型融合` `偏好对齐` `隐式模型` `优化方法` `自然语言处理` `知识提取`

## 📋 核心要点

1. 现有模型融合方法主要集中在监督微调，偏好对齐阶段的研究相对较少，导致性能提升有限。
2. InfiFPO通过在直接偏好优化中引入融合源模型，解决了复杂的词汇对齐问题，同时保留了概率信息。
3. 在11个基准测试中，InfiFPO显著提升了Phi-4模型的平均性能，从79.95提高到83.33，增强了其在多项任务中的能力。

## 📝 摘要（中文）

模型融合通过轻量级训练方法将多个具有不同优势的大语言模型（LLMs）结合成一个更强大的集成模型。现有的模型融合研究主要集中在监督微调（SFT）上，而偏好对齐（PA）这一提升LLM性能的关键阶段却鲜有探索。现有的PA融合方法如WRPO仅利用源模型的响应输出，忽略了概率信息。为了解决这一局限性，本文提出了InfiFPO，一种用于隐式模型融合的偏好优化方法。InfiFPO通过在直接偏好优化（DPO）中用融合源模型替代参考模型，在序列级别合成多源概率，避免了以往方法中复杂的词汇对齐挑战，同时保留了概率信息。通过引入概率裁剪和最大边际融合策略，InfiFPO能够使枢纽模型与人类偏好对齐，并有效提取源模型的知识。综合实验表明，InfiFPO在11个广泛使用的基准上表现优异，显著提升了数学、编码和推理任务的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有模型融合方法在偏好对齐阶段的不足，尤其是忽视概率信息的问题。现有方法如WRPO仅依赖响应输出，导致信息损失。

**核心思路**：InfiFPO的核心思路是用融合源模型替代参考模型，综合多源概率信息，从而在序列级别进行优化，避免了复杂的词汇对齐问题。

**技术框架**：InfiFPO的整体架构包括数据输入、源模型输出的概率合成、偏好优化模块和最终的模型融合。每个模块都旨在提升模型的对齐能力和知识提取效率。

**关键创新**：InfiFPO的主要创新在于引入了概率裁剪和最大边际融合策略，使得枢纽模型能够更好地对齐人类偏好，同时有效提取源模型的知识。这一方法与现有的简单响应输出方法有本质区别。

**关键设计**：在设计中，InfiFPO使用了特定的损失函数来优化偏好对齐，并通过调整概率裁剪参数来控制信息的保留程度，确保模型在不同任务中的表现均衡。整体网络结构经过精心设计，以适应多源信息的融合。

## 📊 实验亮点

在实验中，InfiFPO在11个基准测试上表现优异，使用Phi-4作为枢纽模型时，平均性能从79.95提升至83.33，显著提高了模型在数学、编码和推理任务中的能力，展示了其在模型融合和偏好优化领域的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和教育技术等。通过提升大语言模型的性能，InfiFPO可以在自动问答、编程辅助和逻辑推理等任务中发挥重要作用，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Model fusion combines multiple Large Language Models (LLMs) with different strengths into a more powerful, integrated model through lightweight training methods. Existing works on model fusion focus primarily on supervised fine-tuning (SFT), leaving preference alignment (PA) --a critical phase for enhancing LLM performance--largely unexplored. The current few fusion methods on PA phase, like WRPO, simplify the process by utilizing only response outputs from source models while discarding their probability information. To address this limitation, we propose InfiFPO, a preference optimization method for implicit model fusion. InfiFPO replaces the reference model in Direct Preference Optimization (DPO) with a fused source model that synthesizes multi-source probabilities at the sequence level, circumventing complex vocabulary alignment challenges in previous works and meanwhile maintaining the probability information. By introducing probability clipping and max-margin fusion strategies, InfiFPO enables the pivot model to align with human preferences while effectively distilling knowledge from source models. Comprehensive experiments on 11 widely-used benchmarks demonstrate that InfiFPO consistently outperforms existing model fusion and preference optimization methods. When using Phi-4 as the pivot model, InfiFPO improve its average performance from 79.95 to 83.33 on 11 benchmarks, significantly improving its capabilities in mathematics, coding, and reasoning tasks.

