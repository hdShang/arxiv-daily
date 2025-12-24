---
layout: default
title: "CoRT: Code-integrated Reasoning within Thinking"
---

# CoRT: Code-integrated Reasoning within Thinking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09820" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09820v2</a>
  <a href="https://arxiv.org/pdf/2506.09820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09820v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09820v2', 'CoRT: Code-integrated Reasoning within Thinking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengpeng Li, Zhengyang Tang, Ziniu Li, Mingfeng Xue, Keqin Bao, Tian Ding, Ruoyu Sun, Benyou Wang, Xiang Wang, Junyang Lin, Dayiheng Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-11 (更新: 2025-06-12)

**备注**: work in progress

**🔗 代码/项目**: [GITHUB](https://github.com/ChengpengLi1003/CoRT)

---

## 💡 一句话要点

**提出CoRT框架以提升大规模推理模型的数学运算能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `数学推理` `代码集成` `Hint-Engineering` `后训练框架` `性能提升` `效率优化`

## 📋 核心要点

1. 现有大型推理模型在处理复杂数学运算时效率低下，且准确性不足，亟需改进。
2. 本文提出CoRT框架，通过Hint-Engineering合成数据，优化大型推理模型与代码解释器的交互。
3. 实验结果表明，使用Hint-Engineering的模型在多个数据集上分别提升了4%和8%的性能，并减少了token使用量。

## 📝 摘要（中文）

大型推理模型（LRMs）如o1和DeepSeek-R1在自然语言推理方面取得了显著进展，但在处理复杂数学运算时仍然效率低下或不准确。为了解决这一问题，本文提出了CoRT，一个后训练框架，旨在有效利用代码解释器（CI）。通过Hint-Engineering技术合成代码集成推理数据，优化LRM与CI的交互。实验结果显示，使用Hint-Engineering的模型在多个数学推理数据集上实现了4%和8%的绝对提升，同时在token使用上也显著减少。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在复杂数学运算中的低效率和低准确性问题。现有方法在与外部知识（如代码解释器）结合时，效率不高，导致推理能力受限。

**核心思路**：提出CoRT框架，通过Hint-Engineering技术合成代码集成推理数据，优化模型与代码解释器的交互，从而提升推理效率和准确性。

**技术框架**：CoRT框架包括数据合成、后训练和多种微调策略。首先，通过Hint-Engineering合成高质量的代码集成推理数据，然后对不同参数规模的模型进行后训练，采用监督微调、拒绝微调和强化学习等方法。

**关键创新**：最重要的技术创新在于Hint-Engineering，通过在适当位置插入不同提示，优化了LRM与CI的交互，显著提升了模型的推理能力。

**关键设计**：在实验中，手动创建了30个高质量样本，模型参数范围从1.5B到32B，采用了多种微调策略以提高模型性能，确保了实验的严谨性和有效性。

## 📊 实验亮点

实验结果显示，使用Hint-Engineering的模型在DeepSeek-R1-Distill-Qwen-32B和DeepSeek-R1-Distill-Qwen-1.5B上分别实现了4%和8%的绝对性能提升。此外，32B模型的token使用量减少约30%，1.5B模型减少约50%，显示出显著的效率改进。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学计算等需要复杂数学推理的场景。通过提升大型推理模型的数学运算能力，CoRT框架可以为这些领域提供更高效的智能决策支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs) like o1 and DeepSeek-R1 have shown remarkable progress in natural language reasoning with long chain-of-thought (CoT), yet they remain inefficient or inaccurate when handling complex mathematical operations. Addressing these limitations through computational tools (e.g., computation libraries and symbolic solvers) is promising, but it introduces a technical challenge: Code Interpreter (CI) brings external knowledge beyond the model's internal text representations, thus the direct combination is not efficient. This paper introduces CoRT, a post-training framework for teaching LRMs to leverage CI effectively and efficiently. As a first step, we address the data scarcity issue by synthesizing code-integrated reasoning data through Hint-Engineering, which strategically inserts different hints at appropriate positions to optimize LRM-CI interaction. We manually create 30 high-quality samples, upon which we post-train models ranging from 1.5B to 32B parameters, with supervised fine-tuning, rejection fine-tuning and reinforcement learning. Our experimental results demonstrate that Hint-Engineering models achieve 4\% and 8\% absolute improvements on DeepSeek-R1-Distill-Qwen-32B and DeepSeek-R1-Distill-Qwen-1.5B respectively, across five challenging mathematical reasoning datasets. Furthermore, Hint-Engineering models use about 30\% fewer tokens for the 32B model and 50\% fewer tokens for the 1.5B model compared with the natural language models. The models and code are available at https://github.com/ChengpengLi1003/CoRT.

