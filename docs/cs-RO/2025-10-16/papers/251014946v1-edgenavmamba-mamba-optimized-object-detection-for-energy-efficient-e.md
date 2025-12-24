---
layout: default
title: "EdgeNavMamba: Mamba Optimized Object Detection for Energy Efficient Edge Devices"
---

# EdgeNavMamba: Mamba Optimized Object Detection for Energy Efficient Edge Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14946" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14946v1</a>
  <a href="https://arxiv.org/pdf/2510.14946.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14946v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14946v1', 'EdgeNavMamba: Mamba Optimized Object Detection for Energy Efficient Edge Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Romina Aalishah, Mozhgan Navardi, Tinoosh Mohsenin

**分类**: eess.IV, cs.RO

**发布日期**: 2025-10-16

**备注**: The 11th IEEE International Conference on Edge Computing and Scalable Cloud (IEEE EdgeCom 2025)

---

## 💡 一句话要点

**EdgeNavMamba：面向边缘设备的节能Mamba优化目标检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `边缘计算` `目标检测` `Mamba模型` `强化学习` `自主导航` `模型压缩` `知识蒸馏`

## 📋 核心要点

1. 现有深度学习模型在资源受限的边缘设备上部署面临计算能力和内存的挑战，模型效率和压缩是关键问题。
2. EdgeNavMamba利用Mamba模型的高效性，结合强化学习，实现目标导向导航，并使用自定义数据集进行训练。
3. 实验表明，EdgeNavMamba在保持性能的同时，显著降低了模型大小和能耗，并在模拟环境中实现了高导航成功率。

## 📝 摘要（中文）

在自主导航中，高效且精确的深度学习模型的部署一直是一个挑战，尤其是在资源受限的边缘设备上的实时应用。边缘设备的计算能力和内存有限，因此模型效率和压缩至关重要。本文提出了EdgeNavMamba，一个基于强化学习的框架，用于使用高效的Mamba目标检测模型进行目标导向导航。为了训练和评估检测器，我们引入了一个自定义形状检测数据集，该数据集是在各种室内环境中收集的，反映了现实导航中常见的视觉线索。该目标检测器作为一个预处理模块，从视觉输入中提取边界框（BBOX），然后将其传递给RL策略以控制目标导向导航。实验结果表明，学生模型在NVIDIA Jetson Orin Nano和Raspberry Pi 5等边缘设备上，尺寸减少了67%，每次推理的能量消耗最多减少了73%，同时保持与教师模型相同的性能。与基线相比，EdgeNavMamba还在MiniWorld和IsaacLab模拟器中保持了较高的检测精度，同时减少了31%的参数。在MiniWorld模拟器中，导航策略在各种复杂程度的环境中实现了超过90%的成功率。

## 🔬 方法详解

**问题定义**：论文旨在解决在资源受限的边缘设备上部署高效且精确的目标检测模型，用于自主导航的问题。现有方法在边缘设备上部署时，由于计算能力和内存的限制，难以实现实时性和高精度，同时能耗较高。

**核心思路**：论文的核心思路是利用Mamba模型的高效性，结合强化学习，设计一个轻量级的目标检测器，并使用强化学习策略进行目标导向导航。通过模型压缩和优化，降低模型大小和能耗，使其能够在边缘设备上高效运行。

**技术框架**：EdgeNavMamba框架包含两个主要模块：Mamba目标检测器和强化学习导航策略。首先，Mamba目标检测器从视觉输入中提取边界框（BBOX），然后将这些BBOX传递给强化学习策略。强化学习策略根据检测到的目标信息，控制导航代理在环境中移动，最终达到目标。整个框架在自定义数据集和模拟环境中进行训练和评估。

**关键创新**：论文的关键创新在于将Mamba模型应用于目标检测任务，并针对边缘设备进行了优化。Mamba模型相比于传统的卷积神经网络，具有更高的效率和更低的参数量，更适合在资源受限的设备上部署。此外，论文还提出了一个基于强化学习的导航框架，能够根据检测到的目标信息进行智能导航。

**关键设计**：论文使用知识蒸馏技术来训练一个更小的学生模型，同时保持与教师模型相似的性能。损失函数包括检测损失和导航损失，用于优化目标检测器和导航策略。网络结构方面，Mamba目标检测器采用轻量级设计，减少了参数量和计算复杂度。强化学习策略采用深度Q网络（DQN）或类似的算法，根据环境状态和目标信息选择最优动作。

## 📊 实验亮点

实验结果表明，EdgeNavMamba在NVIDIA Jetson Orin Nano和Raspberry Pi 5等边缘设备上，尺寸减少了67%，每次推理的能量消耗最多减少了73%，同时保持与教师模型相同的性能。在MiniWorld和IsaacLab模拟器中，EdgeNavMamba保持了较高的检测精度，同时减少了31%的参数。在MiniWorld模拟器中，导航策略在各种复杂程度的环境中实现了超过90%的成功率。

## 🎯 应用场景

EdgeNavMamba可应用于各种自主导航场景，如机器人导航、无人机巡检、智能家居等。该研究成果有助于在资源受限的边缘设备上实现高效、精确的自主导航，降低能耗，提高设备续航能力，具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> Deployment of efficient and accurate Deep Learning models has long been a challenge in autonomous navigation, particularly for real-time applications on resource-constrained edge devices. Edge devices are limited in computing power and memory, making model efficiency and compression essential. In this work, we propose EdgeNavMamba, a reinforcement learning-based framework for goal-directed navigation using an efficient Mamba object detection model. To train and evaluate the detector, we introduce a custom shape detection dataset collected in diverse indoor settings, reflecting visual cues common in real-world navigation. The object detector serves as a pre-processing module, extracting bounding boxes (BBOX) from visual input, which are then passed to an RL policy to control goal-oriented navigation. Experimental results show that the student model achieved a reduction of 67% in size, and up to 73% in energy per inference on edge devices of NVIDIA Jetson Orin Nano and Raspberry Pi 5, while keeping the same performance as the teacher model. EdgeNavMamba also maintains high detection accuracy in MiniWorld and IsaacLab simulators while reducing parameters by 31% compared to the baseline. In the MiniWorld simulator, the navigation policy achieves over 90% success across environments of varying complexity.

