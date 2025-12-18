---
layout: default
title: NAUTILUS: A Large Multimodal Model for Underwater Scene Understanding
---

# NAUTILUS: A Large Multimodal Model for Underwater Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27481" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27481v1</a>
  <a href="https://arxiv.org/pdf/2510.27481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27481v1', 'NAUTILUS: A Large Multimodal Model for Underwater Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Xu, Cheng Wang, Dingkang Liang, Zongchuang Zhao, Xingyu Jiang, Peng Zhang, Xiang Bai

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: Accepted to NeurIPS 2025. Data and models are available at https://github.com/H-EmbodVis/NAUTILUS

**🔗 代码/项目**: [GITHUB](https://github.com/H-EmbodVis/NAUTILUS)

---

## 💡 一句话要点

**NAUTILUS：用于水下场景理解的大型多模态模型，提升水下任务鲁棒性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水下场景理解` `多模态模型` `视觉特征增强` `水下图像处理` `大型语言模型` `指令调优` `数据集构建` `物理先验`

## 📋 核心要点

1. 水下场景理解面临缺乏大规模多任务数据集的挑战，限制了相关研究的进展。
2. 论文提出NAUTILUS，通过构建NautData数据集和引入视觉特征增强模块VFE来提升水下场景理解的鲁棒性。
3. 实验结果表明，VFE模块能有效提升LLaVA-1.5和Qwen2.5-VL在水下任务上的性能，验证了NAUTILUS的优越性。

## 📝 摘要（中文）

水下探索为我们星球提供了重要的见解，并在资源勘探、国家安全等领域引起了越来越多的关注。本文研究了水下场景理解方法，旨在实现自动水下探索。水下场景理解任务需要多粒度的多任务感知。然而，缺乏大规模的水下多任务指令调优数据集阻碍了这项研究的进展。为了弥合这一差距，我们构建了NautData，一个包含145万个图像-文本对的数据集，支持八个水下场景理解任务，从而能够开发和全面评估水下场景理解模型。水下图像退化是一个公认的挑战，它干扰了水下任务。为了提高水下场景理解的鲁棒性，我们引入了源自水下成像模型的物理先验，并提出了一个即插即用的视觉特征增强（VFE）模块，该模块显式地恢复清晰的水下信息。我们将此模块集成到著名的基线LLaVA-1.5和Qwen2.5-VL中，并构建了我们的水下LMM，NAUTILUS。在NautData和公共水下数据集上进行的实验表明，VFE模块的有效性，始终如一地提高了两个基线在大多数支持任务上的性能，从而确保了NAUTILUS在水下场景理解领域的优越性。

## 🔬 方法详解

**问题定义**：水下场景理解任务需要多粒度的多任务感知能力，但现有方法受限于缺乏大规模水下多任务指令调优数据集，并且水下图像质量差，存在严重的图像退化问题，影响了模型的性能和鲁棒性。现有方法难以有效利用水下成像的物理先验知识来提升图像质量和特征表达。

**核心思路**：论文的核心思路是构建一个大规模的水下多任务数据集NautData，并设计一个即插即用的视觉特征增强（VFE）模块，利用水下成像的物理先验知识来恢复清晰的水下信息，从而提高水下场景理解模型的性能和鲁棒性。通过将VFE模块集成到现有的LLM中，可以有效提升模型在水下环境下的表现。

**技术框架**：NAUTILUS的整体框架包括数据构建和模型构建两部分。首先，构建包含145万图像-文本对的NautData数据集，支持八个水下场景理解任务。然后，设计VFE模块，该模块利用水下成像模型中的物理先验知识来增强视觉特征。最后，将VFE模块集成到LLaVA-1.5和Qwen2.5-VL等大型多模态模型中，进行指令调优，得到NAUTILUS模型。

**关键创新**：论文的关键创新在于：1) 构建了大规模的水下多任务数据集NautData，为水下场景理解研究提供了数据基础。2) 提出了VFE模块，该模块利用水下成像的物理先验知识来显式地恢复清晰的水下信息，从而提高了模型的鲁棒性。3) 将VFE模块以即插即用的方式集成到现有的大型多模态模型中，实现了水下场景理解能力的提升。

**关键设计**：VFE模块的关键设计在于利用水下成像模型中的衰减系数、散射光等物理参数作为先验知识，通过特定的网络结构来估计和补偿图像中的退化效应。具体实现细节（如网络结构、损失函数等）在论文中未详细描述，属于未知信息。NautData数据集的构建细节，包括数据增强方法和任务定义，也需要参考论文原文。

## 📊 实验亮点

实验结果表明，VFE模块能够显著提升LLaVA-1.5和Qwen2.5-VL在NautData和公共水下数据集上的性能。在大多数支持的任务上，VFE模块都带来了性能提升，验证了NAUTILUS在水下场景理解方面的优越性。具体的性能提升幅度需要参考论文中的实验数据。

## 🎯 应用场景

NAUTILUS在水下机器人、水下资源勘探、海洋环境监测、水下考古、水下搜救等领域具有广泛的应用前景。该研究可以帮助实现自动化的水下探索和作业，提高水下任务的效率和安全性，并为海洋科学研究提供更强大的工具。

## 📄 摘要（原文）

> Underwater exploration offers critical insights into our planet and attracts increasing attention for its broader applications in resource exploration, national security, etc. We study the underwater scene understanding methods, which aim to achieve automated underwater exploration. The underwater scene understanding task demands multi-task perceptions from multiple granularities. However, the absence of large-scale underwater multi-task instruction-tuning datasets hinders the progress of this research. To bridge this gap, we construct NautData, a dataset containing 1.45 M image-text pairs supporting eight underwater scene understanding tasks. It enables the development and thorough evaluation of the underwater scene understanding models. Underwater image degradation is a widely recognized challenge that interferes with underwater tasks. To improve the robustness of underwater scene understanding, we introduce physical priors derived from underwater imaging models and propose a plug-and-play vision feature enhancement (VFE) module, which explicitly restores clear underwater information. We integrate this module into renowned baselines LLaVA-1.5 and Qwen2.5-VL and build our underwater LMM, NAUTILUS. Experiments conducted on the NautData and public underwater datasets demonstrate the effectiveness of the VFE module, consistently improving the performance of both baselines on the majority of supported tasks, thus ensuring the superiority of NAUTILUS in the underwater scene understanding area. Data and models are available at https://github.com/H-EmbodVis/NAUTILUS.

