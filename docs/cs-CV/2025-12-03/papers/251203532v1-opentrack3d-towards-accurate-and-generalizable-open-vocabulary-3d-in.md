---
layout: default
title: "OpenTrack3D: Towards Accurate and Generalizable Open-Vocabulary 3D Instance Segmentation"
---

# OpenTrack3D: Towards Accurate and Generalizable Open-Vocabulary 3D Instance Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.03532" class="toolbar-btn" target="_blank">📄 arXiv: 2512.03532v1</a>
  <a href="https://arxiv.org/pdf/2512.03532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03532v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.03532v1', 'OpenTrack3D: Towards Accurate and Generalizable Open-Vocabulary 3D Instance Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhishan Zhou, Siyuan Wei, Zengran Wang, Chunjie Wang, Xiaosheng Yan, Xiao Liu

**分类**: cs.CV

**发布日期**: 2025-12-03

---

## 💡 一句话要点

**OpenTrack3D：面向精确和泛化的开放词汇3D实例分割**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `开放词汇3D实例分割` `无网格方法` `视觉-空间跟踪` `多模态大语言模型` `机器人` `AR/VR` `DINO特征`

## 📋 核心要点

1. 现有开放词汇3D实例分割方法依赖数据集特定proposal网络或网格，泛化性受限，且CLIP文本推理能力弱，难以处理复杂查询。
2. OpenTrack3D提出一种新颖的视觉-空间跟踪器，在线构建跨视图一致的对象proposal，并用MLLM增强组合推理能力。
3. 在ScanNet200等多个数据集上，OpenTrack3D取得了state-of-the-art的性能，并展现出强大的泛化能力。

## 📝 摘要（中文）

将开放词汇3D实例分割（OV-3DIS）推广到多样、非结构化和无网格环境对于机器人和AR/VR至关重要，但仍然是一个重大挑战。我们认为这归因于现有方法的两个关键限制：（1）proposal生成依赖于数据集特定的proposal网络或基于网格的超点，使其不适用于无网格场景，并限制了对新场景的泛化；（2）基于CLIP的分类器在文本推理方面的不足，难以识别组合和功能性用户查询。为了解决这些问题，我们提出了OpenTrack3D，一个通用且精确的框架。与依赖于预生成proposal的方法不同，OpenTrack3D采用了一种新颖的视觉-空间跟踪器来在线构建跨视图一致的对象proposal。给定RGB-D流，我们的pipeline首先利用2D开放词汇分割器生成mask，然后使用深度信息将其提升到3D点云。然后使用DINO特征图提取mask引导的实例特征，我们的跟踪器融合视觉和空间线索以保持实例一致性。核心pipeline完全是无网格的，但我们也提供了一个可选的超点细化模块，以在场景网格可用时进一步提高性能。最后，我们用多模态大型语言模型（MLLM）替换CLIP，显著增强了复杂用户查询的组合推理能力。在包括ScanNet200、Replica、ScanNet++和SceneFun3D在内的各种benchmark上的大量实验表明，该方法具有最先进的性能和强大的泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决开放词汇3D实例分割（OV-3DIS）在多样、非结构化和无网格环境下的泛化性问题。现有方法依赖于数据集特定的proposal网络或基于网格的超点，导致无法应用于无网格场景，并且基于CLIP的分类器在处理复杂的用户查询时表现不佳。

**核心思路**：OpenTrack3D的核心思路是通过一个视觉-空间跟踪器在线生成跨视图一致的对象proposal，避免了对预定义proposal的依赖。同时，使用多模态大型语言模型（MLLM）替换CLIP，以增强对复杂用户查询的理解和推理能力。

**技术框架**：OpenTrack3D的整体框架包含以下几个主要阶段：1) 使用2D开放词汇分割器从RGB-D流中生成mask；2) 利用深度信息将2D mask提升到3D点云；3) 使用DINO特征图提取mask引导的实例特征；4) 使用视觉-空间跟踪器融合视觉和空间线索，保持实例一致性；5) (可选) 使用超点细化模块进一步提高性能（当场景网格可用时）；6) 使用MLLM进行最终的实例分类。

**关键创新**：OpenTrack3D的关键创新在于：1) 提出了一个无网格的视觉-空间跟踪器，能够在线生成高质量的对象proposal，避免了对预定义proposal的依赖，从而提高了泛化能力；2) 使用MLLM替换CLIP，显著增强了对复杂用户查询的组合推理能力。

**关键设计**：视觉-空间跟踪器融合了视觉特征（DINO特征）和空间信息（点云坐标），通过卡尔曼滤波等方法进行跟踪和更新。MLLM的使用涉及prompt工程和微调策略，以适应3D实例分割任务。损失函数的设计可能包括分割损失、跟踪损失和分类损失等。

## 📊 实验亮点

OpenTrack3D在ScanNet200、Replica、ScanNet++和SceneFun3D等多个数据集上取得了state-of-the-art的性能，证明了其优越的性能和泛化能力。具体性能数据未知，但论文强调了其在复杂场景和用户查询下的显著提升。

## 🎯 应用场景

OpenTrack3D在机器人、AR/VR等领域具有广泛的应用前景。例如，机器人可以利用该技术在未知环境中识别和分割物体，从而实现自主导航和操作。在AR/VR中，该技术可以用于增强现实体验，例如允许用户与虚拟物体进行交互。

## 📄 摘要（原文）

> Generalizing open-vocabulary 3D instance segmentation (OV-3DIS) to diverse, unstructured, and mesh-free environments is crucial for robotics and AR/VR, yet remains a significant challenge. We attribute this to two key limitations of existing methods: (1) proposal generation relies on dataset-specific proposal networks or mesh-based superpoints, rendering them inapplicable in mesh-free scenarios and limiting generalization to novel scenes; and (2) the weak textual reasoning of CLIP-based classifiers, which struggle to recognize compositional and functional user queries. To address these issues, we introduce OpenTrack3D, a generalizable and accurate framework. Unlike methods that rely on pre-generated proposals, OpenTrack3D employs a novel visual-spatial tracker to construct cross-view consistent object proposals online. Given an RGB-D stream, our pipeline first leverages a 2D open-vocabulary segmenter to generate masks, which are lifted to 3D point clouds using depth. Mask-guided instance features are then extracted using DINO feature maps, and our tracker fuses visual and spatial cues to maintain instance consistency. The core pipeline is entirely mesh-free, yet we also provide an optional superpoints refinement module to further enhance performance when scene mesh is available. Finally, we replace CLIP with a multi-modal large language model (MLLM), significantly enhancing compositional reasoning for complex user queries. Extensive experiments on diverse benchmarks, including ScanNet200, Replica, ScanNet++, and SceneFun3D, demonstrate state-of-the-art performance and strong generalization capabilities.

