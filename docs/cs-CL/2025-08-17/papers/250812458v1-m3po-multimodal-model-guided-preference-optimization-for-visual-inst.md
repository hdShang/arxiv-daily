---
layout: default
title: "M3PO: Multimodal-Model-Guided Preference Optimization for Visual Instruction Following"
---

# M3PO: Multimodal-Model-Guided Preference Optimization for Visual Instruction Following

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12458" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12458v1</a>
  <a href="https://arxiv.org/pdf/2508.12458.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12458v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12458v1', 'M3PO: Multimodal-Model-Guided Preference Optimization for Visual Instruction Following')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruirui Gao, Emily Johnson, Bowen Tan, Yanfei Qian

**分类**: cs.CL

**发布日期**: 2025-08-17

---

## 💡 一句话要点

**提出M3PO以解决LVLM偏好优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态指令跟随` `偏好优化` `视觉语言模型` `深度学习` `自一致性评分`

## 📋 核心要点

1. 现有的偏好优化方法在高效利用模型生成空间和识别困难负样本方面存在不足，限制了LVLM的性能提升。
2. 本文提出的M3PO方法通过智能选择学习价值高的偏好样本对，结合多模态对齐评分和模型自信度，优化偏好学习过程。
3. 实验结果显示，M3PO在多个基准测试中表现优异，超越了传统的SFT、模拟RLHF、普通DPO和RM-DPO等方法。

## 📝 摘要（中文）

大型视觉语言模型（LVLMs）在复杂的多模态指令跟随中具有巨大潜力，但其发展常受到高昂的人类标注成本和不一致性的限制。传统的监督微调（SFT）和现有的偏好优化方法如RLHF和DPO在有效利用模型生成空间以识别高信息量的“困难负样本”方面常常面临挑战。为了解决这些问题，本文提出了一种新颖且数据高效的方法——多模态模型引导的偏好优化（M3PO），旨在增强LVLM在视觉指令跟随中的能力。M3PO智能地从多样的LVLM生成候选样本中选择最具“学习价值”的偏好样本对，结合多模态对齐评分（MAS）和模型自一致性/置信度（对数概率）来评估样本质量，最终通过高质量的偏好对进行高效的直接偏好优化（DPO）微调。实验结果表明，M3PO在多个多模态指令跟随基准上均优于强基线。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型（LVLMs）在多模态指令跟随中的偏好优化问题。现有方法如SFT和RLHF在高效利用模型生成空间和识别高信息量的困难负样本方面存在显著不足。

**核心思路**：M3PO通过智能选择最具学习价值的偏好样本对，结合外部质量评估的多模态对齐评分（MAS）和模型内部置信度，优化偏好学习过程。这样的设计旨在提高样本选择的有效性和模型的学习效率。

**技术框架**：M3PO的整体架构包括样本生成、样本选择和偏好优化三个主要模块。首先，从LVLM生成多样的候选样本；其次，通过MAS和自一致性评分选择高质量的偏好样本对；最后，利用这些样本对进行直接偏好优化（DPO）微调。

**关键创新**：M3PO的核心创新在于提出了M3P-Score，这一评分机制结合了外部和内部信号，能够有效识别出模型自信但错误的响应，从而优化偏好学习过程。这与传统方法的样本选择机制有本质区别。

**关键设计**：在M3PO中，关键参数包括多模态对齐评分的计算方式和自一致性评分的评估方法。此外，采用LoRA技术进行DPO微调，以提高模型的训练效率和效果。具体的损失函数设计也针对偏好样本对的优化进行了调整。

## 📊 实验亮点

实验结果表明，M3PO在多个多模态指令跟随基准（如MME-Bench、POPE、IFT、Human Pref. Score）上均显著优于传统方法，提升幅度达到10%以上，展示了其在偏好优化中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人导航等多模态交互场景。通过提升LVLM在视觉指令跟随中的表现，M3PO能够显著提高人机交互的自然性和准确性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) hold immense potential for complex multimodal instruction following, yet their development is often hindered by the high cost and inconsistency of human annotation required for effective fine-tuning and preference alignment. Traditional supervised fine-tuning (SFT) and existing preference optimization methods like RLHF and DPO frequently struggle to efficiently leverage the model's own generation space to identify highly informative "hard negative" samples. To address these challenges, we propose Multimodal-Model-Guided Preference Optimization (M3PO), a novel and data-efficient method designed to enhance LVLMs' capabilities in visual instruction following. M3PO intelligently selects the most "learning-valuable" preference sample pairs from a diverse pool of LVLM-generated candidates. This selection is driven by a sophisticated mechanism that integrates two crucial signals: a Multimodal Alignment Score (MAS) to assess external quality and the model's Self-Consistency / Confidence (log-probability) to gauge internal belief. These are combined into a novel M3P-Score, which specifically identifies preferred responses and challenging dispreferred responses that the model might confidently generate despite being incorrect. These high-quality preference pairs are then used for efficient Direct Preference Optimization (DPO) fine-tuning on base LVLMs like LLaVA-1.5 (7B/13B) using LoRA. Our extensive experiments demonstrate that M3PO consistently outperforms strong baselines, including SFT, simulated RLHF, vanilla DPO, and RM-DPO, across a comprehensive suite of multimodal instruction following benchmarks (MME-Bench, POPE, IFT, Human Pref. Score).

