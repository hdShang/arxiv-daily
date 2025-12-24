---
layout: default
title: "Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting"
---

# Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14059" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14059v1</a>
  <a href="https://arxiv.org/pdf/2505.14059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14059v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14059v1', 'Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Feng, Shu Wei, Xiang Fei, Wei Shi, Yingdong Han, Lei Liao, Jinghui Lu, Binghong Wu, Qi Liu, Chunhui Lin, Jingqun Tang, Hao Liu, Can Huang

**分类**: cs.CV

**发布日期**: 2025-05-20

**备注**: Accepted to ACL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ByteDance/Dolphin)

---

## 💡 一句话要点

**提出Dolphin以解决文档图像解析中的复杂元素问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档图像解析` `多模态模型` `并行解析` `布局元素` `信息提取` `深度学习`

## 📋 核心要点

1. 现有文档图像解析方法面临整合开销和效率瓶颈，且布局结构易退化。
2. Dolphin模型采用分析-再解析的范式，生成布局元素并进行并行内容解析。
3. Dolphin在多个基准测试中表现优异，达到了最先进的性能，且效率显著提升。

## 📝 摘要（中文）

文档图像解析因文本段落、图形、公式和表格等复杂元素的交织而具有挑战性。现有方法通常依赖于专业模型的组合或直接生成页面内容，面临整合开销、效率瓶颈和布局结构退化等问题。为了解决这些局限性，本文提出了Dolphin，一种新颖的多模态文档图像解析模型，采用分析-再解析的范式。Dolphin在第一阶段生成阅读顺序的布局元素，并在第二阶段通过任务特定的提示进行并行内容解析。通过构建超过3000万样本的大规模数据集，Dolphin在多种页面级和元素级设置上实现了最先进的性能，同时通过轻量架构和并行解析机制确保了高效性。

## 🔬 方法详解

**问题定义**：文档图像解析需要处理复杂的元素交织，现有方法在整合和效率上存在明显不足，导致性能受限。

**核心思路**：Dolphin通过分析-再解析的流程，首先生成布局元素，然后利用这些元素进行并行解析，旨在提高效率和准确性。

**技术框架**：Dolphin的整体架构分为两个主要阶段：第一阶段生成阅读顺序的布局元素，第二阶段利用这些元素和任务特定提示进行内容解析。

**关键创新**：Dolphin的核心创新在于引入异构锚点提示，允许模型在解析过程中并行处理多种元素，显著提升了解析效率和准确性。

**关键设计**：在训练过程中，Dolphin使用了超过3000万样本的数据集，设计了轻量级网络结构，并采用了适应性损失函数以优化解析效果。通过这些设计，Dolphin在多种解析任务中展现了优越的性能。

## 📊 实验亮点

Dolphin在多个基准测试中表现出色，达到了最先进的性能，尤其在页面级和元素级解析任务上，性能提升幅度超过了现有主流方法，展示了其高效的解析能力和准确性。

## 🎯 应用场景

Dolphin模型在文档图像解析领域具有广泛的应用潜力，能够有效处理各种复杂文档格式，如学术论文、财务报表和电子书等。其高效的解析能力将为信息提取、文档自动化处理和智能搜索等应用提供支持，推动相关领域的技术进步和商业价值提升。

## 📄 摘要（原文）

> Document image parsing is challenging due to its complexly intertwined elements such as text paragraphs, figures, formulas, and tables. Current approaches either assemble specialized expert models or directly generate page-level content autoregressively, facing integration overhead, efficiency bottlenecks, and layout structure degradation despite their decent performance. To address these limitations, we present \textit{Dolphin} (\textit{\textbf{Do}cument Image \textbf{P}arsing via \textbf{H}eterogeneous Anchor Prompt\textbf{in}g}), a novel multimodal document image parsing model following an analyze-then-parse paradigm. In the first stage, Dolphin generates a sequence of layout elements in reading order. These heterogeneous elements, serving as anchors and coupled with task-specific prompts, are fed back to Dolphin for parallel content parsing in the second stage. To train Dolphin, we construct a large-scale dataset of over 30 million samples, covering multi-granularity parsing tasks. Through comprehensive evaluations on both prevalent benchmarks and self-constructed ones, Dolphin achieves state-of-the-art performance across diverse page-level and element-level settings, while ensuring superior efficiency through its lightweight architecture and parallel parsing mechanism. The code and pre-trained models are publicly available at https://github.com/ByteDance/Dolphin

