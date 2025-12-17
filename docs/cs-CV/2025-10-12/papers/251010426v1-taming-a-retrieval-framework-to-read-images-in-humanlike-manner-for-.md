---
layout: default
title: Taming a Retrieval Framework to Read Images in Humanlike Manner for Augmenting Generation of MLLMs
---

# Taming a Retrieval Framework to Read Images in Humanlike Manner for Augmenting Generation of MLLMs

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10426" target="_blank" class="toolbar-btn">arXiv: 2510.10426v1</a>
    <a href="https://arxiv.org/pdf/2510.10426.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10426v1" 
            onclick="toggleFavorite(this, '2510.10426v1', 'Taming a Retrieval Framework to Read Images in Humanlike Manner for Augmenting Generation of MLLMs')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Suyang Xi, Chenxi Yang, Hong Ding, Yiqing Ni, Catherine C. Liu, Yunhao Liu, Chengqi Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-12

**备注**: 12 pages, 5 figures

---

## 💡 一句话要点

**提出HuLiRAG框架，通过模拟人类视觉处理方式增强多模态大语言模型的生成能力**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉问答` `检索增强生成` `视觉 grounding` `人类视觉模拟`

## 📋 核心要点

1. 现有MLLM在视觉问答中易产生幻觉，原因是文本查询与视觉信息缺乏精确锚定，导致推理不准确。
2. HuLiRAG框架模拟人类视觉处理流程，通过“what-where-reweight”级联实现更精细的视觉信息检索与增强。
3. 实验表明，HuLiRAG能有效提高grounding保真度，减少幻觉，提升多模态问答的事实一致性。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在细粒度视觉问答中表现不佳，常常产生关于物体身份、位置和关系的幻觉，这是因为文本查询没有明确地锚定到视觉参照物上。检索增强生成(RAG)可以缓解一些错误，但它在检索和增强层面都未能与人类的处理方式对齐。具体来说，RAG只关注全局层面的图像信息，缺乏局部细节，并且限制了对细粒度交互的推理。为了克服这个限制，我们提出了Human-Like Retrieval-Augmented Generation (HuLiRAG)，该框架将多模态推理分阶段进行，形成一个“what--where--reweight”的级联。首先通过开放词汇检测将查询锚定到候选参照物(what)，然后使用SAM衍生的掩码在空间上解析，以恢复细粒度精度(where)，最后通过局部和全局对齐之间的权衡来自适应地确定优先级(reweight)。掩码引导的微调进一步将空间证据注入到生成过程中，将grounding从被动偏差转变为对答案公式化的显式约束。大量的实验表明，这种类似人类的级联提高了grounding的保真度和事实一致性，同时减少了幻觉，从而推动多模态问答朝着可信的推理方向发展。

## 🔬 方法详解

**问题定义**：多模态大语言模型在处理细粒度视觉问答时，容易产生幻觉，即生成与图像内容不符的信息。现有检索增强生成方法（RAG）虽然能缓解部分问题，但其检索方式主要关注全局图像信息，忽略了局部细节和细粒度交互，导致无法像人类一样进行精确的视觉推理。

**核心思路**：HuLiRAG的核心思路是模拟人类的视觉处理方式，将多模态推理过程分解为三个阶段：“what-where-reweight”。首先确定图像中可能相关的物体（what），然后精确定位这些物体的位置和边界（where），最后根据局部和全局信息的重要性调整权重，从而更好地理解图像内容。这种分阶段处理的方式旨在提高检索的精度和相关性，减少幻觉的产生。

**技术框架**：HuLiRAG框架包含以下主要模块：1) **开放词汇检测 (What)**：使用开放词汇检测器识别图像中的候选参照物，将文本查询与图像中的物体进行初步关联。2) **空间解析 (Where)**：利用SAM（Segment Anything Model）生成候选参照物的精确掩码，从而获得物体在图像中的精确定位信息。3) **重加权 (Reweight)**：通过权衡局部和全局对齐程度，自适应地调整不同区域的重要性，从而更好地理解图像内容。4) **掩码引导微调**：利用生成的掩码信息对MLLM进行微调，将空间信息显式地融入到生成过程中。

**关键创新**：HuLiRAG的关键创新在于其模拟人类视觉处理的“what-where-reweight”级联框架。与传统的RAG方法相比，HuLiRAG更加关注图像的局部细节和细粒度交互，能够更精确地将文本查询与视觉信息进行关联。此外，掩码引导的微调将空间信息从被动偏差转变为对答案生成的显式约束，进一步提高了生成结果的准确性。

**关键设计**：在“what”阶段，使用开放词汇检测器（如Grounding DINO）来识别图像中的候选参照物。在“where”阶段，利用SAM生成候选参照物的精确掩码。在“reweight”阶段，设计了一种自适应权重调整机制，根据局部和全局对齐程度来调整不同区域的重要性。在掩码引导微调阶段，使用交叉熵损失函数来优化MLLM的生成能力，并使用生成的掩码信息作为额外的输入特征。

## 📊 实验亮点

实验结果表明，HuLiRAG框架在多个视觉问答数据集上取得了显著的性能提升，尤其是在需要细粒度视觉推理的任务上。与传统的RAG方法相比，HuLiRAG能够更有效地减少幻觉，提高grounding的保真度和事实一致性。具体的性能数据在论文中有详细展示，证明了该框架的有效性。

## 🎯 应用场景

HuLiRAG框架可应用于各种需要精确视觉理解的多模态任务，例如视觉问答、图像描述、机器人导航等。该研究有助于提升多模态大语言模型的可信度和可靠性，使其在医疗诊断、自动驾驶、智能客服等领域发挥更大的作用。未来，该框架可以进一步扩展到处理更复杂的视觉场景和任务，例如视频理解和三维场景理解。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) often fail in fine-grained visual question answering, producing hallucinations about object identities, positions, and relations because textual queries are not explicitly anchored to visual referents. Retrieval-augmented generation (RAG) alleviates some errors, but it fails to align with human-like processing at both the retrieval and augmentation levels. Specifically, it focuses only on global-level image information but lacks local detail and limits reasoning about fine-grained interactions. To overcome this limitation, we present Human-Like Retrieval-Augmented Generation (HuLiRAG), a framework that stages multimodal reasoning as a ``what--where--reweight'' cascade. Queries are first anchored to candidate referents via open-vocabulary detection (what), then spatially resolved with SAM-derived masks to recover fine-grained precision (where), and adaptively prioritized through the trade-off between local and global alignment (reweight). Mask-guided fine-tuning further injects spatial evidence into the generation process, transforming grounding from a passive bias into an explicit constraint on answer formulation. Extensive experiments demonstrate that this human-like cascade improves grounding fidelity and factual consistency while reducing hallucinations, advancing multimodal question answering toward trustworthy reasoning.

