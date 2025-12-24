---
layout: default
title: "TRIDENT: Tri-Modal Molecular Representation Learning with Taxonomic Annotations and Local Correspondence"
---

# TRIDENT: Tri-Modal Molecular Representation Learning with Taxonomic Annotations and Local Correspondence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21028" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21028v1</a>
  <a href="https://arxiv.org/pdf/2506.21028.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21028v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21028v1', 'TRIDENT: Tri-Modal Molecular Representation Learning with Taxonomic Annotations and Local Correspondence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Jiang, Mangal Prakash, Hehuan Ma, Jianyuan Deng, Yuzhi Guo, Amina Mollaysa, Tommaso Mansi, Rui Liao, Junzhou Huang

**分类**: cs.LG

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出TRIDENT框架以整合多模态信息提升分子属性预测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子属性预测` `多模态学习` `SMILES` `文本描述` `分类注释` `对齐目标` `深度学习`

## 📋 核心要点

1. 现有方法在分子表示学习中未能充分利用文本和分类信息，导致功能属性预测的准确性不足。
2. TRIDENT框架通过整合分子SMILES、文本描述和分类注释，采用体积对齐和局部对齐目标来提升表示学习效果。
3. TRIDENT在11个下游任务上表现出色，展示了其在分子属性预测中的优越性，超越了现有的基线方法。

## 📝 摘要（中文）

分子属性预测旨在学习将化学结构映射到功能属性的表示。尽管多模态学习已成为学习分子表示的强大范式，但以往的研究在表示学习中大多忽视了分子的文本和分类信息。我们提出TRIDENT，一个新颖的框架，整合分子SMILES、文本描述和分类功能注释，以学习丰富的分子表示。为此，我们策划了一个包含结构化、多层次功能注释的分子-文本对的综合数据集。TRIDENT采用基于体积的对齐目标，联合对齐三模态特征，并引入局部对齐目标，捕捉分子子结构与其对应子文本描述之间的详细关系。TRIDENT在11个下游任务上实现了最先进的性能，展示了结合SMILES、文本和分类功能注释在分子属性预测中的价值。

## 🔬 方法详解

**问题定义**：本论文旨在解决分子属性预测中现有方法未能充分利用文本和分类信息的问题，导致功能属性预测的准确性和有效性不足。

**核心思路**：TRIDENT框架的核心思想是通过整合分子SMILES、文本描述和分类功能注释，采用体积对齐和局部对齐目标，来实现多模态特征的有效对齐，提升分子表示的丰富性和准确性。

**技术框架**：TRIDENT的整体架构包括数据集构建、三模态特征提取、体积对齐和局部对齐模块。数据集包含分子-文本对及其功能注释，特征提取通过深度学习模型实现，最后通过对齐模块进行特征的联合学习。

**关键创新**：TRIDENT的主要创新在于引入了基于体积的对齐目标和局部对齐目标，前者实现全局特征的几何感知对齐，后者则关注分子子结构与文本描述之间的细致关系，这在现有方法中尚未见到。

**关键设计**：在损失函数设计上，TRIDENT结合了全局和局部对齐损失，并采用动量机制动态平衡两者的影响，以便模型能够同时学习广泛的功能语义和细粒度的结构-功能映射。

## 📊 实验亮点

TRIDENT在11个下游任务上实现了最先进的性能，相较于基线方法，性能提升显著，展示了结合多模态信息在分子属性预测中的重要性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括药物发现、材料科学和化学信息学等。通过提高分子属性预测的准确性，TRIDENT可以帮助科学家更有效地识别和设计新材料及药物，从而加速相关领域的研究进展。

## 📄 摘要（原文）

> Molecular property prediction aims to learn representations that map chemical structures to functional properties. While multimodal learning has emerged as a powerful paradigm to learn molecular representations, prior works have largely overlooked textual and taxonomic information of molecules for representation learning. We introduce TRIDENT, a novel framework that integrates molecular SMILES, textual descriptions, and taxonomic functional annotations to learn rich molecular representations. To achieve this, we curate a comprehensive dataset of molecule-text pairs with structured, multi-level functional annotations. Instead of relying on conventional contrastive loss, TRIDENT employs a volume-based alignment objective to jointly align tri-modal features at the global level, enabling soft, geometry-aware alignment across modalities. Additionally, TRIDENT introduces a novel local alignment objective that captures detailed relationships between molecular substructures and their corresponding sub-textual descriptions. A momentum-based mechanism dynamically balances global and local alignment, enabling the model to learn both broad functional semantics and fine-grained structure-function mappings. TRIDENT achieves state-of-the-art performance on 11 downstream tasks, demonstrating the value of combining SMILES, textual, and taxonomic functional annotations for molecular property prediction.

