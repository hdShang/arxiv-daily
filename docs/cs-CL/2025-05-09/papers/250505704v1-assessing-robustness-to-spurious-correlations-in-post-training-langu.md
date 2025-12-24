---
layout: default
title: Assessing Robustness to Spurious Correlations in Post-Training Language Models
---

# Assessing Robustness to Spurious Correlations in Post-Training Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05704" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05704v1</a>
  <a href="https://arxiv.org/pdf/2505.05704.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05704v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05704v1', 'Assessing Robustness to Spurious Correlations in Post-Training Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Julia Shuieh, Prasann Singhal, Apaar Shanker, John Heyer, George Pu, Samuel Denton

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-09

**备注**: ICLR '25 Workshop on Spurious Correlation and Shortcut Learning

---

## 💡 一句话要点

**评估后训练语言模型对虚假相关性的鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚假相关性` `后训练` `语言模型` `微调技术` `鲁棒性评估` `数学推理` `偏好优化`

## 📋 核心要点

1. 现有的微调方法在处理现实世界数据中的虚假相关性时存在不足，可能导致模型性能下降。
2. 本文提出了三种后训练算法，通过系统评估其在不同虚假相关性条件下的表现，探索其鲁棒性。
3. 实验结果显示，偏好基于的方法在数学推理任务中相对鲁棒，而SFT在复杂任务中表现更佳，强调了方法选择的重要性。

## 📝 摘要（中文）

监督和基于偏好的微调技术已成为对齐大型语言模型（LLMs）与用户意图和正确性标准的热门方法。然而，现实世界的训练数据常常表现出虚假相关性，这可能会影响模型的性能或泛化能力。本文系统评估了三种后训练算法——监督微调（SFT）、直接偏好优化（DPO）和KTO（卡尼曼-特沃斯基优化），在多种合成任务和虚假相关性条件下的表现。实验结果表明，模型在较高虚假相关性下的性能通常会下降，但偏好基于的方法在数学推理任务中表现出相对鲁棒性，而SFT在复杂的上下文密集型任务中保持较强的性能。这些发现强调了没有单一的后训练策略在所有场景中都能表现优越，最佳选择依赖于目标任务的类型和虚假相关性的性质。

## 🔬 方法详解

**问题定义**：本文旨在解决后训练语言模型在面对虚假相关性时的鲁棒性问题。现有方法在处理数据中的偏见和伪特征时，常常无法保持稳定的性能。

**核心思路**：通过系统评估三种后训练算法，探索不同虚假相关性条件下的模型表现，旨在找出最佳的微调策略。

**技术框架**：研究设计了多种合成任务，包括数学推理、受限指令跟随和文档基础问答，评估不同算法在10%与90%虚假相关性下的表现。

**关键创新**：本文的创新在于比较了三种后训练算法在不同虚假相关性条件下的表现，揭示了不同方法在特定任务中的优势与劣势。

**关键设计**：实验中设置了不同程度的虚假相关性，并定义了“特征模糊性”和“分布狭窄”两种伪特征，采用了适应性损失函数来优化模型性能。

## 📊 实验亮点

实验结果显示，在90%虚假相关性条件下，偏好基于的方法（DPO/KTO）在数学推理任务中表现出相对鲁棒性，而SFT在复杂任务中保持较强性能。整体上，模型在不同虚假相关性下的表现差异显著，强调了任务类型对微调策略选择的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过提高模型对虚假相关性的鲁棒性，可以增强其在实际应用中的可靠性和准确性，进而提升用户体验。未来，该研究可能影响模型微调的标准实践，推动更为健壮的语言模型的开发。

## 📄 摘要（原文）

> Supervised and preference-based fine-tuning techniques have become popular for aligning large language models (LLMs) with user intent and correctness criteria. However, real-world training data often exhibits spurious correlations -- arising from biases, dataset artifacts, or other "shortcut" features -- that can compromise a model's performance or generalization. In this paper, we systematically evaluate three post-training algorithms -- Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and KTO (Kahneman-Tversky Optimization) -- across a diverse set of synthetic tasks and spuriousness conditions. Our tasks span mathematical reasoning, constrained instruction-following, and document-grounded question answering. We vary the degree of spurious correlation (10% vs. 90%) and investigate two forms of artifacts: "Feature Ambiguity" and "Distributional Narrowness." Our results show that the models often but not always degrade under higher spuriousness. The preference-based methods (DPO/KTO) can demonstrate relative robustness in mathematical reasoning tasks. By contrast, SFT maintains stronger performance in complex, context-intensive tasks. These findings highlight that no single post-training strategy universally outperforms in all scenarios; the best choice depends on the type of target task and the nature of spurious correlations.

