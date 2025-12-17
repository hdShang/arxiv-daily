---
layout: default
title: Enhancing Zero-Shot Anomaly Detection: CLIP-SAM Collaboration with Cascaded Prompts
---

# Enhancing Zero-Shot Anomaly Detection: CLIP-SAM Collaboration with Cascaded Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11028" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11028v1</a>
  <a href="https://arxiv.org/pdf/2510.11028.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11028v1" onclick="toggleFavorite(this, '2510.11028v1', 'Enhancing Zero-Shot Anomaly Detection: CLIP-SAM Collaboration with Cascaded Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanning Hou, Ke Xu, Junfa Li, Yanran Ruan, Jianfeng Qiu

**分类**: cs.CV

**发布日期**: 2025-10-13

**备注**: Accepted by PRCV

---

## 💡 一句话要点

**提出CLIP-SAM协同与级联提示的两阶段框架，提升零样本异常检测性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本学习` `异常检测` `图像分割` `CLIP` `SAM` `工业质检` `特征点提示`

## 📋 核心要点

1. 现有零样本异常分割方法难以有效引导预训练模型，导致分割精度不足。
2. 提出CLIP-SAM协同框架，利用CLIP定位异常，生成点提示引导SAM进行精确分割。
3. 实验表明，该方法在多个数据集上取得了SOTA结果，尤其在Visa数据集上提升显著。

## 📝 摘要（中文）

本文提出了一种新颖的两阶段框架，用于工业异常检测中的零样本异常分割任务。该框架充分利用了CLIP强大的异常定位能力和SAM的边界感知能力。首先，为了缓解SAM对物体分割的倾向，提出了协同特征点提示生成（PPG）模块，该模块协同利用CLIP和SAM生成正负点提示，引导SAM专注于分割异常区域而非整个物体。其次，为了进一步优化SAM的分割结果，减轻粗糙边界和孤立噪声，引入了SAM级联提示（CPS）模块，该模块采用混合提示与SAM的轻量级解码器级联，实现了异常区域的精确分割。在多个数据集上的实验验证表明，该方法实现了最先进的零样本异常分割结果。特别值得注意的是在Visa数据集上的表现，在{$F_1$-max}和AP指标上分别超过了现有最佳方法10.3％和7.7％。

## 🔬 方法详解

**问题定义**：零样本异常分割旨在无需训练的情况下，分割出图像中的异常区域。现有方法通常难以有效利用预训练模型，或者容易将整个物体分割出来，而不是仅仅分割异常部分。此外，分割结果可能存在边界粗糙和噪声点的问题。

**核心思路**：论文的核心思路是结合CLIP的异常定位能力和SAM的边界感知能力，通过协同生成提示来引导SAM专注于异常区域的分割，并使用级联提示优化分割结果。这样可以避免SAM分割整个物体，并提高分割的精度和鲁棒性。

**技术框架**：该框架包含两个主要阶段：1) 协同特征点提示生成（PPG）模块：利用CLIP提取图像特征，并根据特征相似度生成正负点提示，这些提示被输入到SAM中，引导其关注异常区域。2) SAM级联提示（CPS）模块：使用混合提示（包括点提示和掩码提示）与SAM的轻量级解码器级联，逐步优化分割结果，减少边界粗糙和噪声。

**关键创新**：该方法的主要创新在于：1) 协同利用CLIP和SAM，通过特征点提示生成模块，有效引导SAM进行异常区域分割。2) 提出级联提示策略，通过混合提示和轻量级解码器，逐步优化分割结果，提高分割精度。

**关键设计**：PPG模块中，CLIP用于提取图像特征，并计算特征相似度，以确定正负点提示的位置。CPS模块中，混合提示包括来自PPG模块的点提示和SAM先前分割结果的掩码提示。轻量级解码器可能包含卷积层和注意力机制，用于融合不同尺度的特征，并优化分割结果。损失函数可能包括交叉熵损失和Dice损失，以提高分割精度和鲁棒性。具体参数设置和网络结构细节未知。

## 📊 实验亮点

该方法在多个数据集上取得了SOTA结果，尤其在Visa数据集上，F1-max指标提升了10.3%，AP指标提升了7.7%，显著优于现有零样本异常分割方法。这表明该方法能够有效利用预训练模型，实现精确的异常区域分割。

## 🎯 应用场景

该研究成果可应用于工业质检、医疗影像分析、安防监控等领域。例如，在工业生产线上，可以自动检测产品表面的缺陷；在医疗影像中，可以辅助医生诊断病灶；在安防监控中，可以识别异常行为。该方法无需训练，具有很强的通用性和实用价值，有望降低异常检测的成本，提高检测效率。

## 📄 摘要（原文）

> Recently, the powerful generalization ability exhibited by foundation models has brought forth new solutions for zero-shot anomaly segmentation tasks. However, guiding these foundation models correctly to address downstream tasks remains a challenge. This paper proposes a novel two-stage framework, for zero-shot anomaly segmentation tasks in industrial anomaly detection. This framework excellently leverages the powerful anomaly localization capability of CLIP and the boundary perception ability of SAM.(1) To mitigate SAM's inclination towards object segmentation, we propose the Co-Feature Point Prompt Generation (PPG) module. This module collaboratively utilizes CLIP and SAM to generate positive and negative point prompts, guiding SAM to focus on segmenting anomalous regions rather than the entire object. (2) To further optimize SAM's segmentation results and mitigate rough boundaries and isolated noise, we introduce the Cascaded Prompts for SAM (CPS) module. This module employs hybrid prompts cascaded with a lightweight decoder of SAM, achieving precise segmentation of anomalous regions. Across multiple datasets, consistent experimental validation demonstrates that our approach achieves state-of-the-art zero-shot anomaly segmentation results. Particularly noteworthy is our performance on the Visa dataset, where we outperform the state-of-the-art methods by 10.3\% and 7.7\% in terms of {$F_1$-max} and AP metrics, respectively.

