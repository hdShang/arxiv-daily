---
layout: default
title: "TxP: Reciprocal Generation of Ground Pressure Dynamics and Activity Descriptions for Improving Human Activity Recognition"
---

# TxP: Reciprocal Generation of Ground Pressure Dynamics and Activity Descriptions for Improving Human Activity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02052" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02052v1</a>
  <a href="https://arxiv.org/pdf/2505.02052.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02052v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02052v1', 'TxP: Reciprocal Generation of Ground Pressure Dynamics and Activity Descriptions for Improving Human Activity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lala Shakti Swarup Ray, Lars Krupp, Vitor Fortes Rey, Bo Zhou, Sungho Suh, Paul Lukowicz

**分类**: cs.AI, cs.CV

**发布日期**: 2025-05-04

---

## 💡 一句话要点

**提出TxP模型以解决压力传感器在人类活动识别中的应用不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类活动识别` `压力传感器` `生成模型` `多模态学习` `数据增强` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的人类活动识别方法主要依赖惯性测量单元和视觉数据，未能充分利用压力传感器的潜力，导致对微妙身体动态的识别不足。
2. 本文提出的TxP模型通过生成基础模型，将压力数据与自然语言相结合，实现了活动描述与压力序列的双向转换，填补了这一技术空白。
3. 在真实数据集上，TxP在瑜伽和日常活动的识别中表现出色，宏F1分数提高了12.4%，显著提升了压力传感器在HAR中的应用效果。

## 📝 摘要（中文）

基于传感器的人类活动识别（HAR）主要集中在惯性测量单元和视觉数据上，往往忽视了压力传感器的独特能力，这些传感器能够捕捉微妙的身体动态和重心变化。尽管压力传感器在姿势和平衡活动中具有潜力，但由于数据集有限，它们在HAR领域的应用仍然不足。为了解决这一问题，本文提出了一种双向Text×Pressure模型，利用生成基础模型将压力数据解释为自然语言。TxP实现了两个任务：将活动文本描述转换为压力序列，以及从动态压力图生成活动描述和分类。通过在合成的PressLang数据集上训练，TxP在真实世界数据上验证了其在瑜伽和日常任务等活动中的有效性，提供了基于原子动作的数据增强和分类的新方法，HAR性能相比现有技术提高了12.4%的宏F1分数。

## 🔬 方法详解

**问题定义**：本文旨在解决压力传感器在人类活动识别中的应用不足，现有方法主要依赖于惯性测量单元和视觉数据，未能充分利用压力传感器捕捉的微妙动态和重心变化。

**核心思路**：论文提出的TxP模型利用生成基础模型，将压力数据与自然语言进行双向转换，具体实现了Text2Pressure和Pressure2Text两个任务，以此来增强活动识别的准确性和丰富性。

**技术框架**：TxP模型的整体架构包括两个主要模块：Text2Pressure模块将活动描述转换为压力序列，Pressure2Text模块则从压力数据生成活动描述和分类。模型训练使用了合成的PressLang数据集，并结合了预训练模型如CLIP和LLaMA 2 13B Chat。

**关键创新**：TxP的核心创新在于将压力传感器数据与自然语言生成相结合，形成双向生成模型，这一方法在HAR领域尚属首次，显著提升了对复杂活动的理解能力。

**关键设计**：模型训练中采用了特定的损失函数来优化文本与压力序列之间的对应关系，同时在网络结构上结合了多模态学习的思想，以增强模型对不同输入形式的适应能力。

## 📊 实验亮点

TxP模型在真实世界数据集上的实验结果显示，其在瑜伽和日常活动的识别中，宏F1分数提高了12.4%，相较于现有最先进技术表现出显著的性能提升，展示了压力传感器在HAR中的广泛应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括健康监测、运动训练和人机交互等。通过提升压力传感器在活动识别中的应用，TxP模型能够为运动分析、康复训练等提供更精准的反馈，未来可能在智能家居和可穿戴设备中发挥重要作用。

## 📄 摘要（原文）

> Sensor-based human activity recognition (HAR) has predominantly focused on Inertial Measurement Units and vision data, often overlooking the capabilities unique to pressure sensors, which capture subtle body dynamics and shifts in the center of mass. Despite their potential for postural and balance-based activities, pressure sensors remain underutilized in the HAR domain due to limited datasets. To bridge this gap, we propose to exploit generative foundation models with pressure-specific HAR techniques. Specifically, we present a bidirectional Text$\times$Pressure model that uses generative foundation models to interpret pressure data as natural language. TxP accomplishes two tasks: (1) Text2Pressure, converting activity text descriptions into pressure sequences, and (2) Pressure2Text, generating activity descriptions and classifications from dynamic pressure maps. Leveraging pre-trained models like CLIP and LLaMA 2 13B Chat, TxP is trained on our synthetic PressLang dataset, containing over 81,100 text-pressure pairs. Validated on real-world data for activities such as yoga and daily tasks, TxP provides novel approaches to data augmentation and classification grounded in atomic actions. This consequently improved HAR performance by up to 12.4\% in macro F1 score compared to the state-of-the-art, advancing pressure-based HAR with broader applications and deeper insights into human movement.

