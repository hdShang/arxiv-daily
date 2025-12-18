---
layout: default
title: CoT-PL: Visual Chain-of-Thought Reasoning Meets Pseudo-Labeling for Open-Vocabulary Object Detection
---

# CoT-PL: Visual Chain-of-Thought Reasoning Meets Pseudo-Labeling for Open-Vocabulary Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14792" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14792v1</a>
  <a href="https://arxiv.org/pdf/2510.14792.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14792v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14792v1', 'CoT-PL: Visual Chain-of-Thought Reasoning Meets Pseudo-Labeling for Open-Vocabulary Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hojun Choi, Youngsun Lim, Jaeyo Shin, Hyunjung Shim

**分类**: cs.CV

**发布日期**: 2025-10-16

**备注**: 28 pages, 13 Figures, 12 Tables

---

## 💡 一句话要点

**提出CoT-PL框架，通过视觉链式推理和伪标签提升开放词汇目标检测在复杂场景下的性能。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放词汇目标检测` `视觉链式推理` `伪标签` `对比学习` `背景接地`

## 📋 核心要点

1. 现有开放词汇目标检测方法依赖直接图像-文本匹配，忽略了推理步骤，导致在复杂场景下鲁棒性不足。
2. CoT-PL框架通过视觉链式推理分解对象理解为区域感知、类别识别和背景接地三个步骤，提升伪标签质量。
3. 实验表明，CoT-PL在开放词汇COCO和LVIS数据集上显著提升了新类别的检测性能，达到新的SOTA。

## 📝 摘要（中文）

开放词汇目标检测(OVD)旨在识别和定位训练期间未见过的对象类别。现有方法通常利用视觉-语言模型(VLMs)通过图像-文本对齐生成伪标签，使检测器能够推广到未见过的类别而无需显式监督。然而，这些方法严重依赖直接的图像-文本匹配，忽略了解释语义复杂场景所必需的中间推理步骤。这导致在拥挤或遮挡的视觉环境中鲁棒性有限。本文提出了一种新的框架CoT-PL，该框架在伪标签过程中采用了结构化的视觉链式思考(CoT)推理。CoT-PL将对象理解分解为三个可解释的步骤：(1)即使对于未见过的对象，也能进行区域感知；(2)通过零样本推理进行类别识别；(3)背景接地以分离语义复杂的对象。关键是，第三步自然地激发了我们的对比背景学习(CBL)，它使用预先计算的背景线索作为负样本，以促进对象和背景之间的特征解耦。通过这种方式，CoT推理和CBL形成了一个集成的pipeline，专门用于在拥挤或遮挡场景中进行鲁棒的伪标签。值得注意的是，在这两种设置中，我们新类别的伪标签质量分别比最好的现有方法提高了103.4%和168.4%。大量的实验表明，CoT-PL在开放词汇COCO上实现了+7.7 AP50，在LVIS上实现了+2.9 mask AP，为新类别设定了新的state of the art。

## 🔬 方法详解

**问题定义**：开放词汇目标检测旨在识别训练集中未出现的物体类别。现有方法依赖视觉-语言模型生成伪标签，但直接的图像-文本匹配忽略了推理过程，导致在拥挤或遮挡场景下性能下降。现有方法无法有效区分物体和复杂背景，导致伪标签质量不高。

**核心思路**：CoT-PL的核心思路是将复杂的物体识别任务分解为多个可解释的步骤，模拟人类的推理过程。通过显式地建模区域感知、类别识别和背景接地，可以更准确地生成伪标签，从而提升开放词汇目标检测的性能。对比背景学习(CBL)进一步增强了模型区分物体和背景的能力。

**技术框架**：CoT-PL框架包含三个主要阶段：1) 区域感知：利用预训练的视觉模型检测图像中的潜在物体区域，即使这些物体属于未见过的类别。2) 类别识别：使用零样本视觉-语言模型对检测到的区域进行分类，生成候选的伪标签。3) 背景接地：通过对比学习，区分物体和背景，过滤掉错误的伪标签。CBL模块利用预计算的背景线索作为负样本，促进特征解耦。

**关键创新**：CoT-PL的关键创新在于引入了视觉链式推理(CoT)到伪标签生成过程中。与直接图像-文本匹配的方法不同，CoT-PL显式地建模了物体识别的中间推理步骤，从而提高了伪标签的质量和鲁棒性。对比背景学习(CBL)是另一个创新点，它通过利用背景信息作为负样本，增强了模型区分物体和背景的能力。

**关键设计**：CoT-PL的关键设计包括：1) 使用预训练的视觉模型（如CLIP）进行区域感知和类别识别。2) 设计对比损失函数，用于对比背景学习，鼓励模型学习区分物体和背景的特征。3) 使用预计算的背景线索作为负样本，提高CBL的效率。4) 通过实验调整对比损失的权重，以平衡物体和背景的学习。

## 📊 实验亮点

CoT-PL在开放词汇COCO数据集上实现了+7.7 AP50的提升，在LVIS数据集上实现了+2.9 mask AP的提升，显著优于现有方法，达到了新的state-of-the-art。在拥挤和遮挡场景下，CoT-PL的伪标签质量分别比现有最佳方法提高了103.4%和168.4%，证明了其在复杂场景下的鲁棒性。

## 🎯 应用场景

CoT-PL在开放词汇目标检测上的突破，为智能监控、自动驾驶、机器人导航等领域带来了潜在的应用价值。该技术可以使机器人在复杂环境中识别和定位未知的物体，提高其适应性和智能化水平。未来，该方法可以扩展到其他视觉任务，如图像描述和视觉问答。

## 📄 摘要（原文）

> Open-vocabulary object detection (OVD) seeks to recognize and localize object categories beyond those seen during training. Recent approaches typically leverage vision-language models (VLMs) to generate pseudo-labels using image-text alignment, allowing detectors to generalize to unseen classes without explicit supervision. However, these methods depend heavily on direct image-text matching, neglecting the intermediate reasoning steps essential for interpreting semantically complex scenes. This results in limited robustness when confronted with crowded or occluded visual contexts. In this paper, we introduce CoT-PL, a new framework that employs structured visual chain-of-thought (CoT) reasoning into the pseudo-labeling process. CoT-PL decomposes object understanding into three interpretable steps: (1) region perception even for unseen objects, (2) category recognition via zero-shot reasoning, and (3) background grounding to separate semantically complex objects. Crucially, the third step naturally motivates our contrastive background learning (CBL) that uses the pre-computed background cues as negatives to promote feature disentanglement between objects and background. In this way, CoT reasoning and CBL form an integrated pipeline tailored to robust pseudo-labeling in crowded or occluded scenes. Notably, in these two settings, our novel-class pseudo-label quality achieves relative improvements of 103.4% and 168.4% over the best prior, respectively. Our extensive experiments demonstrate that CoT-PL achieves +7.7 AP50 on open-vocabulary COCO and +2.9 mask AP on LVIS for novel classes, setting a new state of the art.

