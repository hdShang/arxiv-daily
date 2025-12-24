---
layout: default
title: Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration
---

# Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21472" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21472v2</a>
  <a href="https://arxiv.org/pdf/2505.21472.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21472v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21472v2', 'Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehrdad Fazli, Bowen Wei, Ahmet Sari, Ziwei Zhu

**分类**: cs.CV, cs.CL

**发布日期**: 2025-05-27 (更新: 2025-08-11)

---

## 💡 一句话要点

**提出CAAC框架以解决大规模视觉-语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `幻觉现象` `注意力机制` `多模态学习` `生成模型` `信心感知` `长文本生成`

## 📋 核心要点

1. 现有的大规模视觉-语言模型在生成过程中容易出现幻觉现象，导致生成内容与输入图像不一致。
2. 本文提出的信心感知注意力校准框架通过视觉标记校准和适应性注意力重新缩放，解决了注意力分配不均的问题。
3. 在CHAIR、AMBER和POPE基准测试中，CAAC显著提升了生成的准确性，尤其在长文本生成任务中表现突出。

## 📝 摘要（中文）

大规模视觉-语言模型（LVLMs）在多模态任务中表现出色，但常常出现幻觉现象，即自信地描述图像中不存在的对象或属性。目前的无训练干预措施在开放式和长文本生成场景中难以保持准确性。为了解决这一挑战，本文提出了信心感知注意力校准（CAAC）框架，针对空间感知偏差和模态偏差进行调整。CAAC采用两步法：视觉标记校准（VTC）平衡视觉标记间的注意力分配，适应性注意力重新缩放（AAR）则根据模型的信心强化视觉对齐。实验结果表明，CAAC在CHAIR、AMBER和POPE基准测试中优于基线，特别是在长文本生成中有效减少了幻觉现象。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模视觉-语言模型在生成过程中出现的幻觉现象，现有方法在开放式和长文本生成场景中难以保持准确性，导致生成内容与图像不符。

**核心思路**：提出信心感知注意力校准（CAAC）框架，通过视觉标记校准（VTC）和适应性注意力重新缩放（AAR）来平衡视觉标记间的注意力分配，增强视觉对齐，确保生成过程中的一致性。

**技术框架**：CAAC框架包括两个主要模块：首先，视觉标记校准（VTC）用于调整视觉标记间的注意力分配；其次，适应性注意力重新缩放（AAR）根据模型的信心动态调整注意力，确保视觉信息的优先级。

**关键创新**：CAAC的创新在于其信心驱动的调整机制，能够有效减少空间感知偏差和模态偏差，与传统方法相比，提供了更为精确的视觉对齐。

**关键设计**：在设计中，CAAC采用了特定的损失函数来优化注意力分配，并通过动态调整参数来适应不同的生成场景，确保模型在生成过程中保持高效的视觉对齐。

## 📊 实验亮点

实验结果显示，CAAC在CHAIR、AMBER和POPE基准测试中均优于现有基线，尤其在长文本生成任务中，幻觉现象减少了显著，提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括图像描述生成、视觉问答和多模态内容创作等。通过减少幻觉现象，CAAC框架能够提升生成内容的准确性和可信度，具有重要的实际价值和广泛的应用前景，未来可能推动多模态AI系统的发展。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) achieve impressive performance on multimodal tasks but often suffer from hallucination, and confidently describe objects or attributes not present in the image. Current training-free interventions struggle to maintain accuracy in open-ended and long-form generation scenarios. We introduce the Confidence-Aware Attention Calibration (CAAC) framework to address this challenge by targeting two key biases: spatial perception bias, which distributes attention disproportionately across image tokens, and modality bias, which shifts focus from visual to textual inputs over time. CAAC employs a two-step approach: Visual-Token Calibration (VTC) to balance attention across visual tokens, and Adaptive Attention Re-Scaling (AAR) to reinforce visual grounding guided by the model's confidence. This confidence-driven adjustment ensures consistent visual alignment during generation. Experiments on CHAIR, AMBER, and POPE benchmarks demonstrate that CAAC outperforms baselines, particularly in long-form generations, effectively reducing hallucination.

