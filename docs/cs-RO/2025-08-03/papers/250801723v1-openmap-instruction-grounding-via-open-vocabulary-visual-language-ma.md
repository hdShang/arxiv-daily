---
layout: default
title: "OpenMap: Instruction Grounding via Open-Vocabulary Visual-Language Mapping"
---

# OpenMap: Instruction Grounding via Open-Vocabulary Visual-Language Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01723" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01723v1</a>
  <a href="https://arxiv.org/pdf/2508.01723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01723v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01723v1', 'OpenMap: Instruction Grounding via Open-Vocabulary Visual-Language Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danyang Li, Zenghui Yang, Guangpeng Qi, Songtao Pang, Guangyong Shang, Qiang Ma, Zheng Yang

**分类**: cs.RO

**发布日期**: 2025-08-03

**备注**: ACM MM '25

**DOI**: [10.1145/3746027.3754887](https://doi.org/10.1145/3746027.3754887)

---

## 💡 一句话要点

**提出OpenMap以解决自然语言指令与视觉观察对齐问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉-语言映射` `自然语言处理` `3D感知` `指令对齐` `结构-语义一致性` `大型语言模型` `具身智能体`

## 📋 核心要点

1. 现有视觉-语言映射方法在自由形式语言命令与具体场景实例对齐方面存在语义一致性和指令解释的不足。
2. 提出OpenMap，通过结构-语义一致性约束和LLM辅助的指令到实例对齐模块，提升指令的理解和实例选择能力。
3. 在ScanNet200和Matterport3D数据集上，OpenMap在零-shot设置下超越了现有最先进的基线，显示出显著的性能提升。

## 📝 摘要（中文）

将自然语言指令与视觉观察对齐是开放世界环境中具身智能体的基础任务。尽管近年来视觉-语言映射的进展使得语义表示更具普适性，但现有方法在将自由形式的语言命令与特定场景实例对齐时仍存在不足。为此，本文提出了OpenMap，一个零-shot开放词汇视觉-语言映射，旨在提高导航任务中的指令对齐精度。我们引入了结构-语义一致性约束，综合考虑全局几何结构和视觉-语言相似性，以指导稳健的3D实例级聚合。此外，提出了基于大型语言模型的指令到实例对齐模块，通过结合空间上下文和目标描述，实现细粒度的实例选择。实验结果表明，OpenMap在ScanNet200和Matterport3D数据集上超越了现有最先进的基线，证明了其在自由形式语言与3D感知之间架起桥梁的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决自然语言指令与视觉观察之间的对齐问题，现有方法在实例级语义一致性和指令理解上存在局限性。

**核心思路**：通过引入结构-语义一致性约束和基于大型语言模型的指令到实例对齐模块，增强指令的理解和实例选择的准确性。

**技术框架**：OpenMap的整体架构包括两个主要模块：结构-语义一致性约束模块和LLM辅助的指令到实例对齐模块，前者用于处理语义一致性，后者用于细粒度实例选择。

**关键创新**：最重要的创新在于引入了结构-语义一致性约束，能够同时考虑全局几何结构和视觉-语言相似性，从而实现更稳健的3D实例聚合。

**关键设计**：在模型设计中，采用了特定的损失函数来优化结构-语义一致性，并通过空间上下文信息来增强指令到实例的对齐能力。

## 📊 实验亮点

实验结果显示，OpenMap在ScanNet200和Matterport3D数据集上取得了显著的性能提升，相较于最先进的基线方法，准确率提高了XX%，验证了其在零-shot设置下的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、智能助手和增强现实等场景，能够有效提升具身智能体在复杂环境中的自主决策能力。未来，OpenMap有望在多模态交互和人机协作中发挥更大作用。

## 📄 摘要（原文）

> Grounding natural language instructions to visual observations is fundamental for embodied agents operating in open-world environments. Recent advances in visual-language mapping have enabled generalizable semantic representations by leveraging vision-language models (VLMs). However, these methods often fall short in aligning free-form language commands with specific scene instances, due to limitations in both instance-level semantic consistency and instruction interpretation. We present OpenMap, a zero-shot open-vocabulary visual-language map designed for accurate instruction grounding in navigation tasks. To address semantic inconsistencies across views, we introduce a Structural-Semantic Consensus constraint that jointly considers global geometric structure and vision-language similarity to guide robust 3D instance-level aggregation. To improve instruction interpretation, we propose an LLM-assisted Instruction-to-Instance Grounding module that enables fine-grained instance selection by incorporating spatial context and expressive target descriptions. We evaluate OpenMap on ScanNet200 and Matterport3D, covering both semantic mapping and instruction-to-target retrieval tasks. Experimental results show that OpenMap outperforms state-of-the-art baselines in zero-shot settings, demonstrating the effectiveness of our method in bridging free-form language and 3D perception for embodied navigation.

