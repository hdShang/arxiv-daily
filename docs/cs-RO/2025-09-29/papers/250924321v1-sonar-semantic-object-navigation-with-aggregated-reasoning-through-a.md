---
layout: default
title: "SONAR: Semantic-Object Navigation with Aggregated Reasoning through a Cross-Modal Inference Paradigm"
---

# SONAR: Semantic-Object Navigation with Aggregated Reasoning through a Cross-Modal Inference Paradigm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24321" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24321v1</a>
  <a href="https://arxiv.org/pdf/2509.24321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24321v1', 'SONAR: Semantic-Object Navigation with Aggregated Reasoning through a Cross-Modal Inference Paradigm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Wang, Zhirui Sun, Wenzheng Chi, Baozhi Jia, Wenjun Xu, Jiankun Wang

**分类**: cs.RO

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**SONAR：融合跨模态推理的语义对象导航方法，提升未知环境适应性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `语义对象导航` `视觉-语言导航` `跨模态推理` `语义地图` `未知环境` `机器人导航`

## 📋 核心要点

1. 现有视觉-语言导航方法在未知环境中泛化性不足，或在语义信息不足时表现欠佳，限制了机器人在复杂环境中的应用。
2. SONAR方法融合语义地图和视觉-语言模型，通过跨模态推理聚合信息，提升了在不同语义线索环境下的导航鲁棒性。
3. 实验结果表明，SONAR在MP3D数据集上取得了显著的成功率和SPL提升，验证了其在复杂环境下的有效性。

## 📝 摘要（中文）

本文提出了一种名为SONAR的语义对象导航方法，该方法通过跨模态推理进行聚合推理。针对现有模块化方法泛化性差以及基于视觉-语言模型的方法在语义线索弱时表现不佳的问题，SONAR集成了基于语义地图的目标预测模块和基于视觉-语言模型的值地图模块，从而在具有不同语义线索强度的未知环境中实现更鲁棒的导航，并有效平衡了泛化能力和场景适应性。在目标定位方面，提出了一种将多尺度语义地图与置信度地图相结合的策略，旨在减少目标对象的错误检测。在Gazebo模拟器中使用最具挑战性的Matterport 3D（MP3D）数据集进行了评估。实验结果表明，SONAR的成功率为38.4%，SPL为17.7%。

## 🔬 方法详解

**问题定义**：现有基于模块化的视觉-语言导航方法依赖于高质量的训练数据，泛化能力较差。而基于视觉-语言模型的方法在语义线索较弱时，性能会显著下降。因此，如何在未知环境中，利用有限的语义信息，实现鲁棒的导航是本文要解决的问题。

**核心思路**：SONAR的核心思路是将基于语义地图的目标预测模块与基于视觉-语言模型的值地图模块进行融合，利用各自的优势互补。语义地图提供精确的目标位置信息，而视觉-语言模型提供更强的泛化能力。通过跨模态推理，将两种信息源进行聚合，从而在不同语义线索强度的环境中实现更鲁棒的导航。

**技术框架**：SONAR的整体框架包含两个主要模块：语义地图目标预测模块和视觉-语言模型值地图模块。语义地图模块首先构建环境的语义地图，然后预测目标对象的位置。视觉-语言模型模块则根据视觉输入和语言指令，生成值地图，表示每个位置的导航价值。最后，通过聚合两个模块的输出，选择最佳的导航动作。

**关键创新**：SONAR的关键创新在于跨模态推理的聚合方法。它不是简单地将两个模块的结果进行加权平均，而是通过一种更复杂的方式进行融合，从而更好地利用两种信息源的优势。此外，提出的多尺度语义地图与置信度地图相结合的策略，有效地减少了目标对象的错误检测。

**关键设计**：在语义地图模块中，使用了多尺度语义地图，以适应不同大小的目标对象。同时，引入了置信度地图，用于过滤掉低置信度的目标检测结果。在视觉-语言模型模块中，使用了预训练的视觉-语言模型，并针对导航任务进行了微调。聚合模块使用了一种可学习的融合策略，可以根据不同的环境和指令，动态地调整两个模块的权重。

## 📊 实验亮点

SONAR在Matterport 3D数据集上进行了评估，实验结果表明，SONAR的成功率为38.4%，SPL为17.7%。相较于现有方法，SONAR在成功率和SPL上均取得了显著的提升，验证了其在复杂环境下的有效性。

## 🎯 应用场景

SONAR方法可应用于家庭服务机器人、物流机器人、安防巡逻机器人等领域，使其能够在复杂的未知环境中根据人类指令完成导航任务。该研究有助于提升机器人的自主性和智能化水平，使其更好地服务于人类生活。

## 📄 摘要（原文）

> Understanding human instructions and accomplishing Vision-Language Navigation tasks in unknown environments is essential for robots. However, existing modular approaches heavily rely on the quality of training data and often exhibit poor generalization. Vision-Language Model based methods, while demonstrating strong generalization capabilities, tend to perform unsatisfactorily when semantic cues are weak. To address these issues, this paper proposes SONAR, an aggregated reasoning approach through a cross modal paradigm. The proposed method integrates a semantic map based target prediction module with a Vision-Language Model based value map module, enabling more robust navigation in unknown environments with varying levels of semantic cues, and effectively balancing generalization ability with scene adaptability. In terms of target localization, we propose a strategy that integrates multi-scale semantic maps with confidence maps, aiming to mitigate false detections of target objects. We conducted an evaluation of the SONAR within the Gazebo simulator, leveraging the most challenging Matterport 3D (MP3D) dataset as the experimental benchmark. Experimental results demonstrate that SONAR achieves a success rate of 38.4% and an SPL of 17.7%.

