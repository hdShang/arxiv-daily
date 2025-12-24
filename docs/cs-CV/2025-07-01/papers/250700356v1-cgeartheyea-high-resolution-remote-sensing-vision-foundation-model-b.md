---
layout: default
title: "CGEarthEye:A High-Resolution Remote Sensing Vision Foundation Model Based on the Jilin-1 Satellite Constellation"
---

# CGEarthEye:A High-Resolution Remote Sensing Vision Foundation Model Based on the Jilin-1 Satellite Constellation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00356" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00356v1</a>
  <a href="https://arxiv.org/pdf/2507.00356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00356v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00356v1', 'CGEarthEye:A High-Resolution Remote Sensing Vision Foundation Model Based on the Jilin-1 Satellite Constellation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiwei Yi, Xin Cheng, Jingyu Ma, Ruifei Zhu, Junwei Tian, Yuanxiu Zhou, Xinge Zhao, Hongzhe Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-07-01

**备注**: A Remote Sensing Fundation Model for Very High Resolution Images

---

## 💡 一句话要点

**提出CGEarthEye以解决高分辨率遥感图像解读问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像解读` `自监督学习` `高分辨率遥感` `吉林一号卫星` `深度学习` `特征可视化` `模型优化`

## 📋 核心要点

1. 现有的高分辨率遥感视觉基础模型受限于超高分辨率图像获取渠道，导致模型发展缓慢。
2. CGEarthEye框架专为吉林一号卫星设计，包含多种参数规模的主干网络，并引入了新的自监督学习数据集JLSSD。
3. 在10个基准数据集上的评估结果显示，CGEarthEye在多个遥感任务上均表现出色，达到了最先进的性能水平。

## 📝 摘要（中文）

深度学习方法显著推动了遥感智能解读的发展，但超高分辨率光学遥感图像获取渠道有限，制约了高分辨率遥感视觉基础模型的进展。作为全球最大的亚米级商业遥感卫星星座，吉林一号星座提供了丰富的亚米级图像资源。本研究提出CGEarthEye，一个专为吉林一号卫星特性设计的遥感视觉基础模型框架，包含五个不同参数规模的主干网络，总计21亿参数。为增强模型的表示能力，我们开发了JLSSD，这是第一个具有全球覆盖的1500万规模多时相自监督学习数据集。综合评估显示CGEarthEye在10个基准数据集上持续达到最先进的性能，展现出在特征可视化、模型收敛、参数效率和实际映射应用中的优越特性。

## 🔬 方法详解

**问题定义**：本研究旨在解决高分辨率遥感视觉基础模型在数据获取渠道有限的情况下，如何有效利用吉林一号卫星的图像资源进行智能解读的问题。现有方法在处理超高分辨率图像时，往往面临数据稀缺和模型性能不足的挑战。

**核心思路**：论文提出的CGEarthEye框架专注于吉林一号卫星的特性，通过构建一个包含多种参数规模的主干网络，结合自监督学习策略，旨在提升模型的表示能力和泛化能力。

**技术框架**：CGEarthEye框架由五个不同参数规模的主干网络组成，整体架构包括数据预处理、模型训练和评估三个主要阶段。特别地，模型训练阶段引入了JLSSD数据集，并采用多种对比学习策略进行预训练。

**关键创新**：最重要的创新点在于构建了JLSSD数据集，这是第一个具有全球覆盖的1500万规模多时相自监督学习数据集，结合了季节性对比、增强对比和掩码补丁对比策略，显著提升了模型的学习效果。

**关键设计**：在模型设计中，采用了多层次表示聚类和采样策略，确保数据的多样性和代表性。此外，模型的损失函数设计考虑了对比学习的特点，以优化模型的特征提取能力。

## 📊 实验亮点

CGEarthEye在10个基准数据集上的评估结果显示，其在四个典型遥感任务上均达到了最先进的性能，具体表现为在特征可视化、模型收敛和参数效率方面的显著提升，进一步验证了其在实际映射应用中的有效性。

## 🎯 应用场景

CGEarthEye的研究成果在遥感图像解读、环境监测、城市规划等领域具有广泛的应用潜力。其卓越的表示能力将推动吉林一号数据在传统地球观测应用中的更高效利用，促进相关领域的技术进步和应用创新。

## 📄 摘要（原文）

> Deep learning methods have significantly advanced the development of intelligent rinterpretation in remote sensing (RS), with foundational model research based on large-scale pre-training paradigms rapidly reshaping various domains of Earth Observation (EO). However, compared to the open accessibility and high spatiotemporal coverage of medium-resolution data, the limited acquisition channels for ultra-high-resolution optical RS imagery have constrained the progress of high-resolution remote sensing vision foundation models (RSVFM). As the world's largest sub-meter-level commercial RS satellite constellation, the Jilin-1 constellation possesses abundant sub-meter-level image resources. This study proposes CGEarthEye, a RSVFM framework specifically designed for Jilin-1 satellite characteristics, comprising five backbones with different parameter scales with totaling 2.1 billion parameters. To enhance the representational capacity of the foundation model, we developed JLSSD, the first 15-million-scale multi-temporal self-supervised learning (SSL) dataset featuring global coverage with quarterly temporal sampling within a single year, constructed through multi-level representation clustering and sampling strategies. The framework integrates seasonal contrast, augmentation-based contrast, and masked patch token contrastive strategies for pre-training. Comprehensive evaluations across 10 benchmark datasets covering four typical RS tasks demonstrate that the CGEarthEye consistently achieves state-of-the-art (SOTA) performance. Further analysis reveals CGEarthEye's superior characteristics in feature visualization, model convergence, parameter efficiency, and practical mapping applications. This study anticipates that the exceptional representation capabilities of CGEarthEye will facilitate broader and more efficient applications of Jilin-1 data in traditional EO application.

