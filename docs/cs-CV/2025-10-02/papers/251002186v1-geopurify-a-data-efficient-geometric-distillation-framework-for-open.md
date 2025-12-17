---
layout: default
title: GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation
---

# GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02186" target="_blank" class="toolbar-btn">arXiv: 2510.02186v1</a>
    <a href="https://arxiv.org/pdf/2510.02186.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02186v1" 
            onclick="toggleFavorite(this, '2510.02186v1', 'GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Weijia Dou, Xu Zhang, Yi Bin, Jian Liu, Bo Peng, Guoqing Wang, Yang Yang, Heng Tao Shen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-02

**🔗 代码/项目**: [GITHUB](https://github.com/tj12323/GeoPurify)

---

## 💡 一句话要点

**GeoPurify通过几何蒸馏，以数据高效的方式实现开放词汇3D分割。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D语义分割` `开放词汇` `几何蒸馏` `数据高效` `视觉-语言模型`

## 📋 核心要点

1. 现有方法直接将2D特征投影到3D时，分割结果噪声大且不连贯，而强制几何一致性则需要大量标注数据。
2. GeoPurify利用3D自监督模型蒸馏出的几何先验，通过Student Affinity Network净化2D VLM生成的3D点特征。
3. 实验表明，GeoPurify仅使用少量训练数据，即可达到或超过现有最佳方法的效果，显著提升数据效率。

## 📝 摘要（中文）

本文提出了一种名为GeoPurify的几何蒸馏框架，用于开放词汇3D语义分割，旨在解决2D视觉-语言模型（VLM）特征迁移到3D分割时存在的难题。直接将2D特征投影到3D会导致预测结果噪声大且分散，而强制几何一致性又需要昂贵的训练流程和大规模标注的3D数据。作者认为，这种局限性源于主流的分割-匹配范式，该范式未能协调2D语义与3D几何结构。论文指出，几何线索并未在2D到3D的迁移过程中消除，而是潜藏在带噪声的、视角聚合的特征中。为了利用这一特性，GeoPurify应用一个小型Student Affinity Network，使用从3D自监督教师模型中蒸馏出的几何先验来净化2D VLM生成的3D点特征。在推理阶段，设计了一个几何引导的池化模块，以进一步去除点云噪声并确保语义和结构一致性。受益于潜在的几何信息和学习到的亲和力网络，GeoPurify有效地缓解了上述难题，并实现了卓越的数据效率。在主要3D基准测试上的大量实验表明，GeoPurify仅使用约1.5%的训练数据即可达到或超过最先进的性能。

## 🔬 方法详解

**问题定义**：现有方法在将2D视觉-语言模型的特征迁移到3D语义分割时，面临着语义信息和几何信息难以对齐的问题。直接将2D特征投影到3D空间会导致分割结果噪声较大，产生很多不连贯的区域。为了解决这个问题，一些方法尝试引入几何约束，但这通常需要大量的3D标注数据和复杂的训练流程，成本很高。因此，如何在数据量有限的情况下，有效地利用2D VLM的语义信息和3D几何信息，是本文要解决的核心问题。

**核心思路**：本文的核心思路是，虽然直接从2D投影到3D的特征包含噪声，但其中仍然蕴含着几何信息。因此，可以通过学习一个亲和力网络（Affinity Network），利用3D自监督模型提取的几何先验知识，来净化这些带噪声的特征，从而提高分割的准确性和连贯性。这种方法避免了直接依赖大规模3D标注数据，而是通过蒸馏的方式，将几何知识从3D自监督模型迁移到2D VLM特征中。

**技术框架**：GeoPurify框架主要包含两个阶段：特征净化和几何引导池化。首先，利用2D VLM提取的特征作为输入，通过一个Student Affinity Network，利用从3D自监督教师模型中蒸馏出的几何先验知识，对特征进行净化。然后，在推理阶段，使用一个Geometry-Guided Pooling模块，进一步去除点云噪声，并确保语义和结构的一致性。整个框架利用了2D VLM的语义信息和3D自监督模型的几何信息，通过蒸馏和净化，实现了数据高效的3D语义分割。

**关键创新**：本文最重要的技术创新点在于提出了GeoPurify框架，该框架通过几何蒸馏的方式，将3D自监督模型的几何先验知识迁移到2D VLM特征中，从而实现了数据高效的3D语义分割。与现有方法相比，GeoPurify不需要大规模的3D标注数据，而是通过学习一个亲和力网络，利用几何先验知识来净化特征，从而提高了分割的准确性和连贯性。

**关键设计**：Student Affinity Network是GeoPurify框架中的关键组件，它学习一个亲和力矩阵，用于表示点云中不同点之间的关系。这个亲和力矩阵是基于3D自监督教师模型提取的几何特征计算得到的。Geometry-Guided Pooling模块则利用学习到的亲和力矩阵，对点云进行池化操作，从而去除噪声并提高分割的准确性。损失函数的设计也至关重要，需要平衡语义分割的准确性和几何一致性。

## 📊 实验亮点

GeoPurify在ScanNet、S3DIS等主流3D基准数据集上进行了大量实验，结果表明，GeoPurify仅使用约1.5%的训练数据，即可达到或超过现有最佳方法的效果。例如，在ScanNet数据集上，GeoPurify的mIoU指标超过了现有最佳方法，证明了其卓越的数据效率和分割性能。

## 🎯 应用场景

GeoPurify在机器人导航、自动驾驶、三维场景理解等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，从而实现更安全、更高效的导航。在自动驾驶领域，GeoPurify可以提高车辆对周围环境的感知能力，从而提高驾驶安全性。此外，GeoPurify还可以应用于三维场景重建、虚拟现实等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent attempts to transfer features from 2D Vision-Language Models (VLMs) to 3D semantic segmentation expose a persistent trade-off. Directly projecting 2D features into 3D yields noisy and fragmented predictions, whereas enforcing geometric coherence necessitates costly training pipelines and large-scale annotated 3D data. We argue that this limitation stems from the dominant segmentation-and-matching paradigm, which fails to reconcile 2D semantics with 3D geometric structure. The geometric cues are not eliminated during the 2D-to-3D transfer but remain latent within the noisy and view-aggregated features. To exploit this property, we propose GeoPurify that applies a small Student Affinity Network to purify 2D VLM-generated 3D point features using geometric priors distilled from a 3D self-supervised teacher model. During inference, we devise a Geometry-Guided Pooling module to further denoise the point cloud and ensure the semantic and structural consistency. Benefiting from latent geometric information and the learned affinity network, GeoPurify effectively mitigates the trade-off and achieves superior data efficiency. Extensive experiments on major 3D benchmarks demonstrate that GeoPurify achieves or surpasses state-of-the-art performance while utilizing only about 1.5% of the training data. Our codes and checkpoints are available at [https://github.com/tj12323/GeoPurify](https://github.com/tj12323/GeoPurify).

