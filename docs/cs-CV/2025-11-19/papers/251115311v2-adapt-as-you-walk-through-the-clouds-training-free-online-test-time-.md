---
layout: default
title: Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models
---

# Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15311" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15311v2</a>
  <a href="https://arxiv.org/pdf/2511.15311.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15311v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.15311v2', 'Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehran Tamjidi, Hamidreza Dastmalchi, Mohammadreza Alimoradijazi, Ali Cheraghian, Aijun An, Morteza Saberi

**分类**: cs.CV

**发布日期**: 2025-11-19 (更新: 2025-11-20)

**备注**: Accepted by AAAI 2026

**🔗 代码/项目**: [PROJECT_PAGE](https://mehran-tam.github.io/Uni-Adapter)

---

## 💡 一句话要点

**提出Uni-Adapter，一种免训练的3D视觉-语言模型在线测试时自适应方法。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D视觉` `视觉-语言模型` `测试时自适应` `点云处理` `动态原型学习`

## 📋 核心要点

1. 现有3D视觉-语言模型在实际应用中，面对噪声、不完整或分布偏移的数据时性能下降。
2. Uni-Adapter通过动态原型学习，构建并更新类特定原型，以适应异构数据分布。
3. 实验表明，Uni-Adapter在多个3D数据集上显著提升了模型的鲁棒性，无需重新训练。

## 📝 摘要（中文）

3D视觉-语言基础模型(VLFMs)在开放世界点云处理任务中表现出强大的泛化和零样本识别能力。然而，在数据嘈杂、不完整或来自与训练数据不同分布的实际场景中，这些模型的性能通常不佳。为了解决这个问题，我们提出Uni-Adapter，一种基于动态原型学习的3D VLFMs新型免训练在线测试时自适应(TTA)策略。我们定义了一个3D缓存来存储类特定的聚类中心作为原型，这些原型不断更新以捕获异构数据分布中的类内变异性。这些动态原型作为通过相似性评分进行基于缓存的logit计算的锚点。同时，基于图的标签平滑模块捕获原型间的相似性，以增强相似原型之间的标签一致性。最后，我们使用熵加权聚合来统一来自原始3D VLFM和精炼的3D缓存的预测，以实现可靠的自适应。无需重新训练，Uni-Adapter有效地缓解了分布偏移，在不同的3D基准测试中，针对不同的3D VLFMs实现了最先进的性能，在ModelNet-40C上提高了10.55%，在ScanObjectNN-C上提高了8.26%，在ShapeNet-C上提高了4.49%。

## 🔬 方法详解

**问题定义**：论文旨在解决3D视觉-语言基础模型在测试时遇到分布偏移问题，即模型在训练数据和实际应用数据之间存在差异时性能显著下降。现有方法通常需要重新训练模型或进行微调，计算成本高昂且效率低下。因此，如何在不进行训练的情况下，使模型适应新的数据分布，是本文要解决的关键问题。

**核心思路**：Uni-Adapter的核心思路是利用动态原型学习，构建一个能够捕获类内变异性的3D缓存。该缓存存储类特定的聚类中心作为原型，并随着新数据的输入不断更新这些原型。通过将输入数据与缓存中的原型进行比较，可以实现对模型预测结果的修正，从而适应新的数据分布。这种方法无需重新训练模型，具有高效性和灵活性。

**技术框架**：Uni-Adapter的整体框架包含三个主要模块：1) 3D缓存：用于存储和更新类特定的原型。2) 基于缓存的Logit计算：通过计算输入数据与原型之间的相似性得分，生成新的logit。3) 基于图的标签平滑：利用原型之间的相似性，增强标签一致性。最后，通过熵加权聚合，将原始模型的预测结果和缓存的预测结果进行融合，得到最终的预测结果。

**关键创新**：Uni-Adapter的关键创新在于其免训练的在线测试时自适应策略。与传统的需要重新训练或微调的方法不同，Uni-Adapter可以在测试时动态地适应新的数据分布，无需任何训练数据。此外，动态原型学习和基于图的标签平滑模块能够有效地捕获类内变异性和类间关系，从而提高模型的鲁棒性。

**关键设计**：3D缓存使用K-means聚类算法来初始化和更新原型。相似性评分采用余弦相似度。基于图的标签平滑模块使用KNN图来构建原型之间的关系。熵加权聚合使用预测结果的熵值来确定原始模型和缓存预测结果的权重。具体参数设置（如K-means的簇数、KNN图的邻居数）需要根据具体数据集进行调整。

## 📊 实验亮点

Uni-Adapter在ModelNet-40C、ScanObjectNN-C和ShapeNet-C等多个3D数据集上取得了显著的性能提升。具体而言，在ModelNet-40C上，Uni-Adapter的性能提升了10.55%；在ScanObjectNN-C上，性能提升了8.26%；在ShapeNet-C上，性能提升了4.49%。这些结果表明，Uni-Adapter能够有效地缓解分布偏移问题，提高模型的鲁棒性。

## 🎯 应用场景

Uni-Adapter可应用于各种需要处理3D点云数据的场景，例如自动驾驶、机器人导航、室内场景理解、三维重建等。该方法能够提升模型在实际应用中的鲁棒性和准确性，尤其是在数据质量较差或数据分布发生变化的情况下。未来，该方法可以进一步扩展到其他模态的数据，例如图像和文本，从而实现更通用的自适应能力。

## 📄 摘要（原文）

> 3D Vision-Language Foundation Models (VLFMs) have shown strong generalization and zero-shot recognition capabilities in open-world point cloud processing tasks. However, these models often underperform in practical scenarios where data are noisy, incomplete, or drawn from a different distribution than the training data. To address this, we propose Uni-Adapter, a novel training-free online test-time adaptation (TTA) strategy for 3D VLFMs based on dynamic prototype learning. We define a 3D cache to store class-specific cluster centers as prototypes, which are continuously updated to capture intra-class variability in heterogeneous data distributions. These dynamic prototypes serve as anchors for cache-based logit computation via similarity scoring. Simultaneously, a graph-based label smoothing module captures inter-prototype similarities to enforce label consistency among similar prototypes. Finally, we unify predictions from the original 3D VLFM and the refined 3D cache using entropy-weighted aggregation for reliable adaptation. Without retraining, Uni-Adapter effectively mitigates distribution shifts, achieving state-of-the-art performance on diverse 3D benchmarks over different 3D VLFMs, improving ModelNet-40C by 10.55%, ScanObjectNN-C by 8.26%, and ShapeNet-C by 4.49% over the source 3D VLFMs. Project page: https://mehran-tam.github.io/Uni-Adapter

