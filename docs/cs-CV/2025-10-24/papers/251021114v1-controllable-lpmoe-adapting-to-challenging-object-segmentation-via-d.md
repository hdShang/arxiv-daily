---
layout: default
title: Controllable-LPMoE: Adapting to Challenging Object Segmentation via Dynamic Local Priors from Mixture-of-Experts
---

# Controllable-LPMoE: Adapting to Challenging Object Segmentation via Dynamic Local Priors from Mixture-of-Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21114" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21114v1</a>
  <a href="https://arxiv.org/pdf/2510.21114.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21114v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21114v1', 'Controllable-LPMoE: Adapting to Challenging Object Segmentation via Dynamic Local Priors from Mixture-of-Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanguang Sun, Jiawei Lian, Jian Yang, Lei Luo

**分类**: cs.CV

**发布日期**: 2025-10-24

**备注**: Accepted at ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/CSYSI/Controllable-LPMoE)

---

## 💡 一句话要点

**Controllable-LPMoE：通过动态局部先验混合专家网络提升目标分割性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `目标分割` `预训练模型` `微调` `局部先验` `混合专家网络`

## 📋 核心要点

1. 现有全参数微调方法计算开销大，prompt微调缺乏语义先验，限制了预训练模型的适应性。
2. 提出Controllable-LPMoE，通过动态控制局部先验自适应调节预训练模型，增强细粒度感知能力。
3. 实验结果表明，该方法在多个二元目标分割任务上优于31种SOTA方法，具有出色的分割性能。

## 📝 摘要（中文）

大规模预训练模型为下游目标分割任务提供了强大的特征表示。然而，通过全参数微调将这些模型适配到特定任务时，需要更新的参数量巨大，导致计算开销显著增加，成为训练效率的瓶颈。现有方法尝试通过直接嵌入可训练的提示（prompt）来微调冻结的模型，但这些提示缺乏固有的语义先验，限制了大规模模型的适应性。本文提出了一种基于动态先验的微调范式，名为Controllable-LPMoE，它通过动态控制局部先验来自适应地调节冻结的预训练模型，从而增强特定分割任务的细粒度感知能力。具体来说，我们构建了一个轻量级的动态混合局部先验提取器，通过异构卷积从输入图像中捕获不同的局部先验，并采用门控网络动态输出后续微调所需的专家先验。此外，我们设计了一个双向交互适配器，采用余弦对齐的可变形注意力和通道导向的自适应尺度增强，在冻结特征和可训练特征之间进行交互和重构，实现高效微调。大量实验验证了Controllable-LPMoE方法的优越性，表明其在多个二元目标分割任务中相比于31种最先进方法具有出色的分割性能和适应性。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模预训练模型在目标分割任务中全参数微调时计算开销过大，以及prompt微调方法缺乏语义先验的问题。现有方法难以在计算效率和模型适应性之间取得平衡，限制了预训练模型在特定分割任务中的应用。

**核心思路**：论文的核心思路是通过引入动态局部先验来指导预训练模型的微调过程。通过提取和利用图像的局部先验信息，模型能够更好地理解和分割目标，同时避免了全参数微调带来的巨大计算开销。动态混合专家网络的设计使得模型能够根据输入图像自适应地选择合适的先验信息。

**技术框架**：Controllable-LPMoE主要包含两个核心模块：动态混合局部先验提取器和双向交互适配器。首先，动态混合局部先验提取器通过异构卷积提取图像的局部先验，并使用门控网络选择合适的专家先验。然后，双向交互适配器利用余弦对齐的可变形注意力和通道导向的自适应尺度增强，在冻结的预训练模型特征和可训练的局部先验特征之间进行交互和融合。最终，融合后的特征用于目标分割。

**关键创新**：该方法的主要创新在于动态局部先验的引入和混合专家网络的设计。与传统的prompt微调方法相比，该方法能够利用图像的局部信息，提供更丰富的语义先验。动态混合专家网络使得模型能够根据输入自适应地选择合适的先验，提高了模型的适应性。双向交互适配器则实现了冻结特征和可训练特征之间的有效融合。

**关键设计**：动态混合局部先验提取器使用异构卷积来捕获不同尺度的局部先验信息。门控网络的设计允许模型根据输入图像的特征动态地选择合适的专家先验。双向交互适配器中的余弦对齐可变形注意力能够更好地对齐不同特征之间的空间关系。通道导向的自适应尺度增强则能够调整不同通道的特征尺度，提高特征的表达能力。

## 📊 实验亮点

实验结果表明，Controllable-LPMoE在多个二元目标分割任务上取得了显著的性能提升，超越了31种SOTA方法。例如，在某个数据集上，Controllable-LPMoE的分割精度比最佳基线方法提高了X%。此外，该方法仅需微调少量参数，大大降低了计算开销，验证了其高效性和实用性。

## 🎯 应用场景

Controllable-LPMoE在二元目标分割任务中表现出色，可应用于医学图像分析（如肿瘤分割）、遥感图像分析（如建筑物提取）、自动驾驶（如道路分割）等领域。该方法通过高效微调预训练模型，降低了计算成本，使得大规模预训练模型能够更好地应用于资源受限的场景，具有重要的实际应用价值和广泛的应用前景。

## 📄 摘要（原文）

> Large-scale foundation models provide powerful feature representations for downstream object segmentation tasks. However, when adapted to specific tasks through the full-parameter fine-tuning, the enormous parameters being updated often results in significant computational overhead, creating a bottleneck in training efficiency. Although existing methods attempt to fine-tune frozen models by directly embedding trainable prompts, these prompts lack inherent semantic priors, limiting the adaptability of large-scale models. In this paper, we propose a novel dynamic priors-based fine-tuning paradigm with fewer trainable parameters, dubbed Controllable-LPMoE, which adaptively modulates frozen foundation models by dynamically controlling local priors to enhance fine-grained perception for specific segmentation tasks. More specifically, we construct a lightweight dynamic mixed local priors extractor that captures diverse local priors from input images through heterogeneous convolutions while employing a gating network to dynamically output expert priors required for the subsequent fine-tuning. Furthermore, we design a bi-directional interaction adapter that employs cosine-aligned deformable attention and channel-oriented adaptive scale enhancement to interact and restructure between frozen and trainable features, achieving efficient fine-tuning. Extensive experiments validate the superiority of our \href{https://github.com/CSYSI/Controllable-LPMoE} {Controllable-LPMoE} approach, demonstrating excellent segmentation performance compared to 31 state-of-the-art (SOTA) methods and adaptability to multiple binary object segmentation tasks.

