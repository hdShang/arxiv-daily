---
layout: default
title: BrepLLM: Native Boundary Representation Understanding with Large Language Models
---

# BrepLLM: Native Boundary Representation Understanding with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16413" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16413v1</a>
  <a href="https://arxiv.org/pdf/2512.16413.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16413v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16413v1', 'BrepLLM: Native Boundary Representation Understanding with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liyuan Deng, Hao Guo, Yunpeng Bai, Yongkang Dai, Huaxi Huang, Yilei Shi

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**BrepLLM：提出一种原生边界表示理解的大语言模型框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `边界表示` `大语言模型` `跨模态学习` `3D几何` `拓扑信息`

## 📋 核心要点

1. 现有的大语言模型难以直接处理包含复杂几何和拓扑信息的3D Brep模型。
2. BrepLLM通过两阶段训练，将Brep数据转换为LLM可理解的token序列，实现跨模态对齐。
3. 实验结果表明，BrepLLM在3D对象分类和描述任务上达到了当前最优水平。

## 📝 摘要（中文）

当前基于token序列的大语言模型(LLMs)不适合直接处理包含复杂几何和拓扑信息的3D边界表示(Brep)模型。我们提出了BrepLLM，这是第一个使LLMs能够解析和推理原始Brep数据的框架，弥合了结构化3D几何和自然语言之间的模态差距。BrepLLM采用两阶段训练流程：跨模态对齐预训练和多阶段LLM微调。在第一阶段，自适应UV采样策略将Brep转换为具有几何和拓扑信息的图表示。然后，我们设计了一个分层BrepEncoder来提取几何（即面和边）和拓扑的特征，生成单个全局token和一系列节点token。然后，我们通过对比学习将全局token与来自冻结的CLIP文本编码器(ViT-L/14)的文本嵌入对齐。在第二阶段，我们将预训练的BrepEncoder集成到LLM中。然后，我们使用三阶段渐进式训练策略对齐其节点token序列：(1)训练一个基于MLP的语义映射，将Brep表示映射到具有2D-LLM先验的2D。(2)执行LLM的微调。(3)设计一个混合查询专家(MQE)来增强几何多样性建模。我们还构建了Brep2Text数据集，包含269,444个Brep-文本问答对。实验表明，BrepLLM在3D对象分类和字幕任务上取得了最先进(SOTA)的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型(LLM)无法直接理解和处理3D边界表示(Brep)模型的问题。现有的LLM主要处理文本序列，而Brep模型包含复杂的几何和拓扑信息，直接输入LLM会导致信息丢失或无法有效利用。因此，如何将Brep数据转换为LLM能够理解的形式，并使其具备对3D几何信息的推理能力是本论文要解决的核心问题。

**核心思路**：论文的核心思路是通过一个两阶段的训练流程，将Brep数据转换为LLM可以处理的token序列，并利用对比学习和多阶段微调，使LLM能够理解和推理Brep数据中的几何和拓扑信息。这种方法的核心在于设计一个有效的BrepEncoder，能够提取Brep数据中的关键特征，并将其映射到与文本嵌入空间对齐的token表示。

**技术框架**：BrepLLM的整体框架包含两个主要阶段：跨模态对齐预训练和多阶段LLM微调。在跨模态对齐预训练阶段，首先使用自适应UV采样策略将Brep模型转换为图表示，然后通过分层BrepEncoder提取几何和拓扑特征，生成全局token和节点token序列。接着，通过对比学习将全局token与CLIP文本编码器的文本嵌入对齐。在多阶段LLM微调阶段，首先训练一个MLP将Brep表示映射到2D空间，然后对LLM进行微调，最后使用混合查询专家(MQE)增强几何多样性建模。

**关键创新**：论文的关键创新在于提出了BrepLLM框架，这是第一个能够使LLM直接解析和推理原始Brep数据的框架。该框架通过设计自适应UV采样策略和分层BrepEncoder，有效地提取了Brep数据中的几何和拓扑信息，并将其转换为LLM可以处理的token表示。此外，论文还提出了一个多阶段的微调策略，有效地提升了LLM对Brep数据的理解和推理能力。

**关键设计**：在跨模态对齐预训练阶段，使用了对比学习损失函数来对齐BrepEncoder提取的全局token和CLIP文本编码器的文本嵌入。在多阶段LLM微调阶段，设计了一个基于MLP的语义映射，将Brep表示映射到2D空间，并使用2D-LLM的先验知识进行指导。此外，还设计了一个混合查询专家(MQE)来增强几何多样性建模，提升了LLM对不同几何形状的适应能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16413v1/images/zhanshitu1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16413v1/images/framework.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16413v1/images/BrepEncoder.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

BrepLLM在3D对象分类和描述任务上取得了显著的性能提升，达到了当前最优水平。具体来说，在Brep2Text数据集上，BrepLLM在3D对象分类任务上超越了现有方法，并在3D对象描述任务上生成了更准确、更丰富的描述文本。这些实验结果表明，BrepLLM能够有效地理解和推理Brep数据中的几何和拓扑信息。

## 🎯 应用场景

BrepLLM具有广泛的应用前景，例如在CAD/CAM领域，可以用于自动化设计、零件识别和智能制造。在机器人领域，可以用于3D场景理解、物体抓取和导航。此外，该技术还可以应用于建筑设计、游戏开发和虚拟现实等领域，实现更智能、更高效的3D内容生成和交互。

## 📄 摘要（原文）

> Current token-sequence-based Large Language Models (LLMs) are not well-suited for directly processing 3D Boundary Representation (Brep) models that contain complex geometric and topological information. We propose BrepLLM, the first framework that enables LLMs to parse and reason over raw Brep data, bridging the modality gap between structured 3D geometry and natural language. BrepLLM employs a two-stage training pipeline: Cross-modal Alignment Pre-training and Multi-stage LLM Fine-tuning. In the first stage, an adaptive UV sampling strategy converts Breps into graphs representation with geometric and topological information. We then design a hierarchical BrepEncoder to extract features from geometry (i.e., faces and edges) and topology, producing both a single global token and a sequence of node tokens. Then we align the global token with text embeddings from a frozen CLIP text encoder (ViT-L/14) via contrastive learning. In the second stage, we integrate the pretrained BrepEncoder into an LLM. We then align its sequence of node tokens using a three-stage progressive training strategy: (1) training an MLP-based semantic mapping from Brep representation to 2D with 2D-LLM priors. (2) performing fine-tuning of the LLM. (3) designing a Mixture-of-Query Experts (MQE) to enhance geometric diversity modeling. We also construct Brep2Text, a dataset comprising 269,444 Brep-text question-answer pairs. Experiments show that BrepLLM achieves state-of-the-art (SOTA) results on 3D object classification and captioning tasks.

