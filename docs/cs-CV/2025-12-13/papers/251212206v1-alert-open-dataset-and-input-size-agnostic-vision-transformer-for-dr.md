---
layout: default
title: ALERT Open Dataset and Input-Size-Agnostic Vision Transformer for Driver Activity Recognition using IR-UWB
---

# ALERT Open Dataset and Input-Size-Agnostic Vision Transformer for Driver Activity Recognition using IR-UWB

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12206v1</a>
  <a href="https://arxiv.org/pdf/2512.12206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.12206v1', 'ALERT Open Dataset and Input-Size-Agnostic Vision Transformer for Driver Activity Recognition using IR-UWB')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeongjun Park, Sunwook Hwang, Hyeonho Noh, Jin Mo Yang, Hyun Jong Yang, Saewoong Bahk

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-12-13

---

## 💡 一句话要点

**提出ISA-ViT和ALERT数据集，用于解决基于IR-UWB雷达的驾驶员行为识别问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `驾驶员行为识别` `IR-UWB雷达` `Vision Transformer` `输入尺寸无关` `领域融合`

## 📋 核心要点

1. 现有基于IR-UWB雷达的驾驶员行为识别方法缺乏大规模真实数据集，且固定输入尺寸的ViT难以适应非标准尺寸的UWB雷达数据。
2. 论文提出ISA-ViT框架，通过调整patch配置和利用预训练的位置嵌入向量，使ViT能够处理任意尺寸的UWB雷达数据，并融合距离域和频率域特征。
3. 实验结果表明，ISA-ViT在UWB雷达驾驶员行为识别任务上，相比现有ViT方法，准确率提升了22.68%。

## 📝 摘要（中文）

分心驾驶是全球致命车祸的重要原因。为了解决这个问题，研究人员正在使用基于脉冲无线电超宽带(IR-UWB)雷达的驾驶员行为识别(DAR)技术，该技术具有抗干扰、低功耗和保护隐私等优点。然而，两个挑战限制了它的应用：缺乏涵盖各种分心驾驶行为的大规模真实UWB数据集，以及难以将固定输入的Vision Transformers (ViTs)应用于具有非标准尺寸的UWB雷达数据。本研究旨在解决这两个挑战。我们提出了ALERT数据集，其中包含在真实驾驶条件下收集的七种分心驾驶活动的10220个雷达样本。我们还提出了一种输入尺寸无关的Vision Transformer (ISA-ViT)框架，专为基于雷达的DAR设计。所提出的方法调整UWB数据的大小以满足ViT输入要求，同时保留雷达特定的信息，如多普勒频移和相位特性。通过调整patch配置和利用预训练的位置嵌入向量(PEV)，ISA-ViT克服了朴素调整大小方法的局限性。此外，领域融合策略结合了距离域和频率域特征，以进一步提高分类性能。综合实验表明，ISA-ViT在基于UWB的DAR上，比现有的基于ViT的方法提高了22.68%的准确率。通过公开发布ALERT数据集并详细介绍我们的输入尺寸无关策略，这项工作促进了更鲁棒和可扩展的分心驾驶检测系统的开发，以用于实际部署。

## 🔬 方法详解

**问题定义**：现有基于IR-UWB雷达的驾驶员行为识别方法面临两个主要问题：一是缺乏大规模、真实场景下的UWB数据集，这限制了模型的泛化能力；二是传统的Vision Transformer (ViT) 需要固定尺寸的输入，而UWB雷达数据通常具有非标准尺寸，直接resize会损失雷达信号的特有信息，例如多普勒频移和相位特征。

**核心思路**：论文的核心思路是设计一个输入尺寸无关的Vision Transformer (ISA-ViT)，使其能够处理任意尺寸的UWB雷达数据，同时尽可能保留雷达信号的原始信息。此外，通过融合距离域和频率域的特征，进一步提升模型的识别性能。

**技术框架**：ISA-ViT框架主要包含以下几个阶段：1) 数据预处理：对原始UWB雷达数据进行预处理，包括降噪、滤波等操作。2) 数据尺寸调整：通过特定的resize策略，将UWB数据调整为适合ViT输入的尺寸，同时尽量保留雷达信号的特征。3) 特征提取：使用ViT提取雷达数据的特征。4) 领域融合：将距离域和频率域的特征进行融合，以获得更全面的信息。5) 分类：使用分类器对融合后的特征进行分类，得到驾驶员的行为类别。

**关键创新**：ISA-ViT的关键创新在于其输入尺寸无关性。传统的ViT需要固定尺寸的输入，而ISA-ViT通过调整patch配置和利用预训练的位置嵌入向量，使其能够处理任意尺寸的输入。此外，领域融合策略也是一个重要的创新，它能够将距离域和频率域的特征进行有效融合，从而提升模型的识别性能。

**关键设计**：在数据尺寸调整方面，论文没有采用简单的resize方法，而是设计了一种能够保留雷达信号特征的resize策略。在patch配置方面，论文根据UWB数据的特点，选择了合适的patch size和stride。在位置嵌入向量方面，论文利用预训练的位置嵌入向量，加速了模型的训练过程。此外，论文还设计了一种有效的领域融合策略，将距离域和频率域的特征进行有效融合。

## 📊 实验亮点

ISA-ViT在ALERT数据集上取得了显著的性能提升，相比于现有的基于ViT的方法，准确率提高了22.68%。这一结果表明，ISA-ViT能够有效地处理任意尺寸的UWB雷达数据，并能够充分利用雷达信号的特征信息。同时，ALERT数据集的发布为该领域的研究提供了宝贵的数据资源。

## 🎯 应用场景

该研究成果可应用于智能汽车、辅助驾驶系统等领域，通过实时监测驾驶员的行为状态，及时发出预警，从而降低因分心驾驶导致交通事故的风险。此外，该技术还可应用于其他雷达信号处理领域，例如人体姿态识别、手势识别等。

## 📄 摘要（原文）

> Distracted driving contributes to fatal crashes worldwide. To address this, researchers are using driver activity recognition (DAR) with impulse radio ultra-wideband (IR-UWB) radar, which offers advantages such as interference resistance, low power consumption, and privacy preservation. However, two challenges limit its adoption: the lack of large-scale real-world UWB datasets covering diverse distracted driving behaviors, and the difficulty of adapting fixed-input Vision Transformers (ViTs) to UWB radar data with non-standard dimensions.
>   This work addresses both challenges. We present the ALERT dataset, which contains 10,220 radar samples of seven distracted driving activities collected in real driving conditions. We also propose the input-size-agnostic Vision Transformer (ISA-ViT), a framework designed for radar-based DAR. The proposed method resizes UWB data to meet ViT input requirements while preserving radar-specific information such as Doppler shifts and phase characteristics. By adjusting patch configurations and leveraging pre-trained positional embedding vectors (PEVs), ISA-ViT overcomes the limitations of naive resizing approaches. In addition, a domain fusion strategy combines range- and frequency-domain features to further improve classification performance.
>   Comprehensive experiments demonstrate that ISA-ViT achieves a 22.68% accuracy improvement over an existing ViT-based approach for UWB-based DAR. By publicly releasing the ALERT dataset and detailing our input-size-agnostic strategy, this work facilitates the development of more robust and scalable distracted driving detection systems for real-world deployment.

