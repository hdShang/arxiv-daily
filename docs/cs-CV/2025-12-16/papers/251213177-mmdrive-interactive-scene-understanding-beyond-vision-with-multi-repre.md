---
layout: default
title: MMDrive: Interactive Scene Understanding Beyond Vision with Multi-representational Fusion
---

# MMDrive: Interactive Scene Understanding Beyond Vision with Multi-representational Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13177" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13177</a>
  <a href="https://arxiv.org/pdf/2512.13177.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13177" onclick="toggleFavorite(this, '2512.13177', 'MMDrive: Interactive Scene Understanding Beyond Vision with Multi-representational Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minghui Hou, Wei-Hsing Huang, Shaofeng Liang, Daizong Liu, Tai-Hao Wen, Gang Wang, Runwei Guan, Weiping Ding

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MMDrive：提出多模态融合的交互式场景理解框架，超越视觉限制。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `自动驾驶` `场景理解` `视觉-语言模型` `3D场景理解`

## 📋 核心要点

1. 现有视觉-语言模型受限于2D图像理解，缺乏3D空间感知和深度语义融合能力，导致在复杂自动驾驶环境中表现欠佳。
2. MMDrive通过融合占用地图、激光雷达点云和文本描述，并设计自适应跨模态融合和关键信息提取模块，实现3D场景理解。
3. 实验表明，MMDrive在DriveLM和NuScenes-QA基准上显著优于现有模型，BLEU-4提升至54.56，NuScenes-QA准确率达62.7%。

## 📝 摘要（中文）

本文提出了MMDrive，一个多模态视觉-语言模型框架，旨在将传统的2D图像理解扩展到广义的3D场景理解。MMDrive融合了占用地图、激光雷达点云和文本场景描述三种互补模态的信息。为此，论文引入了两个新颖的组件，用于自适应跨模态融合和关键信息提取。具体来说，Text-oriented Multimodal Modulator基于问题中的语义线索动态地加权每个模态的贡献，从而指导上下文感知的特征集成。Cross-Modal Abstractor采用可学习的抽象token来生成紧凑的跨模态摘要，突出关键区域和重要语义。在DriveLM和NuScenes-QA基准上的综合评估表明，MMDrive在自动驾驶的视觉-语言模型方面取得了显著的性能提升，在DriveLM上BLEU-4得分为54.56，METEOR得分为41.78，在NuScenes-QA上准确率得分为62.7%。MMDrive有效地打破了传统仅依赖图像理解的障碍，实现了复杂驾驶环境中强大的多模态推理，并为可解释的自动驾驶场景理解提供了新的基础。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在自动驾驶场景中，主要依赖2D图像进行理解和推理，无法充分利用3D空间信息，导致对复杂交通状况的理解存在局限性。痛点在于缺乏有效的多模态融合机制，无法将视觉信息与激光雷达、地图等信息进行深度整合。

**核心思路**：MMDrive的核心思路是将传统的2D图像理解扩展到3D场景理解，通过融合多种模态的信息（占用地图、激光雷达点云、文本描述）来提升模型对复杂驾驶环境的感知和推理能力。通过引入自适应跨模态融合和关键信息提取机制，使模型能够根据任务需求动态地调整不同模态的权重，并提取关键信息。

**技术框架**：MMDrive框架包含三个主要部分：多模态输入编码器、Text-oriented Multimodal Modulator和Cross-Modal Abstractor。首先，多模态输入编码器将占用地图、激光雷达点云和文本描述分别编码成特征向量。然后，Text-oriented Multimodal Modulator根据文本描述中的语义线索，动态地调整不同模态特征的权重，实现自适应跨模态融合。最后，Cross-Modal Abstractor提取融合后的特征中的关键信息，生成紧凑的跨模态摘要，用于后续的推理和问答。

**关键创新**：MMDrive的关键创新在于Text-oriented Multimodal Modulator和Cross-Modal Abstractor的设计。Text-oriented Multimodal Modulator能够根据文本描述动态调整不同模态的权重，实现了上下文感知的特征融合，克服了传统方法中静态融合的局限性。Cross-Modal Abstractor通过可学习的抽象token提取关键信息，减少了冗余信息对推理的影响。与现有方法相比，MMDrive能够更有效地利用多模态信息，提升了对复杂驾驶场景的理解能力。

**关键设计**：Text-oriented Multimodal Modulator使用注意力机制，根据文本描述的嵌入向量计算每个模态的权重。Cross-Modal Abstractor使用Transformer结构，通过可学习的抽象token与多模态特征进行交互，提取关键信息。损失函数包括问答损失和对比学习损失，用于优化模型的推理能力和跨模态表示能力。具体参数设置未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13177/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13177/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13177/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MMDrive在DriveLM和NuScenes-QA两个基准测试中取得了显著的性能提升。在DriveLM上，MMDrive的BLEU-4得分达到54.56，METEOR得分达到41.78，相较于现有最佳模型有显著提升。在NuScenes-QA上，MMDrive的准确率达到62.7%，同样优于其他基线模型。这些结果表明，MMDrive能够有效地融合多模态信息，提升对复杂驾驶场景的理解能力。

## 🎯 应用场景

MMDrive可应用于高级驾驶辅助系统（ADAS）和自动驾驶系统，提升车辆对复杂交通场景的感知和理解能力，从而提高驾驶安全性。该研究还可扩展到其他需要多模态信息融合的机器人应用，例如智能巡检机器人、智能家居等，具有广阔的应用前景。

## 📄 摘要（原文）

> Vision-language models enable the understanding and reasoning of complex traffic scenarios through multi-source information fusion, establishing it as a core technology for autonomous driving. However, existing vision-language models are constrained by the image understanding paradigm in 2D plane, which restricts their capability to perceive 3D spatial information and perform deep semantic fusion, resulting in suboptimal performance in complex autonomous driving environments. This study proposes MMDrive, an multimodal vision-language model framework that extends traditional image understanding to a generalized 3D scene understanding framework. MMDrive incorporates three complementary modalities, including occupancy maps, LiDAR point clouds, and textual scene descriptions. To this end, it introduces two novel components for adaptive cross-modal fusion and key information extraction. Specifically, the Text-oriented Multimodal Modulator dynamically weights the contributions of each modality based on the semantic cues in the question, guiding context-aware feature integration. The Cross-Modal Abstractor employs learnable abstract tokens to generate compact, cross-modal summaries that highlight key regions and essential semantics. Comprehensive evaluations on the DriveLM and NuScenes-QA benchmarks demonstrate that MMDrive achieves significant performance gains over existing vision-language models for autonomous driving, with a BLEU-4 score of 54.56 and METEOR of 41.78 on DriveLM, and an accuracy score of 62.7% on NuScenes-QA. MMDrive effectively breaks the traditional image-only understanding barrier, enabling robust multimodal reasoning in complex driving environments and providing a new foundation for interpretable autonomous driving scene understanding.

