---
layout: default
title: "Towards Objective Obstetric Ultrasound Assessment: Contrastive Representation Learning for Fetal Movement Detection"
---

# Towards Objective Obstetric Ultrasound Assessment: Contrastive Representation Learning for Fetal Movement Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20214" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20214v1</a>
  <a href="https://arxiv.org/pdf/2510.20214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20214v1', 'Towards Objective Obstetric Ultrasound Assessment: Contrastive Representation Learning for Fetal Movement Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Talha Ilyas, Duong Nhu, Allison Thomas, Arie Levin, Lim Wei Yap, Shu Gong, David Vera Anaya, Yiwen Jiang, Deval Mehta, Ritesh Warty, Vinayak Smith, Maya Reddy, Euan Wallace, Wenlong Cheng, Zongyuan Ge, Faezeh Marzbanrad

**分类**: cs.CV

**发布日期**: 2025-10-23

**备注**: This is the preprint version of the manuscript submitted to IEEE Journal of Biomedical and Health Informatics (JBHI) for review

---

## 💡 一句话要点

**提出CURL框架，利用对比学习进行胎儿超声视频中的胎动检测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `胎儿运动检测` `对比学习` `自监督学习` `超声视频` `产前诊断`

## 📋 核心要点

1. 传统胎动检测方法主观性强、准确率低，难以有效评估胎儿健康状况，存在临床需求缺口。
2. CURL框架利用空间和时间对比学习，从无标签超声视频中学习鲁棒的胎动表征，无需人工标注。
3. 实验结果表明，CURL在胎动检测任务上表现出色，灵敏度达到78.01%，AUROC达到81.60%。

## 📝 摘要（中文）

准确的胎动(FM)检测对于评估产前健康至关重要，因为异常的运动模式可能表明潜在的并发症，如胎盘功能障碍或胎儿窘迫。传统的胎动检测方法，包括孕妇感知和心电监护(CTG)，存在主观性和准确性有限的问题。为了应对这些挑战，我们提出了一种新颖的自监督学习框架——对比超声视频表征学习(CURL)，用于从延长的胎儿超声视频记录中进行胎动检测。我们的方法利用双重对比损失，结合了空间和时间对比学习，以学习鲁棒的运动表征。此外，我们引入了一种特定于任务的采样策略，确保在自监督训练期间有效分离运动和非运动片段，同时通过概率微调方法实现对任意长度超声记录的灵活推理。在包含92名受试者、每人30分钟超声会话的内部数据集上进行评估，CURL实现了78.01%的灵敏度和81.60%的AUROC，证明了其在可靠和客观的胎动分析方面的潜力。这些结果突出了自监督对比学习在胎儿运动分析中的潜力，为改善产前监测和临床决策铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决胎儿超声视频中胎动检测的自动化和客观化问题。现有方法，如孕妇感知和心电监护，依赖主观判断，准确性不足，且无法提供连续的、定量的胎动信息。这限制了对胎儿健康状况的准确评估。

**核心思路**：论文的核心思路是利用自监督对比学习，从大量的无标签胎儿超声视频中学习胎动的通用表征。通过对比学习，模型能够区分包含胎动和不包含胎动的视频片段，从而提取出与胎动相关的关键特征。这种方法避免了对大量标注数据的依赖，降低了成本，并提高了模型的泛化能力。

**技术框架**：CURL框架包含以下主要阶段：1) 数据预处理：对超声视频进行裁剪和标准化。2) 自监督训练：使用双重对比损失（空间对比损失和时间对比损失）训练模型，学习胎动表征。3) 微调：使用少量标注数据对模型进行微调，以适应特定的胎动检测任务。4) 推理：使用概率微调方法，对任意长度的超声视频进行胎动检测。

**关键创新**：论文的关键创新在于：1) 提出了双重对比损失，同时考虑了空间和时间上的对比信息，从而学习更鲁棒的胎动表征。2) 引入了任务特定的采样策略，确保在自监督训练期间有效分离运动和非运动片段。3) 提出了概率微调方法，使得模型能够灵活地处理任意长度的超声视频。

**关键设计**：CURL使用ResNet-18作为骨干网络，提取视频帧的特征。空间对比损失旨在区分同一视频中不同位置的帧，而时间对比损失旨在区分同一视频中不同时间段的帧。任务特定的采样策略通过选择包含运动和不包含运动的视频片段来平衡训练数据。概率微调方法使用sigmoid函数将模型的输出转换为概率值，从而实现对任意长度视频的胎动检测。

## 📊 实验亮点

CURL在内部数据集上取得了显著的性能提升，灵敏度达到78.01%，AUROC达到81.60%。这些结果表明，CURL能够有效地检测胎儿的运动，并优于传统的主观评估方法。该研究为胎儿健康监测提供了一种客观、可靠的解决方案。

## 🎯 应用场景

该研究成果可应用于产前胎儿健康监测，为医生提供客观、定量的胎动信息，辅助诊断胎儿窘迫等问题。通过自动化胎动检测，可以减轻医护人员的工作负担，提高诊断效率。未来，该技术有望集成到便携式超声设备中，实现家庭化的胎儿健康监测。

## 📄 摘要（原文）

> Accurate fetal movement (FM) detection is essential for assessing prenatal health, as abnormal movement patterns can indicate underlying complications such as placental dysfunction or fetal distress. Traditional methods, including maternal perception and cardiotocography (CTG), suffer from subjectivity and limited accuracy. To address these challenges, we propose Contrastive Ultrasound Video Representation Learning (CURL), a novel self-supervised learning framework for FM detection from extended fetal ultrasound video recordings. Our approach leverages a dual-contrastive loss, incorporating both spatial and temporal contrastive learning, to learn robust motion representations. Additionally, we introduce a task-specific sampling strategy, ensuring the effective separation of movement and non-movement segments during self-supervised training, while enabling flexible inference on arbitrarily long ultrasound recordings through a probabilistic fine-tuning approach. Evaluated on an in-house dataset of 92 subjects, each with 30-minute ultrasound sessions, CURL achieves a sensitivity of 78.01% and an AUROC of 81.60%, demonstrating its potential for reliable and objective FM analysis. These results highlight the potential of self-supervised contrastive learning for fetal movement analysis, paving the way for improved prenatal monitoring and clinical decision-making.

