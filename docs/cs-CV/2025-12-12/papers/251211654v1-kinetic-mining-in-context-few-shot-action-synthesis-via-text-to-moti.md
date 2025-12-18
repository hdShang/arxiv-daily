---
layout: default
title: Kinetic Mining in Context: Few-Shot Action Synthesis via Text-to-Motion Distillation
---

# Kinetic Mining in Context: Few-Shot Action Synthesis via Text-to-Motion Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11654" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11654v1</a>
  <a href="https://arxiv.org/pdf/2512.11654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11654v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.11654v1', 'Kinetic Mining in Context: Few-Shot Action Synthesis via Text-to-Motion Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Cazzola, Ahed Alboody

**分类**: cs.CV

**发布日期**: 2025-12-12

**🔗 代码/项目**: [PROJECT_PAGE](https://lucazzola.github.io/publications/)

---

## 💡 一句话要点

**KineMIC：通过文本到动作蒸馏实现少样本动作合成，解决HAR数据稀缺问题。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `少样本学习` `动作合成` `文本到动作` `迁移学习` `人体活动识别` `扩散模型` `运动挖掘`

## 📋 核心要点

1. 现有HAR方法依赖大量标注数据，而T2M模型虽然能生成动作，但与HAR任务需求存在领域差异。
2. KineMIC利用文本编码空间的语义对应关系，通过运动挖掘策略，将通用T2M模型迁移到HAR领域。
3. 实验表明，KineMIC在少样本情况下显著提升了动作生成质量，并使HAR准确率提高了23.1%。

## 📝 摘要（中文）

针对基于骨骼的人体活动识别(HAR)中带标注的大型运动数据集获取成本高昂这一关键瓶颈，本文提出了一种名为KineMIC（情境中的运动挖掘）的迁移学习框架，用于少样本动作合成。KineMIC通过假设文本编码空间中的语义对应关系可以为运动学蒸馏提供软监督，从而将文本到动作(T2M)扩散模型适配到HAR领域。具体而言，通过一种运动挖掘策略，利用CLIP文本嵌入来建立稀疏HAR标签和T2M源数据之间的对应关系。该过程指导微调，将通用T2M骨干网络转换为专门的少样本动作到运动生成器。在HumanML3D（源T2M数据集）和NTU RGB+D 120子集（目标HAR领域）上验证了KineMIC，每个动作类别仅随机选择10个样本。实验结果表明，该方法生成了更连贯的动作，提供了一个强大的数据增强来源，实现了+23.1%的准确率提升。

## 🔬 方法详解

**问题定义**：现有基于骨骼的HAR方法严重依赖于大规模、带标注的运动数据集，而这些数据集的获取成本非常高昂。虽然文本到动作(T2M)生成模型提供了一种可扩展的合成数据来源，但其训练目标侧重于通用的艺术性运动，并且数据集结构与HAR对运动学精确、类别区分性动作的要求存在根本差异，导致领域鸿沟。

**核心思路**：KineMIC的核心思路是利用T2M模型中文本编码空间中蕴含的语义信息，通过迁移学习的方式，将通用的T2M模型适配到特定的HAR领域。它假设文本编码空间中的语义对应关系可以为运动学蒸馏提供软监督，从而指导T2M模型生成更适合HAR任务的动作。

**技术框架**：KineMIC框架主要包含以下几个阶段：1) 利用CLIP模型提取HAR标签和T2M数据的文本嵌入；2) 通过运动挖掘策略，建立HAR标签和T2M数据之间的对应关系，即找到与HAR标签语义最相关的T2M动作；3) 使用这些对应关系作为软监督，对T2M扩散模型进行微调，使其能够生成符合HAR任务需求的动作。

**关键创新**：KineMIC的关键创新在于提出了运动挖掘策略，该策略利用CLIP文本嵌入来建立稀疏HAR标签和T2M源数据之间的对应关系。这种方法能够有效地利用T2M模型中蕴含的语义信息，将其迁移到HAR领域，从而解决了HAR数据稀缺的问题。与直接使用T2M模型生成动作不同，KineMIC通过运动挖掘和微调，使得生成的动作更具运动学精确性和类别区分性。

**关键设计**：KineMIC的关键设计包括：1) 使用CLIP模型提取文本嵌入，以捕捉HAR标签和T2M数据之间的语义关系；2) 设计运动挖掘策略，通过计算文本嵌入之间的相似度，找到与HAR标签最相关的T2M动作；3) 使用扩散模型作为T2M骨干网络，并使用运动挖掘的结果作为软监督信号，对扩散模型进行微调。具体的损失函数可能包括重建损失、对抗损失以及基于运动学约束的损失项。

## 📊 实验亮点

KineMIC在NTU RGB+D 120数据集的子集上进行了验证，每个动作类别仅使用10个样本进行训练。实验结果表明，KineMIC能够生成更连贯的动作，并显著提高了HAR的准确率，相比于基线方法，实现了+23.1%的性能提升。这表明KineMIC在少样本情况下具有强大的动作合成能力，能够有效解决HAR数据稀缺的问题。

## 🎯 应用场景

KineMIC具有广泛的应用前景，例如在智能监控、人机交互、康复训练等领域。它可以用于生成各种人体活动，从而扩充训练数据集，提高HAR系统的性能。此外，KineMIC还可以用于生成特定场景下的动作，例如模拟老年人跌倒，帮助评估和改进安全措施。该研究有望推动HAR技术的发展，使其能够更好地应用于实际场景。

## 📄 摘要（原文）

> The acquisition cost for large, annotated motion datasets remains a critical bottleneck for skeletal-based Human Activity Recognition (HAR). Although Text-to-Motion (T2M) generative models offer a compelling, scalable source of synthetic data, their training objectives, which emphasize general artistic motion, and dataset structures fundamentally differ from HAR's requirements for kinematically precise, class-discriminative actions. This disparity creates a significant domain gap, making generalist T2M models ill-equipped for generating motions suitable for HAR classifiers. To address this challenge, we propose KineMIC (Kinetic Mining In Context), a transfer learning framework for few-shot action synthesis. KineMIC adapts a T2M diffusion model to an HAR domain by hypothesizing that semantic correspondences in the text encoding space can provide soft supervision for kinematic distillation. We operationalize this via a kinetic mining strategy that leverages CLIP text embeddings to establish correspondences between sparse HAR labels and T2M source data. This process guides fine-tuning, transforming the generalist T2M backbone into a specialized few-shot Action-to-Motion generator. We validate KineMIC using HumanML3D as the source T2M dataset and a subset of NTU RGB+D 120 as the target HAR domain, randomly selecting just 10 samples per action class. Our approach generates significantly more coherent motions, providing a robust data augmentation source that delivers a +23.1% accuracy points improvement. Animated illustrations and supplementary materials are available at (https://lucazzola.github.io/publications/kinemic).

