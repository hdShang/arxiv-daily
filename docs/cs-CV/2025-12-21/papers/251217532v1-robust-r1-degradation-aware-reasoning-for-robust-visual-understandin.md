---
layout: default
title: Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding
---

# Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17532" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17532v1</a>
  <a href="https://arxiv.org/pdf/2512.17532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17532v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17532v1', 'Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Tang, Jianmin Chen, Wei Wei, Xiaogang Xu, Runtao Liu, Xiangyu Wu, Qipeng Xie, Jiafei Wu, Lei Zhang, Qifeng Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-19

**备注**: Accepted by AAAI2026 Oral

---

## 💡 一句话要点

**提出Robust-R1框架，通过显式建模视觉退化提升多模态大模型在真实场景下的鲁棒性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大模型` `视觉退化` `鲁棒性` `显式建模` `推理链`

## 📋 核心要点

1. 现有鲁棒多模态大模型依赖隐式训练，忽略了对视觉退化的显式建模，导致可解释性差且优化孤立。
2. Robust-R1通过结构化推理链显式建模视觉退化，包含退化感知推理、奖励驱动对齐和动态推理深度缩放三个模块。
3. 在R-Bench等基准测试中，Robust-R1超越了现有通用和鲁棒模型，并在对抗性退化下表现出更强的抗退化能力。

## 📝 摘要（中文）

多模态大语言模型在极端真实视觉退化下难以维持可靠的性能，阻碍了它们的实际鲁棒性。现有的鲁棒MLLM主要依赖于隐式的训练/适应，仅关注视觉编码器的泛化能力，缺乏可解释性和孤立的优化。为了克服这些限制，我们提出了Robust-R1，一种通过结构化推理链显式建模视觉退化的新框架。我们的方法整合了：（i）用于退化感知推理基础的监督微调，（ii）用于准确感知退化参数的奖励驱动对齐，以及（iii）适应于退化强度的动态推理深度缩放。为了促进这种方法，我们引入了一个专门的11K数据集，该数据集具有在四个关键的真实世界视觉处理阶段合成的逼真退化，每个阶段都用连接退化参数、感知影响、原始语义推理链和结论的结构化链进行注释。全面的评估表明了最先进的鲁棒性：Robust-R1在真实世界退化基准R-Bench上优于所有通用和鲁棒基线，同时在MMMB、MMStar和RealWorldQA上保持了多强度对抗退化下的卓越抗退化性能。

## 🔬 方法详解

**问题定义**：多模态大语言模型在实际应用中，面临各种视觉退化（如噪声、模糊、压缩等）的挑战，导致性能显著下降。现有方法主要关注视觉编码器的泛化能力，缺乏对退化过程的显式建模和推理，难以有效应对复杂的退化情况。因此，如何提升多模态大模型在各种视觉退化下的鲁棒性是一个关键问题。

**核心思路**：Robust-R1的核心思路是通过显式地建模视觉退化过程，构建结构化的推理链，从而使模型能够理解退化对图像语义的影响，并进行相应的补偿。这种显式建模的方式提高了模型的可解释性，并允许针对不同的退化情况进行优化。通过奖励驱动的对齐，模型可以更准确地感知退化参数，并根据退化强度动态调整推理深度，从而实现更鲁棒的视觉理解。

**技术框架**：Robust-R1框架主要包含三个阶段：1) 退化感知推理基础：使用监督微调，训练模型理解退化参数与图像语义之间的关系，构建推理基础。2) 奖励驱动对齐：通过奖励机制，鼓励模型准确感知退化参数，并将其与推理链对齐。3) 动态推理深度缩放：根据退化强度，动态调整推理深度，以平衡性能和计算成本。整个框架通过结构化的推理链，将退化参数、感知影响、原始语义推理链和结论连接起来，实现端到端的优化。

**关键创新**：Robust-R1最重要的创新点在于对视觉退化的显式建模。与现有方法不同，Robust-R1不是简单地增强视觉编码器的泛化能力，而是通过结构化的推理链，将退化过程分解为多个步骤，并对每个步骤进行建模和优化。这种显式建模的方式提高了模型的可解释性，并允许针对不同的退化情况进行优化。此外，奖励驱动对齐和动态推理深度缩放也是关键创新，它们使模型能够更准确地感知退化参数，并根据退化强度调整推理策略。

**关键设计**：Robust-R1的关键设计包括：1) 专门构建的包含11K图像的退化数据集，该数据集覆盖了四个关键的真实世界视觉处理阶段，并对每个图像进行了结构化的标注，包括退化参数、感知影响、原始语义推理链和结论。2) 使用奖励函数来鼓励模型准确感知退化参数，奖励函数的设计需要平衡准确性和鲁棒性。3) 设计动态推理深度缩放策略，根据退化强度调整推理深度，以平衡性能和计算成本。具体的网络结构和损失函数等技术细节在论文中进行了详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17532v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17532v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17532v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Robust-R1在R-Bench基准测试中取得了state-of-the-art的性能，超越了所有通用和鲁棒基线。此外，在MMMB、MMStar和RealWorldQA等基准测试中，Robust-R1在多强度对抗退化下表现出卓越的抗退化性能，证明了其在真实场景下的鲁棒性。

## 🎯 应用场景

Robust-R1框架可应用于各种需要鲁棒视觉理解的场景，例如自动驾驶、机器人导航、医学图像分析、安全监控等。该研究有助于提升多模态大模型在真实复杂环境下的可靠性，推动人工智能技术在实际场景中的应用。

## 📄 摘要（原文）

> Multimodal Large Language Models struggle to maintain reliable performance under extreme real-world visual degradations, which impede their practical robustness. Existing robust MLLMs predominantly rely on implicit training/adaptation that focuses solely on visual encoder generalization, suffering from limited interpretability and isolated optimization. To overcome these limitations, we propose Robust-R1, a novel framework that explicitly models visual degradations through structured reasoning chains. Our approach integrates: (i) supervised fine-tuning for degradation-aware reasoning foundations, (ii) reward-driven alignment for accurately perceiving degradation parameters, and (iii) dynamic reasoning depth scaling adapted to degradation intensity. To facilitate this approach, we introduce a specialized 11K dataset featuring realistic degradations synthesized across four critical real-world visual processing stages, each annotated with structured chains connecting degradation parameters, perceptual influence, pristine semantic reasoning chain, and conclusion. Comprehensive evaluations demonstrate state-of-the-art robustness: Robust-R1 outperforms all general and robust baselines on the real-world degradation benchmark R-Bench, while maintaining superior anti-degradation performance under multi-intensity adversarial degradations on MMMB, MMStar, and RealWorldQA.

