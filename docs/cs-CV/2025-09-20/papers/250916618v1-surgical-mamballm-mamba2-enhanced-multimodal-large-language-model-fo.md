---
layout: default
title: "Surgical-MambaLLM: Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery"
---

# Surgical-MambaLLM: Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16618" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16618v1</a>
  <a href="https://arxiv.org/pdf/2509.16618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16618v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16618v1', 'Surgical-MambaLLM: Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengfei Hao, Hongqiu Wang, Shuaibo Li, Zhaohu Xing, Guang Yang, Kaishun Wu, Lei Zhu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-20

**备注**: Early accepted by MICCAI2025

---

## 💡 一句话要点

**Surgical-MambaLLM：基于Mamba2增强的多模态大语言模型，用于机器人手术中的视觉问题定位回答**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人手术` `视觉问题定位回答` `多模态融合` `大语言模型` `Mamba2` `空间信息感知` `手术器械感知`

## 📋 核心要点

1. 现有方法难以建立文本和视觉细节之间复杂的依赖关系，且缺乏对手术场景空间信息的有效感知。
2. Surgical-MambaLLM将Mamba2与LLM结合，利用Mamba2捕获跨模态依赖和感知空间信息的能力，提升LLM对手术图像的理解。
3. 实验结果表明，Surgical-MambaLLM在EndoVis17/18-VQLA数据集上超越现有SOTA方法，显著提升了手术VQLA任务的性能。

## 📝 摘要（中文）

近年来，机器人手术中的视觉问题定位回答（Surgical-VQLA）因其在辅助医学生和初级医生理解手术场景方面的潜力而备受关注。大语言模型（LLM）的快速发展为该任务提供了更有前景的解决方案。然而，当前的方法难以建立文本和视觉细节之间复杂的依赖关系，并且难以感知手术场景的空间信息。为了解决这些挑战，我们提出了一种新方法Surgical-MambaLLM，该方法首次将Mamba2与LLM结合在手术领域，利用Mamba2有效捕获跨模态依赖关系和感知手术场景空间信息的能力，从而增强LLM对手术图像的理解。具体来说，我们提出了跨模态双向Mamba2集成（CBMI）模块，利用Mamba2实现有效的多模态融合，并具有跨模态集成能力。此外，针对手术场景的几何特征，我们设计了手术器械感知（SIP）扫描模式，供Mamba2扫描手术图像，增强模型对手术场景的空间理解。大量实验表明，我们的Surgical-MambaLLM模型在EndoVis17-VQLA和EndoVis18-VQLA数据集上优于最先进的方法，显著提高了Surgical-VQLA任务的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人手术场景下，视觉问题定位回答（Surgical-VQLA）任务中，现有方法无法有效建立文本和视觉信息之间的复杂依赖关系，以及缺乏对手术场景空间信息理解的问题。现有方法的痛点在于无法充分利用手术图像中的空间几何信息，导致对问题的理解不够准确。

**核心思路**：论文的核心思路是利用Mamba2模型在序列建模和空间信息感知方面的优势，将其与大语言模型（LLM）相结合，从而增强LLM对手术场景的理解能力。通过Mamba2，模型能够更好地捕获跨模态依赖关系，并感知手术场景的空间信息，从而更准确地回答视觉问题。

**技术框架**：Surgical-MambaLLM的整体架构包含以下几个主要模块：首先，使用视觉编码器提取手术图像的视觉特征；然后，通过提出的跨模态双向Mamba2集成（CBMI）模块，将视觉特征和文本特征进行融合，CBMI模块利用Mamba2进行有效的多模态融合；接着，利用手术器械感知（SIP）扫描模式，让Mamba2扫描手术图像，增强模型对手术场景的空间理解；最后，将融合后的特征输入到LLM中，生成最终的答案。

**关键创新**：论文最重要的技术创新点在于首次将Mamba2模型引入到手术VQLA任务中，并提出了跨模态双向Mamba2集成（CBMI）模块和手术器械感知（SIP）扫描模式。CBMI模块能够有效地融合视觉和文本信息，而SIP扫描模式则能够增强模型对手术场景空间信息的理解。与现有方法相比，Surgical-MambaLLM能够更好地利用手术图像中的空间几何信息，从而提高VQLA的准确性。

**关键设计**：CBMI模块采用了双向Mamba2结构，分别从视觉到文本和从文本到视觉两个方向进行信息融合。SIP扫描模式则根据手术器械的形状和位置，设计了一种特定的扫描方式，以增强模型对手术器械的感知能力。具体的参数设置和损失函数等技术细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

Surgical-MambaLLM在EndoVis17-VQLA和EndoVis18-VQLA数据集上取得了显著的性能提升，超越了现有的SOTA方法。具体而言，在EndoVis17-VQLA数据集上，模型的性能提升了X%（具体数值未知）；在EndoVis18-VQLA数据集上，模型的性能提升了Y%（具体数值未知）。这些实验结果表明，Surgical-MambaLLM能够有效地提高手术VQLA任务的准确性。

## 🎯 应用场景

Surgical-MambaLLM在机器人手术领域具有广泛的应用前景。它可以辅助医学生和初级医生理解手术场景，提高手术培训的效率。此外，该模型还可以应用于术中导航和决策支持，帮助医生更准确地进行手术操作，降低手术风险。未来，该研究有望推动智能手术机器人的发展，提高手术的智能化水平。

## 📄 摘要（原文）

> In recent years, Visual Question Localized-Answering in robotic surgery (Surgical-VQLA) has gained significant attention for its potential to assist medical students and junior doctors in understanding surgical scenes. Recently, the rapid development of Large Language Models (LLMs) has provided more promising solutions for this task. However, current methods struggle to establish complex dependencies between text and visual details, and have difficulty perceiving the spatial information of surgical scenes. To address these challenges, we propose a novel method, Surgical-MambaLLM, which is the first to combine Mamba2 with LLM in the surgical domain, that leverages Mamba2's ability to effectively capture cross-modal dependencies and perceive spatial information in surgical scenes, thereby enhancing the LLMs' understanding of surgical images. Specifically, we propose the Cross-modal Bidirectional Mamba2 Integration (CBMI) module to leverage Mamba2 for effective multimodal fusion, with its cross-modal integration capabilities. Additionally, tailored to the geometric characteristics of surgical scenes, we design the Surgical Instrument Perception (SIP) scanning mode for Mamba2 to scan the surgical images, enhancing the model's spatial understanding of the surgical scene. Extensive experiments demonstrate that our Surgical-MambaLLM model outperforms the state-of-the-art methods on the EndoVis17-VQLA and EndoVis18-VQLA datasets, significantly improving the performance of the Surgical-VQLA task.

