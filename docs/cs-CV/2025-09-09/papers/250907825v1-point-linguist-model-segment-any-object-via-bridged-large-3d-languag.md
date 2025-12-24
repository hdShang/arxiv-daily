---
layout: default
title: "Point Linguist Model: Segment Any Object via Bridged Large 3D-Language Model"
---

# Point Linguist Model: Segment Any Object via Bridged Large 3D-Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07825" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07825v1</a>
  <a href="https://arxiv.org/pdf/2509.07825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07825v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07825v1', 'Point Linguist Model: Segment Any Object via Bridged Large 3D-Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoxu Huang, Mingqi Gao, Jungong Han

**分类**: cs.CV

**发布日期**: 2025-09-09

**备注**: Preprint

---

## 💡 一句话要点

**提出Point Linguist Model，通过桥接3D-语言大模型实现任意物体分割**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D物体分割` `大型语言模型` `点云处理` `语义理解` `几何推理`

## 📋 核心要点

1. 现有方法在3D物体分割中，LLM与3D点云的表示不对齐，导致输入时语义信息弱化，输出时精度损失。
2. PLM通过Object-centric Discriminative Representation (OcDR)学习物体中心tokens，并使用Geometric Reactivation Decoder (GRD)融合几何信息。
3. 实验结果表明，PLM在多个数据集和任务上均取得了显著的性能提升，证明了其有效性。

## 📝 摘要（中文）

本文提出Point Linguist Model (PLM)，旨在解决3D物体分割中大型语言模型(LLM)与3D点云之间表示不对齐的问题。现有方法受限于输入和输出阶段的不对齐：输入时，密集的点云块需要大量预对齐，削弱了物体级别的语义并混淆了相似的干扰物；输出时，预测仅依赖于密集特征，缺乏明确的几何线索，导致精细精度损失。PLM通过引入Object-centric Discriminative Representation (OcDR)学习以物体为中心的tokens，捕捉目标语义和场景关系，缓解不对齐，增强对干扰物的鲁棒性，并促进LLM中的语义级别推理。此外，Geometric Reactivation Decoder (GRD)结合OcDR tokens和相应的密集特征预测mask，保留了全面的密集特征。实验表明，PLM在ScanNetv2上实现了+7.3 mIoU的提升，在Multi3DRefer上实现了+6.0 mIoU的提升，并在7个基准测试中取得了持续的收益，证明了其在鲁棒3D理解方面的有效性。

## 🔬 方法详解

**问题定义**：现有3D物体分割方法在利用大型语言模型（LLM）时，面临LLM处理高层语义token与3D点云仅包含密集几何结构之间的表示不对齐问题。这种不对齐限制了输入和输出两个阶段。在输入阶段，需要对密集的点云块进行预对齐，这削弱了物体级别的语义信息，并容易混淆相似的干扰物。在输出阶段，预测仅仅依赖于密集特征，缺乏明确的几何线索，导致分割精度下降。

**核心思路**：本文的核心思路是弥合LLM和3D点云之间的表示差距，无需大规模的3D-文本或3D-图像预对齐。通过学习以物体为中心的判别性表示（Object-centric Discriminative Representation, OcDR），使得3D点云能够更好地表达物体级别的语义信息，从而与LLM的token对齐。同时，利用几何重激活解码器（Geometric Reactivation Decoder, GRD）将LLM推理出的几何信息与原始的密集特征相结合，以提高分割的精度。

**技术框架**：PLM的整体框架包含以下几个主要模块：1) 特征提取模块，用于提取3D点云的密集特征；2) Object-centric Discriminative Representation (OcDR)模块，用于学习以物体为中心的判别性表示；3) LLM推理模块，利用LLM对OcDR tokens进行语义推理；4) Geometric Reactivation Decoder (GRD)模块，将LLM推理出的几何信息与原始的密集特征相结合，生成最终的分割mask。

**关键创新**：PLM最重要的技术创新点在于Object-centric Discriminative Representation (OcDR)和Geometric Reactivation Decoder (GRD)的设计。OcDR通过学习以物体为中心的tokens，缓解了LLM和3D点云之间的表示不对齐问题，增强了对干扰物的鲁棒性。GRD则通过将LLM推理出的几何信息与原始的密集特征相结合，提高了分割的精度。与现有方法相比，PLM无需大规模的预对齐，并且能够更好地利用LLM的语义推理能力和3D点云的几何信息。

**关键设计**：OcDR采用hard negative-aware训练目标，鼓励学习到的tokens能够区分目标物体和相似的干扰物。GRD通过将OcDR tokens携带的LLM推理出的几何信息与对应的密集特征进行融合，保留了全面的密集特征。具体的网络结构和参数设置在论文中有详细描述，例如损失函数的设计，以及OcDR和GRD中使用的具体网络层。

## 📊 实验亮点

PLM在ScanNetv2和Multi3DRefer数据集上分别取得了+7.3 mIoU和+6.0 mIoU的显著提升。此外，在包含3D referring segmentation等4个不同任务的7个基准测试中，PLM均取得了持续的收益，证明了其在鲁棒3D理解方面的有效性。这些实验结果表明，PLM能够有效地缓解LLM和3D点云之间的表示不对齐问题，并提高3D物体分割的精度。

## 🎯 应用场景

PLM在3D场景理解方面具有广泛的应用前景，例如机器人导航、自动驾驶、虚拟现实和增强现实等。它可以帮助机器人更好地理解周围环境，从而实现更智能的交互和导航。在自动驾驶领域，PLM可以提高车辆对周围物体的识别和分割精度，从而提高驾驶安全性。在VR/AR领域，PLM可以用于创建更逼真的3D场景和更自然的交互体验。

## 📄 摘要（原文）

> 3D object segmentation with Large Language Models (LLMs) has become a prevailing paradigm due to its broad semantics, task flexibility, and strong generalization. However, this paradigm is hindered by representation misalignment: LLMs process high-level semantic tokens, whereas 3D point clouds convey only dense geometric structures. In prior methods, misalignment limits both input and output. At the input stage, dense point patches require heavy pre-alignment, weakening object-level semantics and confusing similar distractors. At the output stage, predictions depend only on dense features without explicit geometric cues, leading to a loss of fine-grained accuracy. To address these limitations, we present the Point Linguist Model (PLM), a general framework that bridges the representation gap between LLMs and dense 3D point clouds without requiring large-scale pre-alignment between 3D-text or 3D-images. Specifically, we introduce Object-centric Discriminative Representation (OcDR), which learns object-centric tokens that capture target semantics and scene relations under a hard negative-aware training objective. This mitigates the misalignment between LLM tokens and 3D points, enhances resilience to distractors, and facilitates semantic-level reasoning within LLMs. For accurate segmentation, we introduce the Geometric Reactivation Decoder (GRD), which predicts masks by combining OcDR tokens carrying LLM-inferred geometry with corresponding dense features, preserving comprehensive dense features throughout the pipeline. Extensive experiments show that PLM achieves significant improvements of +7.3 mIoU on ScanNetv2 and +6.0 mIoU on Multi3DRefer for 3D referring segmentation, with consistent gains across 7 benchmarks spanning 4 different tasks, demonstrating the effectiveness of comprehensive object-centric reasoning for robust 3D understanding.

