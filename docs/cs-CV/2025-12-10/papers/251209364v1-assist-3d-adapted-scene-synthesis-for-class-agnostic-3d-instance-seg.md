---
layout: default
title: ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation
---

# ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09364" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09364v1</a>
  <a href="https://arxiv.org/pdf/2512.09364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09364v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09364v1', 'ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengchao Zhou, Jiehong Lin, Jiahui Liu, Shizhen Zhao, Chirui Chang, Xiaojuan Qi

**分类**: cs.CV

**发布日期**: 2025-12-10

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**ASSIST-3D：用于类别无关3D实例分割的自适应场景合成**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D实例分割` `场景合成` `数据增强` `大型语言模型` `点云` `机器人` `计算机视觉`

## 📋 核心要点

1. 类别无关3D实例分割面临缺乏标注数据和现有方法泛化性差的挑战。
2. ASSIST-3D通过异构对象选择、LLM引导的场景布局和真实点云构建来合成高质量训练数据。
3. 实验表明，使用ASSIST-3D生成的数据训练的模型在多个数据集上显著优于现有方法。

## 📝 摘要（中文）

本文提出了一种名为ASSIST-3D的自适应3D场景合成流程，用于类别无关的3D实例分割，旨在合成合适的数据以增强模型的泛化能力。现有方法由于缺乏带标注的3D场景数据或2D分割的噪声而难以泛化。虽然合成数据生成提供了一个有希望的解决方案，但现有的3D场景合成方法无法同时满足几何多样性、上下文复杂性和布局合理性，而这些对于该任务至关重要。ASSIST-3D具有三个关键创新：1) 从广泛的3D CAD资产集合中进行异构对象选择，在对象采样中加入随机性以最大化几何和上下文多样性；2) 通过LLM引导的空间推理结合深度优先搜索来生成合理的物体布局；3) 通过多视角RGB-D图像渲染和融合来构建逼真的点云，从而紧密模仿真实世界的传感器数据采集。在ScanNetV2、ScanNet++和S3DIS基准上的实验表明，使用ASSIST-3D生成的数据训练的模型明显优于现有方法。进一步的比较突出了我们专门构建的流程优于现有的3D场景合成方法。

## 🔬 方法详解

**问题定义**：类别无关的3D实例分割旨在分割场景中所有对象实例，包括之前未见过的对象，而不依赖于语义类别信息。现有方法由于缺乏带标注的3D场景数据，或者依赖于有噪声的2D分割结果，导致泛化能力不足。现有的3D场景合成方法难以同时保证几何多样性、上下文复杂性和布局合理性，这限制了合成数据对模型训练的有效性。

**核心思路**：ASSIST-3D的核心思路是通过一个专门设计的3D场景合成流程，生成高质量的合成数据，用于训练类别无关的3D实例分割模型。该流程旨在克服现有合成方法的局限性，同时满足几何多样性、上下文复杂性和布局合理性的要求。通过在合成数据上进行训练，提高模型在真实世界场景中的泛化能力。

**技术框架**：ASSIST-3D包含三个主要模块：1) 异构对象选择：从大量的3D CAD模型库中随机选择对象，以增加几何和上下文的多样性。2) 场景布局生成：利用大型语言模型（LLM）进行空间推理，结合深度优先搜索算法，生成合理的物体布局。3) 真实点云构建：通过多视角RGB-D图像渲染和融合，生成逼真的点云数据，模拟真实传感器的数据采集过程。

**关键创新**：ASSIST-3D的关键创新在于其定制化的3D场景合成流程，该流程专门为类别无关的3D实例分割任务设计。与现有的通用3D场景合成方法相比，ASSIST-3D更加关注几何多样性、上下文复杂性和布局合理性，从而生成更适合模型训练的数据。此外，利用LLM进行空间推理也是一个重要的创新点，可以生成更符合人类直觉的场景布局。

**关键设计**：在异构对象选择中，采用了随机采样策略，以最大化几何和上下文的多样性。在场景布局生成中，LLM被用于指导物体的位置和方向，深度优先搜索算法用于确保物体之间的合理关系。在真实点云构建中，采用了多视角渲染和融合技术，以生成具有真实感的点云数据。具体的参数设置和损失函数细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，使用ASSIST-3D生成的数据训练的模型在ScanNetV2、ScanNet++和S3DIS等数据集上显著优于现有方法。例如，在ScanNetV2数据集上，使用ASSIST-3D训练的模型在类别无关的3D实例分割任务上取得了显著的性能提升（具体数值未知）。与其他3D场景合成方法相比，ASSIST-3D也表现出明显的优势。

## 🎯 应用场景

ASSIST-3D生成的合成数据可用于训练各种3D场景理解模型，例如机器人导航、自动驾驶、室内场景重建等。通过提高模型在未见过的场景和对象上的泛化能力，可以显著提升这些应用在实际环境中的性能和可靠性。未来，该技术可以扩展到其他3D视觉任务，例如3D目标检测和语义分割。

## 📄 摘要（原文）

> Class-agnostic 3D instance segmentation tackles the challenging task of segmenting all object instances, including previously unseen ones, without semantic class reliance. Current methods struggle with generalization due to the scarce annotated 3D scene data or noisy 2D segmentations. While synthetic data generation offers a promising solution, existing 3D scene synthesis methods fail to simultaneously satisfy geometry diversity, context complexity, and layout reasonability, each essential for this task. To address these needs, we propose an Adapted 3D Scene Synthesis pipeline for class-agnostic 3D Instance SegmenTation, termed as ASSIST-3D, to synthesize proper data for model generalization enhancement. Specifically, ASSIST-3D features three key innovations, including 1) Heterogeneous Object Selection from extensive 3D CAD asset collections, incorporating randomness in object sampling to maximize geometric and contextual diversity; 2) Scene Layout Generation through LLM-guided spatial reasoning combined with depth-first search for reasonable object placements; and 3) Realistic Point Cloud Construction via multi-view RGB-D image rendering and fusion from the synthetic scenes, closely mimicking real-world sensor data acquisition. Experiments on ScanNetV2, ScanNet++, and S3DIS benchmarks demonstrate that models trained with ASSIST-3D-generated data significantly outperform existing methods. Further comparisons underscore the superiority of our purpose-built pipeline over existing 3D scene synthesis approaches.

