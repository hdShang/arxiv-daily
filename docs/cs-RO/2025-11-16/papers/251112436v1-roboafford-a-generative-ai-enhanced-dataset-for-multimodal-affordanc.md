---
layout: default
title: RoboAfford++: A Generative AI-Enhanced Dataset for Multimodal Affordance Learning in Robotic Manipulation and Navigation
---

# RoboAfford++: A Generative AI-Enhanced Dataset for Multimodal Affordance Learning in Robotic Manipulation and Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12436" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12436v1</a>
  <a href="https://arxiv.org/pdf/2511.12436.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12436v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12436v1', 'RoboAfford++: A Generative AI-Enhanced Dataset for Multimodal Affordance Learning in Robotic Manipulation and Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoshuai Hao, Yingbo Tang, Lingfeng Zhang, Yanbiao Ma, Yunfeng Diao, Ziyu Jia, Wenbo Ding, Hangjun Ye, Long Chen

**分类**: cs.RO

**发布日期**: 2025-11-16

---

## 💡 一句话要点

**RoboAfford++：一个生成式AI增强的多模态可供性学习数据集，用于机器人操作和导航**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人操作` `机器人导航` `可供性学习` `多模态数据集` `视觉语言模型`

## 📋 核心要点

1. 视觉语言模型在高级任务规划和场景理解方面表现出色，但在推断物理交互的可操作位置（如抓取点和放置区域）方面存在局限性。
2. RoboAfford++数据集通过生成式AI增强，提供了细粒度的物体和空间可供性标注，旨在弥补现有数据集在可供性信息方面的不足。
3. 实验结果表明，在RoboAfford++上微调视觉语言模型可以显著提升其对物体和空间可供性的推理能力，证明了数据集的有效性。

## 📝 摘要（中文）

本文提出了RoboAfford++，一个生成式AI增强的数据集，用于机器人操作和导航中的多模态可供性学习。该数据集包含869,987张图像，并配有200万个问答（QA）标注，涵盖三个关键任务：基于属性和空间关系识别目标物体的物体可供性识别；精确定位用于操作的功能部件的物体可供性预测；以及识别用于物体放置和机器人导航的自由空间的空间可供性定位。此外，本文还提出了RoboAfford-Eval，一个用于评估真实场景中可供性感知预测的综合基准，包含338个精心标注的样本，涵盖上述三个任务。实验结果表明，现有视觉语言模型（VLMs）在可供性学习方面存在不足，而基于RoboAfford++数据集的微调可以显著提高它们对物体和空间可供性的推理能力，验证了数据集的有效性。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLMs）在高级任务规划和场景理解方面表现出色，但缺乏对物体和空间可供性的细粒度理解，导致无法准确推断物理交互的可操作位置，例如功能性的抓取点和允许放置的区域。现有训练数据集缺乏对物体和空间可供性的细粒度标注，是造成这一问题的主要原因。

**核心思路**：本文的核心思路是构建一个大规模、高质量的多模态可供性数据集RoboAfford++，并利用生成式AI技术增强数据集的标注质量和数量。通过在RoboAfford++上微调VLMs，可以显著提升其对物体和空间可供性的推理能力，从而提高机器人在操作和导航任务中的性能。

**技术框架**：RoboAfford++数据集涵盖三个关键任务：物体可供性识别（Object Affordance Recognition）、物体可供性预测（Object Affordance Prediction）和空间可供性定位（Spatial Affordance Localization）。数据集包含图像和问答（QA）标注。此外，还提出了RoboAfford-Eval基准，用于评估模型在真实场景中的可供性感知预测能力。整体流程包括数据收集、标注、生成式AI增强、模型训练和评估。

**关键创新**：该论文的关键创新在于：1) 提出了一个大规模、多模态的可供性数据集RoboAfford++，填补了现有数据集在可供性信息方面的空白。2) 利用生成式AI技术增强数据集的标注质量和数量，提高了数据的可用性。3) 提出了RoboAfford-Eval基准，用于评估模型在真实场景中的可供性感知预测能力。与现有方法相比，该方法能够更有效地提升VLMs对物体和空间可供性的理解和推理能力。

**关键设计**：数据集包含869,987张图像和200万个问答标注，涵盖物体属性、空间关系、功能部件和自由空间等信息。RoboAfford-Eval基准包含338个精心标注的样本，涵盖上述三个任务。具体参数设置、损失函数和网络结构等技术细节未在摘要中详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，在RoboAfford++数据集上微调现有视觉语言模型（VLMs）可以显著提高其对物体和空间可供性的推理能力。具体性能数据和提升幅度未在摘要中给出，属于未知信息。但整体实验结果验证了RoboAfford++数据集的有效性，并表明其能够有效提升VLMs在可供性学习方面的性能。

## 🎯 应用场景

该研究成果可广泛应用于机器人操作、自动驾驶、智能家居等领域。通过提升机器人对环境的理解和交互能力，可以实现更智能、更高效的自动化任务，例如物体抓取、放置、导航等。未来，该数据集和基准可以促进机器人可供性学习领域的发展，推动机器人技术在实际场景中的应用。

## 📄 摘要（原文）

> Robotic manipulation and navigation are fundamental capabilities of embodied intelligence, enabling effective robot interactions with the physical world. Achieving these capabilities requires a cohesive understanding of the environment, including object recognition to localize target objects, object affordances to identify potential interaction areas and spatial affordances to discern optimal areas for both object placement and robot movement. While Vision-Language Models (VLMs) excel at high-level task planning and scene understanding, they often struggle to infer actionable positions for physical interaction, such as functional grasping points and permissible placement regions. This limitation stems from the lack of fine-grained annotations for object and spatial affordances in their training datasets. To tackle this challenge, we introduce RoboAfford++, a generative AI-enhanced dataset for multimodal affordance learning for both robotic manipulation and navigation. Our dataset comprises 869,987 images paired with 2.0 million question answering (QA) annotations, covering three critical tasks: object affordance recognition to identify target objects based on attributes and spatial relationships, object affordance prediction to pinpoint functional parts for manipulation, and spatial affordance localization to identify free space for object placement and robot navigation. Complementing this dataset, we propose RoboAfford-Eval, a comprehensive benchmark for assessing affordance-aware prediction in real-world scenarios, featuring 338 meticulously annotated samples across the same three tasks. Extensive experimental results reveal the deficiencies of existing VLMs in affordance learning, while fine-tuning on the RoboAfford++ dataset significantly enhances their ability to reason about object and spatial affordances, validating the dataset's effectiveness.

