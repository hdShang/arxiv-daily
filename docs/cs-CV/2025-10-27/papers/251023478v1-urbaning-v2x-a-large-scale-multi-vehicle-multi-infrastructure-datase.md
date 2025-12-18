---
layout: default
title: UrbanIng-V2X: A Large-Scale Multi-Vehicle, Multi-Infrastructure Dataset Across Multiple Intersections for Cooperative Perception
---

# UrbanIng-V2X: A Large-Scale Multi-Vehicle, Multi-Infrastructure Dataset Across Multiple Intersections for Cooperative Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23478" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23478v1</a>
  <a href="https://arxiv.org/pdf/2510.23478.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23478v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23478v1', 'UrbanIng-V2X: A Large-Scale Multi-Vehicle, Multi-Infrastructure Dataset Across Multiple Intersections for Cooperative Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karthikeyan Chandra Sekaran, Markus Geisler, Dominik Rößle, Adithya Mohan, Daniel Cremers, Wolfgang Utschick, Michael Botsch, Werner Huber, Torsten Schön

**分类**: cs.CV

**发布日期**: 2025-10-27

**备注**: Accepted to NeurIPS 2025. Including supplemental material. For code and dataset, see https://github.com/thi-ad/UrbanIng-V2X

---

## 💡 一句话要点

**UrbanIng-V2X：用于协同感知的多路口大规模多车辆多基础设施数据集**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `协同感知` `自动驾驶` `数据集` `多模态` `V2X` `城市交通` `传感器融合`

## 📋 核心要点

1. 现有协同感知数据集在路口数量和车辆数量上存在局限性，难以充分评估算法在复杂交通环境下的泛化能力。
2. UrbanIng-V2X数据集旨在提供一个大规模、多模态的协同感知数据集，包含多个路口、多辆车和基础设施传感器。
3. 该数据集包含多种传感器数据，并提供了全面的3D标注，以及代码库、高清地图和数字孪生环境。

## 📝 摘要（中文）

现有的协同感知数据集在推动智能交通应用方面发挥了关键作用，通过智能体间的信息交换，克服遮挡等挑战，提升整体场景理解。然而，现有真实数据集通常仅限于单个路口或单辆车，缺乏包含多个互联车辆和基础设施传感器、覆盖多个路口的综合感知数据集。这限制了算法在多样化交通环境中的基准测试，可能导致过拟合，并在相似的路口布局和交通参与者行为下产生误导性的高性能。为解决此问题，我们推出了UrbanIng-V2X，这是首个大规模多模态数据集，支持车辆和基础设施传感器在德国英戈尔施塔特三个城市路口进行协同感知。UrbanIng-V2X包含34个时间对齐和空间校准的传感器序列，每个序列持续20秒，涉及三个路口之一，包含两辆车和最多三个基础设施传感器杆，在协调场景中运行。总共，UrbanIng-V2X提供来自12个车载RGB相机、2个车载激光雷达、17个基础设施热像仪和12个基础设施激光雷达的数据。所有序列都以10 Hz的频率进行标注，包含13个对象类别的3D边界框，整个数据集约有71.2万个标注实例。我们使用最先进的协同感知方法进行了全面评估，并公开发布了代码库、数据集、高清地图以及完整数据收集环境的数字孪生。

## 🔬 方法详解

**问题定义**：现有协同感知数据集规模有限，尤其是在多路口和多车辆场景下，导致模型容易过拟合特定环境，泛化能力不足。缺乏足够的数据来训练和评估算法在复杂、真实的城市交通环境中的性能。

**核心思路**：通过构建一个大规模、多模态的数据集，包含多个路口、多辆车和基础设施传感器的数据，来解决现有数据集的局限性。数据集的设计旨在模拟真实的城市交通场景，并提供全面的标注信息，以支持协同感知算法的开发和评估。

**技术框架**：UrbanIng-V2X数据集的构建涉及以下几个关键步骤：1) 在三个不同的城市路口部署车辆和基础设施传感器；2) 收集多模态传感器数据，包括RGB图像、激光雷达点云和热图像；3) 对传感器数据进行时间对齐和空间校准；4) 使用3D边界框对所有序列进行标注，涵盖13个对象类别；5) 构建数据收集环境的数字孪生，并提供高清地图。

**关键创新**：UrbanIng-V2X数据集的主要创新点在于其规模和多样性。它是首个大规模、多模态的协同感知数据集，包含多个路口、多辆车和基础设施传感器的数据。此外，该数据集还提供了全面的标注信息和数字孪生环境，为协同感知算法的开发和评估提供了有力的支持。

**关键设计**：数据集包含34个序列，每个序列持续20秒，以10Hz的频率进行标注。标注信息包括13个对象类别的3D边界框。传感器配置包括12个车载RGB相机、2个车载激光雷达、17个基础设施热像仪和12个基础设施激光雷达。数据集还提供高清地图和数据收集环境的数字孪生。

## 📊 实验亮点

论文使用最先进的协同感知方法对UrbanIng-V2X数据集进行了评估，结果表明该数据集能够有效评估算法在复杂城市交通环境中的性能。具体性能数据未知，但数据集的发布为协同感知领域的研究提供了宝贵的资源。

## 🎯 应用场景

UrbanIng-V2X数据集可用于开发和评估各种协同感知算法，例如目标检测、跟踪、场景理解和行为预测。这些算法可以应用于自动驾驶、智能交通管理和高级驾驶辅助系统等领域，提高交通安全和效率，并为智慧城市建设提供支持。

## 📄 摘要（原文）

> Recent cooperative perception datasets have played a crucial role in advancing smart mobility applications by enabling information exchange between intelligent agents, helping to overcome challenges such as occlusions and improving overall scene understanding. While some existing real-world datasets incorporate both vehicle-to-vehicle and vehicle-to-infrastructure interactions, they are typically limited to a single intersection or a single vehicle. A comprehensive perception dataset featuring multiple connected vehicles and infrastructure sensors across several intersections remains unavailable, limiting the benchmarking of algorithms in diverse traffic environments. Consequently, overfitting can occur, and models may demonstrate misleadingly high performance due to similar intersection layouts and traffic participant behavior. To address this gap, we introduce UrbanIng-V2X, the first large-scale, multi-modal dataset supporting cooperative perception involving vehicles and infrastructure sensors deployed across three urban intersections in Ingolstadt, Germany. UrbanIng-V2X consists of 34 temporally aligned and spatially calibrated sensor sequences, each lasting 20 seconds. All sequences contain recordings from one of three intersections, involving two vehicles and up to three infrastructure-mounted sensor poles operating in coordinated scenarios. In total, UrbanIng-V2X provides data from 12 vehicle-mounted RGB cameras, 2 vehicle LiDARs, 17 infrastructure thermal cameras, and 12 infrastructure LiDARs. All sequences are annotated at a frequency of 10 Hz with 3D bounding boxes spanning 13 object classes, resulting in approximately 712k annotated instances across the dataset. We provide comprehensive evaluations using state-of-the-art cooperative perception methods and publicly release the codebase, dataset, HD map, and a digital twin of the complete data collection environment.

