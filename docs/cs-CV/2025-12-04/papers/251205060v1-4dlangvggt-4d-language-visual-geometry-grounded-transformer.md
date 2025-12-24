---
layout: default
title: "4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer"
---

# 4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05060" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05060v1</a>
  <a href="https://arxiv.org/pdf/2512.05060.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05060v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05060v1', '4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang

**分类**: cs.CV

**发布日期**: 2025-12-04

**备注**: Code: https://github.com/hustvl/4DLangVGGT, Webpage: https://hustvl.github.io/4DLangVGGT

**🔗 代码/项目**: [GITHUB](https://github.com/hustvl/4DLangVGGT)

---

## 💡 一句话要点

**提出4DLangVGGT，用于高效且可泛化的4D语言-视觉几何对齐**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D场景理解` `语言对齐` `视觉几何` `Transformer` `动态场景` `神经辐射场` `开放词汇`

## 📋 核心要点

1. 现有4D语义场构建方法依赖逐场景优化，泛化性差，难以扩展到真实场景。
2. 提出4DLangVGGT，通过Transformer联合学习几何感知和语言对齐，无需逐场景优化。
3. 实验表明，4DLangVGGT在HyperNeRF和Neu3D数据集上均达到SOTA性能，泛化能力强。

## 📝 摘要（中文）

构建4D语言场对于具身智能、增强/虚拟现实和4D场景理解至关重要，它提供了动态环境的丰富语义表示，并支持复杂场景中的开放词汇查询。然而，现有的4D语义场构建方法主要依赖于特定场景的高斯溅射，这需要逐场景优化，泛化能力有限，并且难以扩展到实际应用。为了解决这些限制，我们提出了4DLangVGGT，这是第一个基于Transformer的前馈统一框架，用于4D语言对齐，它在单个架构中联合集成了几何感知和语言对齐。4DLangVGGT有两个关键组件：4D视觉几何Transformer，StreamVGGT，它捕获动态场景的时空几何表示；以及语义桥接解码器（SBD），它将几何感知特征投影到语言对齐的语义空间中，从而增强语义可解释性，同时保持结构保真度。与依赖于昂贵的逐场景优化方法不同，4DLangVGGT可以在多个动态场景中联合训练，并在推理期间直接应用，从而实现部署效率和强大的泛化能力。这种设计显著提高了大规模部署的实用性，并为开放词汇4D场景理解建立了一种新范式。在HyperNeRF和Neu3D数据集上的实验表明，我们的方法不仅能有效地泛化，而且还能达到最先进的性能，在逐场景训练下实现了高达2%的增益，在多场景训练下实现了1%的改进。我们的代码已在https://github.com/hustvl/4DLangVGGT发布。

## 🔬 方法详解

**问题定义**：现有4D场景理解方法，特别是基于神经辐射场的方法，通常需要针对每个特定场景进行优化，计算成本高昂，泛化能力不足，难以应用于大规模动态场景。此外，这些方法在处理开放词汇的语言查询时，语义理解能力有限。

**核心思路**：4DLangVGGT的核心在于构建一个可泛化的、端到端的4D语言-视觉几何对齐框架。通过Transformer架构，将动态场景的几何信息和语言信息进行联合编码和解码，从而实现高效的语义理解和场景重建，避免了逐场景优化带来的局限性。

**技术框架**：4DLangVGGT主要包含两个核心模块：StreamVGGT（4D视觉几何Transformer）和Semantic Bridging Decoder (SBD)。StreamVGGT负责捕获动态场景的时空几何表示，将4D场景信息编码成几何特征。SBD则将这些几何特征投影到语言对齐的语义空间，从而实现几何信息和语言信息的融合。整个框架通过联合训练，实现端到端的4D语言对齐。

**关键创新**：4DLangVGGT的关键创新在于其统一的Transformer架构，能够同时处理几何信息和语言信息，并实现跨场景的泛化。与以往依赖于特定场景优化的方法不同，4DLangVGGT可以在多个场景上进行联合训练，从而学习到更通用的场景表示。此外，SBD模块的设计有效地将几何特征映射到语义空间，增强了语义可解释性。

**关键设计**：StreamVGGT采用Transformer结构，输入是4D点云数据，通过自注意力机制学习时空几何特征。SBD使用交叉注意力机制，将StreamVGGT输出的几何特征与语言嵌入进行对齐。损失函数包括几何重建损失和语言对齐损失，用于优化整个网络。具体的参数设置和网络结构细节在论文中有详细描述（未知）。

## 📊 实验亮点

4DLangVGGT在HyperNeRF和Neu3D数据集上取得了state-of-the-art的性能。在per-scene训练下，性能提升高达2%；在multi-scene训练下，性能提升高达1%。这些结果表明，4DLangVGGT具有强大的泛化能力和高效的场景理解能力。

## 🎯 应用场景

4DLangVGGT在具身智能、增强/虚拟现实、机器人导航、自动驾驶等领域具有广泛的应用前景。它可以用于构建动态环境的语义地图，支持机器人进行复杂的场景理解和交互，并为AR/VR应用提供更逼真的沉浸式体验。该研究为开放词汇4D场景理解开辟了新的方向。

## 📄 摘要（原文）

> Constructing 4D language fields is crucial for embodied AI, augmented/virtual reality, and 4D scene understanding, as they provide enriched semantic representations of dynamic environments and enable open-vocabulary querying in complex scenarios. However, existing approaches to 4D semantic field construction primarily rely on scene-specific Gaussian splatting, which requires per-scene optimization, exhibits limited generalization, and is difficult to scale to real-world applications. To address these limitations, we propose 4DLangVGGT, the first Transformer-based feed-forward unified framework for 4D language grounding, that jointly integrates geometric perception and language alignment within a single architecture. 4DLangVGGT has two key components: the 4D Visual Geometry Transformer, StreamVGGT, which captures spatio-temporal geometric representations of dynamic scenes; and the Semantic Bridging Decoder (SBD), which projects geometry-aware features into a language-aligned semantic space, thereby enhancing semantic interpretability while preserving structural fidelity. Unlike prior methods that depend on costly per-scene optimization, 4DLangVGGT can be jointly trained across multiple dynamic scenes and directly applied during inference, achieving both deployment efficiency and strong generalization. This design significantly improves the practicality of large-scale deployment and establishes a new paradigm for open-vocabulary 4D scene understanding. Experiments on HyperNeRF and Neu3D datasets demonstrate that our approach not only generalizes effectively but also achieves state-of-the-art performance, achieving up to 2% gains under per-scene training and 1% improvements under multi-scene training. Our code released in https://github.com/hustvl/4DLangVGGT

