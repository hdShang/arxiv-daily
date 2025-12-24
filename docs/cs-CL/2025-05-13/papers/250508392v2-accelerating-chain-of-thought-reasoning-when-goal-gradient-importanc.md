---
layout: default
title: Accelerating Chain-of-Thought Reasoning: When Goal-Gradient Importance Meets Dynamic Skipping
---

# Accelerating Chain-of-Thought Reasoning: When Goal-Gradient Importance Meets Dynamic Skipping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08392" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08392v2</a>
  <a href="https://arxiv.org/pdf/2505.08392.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08392v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08392v2', 'Accelerating Chain-of-Thought Reasoning: When Goal-Gradient Importance Meets Dynamic Skipping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ren Zhuang, Ben Wang, Shuifa Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-13 (更新: 2025-05-17)

---

## 💡 一句话要点

**提出Adaptive GoGI-Skip以解决长文本推理效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式思维` `动态压缩` `目标梯度重要性` `自适应跳过` `推理效率` `自然语言处理` `机器学习`

## 📋 核心要点

1. 现有的链式思维推理方法在处理复杂任务时，推理过程往往冗长且效率低下，导致计算资源浪费。
2. 论文提出的Adaptive GoGI-Skip框架通过引入目标梯度重要性和自适应动态跳过机制，实现了动态的CoT压缩。
3. 实验结果表明，该方法在多个推理基准上显著提升了效率，平均减少了45%的标记数量，并实现了1.6-2.0倍的推理速度提升。

## 📝 摘要（中文）

大型语言模型利用链式思维（CoT）提示进行复杂任务，但其推理过程往往冗长且低效，导致显著的计算成本和延迟。目前的CoT压缩技术通常依赖于通用的重要性指标和静态压缩率，可能会无意中删除功能关键的标记或无法适应不同的推理复杂性。为了解决这些问题，我们提出了Adaptive GoGI-Skip，一个通过监督微调学习动态CoT压缩的新框架。该方法引入了两个协同创新：目标梯度重要性（GoGI），通过测量中间表示对最终答案损失的梯度影响，准确识别功能相关的标记；自适应动态跳过（ADS），根据运行时模型的不确定性动态调节压缩率，同时通过自适应N标记约束确保局部一致性。经过压缩的MATH数据训练，Adaptive GoGI-Skip在多个推理基准上表现出强大的跨领域泛化能力，平均减少CoT标记数量超过45%，推理速度提升1.6-2.0倍，同时保持高推理准确性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在链式思维推理中的冗长和低效问题。现有方法常依赖静态压缩率，可能会删除关键标记或无法适应推理复杂性。

**核心思路**：提出Adaptive GoGI-Skip框架，通过监督微调实现动态CoT压缩。核心在于引入目标梯度重要性（GoGI）和自适应动态跳过（ADS），以提高推理效率和准确性。

**技术框架**：该框架包括两个主要模块：首先是GoGI模块，通过计算中间表示对最终答案损失的影响来识别重要标记；其次是ADS模块，根据模型的不确定性动态调整压缩率，确保推理过程的局部一致性。

**关键创新**：论文的主要创新在于将目标导向的梯度重要性度量与动态、不确定性感知的跳过机制相结合，这是首次在CoT压缩中实现这种统一。

**关键设计**：在设计中，GoGI通过梯度计算来评估标记的重要性，ADS则使用自适应N标记约束来调节压缩率，确保在高压缩率下仍能保持推理的准确性。

## 📊 实验亮点

实验结果显示，Adaptive GoGI-Skip在多个推理基准上表现优异，平均减少CoT标记数量超过45%，推理速度提升1.6-2.0倍，且在高压缩率下仍能保持高准确性，显著超越现有基线，推动了CoT推理效率与准确性的平衡。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和教育技术等。通过提高推理效率，Adaptive GoGI-Skip能够在资源有限的环境中实现更快的响应时间，提升用户体验，未来可能在实时推理和大规模应用中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models leverage Chain-of-Thought (CoT) prompting for complex tasks, but their reasoning traces are often excessively verbose and inefficient, leading to significant computational costs and latency. Current CoT compression techniques typically rely on generic importance metrics and static compression rates, which may inadvertently remove functionally critical tokens or fail to adapt to varying reasoning complexity. To overcome these limitations, we propose Adaptive GoGI-Skip, a novel framework learning dynamic CoT compression via supervised fine-tuning. This approach introduces two synergistic innovations: (1) Goal-Gradient Importance (GoGI), a novel metric accurately identifying functionally relevant tokens by measuring the gradient influence of their intermediate representations on the final answer loss, and (2) Adaptive Dynamic Skipping (ADS), a mechanism dynamically regulating the compression rate based on runtime model uncertainty while ensuring local coherence through an adaptive N-token constraint. To our knowledge, this is the first work unifying a goal-oriented, gradient-based importance metric with dynamic, uncertainty-aware skipping for CoT compression. Trained on compressed MATH data, Adaptive GoGI-Skip demonstrates strong cross-domain generalization across diverse reasoning benchmarks including AIME, GPQA, and GSM8K. It achieves substantial efficiency gains - reducing CoT token counts by over 45% on average and delivering 1.6-2.0 times inference speedups - while maintaining high reasoning accuracy. Notably, it significantly outperforms existing baselines by preserving accuracy even at high effective compression rates, advancing the state of the art in the CoT reasoning efficiency-accuracy trade-off.

