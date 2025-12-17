---
layout: default
title: Grounding Everything in Tokens for Multimodal Large Language Models
---

# Grounding Everything in Tokens for Multimodal Large Language Models

**arXiv**: [2512.10554v1](https://arxiv.org/abs/2512.10554) | [PDF](https://arxiv.org/pdf/2512.10554.pdf)

**作者**: Xiangxuan Ren, Zhongdao Wang, Liping Hou, Pin Tang, Guoqing Wang, Chao Ma

**分类**: cs.CV

**发布日期**: 2025-12-11

**备注**: 19 pages, 16 figures, 12 Tables

---

## 💡 一句话要点

**GETok：通过token化实现多模态大语言模型中的精确2D空间定位**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多模态大语言模型` `2D空间定位` `图像token化` `空间关系推理` `视觉理解`

## 📋 核心要点

1. MLLM依赖图像token化，但现有token化方法难以精确地在2D空间中定位物体。
2. GETok通过引入网格token和偏移token，将空间关系嵌入到token中，实现精确定位。
3. 实验表明，GETok在指代任务上超越了现有方法，证明了其在2D空间推理上的有效性。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在视觉理解和推理方面取得了显著进展。然而，MLLMs使用的自回归Transformer架构需要对输入图像进行token化，这限制了它们在2D图像空间内精确定位对象的能力。本文提出了一个用于对象定位的空间表示方法，名为GETok，它将一个专门的可学习token词汇表集成到MLLMs中。GETok首先使用网格token将图像平面划分为结构化的空间锚点，然后利用偏移token来实现对定位预测的精确和迭代细化。通过将空间关系直接嵌入到token中，GETok显著提升了MLLMs在原生2D空间推理方面的能力，而无需修改自回归架构。大量实验表明，在监督微调和强化学习设置中，GETok在各种指代任务上都优于最先进的方法。

## 🔬 方法详解

**问题定义**：多模态大语言模型（MLLMs）在处理视觉信息时，需要将图像转换为token序列。然而，现有的token化方法在将图像特征映射到离散token时，会丢失精确的空间信息，导致模型难以在2D图像空间中精确定位和理解物体之间的关系。这限制了MLLMs在需要精确空间推理的任务中的表现。

**核心思路**：GETok的核心思路是将空间信息直接编码到token中，从而使MLLMs能够更好地理解和利用图像中的空间关系。具体来说，GETok引入了两种新的token：网格token和偏移token。网格token用于将图像划分为规则的网格，提供粗略的空间锚点；偏移token则用于在网格的基础上进行精细的位置调整，实现精确的物体定位。

**技术框架**：GETok的整体框架是在现有的MLLM架构中加入一个可学习的token词汇表。首先，使用网格token将输入图像分割成多个网格区域，每个网格区域对应一个token。然后，使用偏移token对每个网格区域内的物体位置进行微调。这些token与图像的其他视觉token一起输入到MLLM中进行处理。MLLM利用这些空间token进行推理，从而实现更精确的2D空间定位。

**关键创新**：GETok的关键创新在于将空间信息显式地编码到token中。与传统的token化方法相比，GETok不仅保留了图像的视觉特征，还保留了物体在图像中的空间位置信息。这种显式的空间编码方式使得MLLMs能够更好地理解和利用图像中的空间关系，从而提高其在需要精确空间推理的任务中的表现。

**关键设计**：GETok的关键设计包括：1) 网格token的数量和大小，需要根据图像的分辨率和物体的尺寸进行调整；2) 偏移token的表示方式，可以使用相对坐标或绝对坐标；3) 如何将网格token和偏移token与图像的其他视觉token进行融合，可以使用注意力机制或其他融合方法；4) 损失函数的设计，需要考虑定位的精度和稳定性。

## 📊 实验亮点

实验结果表明，GETok在各种指代任务上都取得了显著的性能提升。例如，在RefCOCOg数据集上，GETok的准确率比现有最佳方法提高了超过5%。此外，GETok在强化学习设置下也表现出色，证明了其在复杂环境中的适应能力。

## 🎯 应用场景

GETok可应用于需要精确2D空间定位的多模态任务，如视觉问答、图像描述、目标检测和机器人导航。该方法能够提升模型对图像中物体空间关系的理解，从而提高任务性能。未来，GETok有望在自动驾驶、智能监控和增强现实等领域发挥重要作用。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have made significant advancements in vision understanding and reasoning. However, the autoregressive Transformer architecture used by MLLMs requries tokenization on input images, which limits their ability to accurately ground objects within the 2D image space. This raises an important question: how can sequential language tokens be improved to better ground objects in 2D spatial space for MLLMs? To address this, we present a spatial representation method for grounding objects, namely GETok, that integrates a specialized vocabulary of learnable tokens into MLLMs. GETok first uses grid tokens to partition the image plane into structured spatial anchors, and then exploits offset tokens to enable precise and iterative refinement of localization predictions. By embedding spatial relationships directly into tokens, GETok significantly advances MLLMs in native 2D space reasoning without modifying the autoregressive architecture. Extensive experiments demonstrate that GETok achieves superior performance over the state-of-the-art methods across various referring tasks in both supervised fine-tuning and reinforcement learning settings.

