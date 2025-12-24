---
layout: default
title: Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation
---

# Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23912" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23912v1</a>
  <a href="https://arxiv.org/pdf/2505.23912.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23912v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23912v1', 'Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Caiqi Zhang, Xiaochen Zhu, Chengzu Li, Nigel Collier, Andreas Vlachos

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29

---

## 💡 一句话要点

**提出LoVeC以解决长文本生成中的信心估计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本生成` `信心估计` `强化学习` `大语言模型` `幻觉检测`

## 📋 核心要点

1. 现有方法在长文本生成中难以有效估计信心，导致幻觉现象频繁出现。
2. 本文提出LoVeC，通过强化学习实时估计长文本生成的口头信心分数，提升生成内容的可信度。
3. 实验结果显示，RL训练的模型在三个长文本问答数据集上实现了更好的校准效果，且泛化能力强。

## 📝 摘要（中文）

幻觉现象仍然是大语言模型在事实内容生成中安全可信部署的主要挑战。以往的研究探讨了信心估计作为幻觉检测的有效方法，但通常依赖于后验自一致性方法，这些方法需要计算上昂贵的采样。口头信心提供了一种更高效的替代方案，但现有方法主要局限于短文本问答任务，难以推广到开放式生成。本文提出了LoVeC（长文本口头信心），一种用于长文本生成的即时口头信心估计方法。我们利用强化学习训练大语言模型为每个生成的语句附加数值信心分数，作为生成事实性的直接和可解释信号。实验表明，我们的RL训练模型在校准方面表现更佳，并在多个领域中具有良好的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决长文本生成中的信心估计问题，现有方法往往依赖于计算成本高的后验自一致性方法，难以实时应用。

**核心思路**：论文提出的LoVeC方法利用强化学习训练模型为每个生成的语句附加数值信心分数，提供一种直接且可解释的事实性信号，旨在提高生成内容的可信度。

**技术框架**：整体架构包括数据输入、模型生成、信心分数估计和输出四个主要模块。通过强化学习算法（如DPO、ORPO、GRPO）优化模型，使其能够在生成过程中实时评估信心。

**关键创新**：LoVeC的主要创新在于将口头信心估计与长文本生成相结合，克服了现有方法在开放式生成中的局限性，实现了高效的信心评估。

**关键设计**：在模型训练中，采用了强化学习的多种策略，设计了适应长文本生成的损失函数，并通过引入少量的输出标记来提高效率。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，使用LoVeC方法训练的模型在三个长文本问答数据集上，相较于基线模型，校准效果提升显著，且在不同领域中均表现出良好的泛化能力。具体性能数据未详述，待进一步验证。

## 🎯 应用场景

该研究的潜在应用领域包括新闻生成、内容创作和教育辅导等。通过提高长文本生成的可信度，LoVeC能够在实际应用中减少信息误导，提升用户信任度，具有重要的社会价值和影响力。

## 📄 摘要（原文）

> Hallucination remains a major challenge for the safe and trustworthy deployment of large language models (LLMs) in factual content generation. Prior work has explored confidence estimation as an effective approach to hallucination detection, but often relies on post-hoc self-consistency methods that require computationally expensive sampling. Verbalized confidence offers a more efficient alternative, but existing approaches are largely limited to short-form question answering (QA) tasks and do not generalize well to open-ended generation. In this paper, we propose LoVeC (Long-form Verbalized Confidence), an on-the-fly verbalized confidence estimation method for long-form generation. Specifically, we use reinforcement learning (RL) to train LLMs to append numerical confidence scores to each generated statement, serving as a direct and interpretable signal of the factuality of generation. Our experiments consider both on-policy and off-policy RL methods, including DPO, ORPO, and GRPO, to enhance the model calibration. We introduce two novel evaluation settings, free-form tagging and iterative tagging, to assess different verbalized confidence estimation methods. Experiments on three long-form QA datasets show that our RL-trained models achieve better calibration and generalize robustly across domains. Also, our method is highly efficient, as it only requires adding a few tokens to the output being decoded.

