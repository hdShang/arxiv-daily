---
layout: default
title: LISAT: Language-Instructed Segmentation Assistant for Satellite Imagery
---

# LISAT: Language-Instructed Segmentation Assistant for Satellite Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02829" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02829v1</a>
  <a href="https://arxiv.org/pdf/2505.02829.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02829v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02829v1', 'LISAT: Language-Instructed Segmentation Assistant for Satellite Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jerome Quenum, Wen-Han Hsieh, Tsung-Han Wu, Ritwik Gupta, Trevor Darrell, David M. Chan

**分类**: cs.AI

**发布日期**: 2025-05-05

**备注**: 28 pages, 10 figures, 19 tables

**🔗 代码/项目**: [PROJECT_PAGE](https://lisat-bair.github.io/LISAt/)

---

## 💡 一句话要点

**提出LISAT以解决复杂遥感影像的语言指导分割问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感影像` `语言指导` `分割模型` `多模态学习` `地理空间推理`

## 📋 核心要点

1. 现有的推理分割模型在处理复杂遥感影像时表现不佳，无法有效应对用户的复杂查询。
2. LISAT通过结合视觉和语言信息，设计了一种新的模型架构，能够理解复杂场景并进行有效分割。
3. 实验结果表明，LISAT在遥感描述任务上比现有模型提高了10.04%（BLEU-4），在推理分割任务上提升了143.36%（gIoU）。

## 📝 摘要（中文）

分割模型能够识别图像中预定义的一组对象，但对于复杂用户查询的推理分割模型仍处于初级阶段。近期的研究表明，视觉-语言模型能够在开放领域中生成合理的分割掩码。然而，我们的实验显示，这些模型在复杂的遥感影像上表现不佳。为此，本文提出了LISAT，一个旨在描述复杂遥感场景、回答相关问题并分割感兴趣对象的视觉-语言模型。LISAT在一个新的地理空间推理-分割数据集GRES上进行训练，超越了现有的地理空间基础模型，并在推理分割任务上显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理分割模型在复杂遥感影像上无法有效处理用户复杂查询的问题。这些模型在生成分割掩码时缺乏对多对象的推理能力。

**核心思路**：LISAT通过引入多模态学习，结合视觉信息与语言指令，设计了一种新型的模型架构，能够更好地理解复杂场景并进行分割。

**技术框架**：LISAT的整体架构包括数据预处理、模型训练和推理三个主要阶段。首先，利用新创建的GRES数据集进行训练，然后在推理阶段生成分割掩码。

**关键创新**：LISAT的主要创新在于其针对遥感影像的特定设计，能够处理复杂的用户查询并生成高质量的分割结果，与现有方法相比具有显著的性能提升。

**关键设计**：在模型设计中，LISAT采用了多模态预训练数据集PreGRES，并使用了特定的损失函数和网络结构，以优化模型在推理分割任务中的表现。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

LISAT在遥感描述任务上超越了现有的地理空间基础模型RS-GPT4V，提升幅度达到10.04%（BLEU-4）。在推理分割任务上，LISAT的表现更是超过了现有的开放领域模型，提升幅度达到143.36%（gIoU），显示出其卓越的性能。

## 🎯 应用场景

LISAT的研究成果在遥感影像分析、环境监测、城市规划等领域具有广泛的应用潜力。通过提高对复杂场景的理解能力，该模型能够为决策提供更准确的信息，推动相关领域的发展。

## 📄 摘要（原文）

> Segmentation models can recognize a pre-defined set of objects in images. However, models that can reason over complex user queries that implicitly refer to multiple objects of interest are still in their infancy. Recent advances in reasoning segmentation--generating segmentation masks from complex, implicit query text--demonstrate that vision-language models can operate across an open domain and produce reasonable outputs. However, our experiments show that such models struggle with complex remote-sensing imagery. In this work, we introduce LISAt, a vision-language model designed to describe complex remote-sensing scenes, answer questions about them, and segment objects of interest. We trained LISAt on a new curated geospatial reasoning-segmentation dataset, GRES, with 27,615 annotations over 9,205 images, and a multimodal pretraining dataset, PreGRES, containing over 1 million question-answer pairs. LISAt outperforms existing geospatial foundation models such as RS-GPT4V by over 10.04 % (BLEU-4) on remote-sensing description tasks, and surpasses state-of-the-art open-domain models on reasoning segmentation tasks by 143.36 % (gIoU). Our model, datasets, and code are available at https://lisat-bair.github.io/LISAt/

