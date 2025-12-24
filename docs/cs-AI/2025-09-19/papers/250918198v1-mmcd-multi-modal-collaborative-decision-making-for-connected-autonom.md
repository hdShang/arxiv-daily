---
layout: default
title: "MMCD: Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation"
---

# MMCD: Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18198" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18198v1</a>
  <a href="https://arxiv.org/pdf/2509.18198.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18198v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18198v1', 'MMCD: Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Liu, Zikang Wang, Peng Gao, Yu Shen, Pratap Tokekar, Ming Lin

**分类**: cs.AI, cs.MA, cs.RO

**发布日期**: 2025-09-19

**🔗 代码/项目**: [PROJECT_PAGE](https://ruiiu.github.io/mmcd)

---

## 💡 一句话要点

**提出MMCD框架，利用多模态知识蒸馏提升互联自动驾驶在复杂环境下的决策能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `互联自动驾驶` `多模态融合` `知识蒸馏` `协同决策` `鲁棒性` `自动驾驶安全` `空地协同`

## 📋 核心要点

1. 现有互联自动驾驶方法通常假设训练和测试时所有模态数据和互联车辆均可用，这在实际中难以保证。
2. MMCD框架通过融合自车和协同车辆的多模态观测信息，并利用跨模态知识蒸馏，提升系统在数据缺失情况下的鲁棒性。
3. 实验表明，MMCD框架在互联自动驾驶和空地协同场景中，显著提升了驾驶安全性，最高提升达20.7%。

## 📝 摘要（中文）

本文提出了一种用于互联自动驾驶的新型框架MMCD（多模态协同决策）。该框架融合了自车和协同车辆的多模态观测信息，以增强在复杂条件下的决策能力。为了确保在测试期间某些数据模态不可用时的鲁棒性能，本文提出了一种基于跨模态知识蒸馏的方法，该方法采用教师-学生模型结构。教师模型使用多种数据模态进行训练，而学生模型旨在在减少模态的情况下有效运行。在地面车辆互联自动驾驶和空地车辆协作的实验中，我们的方法将驾驶安全性提高了高达20.7%，超过了现有最佳基线，能够更好地检测潜在事故并做出安全的驾驶决策。

## 🔬 方法详解

**问题定义**：论文旨在解决互联自动驾驶系统中，由于传感器故障或互联车辆缺失导致的数据模态不完整问题。现有方法通常依赖于所有模态数据的可用性，这在实际应用中是不现实的，会严重影响系统的安全性和可靠性。因此，如何在部分模态数据缺失的情况下，依然能够做出安全可靠的决策是本论文要解决的核心问题。

**核心思路**：论文的核心思路是利用多模态信息进行协同决策，并通过知识蒸馏技术，将多模态教师模型的知识迁移到单模态或少模态的学生模型中。这样，即使在测试阶段某些模态数据不可用，学生模型也能利用学习到的知识做出合理的决策，从而提高系统的鲁棒性。

**技术框架**：MMCD框架包含以下主要模块：1) 多模态数据融合模块：融合来自自车和协同车辆的RGB图像和LiDAR点云数据。2) 教师-学生模型训练模块：教师模型使用所有模态数据进行训练，学生模型使用部分模态数据进行训练。3) 知识蒸馏模块：利用教师模型的输出作为指导，训练学生模型，使其能够模仿教师模型的行为。4) 决策模块：根据融合后的多模态信息或学生模型的输出，做出最终的驾驶决策。

**关键创新**：论文的关键创新在于提出了基于跨模态知识蒸馏的互联自动驾驶决策框架。与现有方法相比，MMCD框架能够在数据模态不完整的情况下，依然保持较高的决策准确性和安全性。此外，该框架还能够有效地利用协同车辆的信息，提高系统的感知范围和决策能力。

**关键设计**：在知识蒸馏过程中，论文采用了多种损失函数，包括模仿学习损失和一致性损失，以确保学生模型能够有效地学习教师模型的行为。具体的网络结构和参数设置根据不同的应用场景进行调整。例如，在空地协同场景中，需要考虑无人机的运动特性和感知范围，因此需要设计专门的网络结构来处理无人机的数据。

## 📊 实验亮点

实验结果表明，MMCD框架在互联自动驾驶和空地协同场景中均取得了显著的性能提升。在驾驶安全性方面，MMCD框架比现有最佳基线提高了高达20.7%。此外，MMCD框架在数据模态缺失的情况下，依然能够保持较高的决策准确性，证明了其良好的鲁棒性。这些结果表明，MMCD框架是一种有效的互联自动驾驶决策方法。

## 🎯 应用场景

该研究成果可应用于各种互联自动驾驶场景，例如城市道路自动驾驶、高速公路自动驾驶、以及空地协同作业等。通过提高系统在复杂环境下的鲁棒性和安全性，可以降低交通事故的发生率，提高交通效率，并为未来的智能交通系统奠定基础。此外，该方法还可以推广到其他多模态融合和知识蒸馏的应用领域。

## 📄 摘要（原文）

> Autonomous systems have advanced significantly, but challenges persist in accident-prone environments where robust decision-making is crucial. A single vehicle's limited sensor range and obstructed views increase the likelihood of accidents. Multi-vehicle connected systems and multi-modal approaches, leveraging RGB images and LiDAR point clouds, have emerged as promising solutions. However, existing methods often assume the availability of all data modalities and connected vehicles during both training and testing, which is impractical due to potential sensor failures or missing connected vehicles. To address these challenges, we introduce a novel framework MMCD (Multi-Modal Collaborative Decision-making) for connected autonomy. Our framework fuses multi-modal observations from ego and collaborative vehicles to enhance decision-making under challenging conditions. To ensure robust performance when certain data modalities are unavailable during testing, we propose an approach based on cross-modal knowledge distillation with a teacher-student model structure. The teacher model is trained with multiple data modalities, while the student model is designed to operate effectively with reduced modalities. In experiments on $\textit{connected autonomous driving with ground vehicles}$ and $\textit{aerial-ground vehicles collaboration}$, our method improves driving safety by up to ${\it 20.7}\%$, surpassing the best-existing baseline in detecting potential accidents and making safe driving decisions. More information can be found on our website https://ruiiu.github.io/mmcd.

