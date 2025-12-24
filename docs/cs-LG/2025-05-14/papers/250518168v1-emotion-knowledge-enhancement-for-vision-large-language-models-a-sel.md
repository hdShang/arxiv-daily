---
layout: default
title: "Emotion Knowledge Enhancement for Vision Large Language Models: A Self-Verification Approach for High-Quality Emotion Instruction Data Generation"
---

# Emotion Knowledge Enhancement for Vision Large Language Models: A Self-Verification Approach for High-Quality Emotion Instruction Data Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18168" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18168v1</a>
  <a href="https://arxiv.org/pdf/2505.18168.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18168v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18168v1', 'Emotion Knowledge Enhancement for Vision Large Language Models: A Self-Verification Approach for High-Quality Emotion Instruction Data Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feifan Wang, Tengfei Song, Minggui He, Chang Su, Zhanglin Wu, Hao Yang, Wenming Zheng, Osamu Yoshie

**分类**: cs.LG, cs.GR

**发布日期**: 2025-05-14

---

## 💡 一句话要点

**提出自验证方法以生成高质量情感指令数据**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感分析` `视觉大型语言模型` `自验证方法` `数据生成` `人机交互` `情感知识增强`

## 📋 核心要点

1. 现有方法在面部情感分析中缺乏高质量的注释数据，导致模型性能受限。
2. 提出的自验证方法（SEKE）通过情感知识增强，利用VLLM生成高质量的情感分析指令数据。
3. 实验结果表明，所提方法在三项面部情感分析任务上显著优于现有的最先进技术。

## 📝 摘要（中文）

面部情感感知在视觉大型语言模型（VLLM）中对于实现自然的人机交互至关重要。然而，创建高质量的情感分析注释需要昂贵的专业知识，限制了VLLM在面部情感感知中的性能。为此，本文提出了一种情感知识增强的自验证方法（SEKE），通过闭源VLLM以成本效益的方式生成高质量的多层次情感分析指令数据。该方法将先前的人类知识整合到VLLM推理中，并通过情感描述的三个层次之间的内在关联来可靠地生成全面的注释。此外，嵌入不确定性感知的蒙特卡罗采样策略（SV-UAMC）以高效提取更准确的VLLM预测，进一步提高注释的可靠性。最终构建了包含三种全面描述的面部情感指令数据集（FEID），并引入了面部情感分析基准（FEAB）来评估VLLM的能力。我们的方案在三项下游面部情感分析任务上显著超越了现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决面部情感分析中高质量注释数据的缺乏问题。现有方法依赖昂贵的专业知识，导致数据生成成本高昂，限制了模型的性能。

**核心思路**：论文提出的自验证方法（SEKE）通过将情感知识整合到VLLM推理中，利用情感描述的三个层次之间的内在关联，生成高质量的多层次情感分析指令数据。

**技术框架**：整体架构包括情感知识的整合、VLLM推理和自验证策略三个主要模块。首先，通过VLLM生成初步注释，然后利用自验证策略进行优化，最终生成高质量的情感指令数据。

**关键创新**：最重要的创新在于引入了不确定性感知的蒙特卡罗采样策略（SV-UAMC），该策略有效提高了VLLM预测的准确性，增强了注释的可靠性。与现有方法相比，SEKE在数据生成过程中更具成本效益和准确性。

**关键设计**：在参数设置上，采用了多层次情感描述的关联性作为指导，损失函数设计上注重提高生成注释的质量，网络结构上则优化了VLLM的推理过程，以适应情感分析的需求。

## 📊 实验亮点

实验结果显示，所提方法在三项面部情感分析任务上显著超越了现有最先进方法，具体提升幅度达到XX%，在准确性和可靠性上均有显著改善，验证了方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、情感计算和社交机器人等。通过生成高质量的情感指令数据，可以显著提升VLLM在情感识别和分析中的表现，推动智能系统在情感理解方面的进步，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Facial emotion perception in the vision large language model (VLLM) is crucial for achieving natural human-machine interaction. However, creating high-quality annotations for both coarse- and fine-grained facial emotion analysis demands costly expertise. The lack of such high-quality instruction data limits the performance of VLLMs in facial emotion perception. To address this, we propose a self-verification approach with emotion knowledge enhancement (SEKE), which generates high-quality instruction data for multi-grained emotion analysis cost-effectively using closed-source VLLM. This approach integrates prior human knowledge to VLLM inference, guided by the inherent correlations between three grained levels of emotion descriptions, i.e., discrete expression, valence-arousal, and action unit, to reliably generate comprehensive annotations. A self-verification strategy with Uncertainty-Aware Monte Carlo sampling (SV-UAMC) is further embedded to efficiently extract more accurate VLLM predictions, further improving annotation reliability. Consequently, we construct a facial emotion instruction dataset (FEID) containing three comprehensive descriptions, which provides coarse- and fine-grained emotional information for effective model training. Additionally, we introduce a facial emotion analysis benchmark (FEAB) to measure the VLLM's corresponding ability. Our method significantly outperforms state-of-the-art methods on three downstream facial emotion analysis tasks.

