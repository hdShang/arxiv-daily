---
layout: default
title: "EPSegFZ: Efficient Point Cloud Semantic Segmentation for Few- and Zero-Shot Scenarios with Language Guidance"
---

# EPSegFZ: Efficient Point Cloud Semantic Segmentation for Few- and Zero-Shot Scenarios with Language Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.11700" class="toolbar-btn" target="_blank">📄 arXiv: 2511.11700v1</a>
  <a href="https://arxiv.org/pdf/2511.11700.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.11700v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.11700v1', 'EPSegFZ: Efficient Point Cloud Semantic Segmentation for Few- and Zero-Shot Scenarios with Language Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Wang, Haiyue Zhu, Haoren Guo, Abdullah Al Mamun, Cheng Xiang, Tong Heng Lee

**分类**: cs.CV, eess.IV

**发布日期**: 2025-11-12

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出EPSegFZ，利用语言引导实现高效的点云少样本/零样本语义分割**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `点云语义分割` `少样本学习` `零样本学习` `语言引导` `原型学习`

## 📋 核心要点

1. 现有少样本点云语义分割方法过度依赖预训练，限制了模型的灵活性和泛化能力。
2. EPSegFZ通过ProERA、DRPE和LGPE模块，无需预训练即可实现高效的特征提取和语言引导的语义分割。
3. 实验结果表明，EPSegFZ在S3DIS和ScanNet数据集上显著优于现有方法，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种名为EPSegFZ的无需预训练的点云语义分割网络，用于解决少样本和零样本场景下的分割问题。现有方法通常依赖于两阶段学习，即预训练阶段和少样本训练阶段，这导致模型过度依赖预训练，缺乏灵活性和适应性。此外，现有方法未能充分利用支持集中的文本标注等信息。为了解决这些问题，EPSegFZ包含三个关键组件：原型增强寄存器注意力（ProERA）模块和基于双重相对位置编码（DRPE）的交叉注意力机制，用于改进特征提取和构建准确的查询-原型对应关系，无需预训练；语言引导原型嵌入（LGPE）模块，有效利用支持集中的文本信息，提高少样本性能并实现零样本推理。在S3DIS和ScanNet基准测试中，该方法分别优于现有技术5.68%和3.82%。

## 🔬 方法详解

**问题定义**：现有少样本点云语义分割方法主要存在两个痛点：一是过度依赖预训练，导致模型缺乏灵活性和适应性；二是未能充分利用支持集中的文本标注信息，限制了模型的性能和零样本能力。因此，需要一种无需预训练且能有效利用文本信息的少样本/零样本点云语义分割方法。

**核心思路**：EPSegFZ的核心思路是利用语言信息引导点云特征的学习和分割，从而在无需预训练的情况下，提高模型的少样本和零样本分割性能。通过ProERA和DRPE模块增强点云特征的表达能力，并通过LGPE模块将文本信息融入到原型表示中，从而实现更准确的语义分割。

**技术框架**：EPSegFZ的整体框架包括三个主要模块：1) Prototype-Enhanced Registers Attention (ProERA)模块，用于增强点云特征的表达能力；2) Dual Relative Positional Encoding (DRPE)-based cross-attention机制，用于构建准确的查询-原型对应关系；3) Language-Guided Prototype Embedding (LGPE)模块，用于将文本信息融入到原型表示中。整个流程是先通过ProERA提取点云特征，然后利用DRPE构建查询-原型对应关系，最后通过LGPE将文本信息融入原型，进行语义分割。

**关键创新**：EPSegFZ的关键创新在于：1) 提出了一种无需预训练的点云语义分割框架，避免了对预训练模型的依赖；2) 提出了ProERA模块和DRPE机制，用于增强点云特征的表达能力和构建准确的查询-原型对应关系；3) 提出了LGPE模块，有效利用了支持集中的文本信息，提高了模型的少样本和零样本分割性能。

**关键设计**：ProERA模块利用寄存器注意力机制增强点云特征；DRPE机制通过考虑点之间的相对位置关系，提高交叉注意力的准确性；LGPE模块利用预训练的语言模型（如BERT）提取文本特征，并将其融入到原型表示中。损失函数包括分割损失和对比学习损失，用于优化模型的分割性能和原型表示。

## 📊 实验亮点

EPSegFZ在S3DIS和ScanNet数据集上取得了显著的性能提升。在S3DIS数据集上，EPSegFZ的平均IoU比现有最佳方法提高了5.68%。在ScanNet数据集上，EPSegFZ的平均IoU比现有最佳方法提高了3.82%。这些结果表明，EPSegFZ在少样本和零样本点云语义分割方面具有显著的优势。

## 🎯 应用场景

EPSegFZ在机器人、自动驾驶、增强现实等领域具有广泛的应用前景。例如，在机器人场景中，可以利用该方法实现对未知物体的快速识别和分割，从而提高机器人的环境适应能力。在自动驾驶领域，可以利用该方法实现对道路场景的精确分割，从而提高自动驾驶系统的安全性。在增强现实领域，可以利用该方法实现对虚拟物体的精确放置和交互。

## 📄 摘要（原文）

> Recent approaches for few-shot 3D point cloud semantic segmentation typically require a two-stage learning process, i.e., a pre-training stage followed by a few-shot training stage. While effective, these methods face overreliance on pre-training, which hinders model flexibility and adaptability. Some models tried to avoid pre-training yet failed to capture ample information. In addition, current approaches focus on visual information in the support set and neglect or do not fully exploit other useful data, such as textual annotations. This inadequate utilization of support information impairs the performance of the model and restricts its zero-shot ability. To address these limitations, we present a novel pre-training-free network, named Efficient Point Cloud Semantic Segmentation for Few- and Zero-shot scenarios. Our EPSegFZ incorporates three key components. A Prototype-Enhanced Registers Attention (ProERA) module and a Dual Relative Positional Encoding (DRPE)-based cross-attention mechanism for improved feature extraction and accurate query-prototype correspondence construction without pre-training. A Language-Guided Prototype Embedding (LGPE) module that effectively leverages textual information from the support set to improve few-shot performance and enable zero-shot inference. Extensive experiments show that our method outperforms the state-of-the-art method by 5.68% and 3.82% on the S3DIS and ScanNet benchmarks, respectively.

