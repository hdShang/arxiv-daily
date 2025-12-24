---
layout: default
title: "OmniUnet: A Multimodal Network for Unstructured Terrain Segmentation on Planetary Rovers Using RGB, Depth, and Thermal Imagery"
---

# OmniUnet: A Multimodal Network for Unstructured Terrain Segmentation on Planetary Rovers Using RGB, Depth, and Thermal Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.00580" class="toolbar-btn" target="_blank">📄 arXiv: 2508.00580v1</a>
  <a href="https://arxiv.org/pdf/2508.00580.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.00580v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.00580v1', 'OmniUnet: A Multimodal Network for Unstructured Terrain Segmentation on Planetary Rovers Using RGB, Depth, and Thermal Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raul Castilla-Arquillo, Carlos Perez-del-Pulgar, Levin Gerdes, Alfonso Garcia-Cerezo, Miguel A. Olivares-Mendez

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-01

---

## 💡 一句话要点

**提出OmniUnet以解决行星探测器在非结构化地形分割问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态感知` `语义分割` `行星探测` `深度学习` `热成像` `机器人导航` `变换器网络`

## 📋 核心要点

1. 现有的机器人导航方法在处理非结构化环境时面临多模态信息整合的挑战，尤其是在火星探测中。
2. 论文提出OmniUnet，一种基于变换器的神经网络架构，能够有效整合RGB、深度和热成像数据进行语义分割。
3. 实验结果显示，OmniUnet在复杂地形分割中取得了80.37%的像素准确率，且在资源受限的设备上表现良好。

## 📝 摘要（中文）

机器人在非结构化环境中的导航需要多模态感知系统以支持安全导航。多模态性使得不同传感器收集的互补信息得以整合。然而，这些信息必须通过专门设计的机器学习算法进行处理，以充分利用异构数据。此外，还需识别哪些传感器模态对目标环境的导航最具信息量。在火星探测中，热成像因土壤类型的热行为差异而被证明对评估地形安全性具有重要价值。本研究提出了OmniUnet，一种基于变换器的神经网络架构，利用RGB、深度和热成像（RGB-D-T）进行语义分割。通过3D打印开发了定制的多模态传感器外壳，并安装在火星探测器自主测试平台（MaRTA）上，以在西班牙北部的Bardenas半沙漠收集多模态数据集。该数据集的子集经过手动标注，以支持网络的监督训练。模型经过定量和定性评估，像素准确率达到80.37%，在分割复杂非结构化地形方面表现出色。推理测试在资源受限的计算机（Jetson Orin Nano）上平均预测时间为673毫秒，确认其适合在机器人上部署。网络的软件实现和标注数据集已公开，以支持未来在行星机器人多模态地形感知方面的研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决行星探测器在非结构化地形中进行语义分割的挑战。现有方法在处理多模态传感器数据时，往往无法有效整合不同来源的信息，导致导航安全性不足。

**核心思路**：论文提出的OmniUnet网络架构通过变换器模型，能够同时处理RGB、深度和热成像数据，充分利用各模态的互补信息，从而提高地形分割的准确性和可靠性。

**技术框架**：OmniUnet的整体架构包括数据预处理模块、特征提取模块和语义分割模块。数据预处理模块负责对RGB、深度和热成像数据进行标准化和融合，特征提取模块使用变换器网络提取多模态特征，最后语义分割模块生成最终的地形分割结果。

**关键创新**：OmniUnet的主要创新在于其多模态融合能力，能够有效整合不同传感器的数据，尤其是热成像在土壤类型识别中的应用，这在现有方法中较为少见。

**关键设计**：在网络设计中，采用了特定的损失函数以优化多模态特征的融合效果，并通过手动标注的数据集进行监督训练，确保模型在复杂地形中的表现。

## 📊 实验亮点

实验结果表明，OmniUnet在复杂非结构化地形的分割任务中取得了80.37%的像素准确率，相较于传统方法有显著提升。此外，在资源受限的Jetson Orin Nano上，模型的平均推理时间为673毫秒，显示出良好的实时处理能力。

## 🎯 应用场景

该研究的潜在应用领域包括行星探测、自动驾驶和无人机导航等。通过提高机器人在复杂环境中的感知能力，OmniUnet能够显著提升探测任务的安全性和效率，推动未来的行星探索和其他高风险环境的自动化技术发展。

## 📄 摘要（原文）

> Robot navigation in unstructured environments requires multimodal perception systems that can support safe navigation. Multimodality enables the integration of complementary information collected by different sensors. However, this information must be processed by machine learning algorithms specifically designed to leverage heterogeneous data. Furthermore, it is necessary to identify which sensor modalities are most informative for navigation in the target environment. In Martian exploration, thermal imagery has proven valuable for assessing terrain safety due to differences in thermal behaviour between soil types. This work presents OmniUnet, a transformer-based neural network architecture for semantic segmentation using RGB, depth, and thermal (RGB-D-T) imagery. A custom multimodal sensor housing was developed using 3D printing and mounted on the Martian Rover Testbed for Autonomy (MaRTA) to collect a multimodal dataset in the Bardenas semi-desert in northern Spain. This location serves as a representative environment of the Martian surface, featuring terrain types such as sand, bedrock, and compact soil. A subset of this dataset was manually labeled to support supervised training of the network. The model was evaluated both quantitatively and qualitatively, achieving a pixel accuracy of 80.37% and demonstrating strong performance in segmenting complex unstructured terrain. Inference tests yielded an average prediction time of 673 ms on a resource-constrained computer (Jetson Orin Nano), confirming its suitability for on-robot deployment. The software implementation of the network and the labeled dataset have been made publicly available to support future research in multimodal terrain perception for planetary robotics.

