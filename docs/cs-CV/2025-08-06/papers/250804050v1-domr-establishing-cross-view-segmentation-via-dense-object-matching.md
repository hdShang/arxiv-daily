---
layout: default
title: "DOMR: Establishing Cross-View Segmentation via Dense Object Matching"
---

# DOMR: Establishing Cross-View Segmentation via Dense Object Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04050" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04050v1</a>
  <a href="https://arxiv.org/pdf/2508.04050.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04050v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04050v1', 'DOMR: Establishing Cross-View Segmentation via Dense Object Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jitong Liao, Yulu Gao, Shaofei Huang, Jialin Gao, Jie Lei, Ronghua Liang, Si Liu

**分类**: cs.CV

**发布日期**: 2025-08-06

**备注**: Accepted by ACM MM 2025

---

## 💡 一句话要点

**提出DOMR框架以解决跨视角物体匹配问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `跨视角匹配` `物体识别` `视觉理解` `深度学习` `密集匹配` `语义关系` `自动驾驶` `增强现实`

## 📋 核心要点

1. 跨视角物体匹配是视觉理解中的一项关键任务，但现有方法在处理物体间关系时存在不足，难以实现准确匹配。
2. 本文提出的DOMR框架通过密集物体匹配器（DOM）模块，联合建模多个物体的位置信息和语义关系，提升了匹配的准确性。
3. 在Ego-Exo4D基准测试中，DOMR框架在Ego→Exo和Exo→Ego任务上分别实现了49.7%和55.2%的平均IoU，显著优于现有方法。

## 📝 摘要（中文）

跨视角物体对应关系涉及在自我中心（第一人称）视角和外部中心（第三人称）视角之间匹配物体，是视觉理解中的一项关键且具有挑战性的任务。本文提出了密集物体匹配与优化（DOMR）框架，以建立跨视角的密集物体对应关系。该框架围绕密集物体匹配器（DOM）模块展开，联合建模多个物体。与直接将单个物体掩膜与图像特征匹配的方法不同，DOM利用物体之间的位置信息和语义关系来寻找对应关系。通过结合提案生成模块与密集匹配模块，DOM显式构建物体间关系，实现物体的密集匹配。此外，我们还结合了掩膜优化头，以提高预测掩膜的完整性和准确性。对Ego-Exo4D基准的广泛评估表明，我们的方法在Ego→Exo和Exo→Ego的平均IoU上分别达到了49.7%和55.2%的最新性能，超越了之前方法5.8%和4.3%的提升，验证了我们集成方法在跨视角理解中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决跨视角物体匹配中的物体对应关系建立问题。现有方法通常只关注单个物体的匹配，忽视了物体之间的关系，导致匹配准确性不足。

**核心思路**：DOMR框架的核心思想是通过密集物体匹配器（DOM）模块，利用物体的位置信息和语义关系，联合建模多个物体，以实现更准确的物体匹配。

**技术框架**：DOMR框架主要由提案生成模块和密集匹配模块组成。提案生成模块负责生成物体的候选区域，而密集匹配模块则通过编码视觉、空间和语义线索，显式构建物体间的关系，实现密集匹配。

**关键创新**：该研究的创新点在于通过联合建模多个物体，利用物体间的关系来提升匹配精度，而非单独匹配物体掩膜。这一方法在处理复杂场景时表现出更高的鲁棒性。

**关键设计**：在网络结构上，DOM集成了多种特征提取模块，并设计了特定的损失函数以优化物体间的匹配关系。此外，掩膜优化头的引入进一步提升了预测掩膜的完整性和准确性。

## 📊 实验亮点

在Ego-Exo4D基准测试中，DOMR框架在Ego→Exo任务上达到了49.7%的平均IoU，在Exo→Ego任务上达到了55.2%。这些结果分别比之前的方法提升了5.8%和4.3%，验证了该方法在跨视角理解中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、虚拟现实和增强现实等场景，能够帮助系统更好地理解和解析复杂的视觉信息。未来，随着技术的进步，DOMR框架有望在多视角视觉理解中发挥更大作用，推动相关领域的发展。

## 📄 摘要（原文）

> Cross-view object correspondence involves matching objects between egocentric (first-person) and exocentric (third-person) views. It is a critical yet challenging task for visual understanding. In this work, we propose the Dense Object Matching and Refinement (DOMR) framework to establish dense object correspondences across views. The framework centers around the Dense Object Matcher (DOM) module, which jointly models multiple objects. Unlike methods that directly match individual object masks to image features, DOM leverages both positional and semantic relationships among objects to find correspondences. DOM integrates a proposal generation module with a dense matching module that jointly encodes visual, spatial, and semantic cues, explicitly constructing inter-object relationships to achieve dense matching among objects. Furthermore, we combine DOM with a mask refinement head designed to improve the completeness and accuracy of the predicted masks, forming the complete DOMR framework. Extensive evaluations on the Ego-Exo4D benchmark demonstrate that our approach achieves state-of-the-art performance with a mean IoU of 49.7% on Ego$\to$Exo and 55.2% on Exo$\to$Ego. These results outperform those of previous methods by 5.8% and 4.3%, respectively, validating the effectiveness of our integrated approach for cross-view understanding.

