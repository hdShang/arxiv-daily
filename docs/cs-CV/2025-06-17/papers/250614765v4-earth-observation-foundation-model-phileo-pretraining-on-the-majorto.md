---
layout: default
title: "Earth Observation Foundation Model PhilEO: Pretraining on the MajorTOM and FastTOM Datasets"
---

# Earth Observation Foundation Model PhilEO: Pretraining on the MajorTOM and FastTOM Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14765" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14765v4</a>
  <a href="https://arxiv.org/pdf/2506.14765.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14765v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14765v4', 'Earth Observation Foundation Model PhilEO: Pretraining on the MajorTOM and FastTOM Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikolaos Dionelis, Riccardo Musto, Jente Bosmans, Simone Sarti, Giancarlo Paoletti, Sébastien Lefèvre, Bertrand Le Saux, Nicolas Longépé

**分类**: cs.CV

**发布日期**: 2025-06-17 (更新: 2025-09-23)

**备注**: 15 pages, 22 figures, 2 tables, 64 references

---

## 💡 一句话要点

**提出PhilEO以提升地球观测模型的预训练效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地球观测` `基础模型` `预训练` `U-Net` `视觉变换器` `Mamba模型` `下游任务` `数据集`

## 📋 核心要点

1. 现有的地球观测模型在处理大规模未标记数据时效率低下，难以充分利用卫星数据。
2. 本文提出在MajorTOM数据集上预训练基础模型，并探索不同网络架构的有效性，以提高下游任务的性能。
3. 实验结果表明，U-Net 200M-2T在道路和建筑任务中表现优异，且Mamba模型在计算开销上具有优势。

## 📝 摘要（中文）

当前，地球观测卫星生成大量数据。为了充分利用这些数据，必须在大型未标记数据集上预训练地球观测基础模型（FMs），以便在下游任务中实现高效的微调。本文研究了FMs的扩展，使用包含所有区域的MajorTOM 23TB数据集进行训练，结果显示其在与专门小型数据集预训练的模型相比，性能具有竞争力。额外的海洋和冰川数据并未降低在陆地任务上的表现。第二个贡献是探索U-Net卷积神经网络、视觉变换器（ViT）和Mamba状态空间模型作为FMs的应用。我们开发了多种不同架构的模型，并在PhilEO基准上进行微调，结果表明U-Net 200M-2T在大多数情况下优于其他模型。

## 🔬 方法详解

**问题定义**：本文旨在解决地球观测模型在大规模未标记数据集上的预训练效率低下的问题。现有方法往往依赖于较小的专门数据集，限制了模型的泛化能力。

**核心思路**：论文提出在包含全球范围数据的MajorTOM数据集上进行预训练，以提升模型在多样化下游任务中的表现。通过探索不同网络架构（如U-Net、ViT和Mamba），实现对局部和远程相关性的有效捕捉。

**技术框架**：整体架构包括数据预处理、模型训练和微调三个主要阶段。首先，使用MajorTOM数据集进行预训练，然后在PhilEO基准上进行微调，针对道路、建筑和土地覆盖等任务进行评估。

**关键创新**：最重要的创新在于通过大规模的全球数据集训练基础模型，证明了额外的海洋和冰川数据不会影响陆地任务的性能，拓宽了模型的应用范围。

**关键设计**：在模型设计中，采用了不同的参数设置和网络结构，特别是U-Net的200M-2T版本在多个下游任务中表现突出，同时Mamba模型在计算效率上也表现良好。实验中还评估了模型所需的浮点运算量（FLOPs）。

## 📊 实验亮点

实验结果显示，U-Net 200M-2T在道路和建筑任务中优于其他模型，尤其在n-shot学习场景下表现突出。同时，Mamba模型在计算开销上具有优势，提供了与现有模型相当的性能，展示了更高的效率。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、环境监测和灾害响应等。通过提升地球观测模型的预训练效率，可以更好地支持实时数据分析和决策制定，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Today, Earth Observation (EO) satellites generate massive volumes of data. To fully exploit this, it is essential to pretrain EO Foundation Models (FMs) on large unlabeled datasets, enabling efficient fine-tuning for downstream tasks with minimal labeled data. In this paper, we study scaling-up FMs: we train our models on the pretraining dataset MajorTOM 23TB which includes all regions, and the performance on average is competitive versus models pretrained on more specialized datasets which are substantially smaller and include only land. The additional data of oceans and ice do not decrease the performance on land-focused downstream tasks. These results indicate that large FMs trained on global datasets for a wider variety of downstream tasks can be useful for downstream applications that only require a subset of the information included in their training. The second contribution is the exploration of U-Net Convolutional Neural Network (CNN), Vision Transformers (ViT), and Mamba State-Space Models (SSM) as FMs. U-Net captures local correlations amongst pixels, while ViT and Mamba capture local and distant correlations. We develop various models using different architectures, including U-Net, ViT, and Mamba, and different number of parameters. We evaluate the FLoating-point OPerations (FLOPs) needed by the models. We fine-tune on the PhilEO Bench for different downstream tasks: roads, buildings, and land cover. For most n-shots for roads and buildings, U-Net 200M-2T outperforms the other models. Using Mamba, we achieve comparable results on the downstream tasks, with less computational expenses. We also compare with the recent FM TerraMind which we evaluate on PhilEO Bench.

