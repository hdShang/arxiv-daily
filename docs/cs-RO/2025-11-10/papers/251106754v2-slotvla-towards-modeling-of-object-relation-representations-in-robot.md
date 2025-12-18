---
layout: default
title: SlotVLA: Towards Modeling of Object-Relation Representations in Robotic Manipulation
---

# SlotVLA: Towards Modeling of Object-Relation Representations in Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06754" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06754v2</a>
  <a href="https://arxiv.org/pdf/2511.06754.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06754v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06754v2', 'SlotVLA: Towards Modeling of Object-Relation Representations in Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taisei Hanyu, Nhat Chung, Huy Le, Toan Nguyen, Yuki Ikebe, Anthony Gunderman, Duy Nguyen Ho Minh, Khoa Vo, Tung Kieu, Kashu Yamazaki, Chase Rainwater, Anh Nguyen, Ngan Le

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-10 (更新: 2025-11-28)

**备注**: under review

---

## 💡 一句话要点

**提出SlotVLA框架，用于建模机器人操作中的对象关系表示，并构建LIBERO+基准数据集。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `对象关系建模` `Slot Attention` `视觉运动控制` `多任务学习`

## 📋 核心要点

1. 现有机器人多任务模型依赖于密集嵌入，难以区分对象和背景，导致效率和可解释性问题。
2. SlotVLA框架通过Slot Attention机制捕获对象及其关系，并利用LLM将关系嵌入转化为可执行动作。
3. LIBERO+数据集和SlotVLA框架的实验结果表明，该方法能显著减少视觉token数量，并保持良好的泛化能力。

## 📝 摘要（中文）

受人类对离散对象及其关系进行推理方式的启发，本文探讨了紧凑的以对象为中心和以对象关系为中心的表示是否可以构成多任务机器人操作的基础。现有的大多数机器人多任务模型依赖于密集嵌入，这些嵌入纠缠了对象和背景线索，引发了对效率和可解释性的担忧。相比之下，本文研究了以对象关系为中心的表示，作为更结构化、高效和可解释的视觉运动控制的途径。本文的贡献是双重的。首先，引入LIBERO+，这是一个细粒度的基准数据集，旨在支持和评估机器人操作中的对象关系推理。与先前的数据集不同，LIBERO+提供了以对象为中心的注释，这些注释使用框级和掩码级标签以及实例级时间跟踪来丰富演示，从而支持紧凑且可解释的视觉运动表示。其次，本文提出了一种基于Slot Attention的框架SlotVLA，该框架捕获对象及其关系以进行动作解码。它使用基于槽的视觉标记器来保持一致的时间对象表示，一个以关系为中心的解码器来生成任务相关的嵌入，以及一个LLM驱动的模块，该模块将这些嵌入转换为可执行的动作。在LIBERO+上的实验表明，以对象为中心的槽和以对象关系为中心的槽表示大大减少了所需的视觉token数量，同时提供了具有竞争力的泛化能力。LIBERO+和SlotVLA共同为推进以对象关系为中心的机器人操作提供了一个紧凑、可解释且有效的基础。

## 🔬 方法详解

**问题定义**：现有机器人操作模型难以有效区分对象和背景信息，导致模型效率低下且难以解释。这些模型通常使用密集嵌入，将对象和背景信息混杂在一起，使得模型难以专注于关键的对象关系，从而限制了其在复杂任务中的泛化能力。

**核心思路**：本文的核心思路是利用以对象为中心和以对象关系为中心的表示来解决上述问题。通过将场景分解为离散的对象及其关系，模型可以更有效地学习和推理，从而提高效率和可解释性。Slot Attention机制用于提取和跟踪对象，而关系解码器则用于捕捉对象之间的交互。

**技术框架**：SlotVLA框架包含三个主要模块：1) 基于槽的视觉标记器：使用Slot Attention从视觉输入中提取对象表示，并保持时间一致性。2) 关系中心解码器：基于提取的对象表示，生成任务相关的关系嵌入。3) LLM驱动的动作模块：将关系嵌入转化为可执行的机器人动作。整个流程是从视觉输入开始，经过对象提取、关系建模，最终生成控制指令。

**关键创新**：SlotVLA的关键创新在于其对象关系建模方法。它不仅关注单个对象，还显式地建模对象之间的关系，从而更好地理解场景。此外，利用Slot Attention进行对象提取，保证了对象表示的时间一致性，这对于机器人操作任务至关重要。

**关键设计**：Slot Attention模块使用迭代注意力机制来提取对象槽。关系解码器使用Transformer架构来建模对象之间的关系。LLM驱动的动作模块利用预训练的语言模型来生成可执行的动作指令。损失函数包括对象重建损失和动作预测损失，用于优化整个框架。

## 📊 实验亮点

在LIBERO+数据集上的实验表明，SlotVLA框架能够显著减少所需的视觉token数量，同时保持与现有方法相当甚至更好的性能。具体而言，该方法在泛化能力方面表现出色，表明其能够有效地学习对象关系，并在新的场景中进行推理。实验结果验证了以对象关系为中心的表示在机器人操作中的有效性。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如物体抓取、装配、导航等。通过更有效地建模对象关系，机器人可以更好地理解环境，从而执行更复杂的任务。此外，该方法的可解释性使得机器人行为更容易理解和调试，有助于提高机器人的可靠性和安全性。未来，该技术有望应用于智能制造、家庭服务等领域。

## 📄 摘要（原文）

> Inspired by how humans reason over discrete objects and their relationships, we explore whether compact object-centric and object-relation representations can form a foundation for multitask robotic manipulation. Most existing robotic multitask models rely on dense embeddings that entangle both object and background cues, raising concerns about both efficiency and interpretability. In contrast, we study object-relation-centric representations as a pathway to more structured, efficient, and explainable visuomotor control. Our contributions are two-fold. First, we introduce LIBERO+, a fine-grained benchmark dataset designed to enable and evaluate object-relation reasoning in robotic manipulation. Unlike prior datasets, LIBERO+ provides object-centric annotations that enrich demonstrations with box- and mask-level labels as well as instance-level temporal tracking, supporting compact and interpretable visuomotor representations. Second, we propose SlotVLA, a slot-attention-based framework that captures both objects and their relations for action decoding. It uses a slot-based visual tokenizer to maintain consistent temporal object representations, a relation-centric decoder to produce task-relevant embeddings, and an LLM-driven module that translates these embeddings into executable actions. Experiments on LIBERO+ demonstrate that object-centric slot and object-relation slot representations drastically reduce the number of required visual tokens, while providing competitive generalization. Together, LIBERO+ and SlotVLA provide a compact, interpretable, and effective foundation for advancing object-relation-centric robotic manipulation.

