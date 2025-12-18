---
layout: default
title: From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors
---

# From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17439" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17439v1</a>
  <a href="https://arxiv.org/pdf/2510.17439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17439v1', 'From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengshen Zhang, Hao Li, Yalun Dai, Zhengbang Zhu, Lei Zhou, Chenchen Liu, Dong Wang, Francis E. H. Tay, Sijin Chen, Ziwei Liu, Yuxiao Liu, Xinghang Li, Pan Zhou

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-20

**备注**: Project page: https://falcon-vla.github.io/

---

## 💡 一句话要点

**FALCON：利用空间基础先验增强视觉-语言-动作模型的3D环境泛化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `3D空间推理` `空间基础模型` `具身智能` `机器人导航`

## 📋 核心要点

1. 现有VLA模型依赖2D编码器，缺乏3D空间推理能力，限制了其泛化性和适应性。
2. FALCON通过空间基础模型提取3D空间tokens，并注入到动作头中，增强空间感知能力。
3. 实验表明，FALCON在多个模拟和真实世界任务中均取得了SOTA性能，并具有良好的鲁棒性。

## 📝 摘要（中文）

现有的视觉-语言-动作（VLA）模型虽然在3D真实世界中运行，但通常构建在2D编码器之上，导致空间推理存在差距，限制了泛化性和适应性。目前针对VLA的3D集成技术要么需要专用传感器，且跨模态迁移效果差，要么注入的弱线索缺乏几何信息，降低了视觉-语言对齐效果。本文提出了FALCON（From Spatial to Action），一种将丰富的3D空间tokens注入到动作头的全新范例。FALCON利用空间基础模型，仅从RGB图像中提供强大的几何先验，并包含一个具身空间模型，该模型可以选择性地融合深度或姿态信息，以在可用时获得更高的保真度，而无需重新训练或更改架构。为了保持语言推理能力，空间tokens由空间增强动作头消耗，而不是连接到视觉-语言骨干网络中。这些设计使FALCON能够解决空间表示、模态可迁移性和对齐方面的局限性。在三个模拟基准测试和十一个真实世界任务的综合评估中，我们提出的FALCON实现了最先进的性能，始终超越了具有竞争力的基线，并且在杂乱、空间提示条件以及对象尺度和高度变化下保持稳健。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作（VLA）模型在处理真实3D环境时，由于其视觉编码器主要基于2D图像，缺乏对3D空间几何信息的有效利用，导致模型在复杂环境下的泛化能力受限。现有的3D集成方法要么依赖特定传感器（如深度相机），限制了其应用范围，要么提供的3D信息不足，影响了视觉和语言信息的对齐。

**核心思路**：FALCON的核心思路是利用预训练的空间基础模型，从RGB图像中提取丰富的3D空间先验知识，并将这些知识以空间tokens的形式注入到动作头中。通过这种方式，模型可以在不改变视觉-语言骨干网络结构的前提下，增强对3D环境的感知和推理能力。同时，为了更好地利用深度或姿态信息，FALCON还设计了一个具身空间模型，可以在不重新训练的情况下融合这些额外信息。

**技术框架**：FALCON的整体框架包括以下几个主要模块：1) 视觉-语言骨干网络：用于提取图像和语言特征。2) 空间基础模型：用于从RGB图像中提取3D空间tokens。3) 具身空间模型（可选）：用于融合深度或姿态信息，进一步增强空间表示。4) 空间增强动作头：用于接收视觉-语言特征和空间tokens，并生成动作指令。整个流程是，首先通过视觉-语言骨干网络提取特征，然后利用空间基础模型提取空间信息，最后将这些信息融合到动作头中，指导动作的生成。

**关键创新**：FALCON的关键创新在于其将空间基础模型与VLA模型相结合，通过空间tokens的形式将3D空间先验知识注入到动作头中。这种方法避免了直接修改视觉-语言骨干网络，从而保持了语言推理能力。此外，FALCON的具身空间模型可以在不重新训练的情况下融合深度或姿态信息，提高了模型的灵活性和适应性。

**关键设计**：FALCON的关键设计包括：1) 使用预训练的空间基础模型，例如3D检测模型，提取3D bounding box 或 point cloud 等空间信息。2) 设计空间增强动作头，该模块接收视觉-语言特征和空间tokens，并使用注意力机制或其他融合方法将它们结合起来。3) 具身空间模型的设计，允许模型在可用时融合深度或姿态信息，提高空间表示的准确性。具体的损失函数和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

FALCON在三个模拟基准测试和十一个真实世界任务中均取得了最先进的性能。实验结果表明，FALCON在杂乱环境、空间提示条件以及对象尺度和高度变化下均表现出良好的鲁棒性。相较于现有方法，FALCON在多个任务上取得了显著的性能提升，证明了其在3D空间推理方面的优势。

## 🎯 应用场景

FALCON具有广泛的应用前景，例如机器人导航、自动驾驶、虚拟现实和增强现实等领域。它可以帮助机器人在复杂环境中更好地理解人类指令，并执行各种任务。此外，FALCON还可以应用于智能家居、工业自动化等领域，提高机器人的智能化水平和工作效率。未来，FALCON有望成为构建更智能、更可靠的机器人系统的关键技术。

## 📄 摘要（原文）

> Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability. Recent 3D integration techniques for VLAs either require specialized sensors and transfer poorly across modalities, or inject weak cues that lack geometry and degrade vision-language alignment. In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head. FALCON leverages spatial foundation models to deliver strong geometric priors from RGB alone, and includes an Embodied Spatial Model that can optionally fuse depth, or pose for higher fidelity when available, without retraining or architectural changes. To preserve language reasoning, spatial tokens are consumed by a Spatial-Enhanced Action Head rather than being concatenated into the vision-language backbone. These designs enable FALCON to address limitations in spatial representation, modality transferability, and alignment. In comprehensive evaluations across three simulation benchmarks and eleven real-world tasks, our proposed FALCON achieves state-of-the-art performance, consistently surpasses competitive baselines, and remains robust under clutter, spatial-prompt conditioning, and variations in object scale and height.

