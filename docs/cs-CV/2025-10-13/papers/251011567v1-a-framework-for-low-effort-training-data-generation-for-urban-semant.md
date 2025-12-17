---
layout: default
title: A Framework for Low-Effort Training Data Generation for Urban Semantic Segmentation
---

# A Framework for Low-Effort Training Data Generation for Urban Semantic Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11567" target="_blank" class="toolbar-btn">arXiv: 2510.11567v1</a>
    <a href="https://arxiv.org/pdf/2510.11567.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11567v1" 
            onclick="toggleFavorite(this, '2510.11567v1', 'A Framework for Low-Effort Training Data Generation for Urban Semantic Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Denis Zavadski, Damjan Kalšan, Tim Küchler, Haebom Lee, Stefan Roth, Carsten Rother

**分类**: cs.CV, cs.GR, cs.LG

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**提出基于扩散模型的低成本训练数据生成框架，提升城市语义分割性能。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `城市语义分割` `合成数据生成` `扩散模型` `领域自适应` `低成本训练数据`

## 📋 核心要点

1. 现有方法在利用合成数据训练城市语义分割模型时，存在与真实图像的领域差距，限制了下游性能。
2. 该框架利用扩散模型，通过伪标签将合成数据适配到目标领域，生成高保真、目标对齐的图像。
3. 实验表明，该方法在多个数据集上取得了显著的分割性能提升，证明了低成本合成数据的有效性。

## 📝 摘要（中文）

本文提出了一种新的框架，该框架利用扩散模型，仅使用不完善的伪标签，即可将模型适配到目标领域。训练完成后，该框架能够从任何合成数据集的语义地图生成高保真、目标对齐的图像，包括那些低成本、快速构建的数据集。该方法过滤次优生成结果，校正图像-标签错位，并标准化跨数据集的语义，从而将弱合成数据转化为具有竞争力的真实领域训练集。在五个合成数据集和两个真实目标数据集上的实验表明，与最先进的转换方法相比，分割性能提升高达+8.0%pt mIoU。这使得快速构建的合成数据集与需要大量人工设计的高成本、耗时合成数据集一样有效。这项工作突出了一个有价值的协作模式，即快速语义原型设计与生成模型相结合，能够为城市场景理解实现可扩展、高质量的训练数据创建。

## 🔬 方法详解

**问题定义**：论文旨在解决城市语义分割中，使用合成数据训练模型时，合成数据与真实数据之间存在的领域差距问题。现有方法，如直接使用合成数据或使用图像转换方法，无法有效弥合这一差距，导致模型在真实数据上的性能下降。高精度的合成数据制作成本高昂，无法满足低成本训练数据的需求。

**核心思路**：论文的核心思路是利用扩散模型强大的生成能力，将低成本合成数据集的语义信息转化为高保真、目标领域对齐的图像。通过在目标领域数据上训练扩散模型，使其能够学习到目标领域的图像风格和特征分布，从而生成更逼真的合成数据。

**技术框架**：该框架主要包含以下几个阶段：1) 使用低成本的合成数据集生成语义地图；2) 使用扩散模型，将语义地图转换为图像，扩散模型在目标领域数据上进行训练，以学习目标领域的图像风格；3) 对生成的图像进行过滤，去除质量较差的图像；4) 对图像和标签进行校正，以解决图像-标签错位问题；5) 对不同数据集的语义进行标准化，以保证语义的一致性。

**关键创新**：该方法最重要的创新点在于利用扩散模型进行图像生成，从而能够生成高保真、目标领域对齐的合成数据。与传统的图像转换方法相比，扩散模型能够更好地捕捉目标领域的图像风格和特征分布，从而生成更逼真的图像。此外，该方法还提出了一系列后处理步骤，如图像过滤、图像-标签校正和语义标准化，以进一步提高合成数据的质量。

**关键设计**：扩散模型采用标准的U-Net结构，损失函数采用标准的扩散模型训练损失。图像过滤采用基于图像质量评估指标的方法，如FID score。图像-标签校正采用基于光流的方法，对图像和标签进行对齐。语义标准化采用语义映射的方法，将不同数据集的语义映射到统一的语义空间。

## 📊 实验亮点

实验结果表明，该方法在五个合成数据集和两个真实目标数据集上取得了显著的分割性能提升，与最先进的转换方法相比，分割性能提升高达+8.0%pt mIoU。这表明，通过该方法生成的低成本合成数据集，可以达到甚至超过高成本合成数据集的性能。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人导航、城市规划等领域。通过低成本生成高质量的训练数据，可以降低模型训练的成本和时间，加速相关技术的研发和应用。该方法还可用于生成特定场景下的合成数据，例如恶劣天气、光照不足等情况，从而提高模型在复杂环境下的鲁棒性。

## 📄 摘要（原文）

> Synthetic datasets are widely used for training urban scene recognition models, but even highly realistic renderings show a noticeable gap to real imagery. This gap is particularly pronounced when adapting to a specific target domain, such as Cityscapes, where differences in architecture, vegetation, object appearance, and camera characteristics limit downstream performance. Closing this gap with more detailed 3D modelling would require expensive asset and scene design, defeating the purpose of low-cost labelled data. To address this, we present a new framework that adapts an off-the-shelf diffusion model to a target domain using only imperfect pseudo-labels. Once trained, it generates high-fidelity, target-aligned images from semantic maps of any synthetic dataset, including low-effort sources created in hours rather than months. The method filters suboptimal generations, rectifies image-label misalignments, and standardises semantics across datasets, transforming weak synthetic data into competitive real-domain training sets. Experiments on five synthetic datasets and two real target datasets show segmentation gains of up to +8.0%pt. mIoU over state-of-the-art translation methods, making rapidly constructed synthetic datasets as effective as high-effort, time-intensive synthetic datasets requiring extensive manual design. This work highlights a valuable collaborative paradigm where fast semantic prototyping, combined with generative models, enables scalable, high-quality training data creation for urban scene understanding.

