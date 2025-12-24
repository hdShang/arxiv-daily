---
layout: default
title: "Manager: Aggregating Insights from Unimodal Experts in Two-Tower VLMs and MLLMs"
---

# Manager: Aggregating Insights from Unimodal Experts in Two-Tower VLMs and MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11515" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11515v1</a>
  <a href="https://arxiv.org/pdf/2506.11515.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11515v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11515v1', 'Manager: Aggregating Insights from Unimodal Experts in Two-Tower VLMs and MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Xu, Libo Qin, Wanxiang Che, Min-Yen Kan

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-06-13

**备注**: Accepted by IEEE Transactions on Circuits and Systems for Video Technology (TCSVT). June 2025. DOI: https://doi.org/10.1109/TCSVT.2025.3578266

**DOI**: [10.1109/TCSVT.2025.3578266](https://doi.org/10.1109/TCSVT.2025.3578266)

**🔗 代码/项目**: [GITHUB](https://github.com/LooperXX/ManagerTower)

---

## 💡 一句话要点

**提出Manager插件以解决两塔VLMs和MLLMs中的单模态专家聚合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `多模态融合` `单模态专家` `跨模态对齐` `深度学习`

## 📋 核心要点

1. 现有的两塔VLMs方法在单模态表示的利用和语义知识的灵活性方面存在明显不足，限制了其性能。
2. 本文提出Manager插件，通过在每个跨模态层引入管理器，适应性地聚合不同层次的单模态专家见解，提升视觉-语言对齐效果。
3. 实验结果表明，ManagerTower在四个下游VL任务中超越了强基线，并且在20个数据集上显著提升了LLaVA-OV的零-shot性能。

## 📝 摘要（中文）

两塔视觉-语言模型（VLMs）在多种下游视觉-语言任务中表现出色。然而，现有的BridgeTower方法在单模态表示的逐层利用、不同层次语义知识的灵活利用以及仅限于低分辨率数据集的评估方面存在不足。为此，本文提出了Manager，一个轻量、高效且有效的插件，能够自适应地聚合来自不同层次的预训练单模态专家的见解，从而促进更全面的视觉-语言对齐与融合。通过引入ManagerTower，本文在多个下游任务中超越了之前的强基线，并在最新的多模态大语言模型（MLLM）架构中也取得了显著的零-shot性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有两塔VLMs在单模态表示利用和语义知识灵活性方面的不足，尤其是BridgeTower方法的局限性。

**核心思路**：提出Manager插件，通过在跨模态层引入管理器，聚合不同层次的单模态专家见解，以实现更全面的视觉-语言对齐与融合。

**技术框架**：整体架构包括ManagerTower，作为一种新型的VLM，在每个跨模态层中引入管理器模块，能够根据任务需求动态调整信息流。

**关键创新**：Manager插件的引入是本文的核心创新，它通过多层次的单模态专家聚合，显著提升了模型的性能，克服了传统方法的局限。

**关键设计**：在设计中，Manager插件的参数设置经过精心调整，损失函数结合了多模态对齐的需求，网络结构则采用了灵活的跨模态层管理机制。

## 📊 实验亮点

实验结果显示，ManagerTower在四个下游VL任务中超越了之前的强基线，且在20个数据集上，LLaVA-OV-Manager的零-shot性能显著提升，尤其在不同类别的能力、图像和分辨率上均表现出色。

## 🎯 应用场景

该研究的潜在应用场景包括图像描述生成、视觉问答、跨模态检索等领域，能够为多模态交互系统提供更强的支持。未来，该方法有望推动更复杂的视觉-语言任务的发展，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Two-Tower Vision--Language Models (VLMs) have demonstrated strong performance across various downstream VL tasks. While BridgeTower further enhances performance by building bridges between encoders, it \textit{(i)} suffers from ineffective layer-by-layer utilization of unimodal representations, \textit{(ii)} restricts the flexible exploitation of different levels of unimodal semantic knowledge, and \textit{(iii)} is limited to the evaluation on traditional low-resolution datasets only with the Two-Tower VLM architecture. In this work, we propose Manager, a lightweight, efficient and effective plugin that adaptively aggregates insights from different levels of pre-trained unimodal experts to facilitate more comprehensive VL alignment and fusion. First, under the Two-Tower VLM architecture, we introduce ManagerTower, a novel VLM that introduces the manager in each cross-modal layer. Whether with or without VL pre-training, ManagerTower outperforms previous strong baselines and achieves superior performance on 4 downstream VL tasks. Moreover, we extend our exploration to the latest Multimodal Large Language Model (MLLM) architecture. We demonstrate that LLaVA-OV-Manager significantly boosts the zero-shot performance of LLaVA-OV across different categories of capabilities, images, and resolutions on 20 downstream datasets, whether the multi-grid algorithm is enabled or not. In-depth analysis reveals that both our manager and the multi-grid algorithm can be viewed as a plugin that improves the visual representation by capturing more diverse visual details from two orthogonal perspectives (depth and width). Their synergy can mitigate the semantic ambiguity caused by the multi-grid algorithm and further improve performance. Code and models are available at https://github.com/LooperXX/ManagerTower.

