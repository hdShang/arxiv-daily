---
layout: default
title: Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization
---

# Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.25616" class="toolbar-btn" target="_blank">📄 arXiv: 2510.25616v1</a>
  <a href="https://arxiv.org/pdf/2510.25616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25616v1" onclick="toggleFavorite(this, '2510.25616v1', 'Don\'t Blind Your VLA: Aligning Visual Representations for OOD Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikita Kachaev, Mikhail Kolosov, Daniil Zelezetsky, Alexey K. Kovalev, Aleksandr I. Panov

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-10-29

**备注**: 13 pages, 6 figures

---

## 💡 一句话要点

**提出视觉表征对齐方法，解决VLA模型OOD泛化能力退化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `表征对齐` `分布外泛化` `动作微调` `视觉表征退化`

## 📋 核心要点

1. VLA模型在动作微调后，其视觉表征会发生退化，导致模型泛化能力下降，这是当前VLA模型面临的关键问题。
2. 论文提出一种视觉表征对齐方法，旨在缓解动作微调对视觉表征的负面影响，从而提升VLA模型的泛化能力。
3. 实验结果表明，该方法能够有效减轻视觉表征退化，并在OOD场景下显著提升VLA模型的性能。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型的日益成功源于预训练视觉-语言模型(VLM)能够赋予智能体可迁移的世界知识和视觉-语言(VL)基础，为具有更广泛泛化能力的动作模型奠定基础。然而，当这些VLM被适配到动作模态时，它们原始的VL表征和知识在多大程度上被保留仍然不清楚。本文对VLA微调期间的表征保留进行了系统研究，表明朴素的动作微调会导致视觉表征的退化。为了描述和衡量这些影响，我们探测了VLA的隐藏表征并分析了注意力图。此外，我们设计了一组有针对性的任务和方法，将VLA模型与其对应的VLM进行对比，从而分离出动作微调引起的VL能力变化。我们进一步评估了一系列对齐视觉表征的策略，并引入了一种简单而有效的方法，可以减轻退化并提高对分布外(OOD)场景的泛化能力。总而言之，我们的分析阐明了动作微调与VL表征退化之间的权衡，并强调了恢复继承的VL能力的实用方法。

## 🔬 方法详解

**问题定义**：VLA模型在进行动作微调时，会不可避免地改变其原有的视觉表征，导致模型在视觉-语言任务上的性能下降，尤其是在分布外(OOD)场景下。现有方法通常忽略了这种表征退化问题，导致VLA模型的泛化能力受限。

**核心思路**：论文的核心思路是通过对齐VLA模型和原始VLM的视觉表征，来缓解动作微调带来的表征退化。具体来说，就是在动作微调过程中，引入额外的约束，使得VLA模型的视觉表征尽可能地接近原始VLM的视觉表征，从而保留VLM的知识和能力。

**技术框架**：论文首先通过实验分析了动作微调对VLA模型视觉表征的影响，包括探测隐藏层表征和分析注意力图。然后，设计了一系列有针对性的任务，用于评估VLA模型在动作微调后的VL能力变化。最后，提出了一种视觉表征对齐方法，并在实验中验证了其有效性。

**关键创新**：论文的关键创新在于发现了动作微调对VLA模型视觉表征的负面影响，并提出了一种简单有效的视觉表征对齐方法来缓解这种影响。与现有方法相比，该方法更加关注视觉表征的保留，从而提升了VLA模型的泛化能力。

**关键设计**：论文提出的视觉表征对齐方法主要通过在动作微调过程中添加额外的损失函数来实现。该损失函数的目标是最小化VLA模型和原始VLM的视觉表征之间的距离。具体的损失函数形式可以是均方误差(MSE)或余弦相似度等。此外，论文还探索了不同的对齐策略，例如只对齐特定层的表征或使用不同的权重来平衡动作微调损失和表征对齐损失。

## 📊 实验亮点

论文通过实验证明，提出的视觉表征对齐方法能够有效减轻动作微调对VLA模型视觉表征的负面影响，并在OOD场景下显著提升VLA模型的性能。具体来说，在多个OOD数据集上，该方法相比基线方法取得了显著的性能提升，验证了其有效性。

## 🎯 应用场景

该研究成果可应用于机器人、自动驾驶、智能助手等领域。通过提升VLA模型的泛化能力，可以使智能体在更复杂的环境中执行任务，并更好地理解人类指令。例如，在机器人领域，可以使机器人更好地理解用户的视觉指令，从而完成更复杂的任务。

## 📄 摘要（原文）

> The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

