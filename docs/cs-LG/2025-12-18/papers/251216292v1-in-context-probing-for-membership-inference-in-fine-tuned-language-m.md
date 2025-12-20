---
layout: default
title: In-Context Probing for Membership Inference in Fine-Tuned Language Models
---

# In-Context Probing for Membership Inference in Fine-Tuned Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16292" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16292v1</a>
  <a href="https://arxiv.org/pdf/2512.16292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16292v1', 'In-Context Probing for Membership Inference in Fine-Tuned Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhexi Lu, Hongliang Chi, Nathalie Baracaldo, Swanand Ravindra Kadhe, Yuseok Jeon, Lei Yu

**分类**: cs.CR, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出ICP-MIA框架以解决细调语言模型的成员推断攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `成员推断攻击` `隐私保护` `语言模型` `优化差距` `上下文探测` `黑箱攻击` `模型安全性`

## 📋 核心要点

1. 现有的黑箱成员推断攻击方法依赖于置信度分数，导致泛化能力差和信噪比低。
2. 本文提出ICP-MIA框架，利用优化差距作为成员资格信号，设计上下文探测方法以估计该差距。
3. 实验结果显示，ICP-MIA在多个任务上显著提升了攻击效果，尤其在低假阳性率下表现优异。

## 📝 摘要（中文）

成员推断攻击（MIA）对细调的大型语言模型（LLMs）构成了严重的隐私威胁，尤其是在使用敏感数据进行领域特定任务适配时。以往的黑箱MIA技术依赖于置信度分数或标记似然性，但这些信号常常与样本的内在属性交织在一起，导致泛化能力差和信噪比低。本文提出了ICP-MIA，一个基于训练动态理论的新型MIA框架，特别是优化过程中的收益递减现象。我们引入了优化差距作为成员资格的基本信号：在收敛时，成员样本的剩余损失减少潜力最小，而非成员则保留显著的进一步优化潜力。为在黑箱设置中估计这一差距，我们提出了上下文探测（ICP），一种通过战略性构建输入上下文模拟细调行为的无训练方法。实验表明，ICP-MIA在多个LLM上显著优于以往的黑箱MIA，尤其是在低假阳性率下。

## 🔬 方法详解

**问题定义**：本文解决的是细调语言模型中的成员推断攻击问题，现有方法依赖于置信度分数，导致信号与样本属性交织，影响攻击效果。

**核心思路**：提出ICP-MIA框架，利用优化差距作为成员资格信号，设计上下文探测方法以在黑箱环境中估计该差距，从而提高攻击的准确性和有效性。

**技术框架**：ICP-MIA框架包括两个主要模块：优化差距的定义与估计，以及上下文探测策略的实施。上下文探测通过构建参考数据和自扰动两种策略来模拟细调行为。

**关键创新**：最重要的创新在于引入优化差距作为成员资格的信号，并通过上下文探测方法在无训练的情况下有效估计这一差距，显著提升了攻击的准确性。

**关键设计**：关键设计包括参考数据的选择（使用语义相似的公共样本）和自扰动策略（通过掩蔽或生成），确保探测过程的有效性和准确性。实验中还考虑了模型类型、PEFT配置和训练计划对攻击效果的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16292v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16292v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16292v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ICP-MIA在三个任务和多种大型语言模型上显著优于以往的黑箱MIA方法，尤其在低假阳性率下，提升幅度达到XX%（具体数据需根据实验结果填写）。

## 🎯 应用场景

该研究的潜在应用领域包括隐私审计、模型安全性评估以及敏感数据处理等。ICP-MIA框架为评估和降低部署语言模型的隐私风险提供了理论基础和实践指导，未来可广泛应用于各类需要保护用户隐私的AI系统中。

## 📄 摘要（原文）

> Membership inference attacks (MIAs) pose a critical privacy threat to fine-tuned large language models (LLMs), especially when models are adapted to domain-specific tasks using sensitive data. While prior black-box MIA techniques rely on confidence scores or token likelihoods, these signals are often entangled with a sample's intrinsic properties - such as content difficulty or rarity - leading to poor generalization and low signal-to-noise ratios. In this paper, we propose ICP-MIA, a novel MIA framework grounded in the theory of training dynamics, particularly the phenomenon of diminishing returns during optimization. We introduce the Optimization Gap as a fundamental signal of membership: at convergence, member samples exhibit minimal remaining loss-reduction potential, while non-members retain significant potential for further optimization. To estimate this gap in a black-box setting, we propose In-Context Probing (ICP), a training-free method that simulates fine-tuning-like behavior via strategically constructed input contexts. We propose two probing strategies: reference-data-based (using semantically similar public samples) and self-perturbation (via masking or generation). Experiments on three tasks and multiple LLMs show that ICP-MIA significantly outperforms prior black-box MIAs, particularly at low false positive rates. We further analyze how reference data alignment, model type, PEFT configurations, and training schedules affect attack effectiveness. Our findings establish ICP-MIA as a practical and theoretically grounded framework for auditing privacy risks in deployed LLMs.

