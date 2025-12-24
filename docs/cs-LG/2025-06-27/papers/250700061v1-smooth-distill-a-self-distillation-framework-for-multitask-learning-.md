---
layout: default
title: "Smooth-Distill: A Self-distillation Framework for Multitask Learning with Wearable Sensor Data"
---

# Smooth-Distill: A Self-distillation Framework for Multitask Learning with Wearable Sensor Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00061" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00061v1</a>
  <a href="https://arxiv.org/pdf/2507.00061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00061v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00061v1', 'Smooth-Distill: A Self-distillation Framework for Multitask Learning with Wearable Sensor Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hoang-Dieu Vu, Duc-Nghia Tran, Quang-Tu Pham, Hieu H. Pham, Nicolas Vuillerme, Duc-Tan Tran

**分类**: cs.LG, cs.AI, eess.SP

**发布日期**: 2025-06-27

**🔗 代码/项目**: [GITHUB](https://github.com/Kuan2vn/smooth)

---

## 💡 一句话要点

**提出Smooth-Distill框架以解决可穿戴传感器数据的多任务学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自蒸馏` `多任务学习` `可穿戴传感器` `人类活动识别` `加速度计数据` `模型训练效率` `深度学习`

## 📋 核心要点

1. 现有的多任务学习方法通常需要独立的教师和学生模型，导致计算开销大且训练效率低。
2. Smooth-Distill框架通过使用模型自身的平滑历史版本作为教师，简化了训练过程并提高了效率。
3. 实验结果显示，Smooth-Distill在HAR和传感器放置检测任务中均显著优于传统基线，且收敛模式更稳定，过拟合现象减少。

## 📝 摘要（中文）

本文介绍了Smooth-Distill，一种新颖的自蒸馏框架，旨在利用可穿戴传感器数据同时进行人类活动识别（HAR）和传感器放置检测。该方法采用统一的基于CNN的架构MTL-net，处理加速度计数据并为每个任务分支输出。与传统的蒸馏方法不同，该框架使用模型自身的平滑历史版本作为教师，显著降低了训练计算开销，同时保持了性能优势。为支持本研究，我们开发了一个全面的加速度计数据集，捕捉了三种不同佩戴位置下的12种不同睡姿。实验结果表明，Smooth-Distill在不同评估场景中始终优于替代方法，在人类活动识别和设备放置检测任务中均取得了显著改善。

## 🔬 方法详解

**问题定义**：本文旨在解决可穿戴传感器数据的多任务学习问题，尤其是人类活动识别和传感器放置检测。现有方法通常依赖于独立的教师和学生模型，导致训练效率低下和计算资源浪费。

**核心思路**：Smooth-Distill框架的核心思路是利用模型自身的平滑历史版本作为教师模型，从而减少计算开销并提高训练效率。这种设计使得模型在自我蒸馏中保持性能优势。

**技术框架**：整体架构为MTL-net，采用统一的CNN结构处理加速度计数据，分支出两个输出以分别完成HAR和传感器放置检测任务。框架的设计使得两个任务可以共享特征，增强了模型的学习能力。

**关键创新**：最重要的技术创新在于使用平滑的历史模型作为教师，避免了传统蒸馏方法的复杂性。这种方法不仅降低了计算成本，还提高了模型的稳定性和收敛速度。

**关键设计**：在网络结构上，MTL-net采用了卷积层和全连接层的组合，损失函数设计为多任务损失，确保两个任务的学习相辅相成。关键参数设置经过多次实验调优，以达到最佳性能。

## 📊 实验亮点

实验结果表明，Smooth-Distill在HAR和传感器放置检测任务中均显著优于传统基线，具体表现为在多个评估场景中提高了识别准确率和降低了过拟合现象，展示了其在训练效率和模型性能上的双重优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、健康监测和运动分析等，能够为人类活动识别系统提供高效的解决方案。未来，该框架可能在资源受限的平台上实现更频繁的模型更新，具有重要的实际价值。

## 📄 摘要（原文）

> This paper introduces Smooth-Distill, a novel self-distillation framework designed to simultaneously perform human activity recognition (HAR) and sensor placement detection using wearable sensor data. The proposed approach utilizes a unified CNN-based architecture, MTL-net, which processes accelerometer data and branches into two outputs for each respective task. Unlike conventional distillation methods that require separate teacher and student models, the proposed framework utilizes a smoothed, historical version of the model itself as the teacher, significantly reducing training computational overhead while maintaining performance benefits. To support this research, we developed a comprehensive accelerometer-based dataset capturing 12 distinct sleep postures across three different wearing positions, complementing two existing public datasets (MHealth and WISDM). Experimental results show that Smooth-Distill consistently outperforms alternative approaches across different evaluation scenarios, achieving notable improvements in both human activity recognition and device placement detection tasks. This method demonstrates enhanced stability in convergence patterns during training and exhibits reduced overfitting compared to traditional multitask learning baselines. This framework contributes to the practical implementation of knowledge distillation in human activity recognition systems, offering an effective solution for multitask learning with accelerometer data that balances accuracy and training efficiency. More broadly, it reduces the computational cost of model training, which is critical for scenarios requiring frequent model updates or training on resource-constrained platforms. The code and model are available at https://github.com/Kuan2vn/smooth\_distill.

