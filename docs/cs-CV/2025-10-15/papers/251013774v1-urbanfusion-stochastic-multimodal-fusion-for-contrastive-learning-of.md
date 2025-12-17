---
layout: default
title: UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations
---

# UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.13774" target="_blank" class="toolbar-btn">arXiv: 2510.13774v1</a>
    <a href="https://arxiv.org/pdf/2510.13774.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13774v1" 
            onclick="toggleFavorite(this, '2510.13774v1', 'UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Dominik J. Mühlematter, Lin Che, Ye Hong, Martin Raubal, Nina Wiedemann

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-15

**🔗 代码/项目**: [GITHUB](https://github.com/DominikM198/UrbanFusion)

---

## 💡 一句话要点

**UrbanFusion：基于随机多模态融合的对比学习，用于稳健的空间表征**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `地理空间数据` `对比学习` `Geo-Foundation Model` `城市现象预测` `Transformer` `随机多模态融合`

## 📋 核心要点

1. 现有方法主要依赖于任务特定的模型，而空间表征的基础模型通常只支持有限的模态，缺乏多模态融合能力。
2. UrbanFusion采用随机多模态融合(SMF)，通过Transformer融合模块整合街景、遥感、地图和POI等多模态数据，学习统一表征。
3. 实验结果表明，UrbanFusion在位置编码、多模态输入和区域泛化方面均优于现有GeoAI模型，并在全球56个城市的41项任务中表现出强大的泛化能力。

## 📝 摘要（中文）

本文提出UrbanFusion，一个基于Geo-Foundation Model (GeoFM)的框架，它采用随机多模态融合(SMF)来有效整合各种地理空间数据，以预测城市现象，如房价和公共健康指标。该框架利用模态特定的编码器处理不同类型的输入，包括街景图像、遥感数据、地图和兴趣点(POI)数据。这些多模态输入通过基于Transformer的融合模块进行整合，学习统一的表征。在56个城市进行的41项任务的广泛评估表明，与最先进的GeoAI模型相比，UrbanFusion具有强大的泛化能力和预测性能。它在位置编码方面优于先前的基础模型，支持推理期间的多模态输入，并且能够很好地泛化到训练期间未见过的区域。UrbanFusion可以在预训练和推理期间灵活地利用给定位置的可用模态子集，从而实现跨不同数据可用性场景的广泛适用性。

## 🔬 方法详解

**问题定义**：现有方法在预测城市现象时，要么依赖于任务特定的模型，泛化能力不足；要么空间表征模型仅支持有限模态，无法有效融合多源地理空间数据。这限制了模型在不同数据可用性场景下的应用。

**核心思路**：UrbanFusion的核心在于通过随机多模态融合（SMF）策略，训练一个能够灵活处理不同模态组合的Geo-Foundation Model。通过在训练过程中随机mask掉部分模态，模型能够学习到更鲁棒的表征，从而适应推理阶段不同模态数据可用性的情况。Transformer架构则用于融合不同模态的特征，学习统一的空间表征。

**技术框架**：UrbanFusion框架包含以下几个主要模块：1) 模态特定编码器：针对街景图像、遥感数据、地图和POI数据等不同模态，使用不同的编码器提取特征。2) Transformer融合模块：将不同模态的特征输入Transformer，学习多模态融合的表征。3) 对比学习目标：使用对比学习损失函数，鼓励相似位置的表征更加接近，不同位置的表征更加远离。4) 随机多模态融合（SMF）：在训练过程中，随机mask掉部分模态的数据，迫使模型学习更鲁棒的表征。

**关键创新**：UrbanFusion的关键创新在于随机多模态融合（SMF）策略。与以往的多模态融合方法不同，SMF允许模型在训练和推理阶段灵活地利用任意模态子集，从而提高了模型在不同数据可用性场景下的适应性。此外，UrbanFusion作为一个Geo-Foundation Model，能够通过对比学习学习到通用的空间表征，从而支持各种下游任务。

**关键设计**：模态特定编码器方面，图像数据可以使用预训练的ResNet等模型，POI数据可以使用embedding层。Transformer融合模块可以使用标准的Transformer结构，并根据输入模态的数量调整输入维度。对比学习损失函数可以使用InfoNCE loss。SMF的mask比例是一个重要的超参数，需要根据具体数据集进行调整。训练过程中，batch size和学习率等参数也需要仔细调整。

## 📊 实验亮点

UrbanFusion在56个城市的41项任务中进行了广泛评估，结果表明其性能优于现有的GeoAI模型。例如，在位置编码任务上，UrbanFusion显著优于先前的基础模型。此外，UrbanFusion还展现出良好的泛化能力，能够很好地适应训练期间未见过的区域。最重要的是，UrbanFusion能够灵活地利用任意模态子集进行推理，这使其在实际应用中具有很强的灵活性。

## 🎯 应用场景

UrbanFusion可应用于多种城市规划和管理领域，例如房价预测、公共健康指标预测、交通流量预测、犯罪风险评估等。其能够有效整合多源地理空间数据，提高预测精度和泛化能力，为城市决策提供更可靠的依据。未来，该模型可以进一步扩展到其他地理空间领域，例如环境监测、灾害预警等。

## 📄 摘要（原文）

> Forecasting urban phenomena such as housing prices and public health indicators requires the effective integration of various geospatial data. Current methods primarily utilize task-specific models, while recent foundation models for spatial representations often support only limited modalities and lack multimodal fusion capabilities. To overcome these challenges, we present UrbanFusion, a Geo-Foundation Model (GeoFM) that features Stochastic Multimodal Fusion (SMF). The framework employs modality-specific encoders to process different types of inputs, including street view imagery, remote sensing data, cartographic maps, and points of interest (POIs) data. These multimodal inputs are integrated via a Transformer-based fusion module that learns unified representations. An extensive evaluation across 41 tasks in 56 cities worldwide demonstrates UrbanFusion's strong generalization and predictive performance compared to state-of-the-art GeoAI models. Specifically, it 1) outperforms prior foundation models on location-encoding, 2) allows multimodal input during inference, and 3) generalizes well to regions unseen during training. UrbanFusion can flexibly utilize any subset of available modalities for a given location during both pretraining and inference, enabling broad applicability across diverse data availability scenarios. All source code is available at https://github.com/DominikM198/UrbanFusion.

