---
layout: default
title: "FusWay: Multimodal hybrid fusion approach. Application to Railway Defect Detection"
---

# FusWay: Multimodal hybrid fusion approach. Application to Railway Defect Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06987" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06987v1</a>
  <a href="https://arxiv.org/pdf/2509.06987.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06987v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06987v1', 'FusWay: Multimodal hybrid fusion approach. Application to Railway Defect Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexey Zhukov, Jenny Benois-Pineau, Amira Youssef, Akka Zemmari, Mohamed Mosbah, Virginie Taillandier

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**提出FusWay多模态融合方法，用于提升铁路缺陷检测精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `铁路缺陷检测` `多模态融合` `YOLOv8` `Vision Transformer` `音频特征` `目标检测` `结构健康监测`

## 📋 核心要点

1. 现有铁路缺陷检测方法依赖单一视觉模态，易受干扰，导致过度检测，影响检测精度。
2. FusWay融合图像和音频信息，利用YOLOv8n快速检测和ViT提取多层特征，提升检测准确率。
3. 实验表明，FusWay在铁路缺陷检测中，精度和整体准确率相较于仅视觉方法提升0.2个百分点。

## 📝 摘要（中文）

多模态融合是一种多媒体技术，已广泛应用于图像信息伴随信号/音频的任务中。后者可能不传达高度语义信息，例如语音或音乐，但可以包含用于检测轨道结构元素或缺陷的音频信号。虽然诸如YOLO系列检测器等经典检测方法可以有效地部署在图像模态上进行缺陷检测，但单模态方法仍然存在局限性，在出现与正常结构元素相似的外观时容易过度检测。本文提出了一种新的多模态融合架构，该架构基于领域规则，并结合了YOLO和Vision Transformer骨干网络。它集成了YOLOv8n用于快速目标检测，并使用Vision Transformer (ViT) 结合从多个层（7、16和19）提取的特征图以及合成的音频表示，用于两种缺陷类别：轨道断裂和表面缺陷。融合在音频和图像之间进行。在真实铁路数据集上的实验评估表明，与仅使用视觉的方法相比，我们的多模态融合将精度和整体准确率提高了0.2个百分点。Student's unpaired t-test也证实了平均准确率差异的统计显著性。

## 🔬 方法详解

**问题定义**：铁路缺陷检测是保障铁路安全的关键环节。现有的基于视觉的缺陷检测方法，例如YOLO系列，在复杂场景下容易受到光照、阴影等因素的干扰，导致将正常结构元素误判为缺陷，产生过度检测的问题。这降低了检测的准确性和可靠性。

**核心思路**：FusWay的核心思路是利用多模态融合，将图像信息和音频信息结合起来，互补彼此的不足。图像信息提供缺陷的视觉特征，而音频信息则提供缺陷产生的振动或声音特征。通过融合这两种模态的信息，可以更准确地判断缺陷的存在和类型，减少过度检测。

**技术框架**：FusWay的整体架构包含以下几个主要模块：1) YOLOv8n目标检测器：用于快速检测图像中的潜在缺陷区域。2) Vision Transformer (ViT)：用于提取图像的多层特征，捕捉更丰富的上下文信息。3) 音频特征提取模块：用于将音频信号转换为可用的特征表示。4) 多模态融合模块：将图像特征和音频特征进行融合，得到最终的缺陷检测结果。

**关键创新**：FusWay的关键创新在于其多模态融合策略。它不是简单地将图像和音频特征进行拼接，而是根据领域知识，选择性地融合不同模态的信息。例如，对于某些类型的缺陷，音频信息可能更具有判别性，因此在融合时会赋予音频特征更高的权重。此外，FusWay还利用ViT提取图像的多层特征，从而更好地捕捉缺陷的上下文信息。

**关键设计**：FusWay的关键设计包括：1) YOLOv8n作为快速目标检测器，保证了检测的效率。2) ViT提取图像的第7、16和19层特征，以捕捉不同尺度的信息。3) 音频特征的合成方式，需要根据具体的音频信号特点进行设计。4) 多模态融合模块的融合策略，需要根据不同缺陷类型的特点进行优化。损失函数的设计也需要考虑多模态信息的特点，例如可以使用对比损失来增强不同模态之间的关联性。

## 📊 实验亮点

FusWay在真实铁路数据集上进行了评估，实验结果表明，与仅使用视觉的方法相比，FusWay将精度和整体准确率提高了0.2个百分点。Student's unpaired t-test也证实了平均准确率差异的统计显著性。这表明FusWay的多模态融合策略能够有效地提升铁路缺陷检测的性能。

## 🎯 应用场景

FusWay可应用于铁路轨道安全检测、桥梁结构健康监测等领域。通过融合视觉和听觉等多模态信息，能够更准确、更可靠地检测结构性缺陷，降低安全风险，减少维护成本，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Multimodal fusion is a multimedia technique that has become popular in the wide range of tasks where image information is accompanied by a signal/audio. The latter may not convey highly semantic information, such as speech or music, but some measures such as audio signal recorded by mics in the goal to detect rail structure elements or defects. While classical detection approaches such as You Only Look Once (YOLO) family detectors can be efficiently deployed for defect detection on the image modality, the single modality approaches remain limited. They yield an overdetection in case of the appearance similar to normal structural elements. The paper proposes a new multimodal fusion architecture built on the basis of domain rules with YOLO and Vision transformer backbones. It integrates YOLOv8n for rapid object detection with a Vision Transformer (ViT) to combine feature maps extracted from multiple layers (7, 16, and 19) and synthesised audio representations for two defect classes: rail Rupture and Surface defect. Fusion is performed between audio and image. Experimental evaluation on a real-world railway dataset demonstrates that our multimodal fusion improves precision and overall accuracy by 0.2 points compared to the vision-only approach. Student's unpaired t-test also confirms statistical significance of differences in the mean accuracy.

