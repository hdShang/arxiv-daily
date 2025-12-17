---
layout: default
title: MobiAct: Efficient MAV Action Recognition Using MobileNetV4 with Contrastive Learning and Knowledge Distillation
---

# MobiAct: Efficient MAV Action Recognition Using MobileNetV4 with Contrastive Learning and Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19273" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19273v1</a>
  <a href="https://arxiv.org/pdf/2510.19273.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19273v1" onclick="toggleFavorite(this, '2510.19273v1', 'MobiAct: Efficient MAV Action Recognition Using MobileNetV4 with Contrastive Learning and Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhang Nengbo, Ho Hann Woei

**分类**: cs.CV

**发布日期**: 2025-10-22

---

## 💡 一句话要点

**提出MobiAct：一种基于MobileNetV4、对比学习和知识蒸馏的高效MAV动作识别框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `微型飞行器` `动作识别` `MobileNetV4` `知识蒸馏` `对比学习` `轻量级模型` `无人机集群`

## 📋 核心要点

1. 现有MAV动作识别方法依赖于计算密集型模型，难以在资源受限的MAV平台上实现实时感知和协同。
2. MobiAct采用MobileNetV4作为骨干网络，并结合阶段式正交知识蒸馏和无参数注意力机制，提升模型效率和精度。
3. 实验结果表明，MobiAct在保持高识别精度的同时，显著降低了能耗和计算量，并实现了更快的动作解码速度。

## 📝 摘要（中文）

本文提出了一种轻量级的微型飞行器(MAV)动作识别框架MobiAct，旨在以低计算成本实现高精度。MobiAct采用MobileNetV4作为骨干网络，并引入了一种阶段式正交知识蒸馏(SOKD)策略，有效地将MAV运动特征从教师网络(ResNet18)转移到学生网络，从而提高知识转移效率。此外，该架构还集成了一种无参数注意力机制，以提高识别精度，而无需增加模型复杂度。此外，还开发了一种混合损失训练策略，将多个损失目标结合起来，确保训练期间的稳定和鲁棒优化。实验结果表明，所提出的MobiAct实现了低能耗和低计算的MAV动作识别，同时在比较方法中保持了最快的动作解码速度。在所有三个自收集的数据集上，MobiAct实现了92.12%的平均识别精度，同时仅消耗136.16 pJ的能量，并以每秒8.84个动作的速度进行识别。值得注意的是，MobiAct的动作解码速度比领先方法快2倍，且识别精度具有高度可比性，突出了其在MAV动作识别中的卓越效率。

## 🔬 方法详解

**问题定义**：现有的微型飞行器（MAV）动作识别方法通常依赖于大型、计算量高的模型，这使得它们不适合资源有限的MAV平台。因此，如何在保持识别精度的前提下，降低计算成本和能耗，是当前MAV动作识别领域面临的关键问题。现有方法的痛点在于精度和效率之间的权衡，难以同时满足实时性和准确性的需求。

**核心思路**：MobiAct的核心思路是利用轻量级网络结构（MobileNetV4）作为基础，并通过知识蒸馏技术将大型模型的知识迁移到小型模型中，从而在降低计算复杂度的同时，保持较高的识别精度。此外，引入无参数注意力机制进一步提升模型对关键特征的关注能力。

**技术框架**：MobiAct的整体框架包括以下几个主要模块：1) 数据预处理；2) 特征提取（使用MobileNetV4）；3) 知识蒸馏（使用阶段式正交知识蒸馏SOKD）；4) 注意力机制（无参数注意力）；5) 分类器（例如，全连接层）；6) 混合损失训练。流程是：首先，使用预处理后的MAV动作数据训练一个大型教师网络（ResNet18）。然后，利用SOKD策略将教师网络的知识迁移到MobileNetV4学生网络。在训练过程中，使用混合损失函数优化学生网络。

**关键创新**：MobiAct的关键创新在于以下几个方面：1) 采用了轻量级的MobileNetV4作为骨干网络，降低了计算复杂度；2) 提出了阶段式正交知识蒸馏（SOKD）策略，提高了知识迁移的效率；3) 集成了无参数注意力机制，增强了模型对关键特征的关注能力，而无需增加额外的参数；4) 开发了混合损失训练策略，确保训练过程的稳定性和鲁棒性。

**关键设计**：在知识蒸馏方面，SOKD策略通过在不同阶段对教师和学生网络的特征进行正交化处理，从而提高知识迁移的效率。无参数注意力机制的具体实现细节未知，但其目标是在不增加模型参数的情况下，提升模型对重要特征的关注度。混合损失函数可能包括分类损失、蒸馏损失以及其他正则化项，以平衡模型的精度和泛化能力。具体的损失函数权重和参数设置未知。

## 📊 实验亮点

MobiAct在三个自收集的数据集上取得了平均92.12%的识别精度，同时仅消耗136.16 pJ的能量，并以每秒8.84个动作的速度进行识别。与现有方法相比，MobiAct的动作解码速度提高了2倍，且识别精度具有高度可比性，充分证明了其在MAV动作识别方面的卓越效率。

## 🎯 应用场景

MobiAct在自主无人机集群、智能监控、灾害救援等领域具有广泛的应用前景。通过在资源受限的MAV平台上实现高效准确的动作识别，可以提升无人机的自主导航、目标跟踪和协同作业能力。该研究成果有助于推动无人机技术在实际场景中的应用，并为未来的智能空中机器人发展奠定基础。

## 📄 摘要（原文）

> Accurate and efficient recognition of Micro Air Vehicle (MAV) motion is essential for enabling real-time perception and coordination in autonomous aerial swarm. However, most existing approaches rely on large, computationally intensive models that are unsuitable for resource-limited MAV platforms, which results in a trade-off between recognition accuracy and inference speed. To address these challenges, this paper proposes a lightweight MAV action recognition framework, MobiAct, designed to achieve high accuracy with low computational cost. Specifically, MobiAct adopts MobileNetV4 as the backbone network and introduces a Stage-wise Orthogonal Knowledge Distillation (SOKD) strategy to effectively transfer MAV motion features from a teacher network (ResNet18) to a student network, thereby enhancing knowledge transfer efficiency. Furthermore, a parameter-free attention mechanism is integrated into the architecture to improve recognition accuracy without increasing model complexity. In addition, a hybrid loss training strategy is developed to combine multiple loss objectives, which ensures stable and robust optimization during training. Experimental results demonstrate that the proposed MobiAct achieves low-energy and low-computation MAV action recognition, while maintaining the fastest action decoding speed among compared methods. Across all three self-collected datasets, MobiAct achieves an average recognition accuracy of 92.12%, while consuming only 136.16 pJ of energy and processing recognition at a rate of 8.84 actions per second. Notably, MobiAct decodes actions up to 2 times faster than the leading method, with highly comparable recognition accuracy, highlighting its superior efficiency in MAV action recognition.

