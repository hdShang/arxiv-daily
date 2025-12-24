---
layout: default
title: "NeurNCD: Novel Class Discovery via Implicit Neural Representation"
---

# NeurNCD: Novel Class Discovery via Implicit Neural Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06412" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06412v1</a>
  <a href="https://arxiv.org/pdf/2506.06412.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06412v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06412v1', 'NeurNCD: Novel Class Discovery via Implicit Neural Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junming Wang, Yi Shi

**分类**: cs.LG, cs.CV

**发布日期**: 2025-06-06

**备注**: Accepted by ICMR 2024

---

## 💡 一句话要点

**提出NeurNCD以解决开放世界中新类发现问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新类发现` `隐式神经表示` `语义嵌入` `KL散度` `特征增强` `开放世界` `自动驾驶` `机器人视觉`

## 📋 核心要点

1. 现有方法在开放世界中新类发现中面临显式表示的局限性，导致准确性不足。
2. NeurNCD框架通过Embedding-NeRF模型和KL散度，提供了一种新的隐式表示方法，克服了传统方法的缺陷。
3. 实验结果显示，NeurNCD在NYUv2和Replica数据集上超越了现有技术，展现出优越的分割性能。

## 📝 摘要（中文）

在开放世界环境中发现新类对于实际应用至关重要。传统的显式表示方法，如物体描述符或3D分割图，由于其离散性、易出现空洞和噪声，限制了新类发现的准确性。为了解决这些挑战，本文提出了NeurNCD，这是第一个多功能且数据高效的新类发现框架，采用精心设计的Embedding-NeRF模型，并结合KL散度替代传统显式3D分割图，以聚合视觉嵌入空间中的语义嵌入和熵。NeurNCD还整合了特征查询、特征调制和聚类等关键组件，促进了预训练语义分割网络与隐式神经表示之间的特征增强和信息交换。实验结果表明，该方法在NYUv2和Replica数据集上显著优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决开放世界中新类发现的问题，现有方法依赖的显式表示存在离散性和噪声等缺陷，限制了其在实际应用中的有效性。

**核心思路**：NeurNCD通过Embedding-NeRF模型结合KL散度，提供了一种隐式的语义嵌入表示，能够更有效地聚合信息，减少噪声影响，从而提升新类发现的准确性。

**技术框架**：该框架包括几个主要模块：Embedding-NeRF模型用于生成隐式表示，特征查询和调制模块用于增强特征表达，聚类模块则促进信息的有效交换。整体流程通过这些模块的协同作用，实现了高效的新类发现。

**关键创新**：NeurNCD的核心创新在于引入了隐式神经表示和KL散度替代传统的3D分割图，这一设计使得模型在处理新类时更加灵活和高效，显著提升了分割性能。

**关键设计**：在技术细节上，NeurNCD采用了特征查询和调制机制，以增强特征的表达能力，同时在损失函数中引入了KL散度，以优化嵌入空间的语义聚合效果。

## 📊 实验亮点

在NYUv2和Replica数据集上的实验结果表明，NeurNCD在分割性能上显著优于现有最先进的方法，具体提升幅度达到XX%（具体数据未知），展示了其在新类发现任务中的有效性和优越性。

## 🎯 应用场景

该研究在开放世界场景中的新类发现具有广泛的应用潜力，尤其是在自动驾驶、机器人视觉和智能监控等领域。通过提高新类的识别能力，NeurNCD能够推动这些领域的技术进步，提升系统的智能化水平和适应性。

## 📄 摘要（原文）

> Discovering novel classes in open-world settings is crucial for real-world applications. Traditional explicit representations, such as object descriptors or 3D segmentation maps, are constrained by their discrete, hole-prone, and noisy nature, which hinders accurate novel class discovery. To address these challenges, we introduce NeurNCD, the first versatile and data-efficient framework for novel class discovery that employs the meticulously designed Embedding-NeRF model combined with KL divergence as a substitute for traditional explicit 3D segmentation maps to aggregate semantic embedding and entropy in visual embedding space. NeurNCD also integrates several key components, including feature query, feature modulation and clustering, facilitating efficient feature augmentation and information exchange between the pre-trained semantic segmentation network and implicit neural representations. As a result, our framework achieves superior segmentation performance in both open and closed-world settings without relying on densely labelled datasets for supervised training or human interaction to generate sparse label supervision. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art approaches on the NYUv2 and Replica datasets.

