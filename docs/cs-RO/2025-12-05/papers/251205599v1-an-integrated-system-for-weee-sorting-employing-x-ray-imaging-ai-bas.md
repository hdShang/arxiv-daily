---
layout: default
title: An Integrated System for WEEE Sorting Employing X-ray Imaging, AI-based Object Detection and Segmentation, and Delta Robot Manipulation
---

# An Integrated System for WEEE Sorting Employing X-ray Imaging, AI-based Object Detection and Segmentation, and Delta Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05599" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05599v1</a>
  <a href="https://arxiv.org/pdf/2512.05599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05599v1" onclick="toggleFavorite(this, '2512.05599v1', 'An Integrated System for WEEE Sorting Employing X-ray Imaging, AI-based Object Detection and Segmentation, and Delta Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Panagiotis Giannikos, Lampis Papakostas, Evangelos Katralis, Panagiotis Mavridis, George Chryssinas, Myrto Inglezou, Nikolaos Panagopoulos, Antonis Porichis, Athanasios Mastrogeorgiou, Panagiotis Chatzakos

**分类**: cs.RO

**发布日期**: 2025-12-05

**DOI**: [10.1109/AIM64088.2025.11175846](https://doi.org/10.1109/AIM64088.2025.11175846)

---

## 💡 一句话要点

**提出集成X射线成像、AI检测分割和Delta机器人的WEEE分拣系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `WEEE分拣` `X射线成像` `目标检测` `图像分割` `Delta机器人` `自动化回收` `人工智能`

## 📋 核心要点

1. 现有WEEE电池分拣系统在准确识别和分拣不同类型WEEE中的电池方面存在不足，缺乏全自动解决方案。
2. 该方法集成了X射线成像、AI目标检测分割和Delta机器人操作，实现高对比度图像重建和精确的电池提取。
3. 通过在NVIDIA Isaac Sim仿真环境和真实环境中验证，证明了该方法在WEEE电池分拣中的有效性。

## 📝 摘要（中文）

随着电池使用量的快速增长和自然资源的日益有限，电池回收变得越来越重要。此外，随着电池能量密度的不断提高，回收过程中的不当操作会带来严重的安全隐患，包括回收设施发生火灾的风险。目前已提出许多用于从WEEE回收线上检测和移除电池的系统，包括基于X射线和RGB的视觉检测方法，这些方法通常由人工智能驱动的目标检测模型（如Mask R-CNN、YOLO、ResNets）驱动。尽管在优化检测技术和模型修改方面取得了进展，但尚未实现能够准确识别和分拣各种WEEE类型电池的全自动解决方案。为了应对这些挑战，我们提出了一种新颖的方法，该方法集成了专门的X射线透射双能成像子系统和先进的预处理算法，从而能够进行高对比度图像重建，从而有效地区分WEEE中的致密和薄材料。设备沿着传送带移动通过高分辨率X射线成像系统，YOLO和U-Net模型在其中精确地检测和分割包含电池的物品。然后，智能跟踪和位置估计算法引导配备吸盘夹具的Delta机器人选择性地提取并正确丢弃目标设备。该方法在NVIDIA Isaac Sim中开发的光真实感仿真环境和真实设置中得到了验证。

## 🔬 方法详解

**问题定义**：论文旨在解决电子垃圾（WEEE）中电池的自动分拣问题。现有方法，如基于RGB图像的视觉检测，在处理复杂场景和遮挡时效果不佳。X射线成像虽然能穿透物体，但如何有效利用X射线图像进行精确的电池检测和分割仍然是一个挑战。此外，缺乏一个集成化的系统，能够将检测、分割和机器人操作无缝结合。

**核心思路**：论文的核心思路是结合X射线成像的穿透能力和AI目标检测分割的精确性，构建一个完整的自动化分拣系统。通过X射线成像获取WEEE内部结构信息，利用AI模型进行电池的精确检测和分割，最后通过Delta机器人进行抓取和分拣。这种方法旨在克服传统视觉方法的局限性，提高分拣效率和准确性。

**技术框架**：该系统主要包含以下几个模块：1) X射线成像子系统：用于获取WEEE的X射线图像。2) 图像预处理模块：对X射线图像进行增强和降噪，提高图像质量。3) AI检测分割模块：使用YOLO和U-Net模型对图像中的电池进行检测和分割。4) 跟踪和位置估计模块：跟踪目标物体的位置，并估计其姿态。5) Delta机器人操作模块：根据位置和姿态信息，控制Delta机器人进行抓取和分拣。

**关键创新**：该论文的关键创新在于：1) 集成了X射线成像和AI目标检测分割，实现对WEEE内部电池的精确识别。2) 提出了一个完整的自动化分拣系统，包括图像获取、处理、检测、分割、跟踪和机器人操作。3) 使用双能X射线成像技术，提高了图像对比度，从而更容易区分不同材料。

**关键设计**：论文中使用了YOLO和U-Net模型进行目标检测和分割。YOLO负责快速定位电池的位置，U-Net负责精确分割电池的轮廓。此外，论文还设计了一种智能跟踪和位置估计算法，用于准确跟踪目标物体的位置和姿态。Delta机器人配备了吸盘夹具，能够安全可靠地抓取电池。

## 📊 实验亮点

论文在NVIDIA Isaac Sim仿真环境和真实环境中验证了所提出的方法。实验结果表明，该系统能够有效地检测和分割WEEE中的电池，并能够通过Delta机器人进行准确的抓取和分拣。虽然论文中没有给出具体的性能数据，但仿真和真实环境的验证表明了该方法的有效性和可行性。

## 🎯 应用场景

该研究成果可应用于电子垃圾回收行业，实现电池的自动化分拣，提高回收效率和安全性。通过精确识别和分拣不同类型的电池，可以更好地进行后续的回收处理，减少环境污染，并为电池材料的再利用提供支持。未来，该技术还可以扩展到其他类型废弃物的分拣，例如金属、塑料等。

## 📄 摘要（原文）

> Battery recycling is becoming increasingly critical due to the rapid growth in battery usage and the limited availability of natural resources. Moreover, as battery energy densities continue to rise, improper handling during recycling poses significant safety hazards, including potential fires at recycling facilities. Numerous systems have been proposed for battery detection and removal from WEEE recycling lines, including X-ray and RGB-based visual inspection methods, typically driven by AI-powered object detection models (e.g., Mask R-CNN, YOLO, ResNets). Despite advances in optimizing detection techniques and model modifications, a fully autonomous solution capable of accurately identifying and sorting batteries across diverse WEEEs types has yet to be realized. In response to these challenges, we present our novel approach which integrates a specialized X-ray transmission dual energy imaging subsystem with advanced pre-processing algorithms, enabling high-contrast image reconstruction for effective differentiation of dense and thin materials in WEEE. Devices move along a conveyor belt through a high-resolution X-ray imaging system, where YOLO and U-Net models precisely detect and segment battery-containing items. An intelligent tracking and position estimation algorithm then guides a Delta robot equipped with a suction gripper to selectively extract and properly discard the targeted devices. The approach is validated in a photorealistic simulation environment developed in NVIDIA Isaac Sim and on the real setup.

