---
layout: default
title: "Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?"
---

# Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20903" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20903v1</a>
  <a href="https://arxiv.org/pdf/2505.20903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20903v1', 'Towards Objective Fine-tuning: How LLMs\' Prior Knowledge Causes Potential Poor Calibration?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziming Wang, Zeyu Shi, Haoyi Zhou, Shiqi Gao, Qingyun Sun, Jianxin Li

**分类**: cs.CL

**发布日期**: 2025-05-27

**备注**: Accepted to ACL2025 Main; The code will be released soon

---

## 💡 一句话要点

**提出CogCalib框架以解决LLMs校准不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `微调` `模型校准` `认知感知` `学习策略` `自然语言处理` `人机交互`

## 📋 核心要点

1. 现有的微调LLMs方法在校准方面存在不足，置信度与实际表现不一致，影响模型的可靠性。
2. 论文提出CogCalib框架，通过针对性学习策略，利用LLMs的先验知识来改善模型的校准能力。
3. 实验结果显示，CogCalib在7个任务上显著提高了校准效果，平均降低57%的ECE，同时保持了模型性能。

## 📝 摘要（中文）

微调的大型语言模型（LLMs）常常表现出较差的校准，其置信度分数与实际表现不一致。尽管校准在从头训练的模型中得到了广泛研究，但LLMs的先验知识在微调过程中对校准的影响仍未得到充分探讨。我们的研究揭示，LLMs的先验知识因真实世界微调中已知数据的普遍存在而导致潜在的校准不足。具体而言，与LLMs的先验知识对齐的数据会引发过度自信，而新知识则有助于改善校准。我们的发现揭示了一种矛盾：LLMs的百科知识虽然增强了任务的多样性，但通过不可避免的知识重叠削弱了校准。为此，我们提出了CogCalib，一个认知感知框架，根据模型的先验知识应用有针对性的学习策略。实验表明，CogCalib在保持性能的同时显著改善了校准，在Llama3-8B上实现了平均57%的ECE降低。

## 🔬 方法详解

**问题定义**：本论文旨在解决微调大型语言模型（LLMs）时校准不足的问题。现有方法未能充分考虑LLMs的先验知识对校准的影响，导致模型在实际应用中表现不佳。

**核心思路**：CogCalib框架的核心思路是根据模型的先验知识应用有针对性的学习策略，以减少因已知数据引发的过度自信现象，同时增强新知识的引入。

**技术框架**：CogCalib的整体架构包括数据选择模块、学习策略模块和校准评估模块。数据选择模块根据模型的先验知识筛选训练数据，学习策略模块则应用不同的训练策略以优化模型的校准，最后通过校准评估模块监控模型的校准效果。

**关键创新**：CogCalib的主要创新在于其认知感知的学习策略，能够动态调整训练过程以适应模型的先验知识。这一方法与传统的微调方法相比，能够更有效地处理知识重叠问题。

**关键设计**：在设计上，CogCalib采用了特定的损失函数来平衡置信度和实际表现，并引入了多任务学习机制以增强模型的泛化能力。

## 📊 实验亮点

实验结果显示，CogCalib在Llama3-8B模型上实现了平均57%的ECE降低，相较于标准微调方法显著提升了校准效果。这一改进在7个不同任务中均得到了验证，并且在领域外任务中也表现出良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等。通过提高LLMs的校准能力，CogCalib能够增强模型在关键人机交互应用中的可靠性和信任度，提升用户体验和安全性。

## 📄 摘要（原文）

> Fine-tuned Large Language Models (LLMs) often demonstrate poor calibration, with their confidence scores misaligned with actual performance. While calibration has been extensively studied in models trained from scratch, the impact of LLMs' prior knowledge on calibration during fine-tuning remains understudied. Our research reveals that LLMs' prior knowledge causes potential poor calibration due to the ubiquitous presence of known data in real-world fine-tuning, which appears harmful for calibration. Specifically, data aligned with LLMs' prior knowledge would induce overconfidence, while new knowledge improves calibration. Our findings expose a tension: LLMs' encyclopedic knowledge, while enabling task versatility, undermines calibration through unavoidable knowledge overlaps. To address this, we propose CogCalib, a cognition-aware framework that applies targeted learning strategies according to the model's prior knowledge. Experiments across 7 tasks using 3 LLM families prove that CogCalib significantly improves calibration while maintaining performance, achieving an average 57\% reduction in ECE compared to standard fine-tuning in Llama3-8B. These improvements generalize well to out-of-domain tasks, enhancing the objectivity and reliability of domain-specific LLMs, and making them more trustworthy for critical human-AI interaction applications.

