---
layout: default
title: "ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Long Video Understanding"
---

# ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Long Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21496" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21496v2</a>
  <a href="https://arxiv.org/pdf/2508.21496.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21496v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21496v2', 'ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Long Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Lu, Jiahao Wang, Yaolun Zhang, Ruohui Wang, Xuanyu Zheng, Yepeng Tang, Dahua Lin, Lewei Lu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-29 (更新: 2025-09-02)

---

## 💡 一句话要点

**提出ELV-Halluc以解决长视频理解中的语义聚合幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `语义聚合幻觉` `多模态大语言模型` `数据集构建` `模型训练` `性能评估` `缓解策略`

## 📋 核心要点

1. 现有视频幻觉基准主要集中在短视频，未能深入探讨长视频中的语义聚合幻觉问题。
2. 提出ELV-Halluc基准，专注于长视频中的语义聚合幻觉，系统性分析其成因及影响。
3. 实验结果表明，SAH在语义复杂性增加时显著上升，并通过新策略实现了27.7%的SAH比率降低。

## 📝 摘要（中文）

视频多模态大语言模型（Video-MLLMs）在视频理解方面取得了显著进展，但仍然容易产生与视频输入不一致或无关的幻觉内容。现有的视频幻觉基准主要集中在短视频上，过于简化了幻觉产生的原因。本文提出了ELV-Halluc，这是第一个专注于长视频幻觉的基准，系统性地研究了语义聚合幻觉（SAH）。实验确认SAH的存在，并显示其在语义复杂性增加时更为明显。我们还探讨了缓解SAH的潜在方法，并通过数据集的构建实现了27.7%的SAH比率降低。

## 🔬 方法详解

**问题定义**：本文旨在解决长视频理解中出现的语义聚合幻觉（SAH）问题。现有方法主要关注短视频，未能充分考虑长视频中语义复杂性带来的挑战。

**核心思路**：通过引入ELV-Halluc基准，系统性地分析SAH的成因，并提出缓解策略，以提高长视频理解的准确性。

**技术框架**：整体架构包括数据集构建、SAH识别与分析、以及缓解策略的实施。主要模块包括数据对比、模型训练和性能评估。

**关键创新**：最重要的创新在于首次定义并系统性研究了SAH，揭示其在长视频中的重要性，并提出了有效的缓解策略。

**关键设计**：采用位置编码策略和DPO策略来增强模型的语义区分能力，设计了包含8K对抗数据对的数据集，以支持实验和评估。实验结果显示，SAH比率显著降低。

## 📊 实验亮点

实验结果显示，SAH在语义复杂性增加时显著上升，采用新策略后，SAH比率降低了27.7%。此外，模型在快速变化语义场景下的表现得到改善，验证了提出方法的有效性。

## 🎯 应用场景

该研究在长视频理解领域具有广泛的应用潜力，能够提升视频分析、自动摘要生成和多模态检索等任务的性能。通过解决SAH问题，未来可在智能监控、视频内容推荐和人机交互等领域发挥重要作用。

## 📄 摘要（原文）

> Video multimodal large language models (Video-MLLMs) have achieved remarkable progress in video understanding. However, they remain vulnerable to hallucination-producing content inconsistent with or unrelated to video inputs. Previous video hallucination benchmarks primarily focus on short-videos. They attribute hallucinations to factors such as strong language priors, missing frames, or vision-language biases introduced by the visual encoder. While these causes indeed account for most hallucinations in short videos, they still oversimplify the cause of hallucinations. Sometimes, models generate incorrect outputs but with correct frame-level semantics. We refer to this type of hallucination as Semantic Aggregation Hallucination (SAH), which arises during the process of aggregating frame-level semantics into event-level semantic groups. Given that SAH becomes particularly critical in long videos due to increased semantic complexity across multiple events, it is essential to separate and thoroughly investigate the causes of this type of hallucination. To address the above issues, we introduce ELV-Halluc, the first benchmark dedicated to long-video hallucination, enabling a systematic investigation of SAH. Our experiments confirm the existence of SAH and show that it increases with semantic complexity. Additionally, we find that models are more prone to SAH on rapidly changing semantics. Moreover, we discuss potential approaches to mitigate SAH. We demonstrate that positional encoding strategy contributes to alleviating SAH, and further adopt DPO strategy to enhance the model's ability to distinguish semantics within and across events. To support this, we curate a dataset of 8K adversarial data pairs and achieve improvements on both ELV-Halluc and Video-MME, including a substantial 27.7% reduction in SAH ratio.

