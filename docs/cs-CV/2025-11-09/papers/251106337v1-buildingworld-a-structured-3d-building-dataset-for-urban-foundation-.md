---
layout: default
title: "BuildingWorld: A Structured 3D Building Dataset for Urban Foundation Models"
---

# BuildingWorld: A Structured 3D Building Dataset for Urban Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06337" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06337v1</a>
  <a href="https://arxiv.org/pdf/2511.06337.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06337v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06337v1', 'BuildingWorld: A Structured 3D Building Dataset for Urban Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangfeng Huang, Ruisheng Wang, Xin Wang

**分类**: cs.CV

**发布日期**: 2025-11-09

---

## 💡 一句话要点

**BuildingWorld：构建用于城市基础模型的结构化3D建筑数据集**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D建筑数据集` `城市建模` `数字孪生` `LiDAR点云` `深度学习` `城市基础模型` `建筑重建` `语义分割`

## 📋 核心要点

1. 现有3D城市建模方法在建筑数据集上训练，建筑多样性不足，导致模型在异构城市环境中的泛化能力受限。
2. BuildingWorld通过构建一个包含全球多样建筑风格的结构化3D建筑数据集，弥合了风格多样性方面的差距。
3. 该数据集包含约五百万个LOD2建筑模型，附带真实和模拟的LiDAR点云，并提供标准化评估指标。

## 📝 摘要（中文）

随着数字孪生在现代城市转型中占据核心地位，准确且结构化的3D建筑模型成为构建高保真、可更新城市表示的关键。这些模型支撑着能源建模、城市规划、自动导航和实时推理等多种应用。然而，目前基于学习的模型大多在建筑数据集上训练，这些数据集的建筑多样性有限，严重削弱了模型在异构城市环境中的泛化能力。为了解决这一局限性，我们提出了BuildingWorld，一个综合性的结构化3D建筑数据集，旨在弥合风格多样性方面的差距。它涵盖了来自北美、欧洲、亚洲、非洲和大洋洲等地理和建筑风格多样的地区的建筑物，为城市级基础建模和分析提供了一个具有全球代表性的数据集。具体来说，BuildingWorld提供了约五百万个从不同来源收集的LOD2建筑模型，并附带真实和模拟的机载LiDAR点云。这使得对3D建筑重建、检测和分割的全面研究成为可能。我们还引入了一个虚拟城市模型Cyber City，以生成具有定制和结构多样性点云分布的无限训练数据。此外，我们提供了为建筑重建量身定制的标准化评估指标，旨在促进结构化3D城市环境中大规模视觉模型和基础模型的训练、评估和比较。

## 🔬 方法详解

**问题定义**：论文旨在解决现有3D建筑数据集建筑风格多样性不足的问题，这限制了基于学习的模型在异构城市环境中的泛化能力。现有方法难以处理不同地域和建筑风格的建筑重建、检测和分割任务。

**核心思路**：论文的核心思路是构建一个包含全球多样建筑风格的结构化3D建筑数据集BuildingWorld，该数据集涵盖了来自北美、欧洲、亚洲、非洲和大洋洲等地区的建筑物，从而提高模型在不同城市环境中的泛化能力。

**技术框架**：BuildingWorld数据集包含以下几个关键组成部分：1) 约五百万个LOD2建筑模型，从不同来源收集；2) 真实和模拟的机载LiDAR点云，用于3D建筑重建、检测和分割研究；3) 虚拟城市模型Cyber City，用于生成具有定制和结构多样性点云分布的无限训练数据；4) 为建筑重建量身定制的标准化评估指标，用于模型评估和比较。

**关键创新**：该论文的关键创新在于构建了一个具有全球代表性的、包含大量结构化3D建筑模型的数据集，并提供了相应的LiDAR点云和评估指标。与现有数据集相比，BuildingWorld在建筑风格多样性方面具有显著优势，更适合训练城市级基础模型。此外，Cyber City虚拟城市模型的引入，可以生成无限的训练数据，进一步提升模型的性能。

**关键设计**：BuildingWorld数据集的关键设计包括：1) LOD2建筑模型的选择，在保证细节的同时，降低了数据处理的复杂度；2) 真实和模拟LiDAR点云的结合，提供了更全面的训练数据；3) Cyber City虚拟城市模型的参数化设计，允许用户自定义点云分布，生成更具挑战性的训练数据；4) 标准化评估指标的设计，方便研究人员进行模型评估和比较。

## 📊 实验亮点

BuildingWorld数据集包含约五百万个LOD2建筑模型，覆盖全球多个地区，提供了真实和模拟的LiDAR点云。Cyber City虚拟城市模型可以生成无限的训练数据。该数据集为3D建筑重建、检测和分割等任务提供了丰富的资源，并为城市级基础模型的研究奠定了基础。

## 🎯 应用场景

BuildingWorld数据集可广泛应用于城市数字孪生、智慧城市建设、自动驾驶、城市规划、能源建模等领域。该数据集能够提升相关算法在不同城市环境下的泛化能力，促进城市级基础模型的发展，为城市智能化提供有力支撑，并为未来的城市可持续发展提供数据基础。

## 📄 摘要（原文）

> As digital twins become central to the transformation of modern cities, accurate and structured 3D building models emerge as a key enabler of high-fidelity, updatable urban representations. These models underpin diverse applications including energy modeling, urban planning, autonomous navigation, and real-time reasoning. Despite recent advances in 3D urban modeling, most learning-based models are trained on building datasets with limited architectural diversity, which significantly undermines their generalizability across heterogeneous urban environments. To address this limitation, we present BuildingWorld, a comprehensive and structured 3D building dataset designed to bridge the gap in stylistic diversity. It encompasses buildings from geographically and architecturally diverse regions -- including North America, Europe, Asia, Africa, and Oceania -- offering a globally representative dataset for urban-scale foundation modeling and analysis. Specifically, BuildingWorld provides about five million LOD2 building models collected from diverse sources, accompanied by real and simulated airborne LiDAR point clouds. This enables comprehensive research on 3D building reconstruction, detection and segmentation. Cyber City, a virtual city model, is introduced to enable the generation of unlimited training data with customized and structurally diverse point cloud distributions. Furthermore, we provide standardized evaluation metrics tailored for building reconstruction, aiming to facilitate the training, evaluation, and comparison of large-scale vision models and foundation models in structured 3D urban environments.

