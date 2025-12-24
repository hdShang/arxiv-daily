---
layout: default
title: "DoGFlow: Self-Supervised LiDAR Scene Flow via Cross-Modal Doppler Guidance"
---

# DoGFlow: Self-Supervised LiDAR Scene Flow via Cross-Modal Doppler Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18506" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18506v1</a>
  <a href="https://arxiv.org/pdf/2508.18506.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18506v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18506v1', 'DoGFlow: Self-Supervised LiDAR Scene Flow via Cross-Modal Doppler Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ajinkya Khoche, Qingwen Zhang, Yixi Cai, Sina Sharif Mansouri, Patric Jensfelt

**分类**: cs.CV

**发布日期**: 2025-08-25

**备注**: Under Review

**🔗 代码/项目**: [PROJECT_PAGE](https://ajinkyakhoche.github.io/DogFlow/)

---

## 💡 一句话要点

**提出DoGFlow以解决自监督LiDAR场景流估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自监督学习` `LiDAR场景流` `跨模态融合` `多普勒测量` `动态环境` `自动驾驶` `机器人导航`

## 📋 核心要点

1. 现有自监督方法在动态环境中的3D场景流估计表现不如完全监督方法，尤其是在长距离和恶劣天气条件下。
2. DoGFlow通过跨模态标签传递，利用4D雷达多普勒测量实时计算运动伪标签，并将其转移到LiDAR领域。
3. 在MAN TruckScenes数据集上，DoGFlow的性能显著提升，使得LiDAR网络在仅用10%真实数据的情况下达到90%的完全监督性能。

## 📝 摘要（中文）

准确的3D场景流估计对于自主系统在动态环境中安全导航至关重要，但创建所需的大规模手动标注数据集仍然是开发稳健感知模型的重大瓶颈。现有自监督方法在长距离和恶劣天气场景下的表现难以匹敌完全监督的方法，而监督方法由于依赖昂贵的人力标注而难以扩展。本文提出了DoGFlow，一个新颖的自监督框架，能够在不需要任何手动真实标注的情况下恢复LiDAR场景流估计中的完整3D物体运动。我们提出的跨模态标签传递方法，通过实时计算4D雷达多普勒测量的运动伪标签，并利用动态感知关联和消歧传播将其转移到LiDAR领域。在具有挑战性的MAN TruckScenes数据集上，DoGFlow显著超越现有自监督方法，并通过使LiDAR骨干网络在仅使用10%真实数据的情况下实现超过90%的完全监督性能，从而提高了标签效率。

## 🔬 方法详解

**问题定义**：本文旨在解决自监督LiDAR场景流估计中的数据标注瓶颈问题。现有方法在动态环境下的表现不佳，且完全监督方法的标注成本高昂，难以扩展。

**核心思路**：DoGFlow的核心思路是通过跨模态标签传递，从4D雷达多普勒测量中实时计算运动伪标签，并将其有效转移到LiDAR数据中，以实现自监督学习。

**技术框架**：DoGFlow的整体架构包括数据采集、伪标签计算、动态感知关联和标签传播四个主要模块。首先，从4D雷达获取数据，然后计算运动伪标签，接着通过动态感知关联将标签与LiDAR数据关联，最后进行标签传播。

**关键创新**：DoGFlow的关键创新在于其跨模态标签传递机制，能够在没有手动标注的情况下，利用雷达数据生成高质量的伪标签，从而显著提高自监督学习的效果。

**关键设计**：在设计中，DoGFlow采用了动态感知关联算法，以解决不同模态数据之间的匹配问题，并通过消歧传播技术来提高标签的准确性和可靠性。

## 📊 实验亮点

在MAN TruckScenes数据集上，DoGFlow显著超越了现有自监督方法，LiDAR骨干网络在仅使用10%真实数据的情况下，达到了超过90%的完全监督性能。这一结果表明，DoGFlow在标签效率和场景流估计精度方面具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能交通系统等。通过提高LiDAR场景流估计的效率和准确性，DoGFlow能够帮助自主系统更好地理解和适应动态环境，从而提升安全性和可靠性。未来，随着技术的进一步发展，DoGFlow可能会在更多复杂场景中得到应用。

## 📄 摘要（原文）

> Accurate 3D scene flow estimation is critical for autonomous systems to navigate dynamic environments safely, but creating the necessary large-scale, manually annotated datasets remains a significant bottleneck for developing robust perception models. Current self-supervised methods struggle to match the performance of fully supervised approaches, especially in challenging long-range and adverse weather scenarios, while supervised methods are not scalable due to their reliance on expensive human labeling. We introduce DoGFlow, a novel self-supervised framework that recovers full 3D object motions for LiDAR scene flow estimation without requiring any manual ground truth annotations. This paper presents our cross-modal label transfer approach, where DoGFlow computes motion pseudo-labels in real-time directly from 4D radar Doppler measurements and transfers them to the LiDAR domain using dynamic-aware association and ambiguity-resolved propagation. On the challenging MAN TruckScenes dataset, DoGFlow substantially outperforms existing self-supervised methods and improves label efficiency by enabling LiDAR backbones to achieve over 90% of fully supervised performance with only 10% of the ground truth data. For more details, please visit https://ajinkyakhoche.github.io/DogFlow/

