---
layout: default
title: On-Device Continual Learning for Unsupervised Visual Anomaly Detection in Dynamic Manufacturing
---

# On-Device Continual Learning for Unsupervised Visual Anomaly Detection in Dynamic Manufacturing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13497" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13497v1</a>
  <a href="https://arxiv.org/pdf/2512.13497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13497v1" onclick="toggleFavorite(this, '2512.13497v1', 'On-Device Continual Learning for Unsupervised Visual Anomaly Detection in Dynamic Manufacturing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Ren, Kay Koehle, Kirill Dorofeev, Darko Anicic

**分类**: cs.LG, cs.CV

**发布日期**: 2025-12-15

**备注**: Accepted by European Conference on EDGE AI Technologies and Applications (EEAI) 2025

---

## 💡 一句话要点

**提出基于设备端持续学习的PatchCore改进方法，用于动态制造中的无监督视觉异常检测。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉异常检测` `持续学习` `设备端学习` `智能制造` `PatchCore` `无监督学习` `动态环境`

## 📋 核心要点

1. 传统VAD方法难以适应动态制造环境中频繁的产品变更，且边缘设备算力有限，无法支持大型模型和频繁的云端重训练。
2. 提出一种基于设备端持续学习的PatchCore改进方法，利用轻量级特征提取器和增量式coreset更新机制，实现快速自适应和内存高效。
3. 实验表明，该方法在工业用例中AUROC提升12%，内存占用减少80%，训练速度优于批量重训练，适用于动态智能制造。

## 📝 摘要（中文）

在现代制造业中，视觉异常检测（VAD）对于自动化检测和一致的产品质量至关重要。然而，日益动态和灵活的生产环境带来了关键挑战：首先，小批量和按需制造中频繁的产品变更需要快速的模型更新；其次，传统边缘硬件缺乏训练和运行大型AI模型的资源；最后，异常和正常的训练数据通常都很稀缺，特别是对于新引入的产品变体。本文研究了用于无监督VAD与定位的设备端持续学习，扩展了PatchCore以结合在线学习，从而适应真实的工业场景。所提出的方法利用轻量级特征提取器和基于k-中心选择的增量式coreset更新机制，从而能够从有限的数据中进行快速、内存高效的自适应，同时消除了昂贵的云端重新训练。在工业用例中，使用旨在模拟灵活生产的测试平台进行了评估，该测试平台在受控环境中频繁进行变体更改。我们的方法比基线实现了12%的AUROC改进，内存使用量减少了80%，并且训练速度比批量重新训练更快。这些结果证实，我们的方法提供了准确、资源高效且自适应的VAD，适用于动态和智能制造。

## 🔬 方法详解

**问题定义**：论文旨在解决动态制造环境中，视觉异常检测模型难以适应频繁产品变更、边缘设备算力不足以及训练数据稀缺的问题。现有方法通常需要大量的计算资源和数据，无法在边缘设备上进行快速部署和更新，导致检测精度下降和响应延迟。

**核心思路**：论文的核心思路是利用设备端持续学习，使模型能够逐步适应新的产品变体，而无需从头开始重新训练。通过轻量级的特征提取器和增量式coreset更新机制，减少计算和存储开销，实现快速、高效的在线学习。

**技术框架**：该方法基于PatchCore框架，主要包含以下几个模块：1) 轻量级特征提取器，用于提取图像的局部特征；2) Coreset选择模块，基于k-中心选择算法，选择最具代表性的正常样本，构建coreset；3) 异常检测模块，通过比较输入图像的特征与coreset中的特征，判断是否存在异常。在持续学习过程中，新的正常样本会逐步添加到coreset中，从而使模型能够适应新的产品变体。

**关键创新**：该方法的关键创新在于将持续学习引入到PatchCore框架中，并设计了一种增量式的coreset更新机制。传统的PatchCore需要离线训练，无法适应动态变化的环境。而该方法通过在线学习，能够逐步适应新的产品变体，并保持较高的检测精度。此外，轻量级特征提取器和coreset选择机制也降低了计算和存储开销，使其能够在边缘设备上运行。

**关键设计**：在coreset选择方面，采用了k-中心选择算法，选择最具代表性的正常样本，以减少coreset的大小，并提高检测精度。在特征提取方面，使用了轻量级的卷积神经网络，以降低计算开销。在损失函数方面，使用了基于距离的异常评分函数，通过比较输入图像的特征与coreset中的特征，计算异常得分。

## 📊 实验亮点

实验结果表明，该方法在工业用例中取得了显著的性能提升。与基线方法相比，AUROC提高了12%，内存使用量减少了80%，训练速度也更快。这些结果表明，该方法能够有效地适应动态制造环境，并提供准确、资源高效的视觉异常检测。

## 🎯 应用场景

该研究成果可广泛应用于智能制造领域，例如产品质量检测、缺陷识别、设备故障诊断等。通过在生产线上部署该方法，可以实现实时的异常检测和预警，提高产品质量和生产效率，降低生产成本。此外，该方法还可应用于其他需要持续学习和在线自适应的场景，例如智能监控、自动驾驶等。

## 📄 摘要（原文）

> In modern manufacturing, Visual Anomaly Detection (VAD) is essential for automated inspection and consistent product quality. Yet, increasingly dynamic and flexible production environments introduce key challenges: First, frequent product changes in small-batch and on-demand manufacturing require rapid model updates. Second, legacy edge hardware lacks the resources to train and run large AI models. Finally, both anomalous and normal training data are often scarce, particularly for newly introduced product variations. We investigate on-device continual learning for unsupervised VAD with localization, extending the PatchCore to incorporate online learning for real-world industrial scenarios. The proposed method leverages a lightweight feature extractor and an incremental coreset update mechanism based on k-center selection, enabling rapid, memory-efficient adaptation from limited data while eliminating costly cloud retraining. Evaluations on an industrial use case are conducted using a testbed designed to emulate flexible production with frequent variant changes in a controlled environment. Our method achieves a 12% AUROC improvement over the baseline, an 80% reduction in memory usage, and faster training compared to batch retraining. These results confirm that our method delivers accurate, resource-efficient, and adaptive VAD suitable for dynamic and smart manufacturing.

