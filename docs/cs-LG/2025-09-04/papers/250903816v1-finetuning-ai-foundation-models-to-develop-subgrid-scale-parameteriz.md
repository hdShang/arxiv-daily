---
layout: default
title: "Finetuning AI Foundation Models to Develop Subgrid-Scale Parameterizations: A Case Study on Atmospheric Gravity Waves"
---

# Finetuning AI Foundation Models to Develop Subgrid-Scale Parameterizations: A Case Study on Atmospheric Gravity Waves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03816" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03816v1</a>
  <a href="https://arxiv.org/pdf/2509.03816.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03816v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03816v1', 'Finetuning AI Foundation Models to Develop Subgrid-Scale Parameterizations: A Case Study on Atmospheric Gravity Waves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aman Gupta, Aditi Sheshadri, Sujit Roy, Johannes Schmude, Vishal Gaur, Wei Ji Leong, Manil Maskey, Rahul Ramachandran

**分类**: physics.ao-ph, cs.LG

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**微调AI基础模型，为大气重力波开发次网格尺度参数化方案**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI基础模型` `气候模型` `参数化` `重力波` `微调` `深度学习` `次网格尺度` `大气科学`

## 📋 核心要点

1. 全球气候模型中次网格尺度过程的参数化是模型不确定性的主要来源，现有方法难以准确建模。
2. 利用预训练的AI基础模型，通过微调方式学习高分辨率数据中的通量，从而为粗分辨率模型提供更准确的参数化。
3. 实验表明，微调后的模型在预测性能上优于传统机器学习模型，尤其是在预训练未覆盖的区域，Hellinger距离显著降低。

## 📝 摘要（中文）

全球气候模型对无法充分解析的大气-海洋过程（如重力波、云、湿对流和湍流）进行参数化。这些未解析过程的次网格尺度闭合是模型不确定性的主要来源。本文提出了一种新的方法，通过微调预训练的AI基础模型（FM）来开发小尺度气候过程的机器学习参数化方案。FM在气候研究中尚未被充分探索。来自一个23亿参数FM（NASA和IBM Research的Prithvi WxC）的预训练编码器-解码器，包含大气演化的潜在概率表示，被微调（或重用）以创建一个用于大气重力波（GWs）的深度学习参数化方案。该参数化方案通过学习来自具有10倍精细分辨率的大气再分析的通量，来捕获粗分辨率气候模型的GW效应。与机器学习模型基线（Attention U-Net）的月平均值和瞬时演化的比较表明，FM参数化方案在整个大气中都具有卓越的预测性能，即使在预训练中排除的区域也是如此。这种性能提升使用Hellinger距离进行量化，基线为0.11，微调模型为0.06。研究结果强调了FM的多功能性和可重用性，可用于完成一系列与大气和气候相关的应用，从而为更多地球系统过程创建由观测驱动且物理上准确的参数化方案铺平道路。

## 🔬 方法详解

**问题定义**：全球气候模型需要对无法直接解析的次网格尺度过程进行参数化，例如大气重力波。传统的参数化方法存在较大的不确定性，影响了气候模型的预测精度。现有的机器学习方法虽然可以学习这些过程，但往往需要从头开始训练，计算成本高昂，且泛化能力有限。

**核心思路**：利用预训练的AI基础模型（Foundation Model）的强大表征能力，通过微调的方式，使其适应特定的气候过程参数化任务。这种方法可以有效利用预训练模型中已经学习到的通用知识，减少训练时间和数据需求，并提高模型的泛化能力。

**技术框架**：该方法的核心是使用NASA和IBM Research的Prithvi WxC模型，这是一个包含23亿参数的预训练编码器-解码器模型。该模型已经学习了大气演化的潜在概率表示。研究人员将该模型进行微调，使其能够学习高分辨率大气再分析数据中的重力波通量，从而为粗分辨率气候模型提供参数化方案。整体流程包括：1) 选择合适的预训练模型；2) 准备高分辨率训练数据；3) 微调预训练模型的编码器-解码器部分；4) 在粗分辨率气候模型中集成微调后的参数化方案；5) 评估模型性能。

**关键创新**：该方法最重要的创新点在于将AI基础模型引入气候过程参数化领域。与传统的从头开始训练的机器学习模型相比，微调预训练模型可以显著提高模型的性能和泛化能力。此外，该方法还展示了AI基础模型在气候研究中的多功能性和可重用性。

**关键设计**：研究中使用了Hellinger距离作为评估模型性能的指标。Attention U-Net被用作基线模型进行比较。关键参数包括微调的学习率、训练epochs以及损失函数的选择。具体网络结构细节未在摘要中详细描述，但强调了编码器-解码器结构的重要性。

## 📊 实验亮点

实验结果表明，通过微调AI基础模型得到的参数化方案在预测性能上优于传统的Attention U-Net模型。具体而言，微调模型的Hellinger距离为0.06，而基线模型的Hellinger距离为0.11，表明微调模型在捕捉大气重力波效应方面具有显著优势，即使在预训练数据未覆盖的区域也表现良好。

## 🎯 应用场景

该研究成果可应用于改进全球气候模型中大气重力波的参数化，从而提高气候模型的预测精度。此外，该方法还可以推广到其他气候过程的参数化，例如云、湿对流和湍流等。通过构建更准确、更高效的参数化方案，可以更好地理解和预测气候变化，为应对气候变化提供科学依据。

## 📄 摘要（原文）

> Global climate models parameterize a range of atmospheric-oceanic processes like gravity waves, clouds, moist convection, and turbulence that cannot be sufficiently resolved. These subgrid-scale closures for unresolved processes are a leading source of model uncertainty. Here, we present a new approach to developing machine learning parameterizations of small-scale climate processes by fine-tuning a pre-trained AI foundation model (FM). FMs are largely unexplored in climate research. A pre-trained encoder-decoder from a 2.3 billion parameter FM (NASA and IBM Research's Prithvi WxC) -- which contains a latent probabilistic representation of atmospheric evolution -- is fine-tuned (or reused) to create a deep learning parameterization for atmospheric gravity waves (GWs). The parameterization captures GW effects for a coarse-resolution climate model by learning the fluxes from an atmospheric reanalysis with 10 times finer resolution. A comparison of monthly averages and instantaneous evolution with a machine learning model baseline (an Attention U-Net) reveals superior predictive performance of the FM parameterization throughout the atmosphere, even in regions excluded from pre-training. This performance boost is quantified using the Hellinger distance, which is 0.11 for the baseline and 0.06 for the fine-tuned model. Our findings emphasize the versatility and reusability of FMs, which could be used to accomplish a range of atmosphere- and climate-related applications, leading the way for the creation of observations-driven and physically accurate parameterizations for more earth-system processes.

