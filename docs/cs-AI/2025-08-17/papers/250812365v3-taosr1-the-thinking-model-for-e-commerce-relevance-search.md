---
layout: default
title: "TaoSR1: The Thinking Model for E-commerce Relevance Search"
---

# TaoSR1: The Thinking Model for E-commerce Relevance Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12365" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12365v3</a>
  <a href="https://arxiv.org/pdf/2508.12365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12365v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12365v3', 'TaoSR1: The Thinking Model for E-commerce Relevance Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenhe Dong, Shaowei Yao, Pengkun Jiao, Jianhui Yang, Yiming Jin, Zerui Huang, Xiaojiang Zhou, Dan Ou, Haihong Tang, Bo Zheng

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-08-17 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出TaoSR1以解决电商相关性搜索中的推理不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电商搜索` `查询相关性` `推理能力` `链式思维` `动态采样` `大型语言模型` `生成质量` `判别性幻觉`

## 📋 核心要点

1. 现有的基于BERT的模型在电商搜索中缺乏复杂推理能力，导致查询与产品的相关性预测效果不佳。
2. 论文提出的TaoSR1框架通过引入链式思维（CoT）和动态采样策略，增强了模型的推理能力和生成质量。
3. 实验结果表明，TaoSR1在离线数据集上显著超越了基线模型，并在在线评估中获得了显著的用户满意度提升。

## 📝 摘要（中文）

查询与产品相关性预测是电商搜索中的核心任务。尽管基于BERT的模型在语义匹配上表现优异，但在复杂推理能力上存在不足。虽然大型语言模型（LLMs）被探索，但大多数仍采用判别性微调或蒸馏为小模型进行部署。我们提出了一种框架，直接将LLMs应用于此任务，解决了链式思维（CoT）错误累积、判别性幻觉和部署可行性等关键挑战。TaoSR1框架包括三个阶段：1) 使用CoT进行监督微调，以增强推理能力；2) 采用pass@N策略和直接偏好优化（DPO）进行离线采样，以提高生成质量；3) 基于难度的动态采样与组相对策略优化（GRPO）以减轻判别性幻觉。此外，后CoT处理和基于累积概率的分区方法使在线部署更加高效。TaoSR1在离线数据集上显著超越基线，并在在线对比的人类评估中取得了显著提升，提出了一种将CoT推理应用于相关性分类的新范式。

## 🔬 方法详解

**问题定义**：本论文旨在解决电商搜索中查询与产品相关性预测的推理不足问题。现有的BERT模型虽然在语义匹配上表现良好，但在复杂推理和生成质量上存在明显短板。

**核心思路**：TaoSR1框架通过引入链式思维（CoT）和动态采样策略，旨在增强模型的推理能力，减少判别性幻觉，并提高在线部署的可行性。

**技术框架**：TaoSR1框架分为三个主要阶段：1) 监督微调（SFT）阶段，通过CoT增强推理能力；2) 离线采样阶段，采用pass@N策略和直接偏好优化（DPO）提升生成质量；3) 动态采样阶段，利用组相对策略优化（GRPO）减轻判别性幻觉。

**关键创新**：TaoSR1的核心创新在于将CoT推理直接应用于相关性分类，并通过动态采样策略有效降低了判别性幻觉的影响，这与传统的微调方法有本质区别。

**关键设计**：在模型设计中，采用了特定的损失函数和参数设置，以优化CoT推理的效果，并通过后CoT处理和基于累积概率的分区方法实现高效的在线部署。

## 📊 实验亮点

在实验中，TaoSR1在离线数据集上显著超越了基线模型，提升幅度达到XX%（具体数据待补充），并在在线评估中获得了用户满意度的显著提升，展示了其在实际应用中的有效性。

## 🎯 应用场景

TaoSR1框架在电商搜索引擎中具有广泛的应用潜力，可以显著提升用户查询与产品匹配的准确性和效率。其创新的推理机制和动态采样策略为未来的电商推荐系统提供了新的思路，可能会对用户体验和销售转化率产生积极影响。

## 📄 摘要（原文）

> Query-product relevance prediction is a core task in e-commerce search. BERT-based models excel at semantic matching but lack complex reasoning capabilities. While Large Language Models (LLMs) are explored, most still use discriminative fine-tuning or distill to smaller models for deployment. We propose a framework to directly deploy LLMs for this task, addressing key challenges: Chain-of-Thought (CoT) error accumulation, discriminative hallucination, and deployment feasibility. Our framework, TaoSR1, involves three stages: (1) Supervised Fine-Tuning (SFT) with CoT to instill reasoning; (2) Offline sampling with a pass@N strategy and Direct Preference Optimization (DPO) to improve generation quality; and (3) Difficulty-based dynamic sampling with Group Relative Policy Optimization (GRPO) to mitigate discriminative hallucination. Additionally, post-CoT processing and a cumulative probability-based partitioning method enable efficient online deployment. TaoSR1 significantly outperforms baselines on offline datasets and achieves substantial gains in online side-by-side human evaluations, introducing a novel paradigm for applying CoT reasoning to relevance classification.

