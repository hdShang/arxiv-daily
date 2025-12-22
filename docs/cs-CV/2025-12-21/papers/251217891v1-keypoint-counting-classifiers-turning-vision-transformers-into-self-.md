---
layout: default
title: Keypoint Counting Classifiers: Turning Vision Transformers into Self-Explainable Models Without Training
---

# Keypoint Counting Classifiers: Turning Vision Transformers into Self-Explainable Models Without Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17891" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17891v1</a>
  <a href="https://arxiv.org/pdf/2512.17891.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17891v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17891v1', 'Keypoint Counting Classifiers: Turning Vision Transformers into Self-Explainable Models Without Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kristoffer Wickstrøm, Teresa Dorszewski, Siyan Chen, Michael Kampffmeyer, Elisabeth Wetzer, Robert Jenssen

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出无需训练的Keypoint Counting Classifiers，将ViT转化为自解释模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自解释模型` `Vision Transformer` `关键点检测` `可解释性` `人机交互`

## 📋 核心要点

1. 现有自解释模型训练复杂、架构特定，难以应用于ViT等通用基础模型。
2. 提出Keypoint Counting Classifiers (KCCs)，利用ViT自动识别的关键点，构建可解释的决策过程。
3. 实验表明，KCCs在人机交互方面优于现有基线，提升了ViT模型的透明性和可靠性。

## 📝 摘要（中文）

当前自解释模型（SEM）的设计方法需要复杂的训练过程和特定的架构，这使其不切实际。随着基于Vision Transformers（ViT）的通用基础模型的进步，这种不切实际的问题变得更加突出。因此，需要新的方法来为基于ViT的基础模型提供透明度和可靠性。本文提出了一种新的方法，可以将任何经过良好训练的基于ViT的模型转化为SEM，而无需重新训练，我们称之为Keypoint Counting Classifiers（KCCs）。最近的研究表明，ViT可以自动识别图像之间的高精度匹配关键点，我们在此基础上创建了一个易于解释的决策过程，该过程在输入中具有固有的可视化能力。我们进行了广泛的评估，结果表明，与最近的基线相比，KCCs改善了人机通信。我们认为，KCCs是使基于ViT的基础模型更加透明和可靠的重要一步。

## 🔬 方法详解

**问题定义**：现有自解释模型（SEM）的训练过程复杂，需要特定的网络架构，这使得它们难以应用于像Vision Transformers（ViT）这样的通用基础模型。因此，如何为预训练的ViT模型提供无需重新训练的自解释能力是一个关键问题。现有方法的痛点在于需要从头开始训练或者对现有模型进行微调，计算成本高昂，且可能破坏预训练模型的泛化能力。

**核心思路**：本文的核心思路是利用ViT模型本身所具备的关键点检测能力，构建一个基于关键点计数的分类器。通过统计图像中特定关键点的数量，并将其作为分类的依据，从而实现模型的自解释性。这种方法无需重新训练ViT模型，而是直接利用其已学习到的特征表示。

**技术框架**：KCCs方法主要包含以下几个阶段：1) 利用预训练的ViT模型提取图像的关键点特征；2) 对提取的关键点进行聚类，形成若干个关键点簇；3) 对于每个类别，统计图像中属于该类别对应关键点簇的关键点数量；4) 基于关键点数量进行分类决策。整体流程简单明了，易于实现和部署。

**关键创新**：KCCs最重要的创新在于它提供了一种无需重新训练即可将预训练ViT模型转化为自解释模型的方法。与现有方法相比，KCCs避免了复杂的训练过程和特定的网络架构设计，大大降低了计算成本和开发难度。此外，KCCs基于关键点计数进行分类，使得模型的决策过程具有高度的可解释性。

**关键设计**：KCCs的关键设计在于如何选择合适的关键点聚类算法以及如何确定每个类别对应的关键点簇。论文中可能使用了诸如K-means等聚类算法，并通过实验验证了不同聚类参数对模型性能的影响。此外，论文可能还探讨了如何利用先验知识或领域知识来指导关键点簇的选择，以进一步提高模型的准确性和可解释性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17891v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17891v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17891v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了KCCs在人机交互方面的优越性。与现有基线方法相比，KCCs能够提供更清晰、更易于理解的决策依据，从而显著改善人机通信效果。具体的性能数据和提升幅度需要在论文中查找，但整体而言，实验结果表明KCCs是一种有效的自解释模型构建方法。

## 🎯 应用场景

KCCs方法可广泛应用于需要模型可解释性的计算机视觉任务中，例如医疗图像诊断、自动驾驶决策、安全监控等领域。通过提供清晰的决策依据，KCCs可以增强用户对模型的信任，并促进人机协作。未来，KCCs有望成为提升AI系统透明度和可靠性的重要工具。

## 📄 摘要（原文）

> Current approaches for designing self-explainable models (SEMs) require complicated training procedures and specific architectures which makes them impractical. With the advance of general purpose foundation models based on Vision Transformers (ViTs), this impracticability becomes even more problematic. Therefore, new methods are necessary to provide transparency and reliability to ViT-based foundation models. In this work, we present a new method for turning any well-trained ViT-based model into a SEM without retraining, which we call Keypoint Counting Classifiers (KCCs). Recent works have shown that ViTs can automatically identify matching keypoints between images with high precision, and we build on these results to create an easily interpretable decision process that is inherently visualizable in the input. We perform an extensive evaluation which show that KCCs improve the human-machine communication compared to recent baselines. We believe that KCCs constitute an important step towards making ViT-based foundation models more transparent and reliable.

