---
layout: default
title: "WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond"
---

# WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27133" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27133v1</a>
  <a href="https://arxiv.org/pdf/2510.27133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27133v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27133v1', 'WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicong Sun, Jacqueline Lo, Jinxing Hu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-31

**备注**: This paper has been accepted by MMM 2026

**🔗 代码/项目**: [PROJECT_PAGE](https://zhicongsun.github.io/wildfirexslam)

---

## 💡 一句话要点

**WildfireX-SLAM：用于野火SLAM及其他应用的大规模低空RGB-D数据集**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `SLAM` `三维高斯溅射` `RGB-D数据集` `野火应急响应` `森林管理` `合成数据` `无人机`

## 📋 核心要点

1. 现有基于3DGS的SLAM方法主要集中于小规模室内场景，缺乏针对大规模森林环境的有效数据集，阻碍了其在野火应急响应等领域的应用。
2. 论文构建了一个大规模、高质量的合成数据集WildfireX-SLAM，通过Unreal Engine 5模拟真实森林环境，并提供多种环境因素的灵活控制。
3. 论文在WildfireX-SLAM上进行了基准测试，揭示了3DGS-based SLAM在森林环境中的挑战，并为未来的改进方向提供了参考。

## 📝 摘要（中文）

三维高斯溅射（3DGS）及其变体在同步定位与建图（SLAM）方面取得了显著进展。虽然最近大多数基于3DGS的SLAM工作都集中在小规模室内场景，但为大规模森林场景开发基于3DGS的SLAM方法在许多实际应用中具有巨大的潜力，尤其是在野火应急响应和森林管理方面。然而，由于缺乏全面和高质量的数据集，这项研究受到了阻碍，并且在真实场景中收集此类数据集的成本高昂且技术上不可行。为此，我们构建了一个大规模、全面和高质量的合成数据集，用于野火和森林环境中的SLAM。利用Unreal Engine 5 Electric Dreams环境示例项目，我们开发了一个管道，可以轻松地收集无人机的空中和地面视图，包括地面实况相机姿势和来自无人机的各种附加数据模态。我们的管道还提供了对环境因素（如光照、天气以及野火的类型和条件）的灵活控制，支持涵盖森林测绘、野火应急响应等各种任务的需求。由此产生的试点数据集WildfireX-SLAM包含来自一个总面积为16平方公里的大规模森林地图的5.5k低空RGB-D航拍图像。在WildfireX-SLAM的基础上，还进行了全面的基准测试，这不仅揭示了基于3DGS的SLAM在森林中面临的独特挑战，而且突出了未来工作的潜在改进。数据集和代码将公开发布。

## 🔬 方法详解

**问题定义**：现有基于3DGS的SLAM方法在处理大规模森林场景时面临挑战，缺乏高质量的训练和测试数据集。真实场景数据采集成本高昂且技术难度大，限制了相关研究的进展。因此，需要一个大规模、高质量的森林环境数据集，以促进基于3DGS的SLAM方法在野火应急响应和森林管理等领域的应用。

**核心思路**：论文的核心思路是利用Unreal Engine 5等游戏引擎的强大渲染能力，构建一个逼真的大规模森林环境，并生成包含RGB-D图像、相机姿态等信息的合成数据集。通过控制光照、天气、野火条件等环境因素，模拟真实森林场景的多样性，为SLAM算法的训练和评估提供高质量的数据。

**技术框架**：该数据集构建流程主要包括以下几个阶段：1) 利用Unreal Engine 5 Electric Dreams环境示例项目构建大规模森林场景；2) 开发数据采集管道，模拟无人机在森林中进行低空飞行，并获取RGB-D图像和相机姿态信息；3) 通过调整光照、天气、野火条件等参数，生成不同环境下的数据；4) 对采集到的数据进行处理和标注，生成最终的WildfireX-SLAM数据集。

**关键创新**：该论文的关键创新在于构建了一个大规模、高质量的合成数据集，专门用于野火和森林环境中的SLAM研究。与现有的SLAM数据集相比，WildfireX-SLAM具有更大的场景规模、更逼真的森林环境和更丰富的环境因素变化，更贴近实际应用场景的需求。

**关键设计**：在数据采集管道的设计中，论文考虑了无人机的飞行轨迹、相机参数、图像分辨率等因素，以保证数据的质量和多样性。同时，论文还提供了对光照、天气、野火条件等环境因素的灵活控制，允许用户根据自己的需求生成特定的数据集。此外，论文还对数据集进行了全面的基准测试，为未来的研究提供了参考。

## 📊 实验亮点

论文构建的WildfireX-SLAM数据集包含5.5k低空RGB-D航拍图像，覆盖16平方公里的森林区域。通过基准测试，论文揭示了3DGS-based SLAM在森林环境中面临的挑战，例如光照变化、植被遮挡等，并为未来的改进方向提供了参考。该数据集的公开将促进相关领域的研究进展。

## 🎯 应用场景

该研究成果可广泛应用于野火应急响应、森林管理、环境监测等领域。通过利用WildfireX-SLAM数据集训练的SLAM算法，可以实现对森林环境的快速、准确建模，为野火蔓延预测、火灾扑救、森林资源评估等提供技术支持，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> 3D Gaussian splatting (3DGS) and its subsequent variants have led to remarkable progress in simultaneous localization and mapping (SLAM). While most recent 3DGS-based SLAM works focus on small-scale indoor scenes, developing 3DGS-based SLAM methods for large-scale forest scenes holds great potential for many real-world applications, especially for wildfire emergency response and forest management. However, this line of research is impeded by the absence of a comprehensive and high-quality dataset, and collecting such a dataset over real-world scenes is costly and technically infeasible. To this end, we have built a large-scale, comprehensive, and high-quality synthetic dataset for SLAM in wildfire and forest environments. Leveraging the Unreal Engine 5 Electric Dreams Environment Sample Project, we developed a pipeline to easily collect aerial and ground views, including ground-truth camera poses and a range of additional data modalities from unmanned aerial vehicle. Our pipeline also provides flexible controls on environmental factors such as light, weather, and types and conditions of wildfire, supporting the need for various tasks covering forest mapping, wildfire emergency response, and beyond. The resulting pilot dataset, WildfireX-SLAM, contains 5.5k low-altitude RGB-D aerial images from a large-scale forest map with a total size of 16 km2. On top of WildfireX-SLAM, a thorough benchmark is also conducted, which not only reveals the unique challenges of 3DGS-based SLAM in the forest but also highlights potential improvements for future works. The dataset and code will be publicly available. Project page: https://zhicongsun.github.io/wildfirexslam.

