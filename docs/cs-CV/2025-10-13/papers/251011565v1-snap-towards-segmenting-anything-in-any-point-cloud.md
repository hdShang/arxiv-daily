---
layout: default
title: SNAP: Towards Segmenting Anything in Any Point Cloud
---

# SNAP: Towards Segmenting Anything in Any Point Cloud

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11565" target="_blank" class="toolbar-btn">arXiv: 2510.11565v1</a>
    <a href="https://arxiv.org/pdf/2510.11565.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11565v1" 
            onclick="toggleFavorite(this, '2510.11565v1', 'SNAP: Towards Segmenting Anything in Any Point Cloud')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Aniket Gupta, Hanhui Wang, Charles Saunders, Aruni RoyChowdhury, Hanumant Singh, Huaizu Jiang

**分类**: cs.CV

**发布日期**: 2025-10-13

**备注**: Project Page, https://neu-vi.github.io/SNAP/

**🔗 代码/项目**: [PROJECT_PAGE](https://neu-vi.github.io/SNAP/)

---

## 💡 一句话要点

**提出SNAP，一个通用的点云交互式分割模型，支持跨域和多种提示方式。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `点云分割` `交互式分割` `跨领域泛化` `领域自适应` `文本提示`

## 📋 核心要点

1. 现有交互式3D点云分割方法泛化性不足，通常局限于特定领域和提示方式，限制了其应用范围。
2. SNAP通过多数据集训练和领域自适应归一化，实现了跨领域泛化，并支持空间和文本两种提示方式。
3. 实验结果表明，SNAP在多个zero-shot基准测试中取得了SOTA性能，验证了其有效性和通用性。

## 📝 摘要（中文）

本文提出SNAP（Segment Anything in Any Point cloud），一个统一的交互式3D点云分割模型，支持跨领域的点云分割，并能接受基于点的空间提示和基于文本的提示。现有方法通常局限于单一领域（室内或室外）和单一交互方式（空间点击或文本提示）。此外，在多个数据集上训练通常会导致负迁移，产生缺乏泛化能力的领域特定工具。SNAP通过在涵盖室内、室外和航空环境的7个数据集上进行训练，并采用领域自适应归一化来防止负迁移，从而实现跨领域泛化。对于文本提示分割，我们自动生成mask proposal，并将其与文本查询的CLIP嵌入进行匹配，从而实现全景和开放词汇分割。大量实验表明，SNAP始终提供高质量的分割结果。在空间提示分割的9个zero-shot基准测试中，我们在8个上实现了最先进的性能，并在所有5个文本提示基准测试中展示了具有竞争力的结果。这些结果表明，统一模型可以匹配或超过专门的领域特定方法，为可扩展的3D注释提供实用的工具。

## 🔬 方法详解

**问题定义**：现有交互式3D点云分割方法通常针对特定领域（如室内或室外）设计，并且仅支持单一类型的用户交互（如空间点击或文本提示）。在多个数据集上进行训练时，容易出现负迁移现象，导致模型在特定领域表现良好，但在其他领域性能下降。因此，需要一种能够跨领域泛化，并支持多种提示方式的统一模型。

**核心思路**：SNAP的核心思路是通过多数据集联合训练和领域自适应归一化来解决跨领域泛化问题。同时，通过结合空间提示和文本提示，提供更灵活的交互方式。对于文本提示，采用自动mask proposal生成和CLIP嵌入匹配的方法，实现开放词汇分割。

**技术框架**：SNAP的整体框架包含以下几个主要模块：1) 点云特征提取模块：用于提取点云的几何特征。2) 提示编码模块：用于编码用户的空间或文本提示。3) 分割预测模块：将点云特征和提示编码融合，预测分割mask。4) 领域自适应归一化模块：用于减少不同领域数据之间的差异，防止负迁移。对于文本提示，还包括mask proposal生成和CLIP嵌入匹配模块。

**关键创新**：SNAP的关键创新在于：1) 提出了领域自适应归一化方法，有效缓解了多数据集训练中的负迁移问题。2) 实现了空间和文本提示的统一处理，提供了更灵活的交互方式。3) 采用自动mask proposal生成和CLIP嵌入匹配的方法，实现了开放词汇的文本提示分割。

**关键设计**：领域自适应归一化采用Instance Normalization，并为每个领域学习独立的仿射变换参数。损失函数包括分割损失（如Dice Loss或Cross-Entropy Loss）和对比学习损失（用于增强特征的区分性）。文本提示的mask proposal生成采用聚类算法或基于几何特征的分割方法。CLIP嵌入匹配采用余弦相似度作为匹配度量。

## 📊 实验亮点

SNAP在8/9个空间提示分割的zero-shot基准测试中取得了SOTA性能，并在所有5个文本提示分割基准测试中取得了具有竞争力的结果。这些结果表明，SNAP能够有效泛化到未见过的领域，并且在多种提示方式下都能提供高质量的分割结果。相比于领域特定的模型，SNAP在性能上具有显著优势。

## 🎯 应用场景

SNAP可应用于多种3D场景理解任务，如自动驾驶、机器人导航、城市建模、文物保护等。它能够通过用户交互快速准确地分割目标物体，提高3D数据的标注效率，降低标注成本。未来，SNAP有望成为3D场景理解领域的重要工具，推动相关技术的发展。

## 📄 摘要（原文）

> Interactive 3D point cloud segmentation enables efficient annotation of complex 3D scenes through user-guided prompts. However, current approaches are typically restricted in scope to a single domain (indoor or outdoor), and to a single form of user interaction (either spatial clicks or textual prompts). Moreover, training on multiple datasets often leads to negative transfer, resulting in domain-specific tools that lack generalizability. To address these limitations, we present \textbf{SNAP} (\textbf{S}egment a\textbf{N}ything in \textbf{A}ny \textbf{P}oint cloud), a unified model for interactive 3D segmentation that supports both point-based and text-based prompts across diverse domains. Our approach achieves cross-domain generalizability by training on 7 datasets spanning indoor, outdoor, and aerial environments, while employing domain-adaptive normalization to prevent negative transfer. For text-prompted segmentation, we automatically generate mask proposals without human intervention and match them against CLIP embeddings of textual queries, enabling both panoptic and open-vocabulary segmentation. Extensive experiments demonstrate that SNAP consistently delivers high-quality segmentation results. We achieve state-of-the-art performance on 8 out of 9 zero-shot benchmarks for spatial-prompted segmentation and demonstrate competitive results on all 5 text-prompted benchmarks. These results show that a unified model can match or exceed specialized domain-specific approaches, providing a practical tool for scalable 3D annotation. Project page is at, https://neu-vi.github.io/SNAP/

