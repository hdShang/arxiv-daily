---
layout: default
title: "LENS: Learning to Segment Anything with Unified Reinforced Reasoning"
---

# LENS: Learning to Segment Anything with Unified Reinforced Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14153" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14153v2</a>
  <a href="https://arxiv.org/pdf/2508.14153.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14153v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14153v2', 'LENS: Learning to Segment Anything with Unified Reinforced Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lianghui Zhu, Bin Ouyang, Yuxuan Zhang, Tianheng Cheng, Rui Hu, Haocheng Shen, Longjin Ran, Xiaoxin Chen, Li Yu, Wenyu Liu, Xinggang Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-19 (更新: 2025-11-18)

**备注**: Code is released at https://github.com/hustvl/LENS

**🔗 代码/项目**: [GITHUB](https://github.com/hustvl/LENS)

---

## 💡 一句话要点

**提出LENS框架以解决文本提示图像分割中的推理不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像分割` `强化学习` `推理机制` `多模态学习` `视觉语言模型`

## 📋 核心要点

1. 现有的图像分割方法在处理文本提示时，缺乏有效的推理机制，导致在新场景中的表现不佳。
2. LENS框架通过强化学习联合优化推理和分割过程，采用统一的奖励机制来提升模型的推理能力和分割质量。
3. 在多个基准测试中，LENS的表现显著优于传统微调方法，验证了其在文本提示分割中的有效性和实用性。

## 📝 摘要（中文）

文本提示的图像分割对于细粒度视觉理解至关重要，尤其在人机交互和机器人领域。然而，现有的监督微调方法在测试时通常忽视显式的推理过程，限制了其在未见提示和领域中的泛化能力。为了解决这一问题，本文提出了LENS，一个可扩展的强化学习框架，能够端到端地优化推理过程和分割。我们提出了统一的强化学习奖励机制，涵盖句子、框和分割级别的线索，鼓励模型生成信息丰富的推理理由，同时提升掩膜质量。使用一个公开的30亿参数的视觉语言模型，LENS在RefCOCO、RefCOCO+和RefCOCOg基准上实现了81.2%的平均cIoU，超越了强大的微调方法GLaMM，提升幅度达到5.6%。这些结果表明，基于强化学习的推理显著增强了文本提示的分割能力，为更具泛化能力的Segment Anything模型提供了实际路径。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文本提示图像分割方法在推理过程中的不足，尤其是在未见提示和领域中的泛化能力差的问题。现有方法通常依赖于静态的微调策略，缺乏动态推理能力。

**核心思路**：LENS框架的核心思路是通过强化学习来联合优化推理和分割过程。通过引入统一的奖励机制，模型能够在生成分割掩膜的同时，进行有效的推理，从而提升整体性能。

**技术框架**：LENS的整体架构包括三个主要模块：推理模块、分割模块和奖励机制。推理模块负责生成推理理由，分割模块则生成最终的分割掩膜，而奖励机制则根据推理和分割的质量进行反馈，指导模型的学习过程。

**关键创新**：LENS的主要创新在于引入了统一的强化学习奖励机制，涵盖了句子、框和分割级别的线索。这种设计使得模型能够在生成分割掩膜的同时，进行有效的推理，从而显著提升了分割质量。

**关键设计**：在模型设计中，采用了30亿参数的视觉语言模型Qwen2.5-VL-3B-Instruct，并通过精心设计的损失函数和参数设置，确保模型在推理和分割任务中能够达到最佳性能。

## 📊 实验亮点

LENS在RefCOCO、RefCOCO+和RefCOCOg基准上实现了81.2%的平均cIoU，相较于微调方法GLaMM提升了5.6%。这一结果表明，基于强化学习的推理机制显著增强了文本提示分割的效果，具有重要的研究价值。

## 🎯 应用场景

LENS框架在人机交互、机器人视觉和自动驾驶等领域具有广泛的应用潜力。通过提升文本提示图像分割的准确性和泛化能力，LENS能够为智能系统提供更为精准的视觉理解，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Text-prompted image segmentation enables fine-grained visual understanding and is critical for applications such as human-computer interaction and robotics. However, existing supervised fine-tuning methods typically ignore explicit chain-of-thought (CoT) reasoning at test time, which limits their ability to generalize to unseen prompts and domains. To address this issue, we introduce LENS, a scalable reinforcement-learning framework that jointly optimizes the reasoning process and segmentation in an end-to-end manner. We propose unified reinforcement-learning rewards that span sentence-, box-, and segment-level cues, encouraging the model to generate informative CoT rationales while refining mask quality. Using a publicly available 3-billion-parameter vision-language model, i.e., Qwen2.5-VL-3B-Instruct, LENS achieves an average cIoU of 81.2% on the RefCOCO, RefCOCO+, and RefCOCOg benchmarks, outperforming the strong fine-tuned method, i.e., GLaMM, by up to 5.6%. These results demonstrate that RL-driven CoT reasoning significantly enhances text-prompted segmentation and offers a practical path toward more generalizable Segment Anything models (SAM). Code is available at https://github.com/hustvl/LENS.

