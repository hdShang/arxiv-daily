---
layout: default
title: TiS-TSL: Image-Label Supervised Surgical Video Stereo Matching via Time-Switchable Teacher-Student Learning
---

# TiS-TSL: Image-Label Supervised Surgical Video Stereo Matching via Time-Switchable Teacher-Student Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06817" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06817v3</a>
  <a href="https://arxiv.org/pdf/2511.06817.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06817v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06817v3', 'TiS-TSL: Image-Label Supervised Surgical Video Stereo Matching via Time-Switchable Teacher-Student Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Wang, Ying Zhou, Hao Wang, Wenwei Zhang, Qiang Li, Zhiwei Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-10 (更新: 2025-11-12)

**备注**: 8 pages, 4 figures

---

## 💡 一句话要点

**提出TiS-TSL，通过时序可切换的师生学习解决手术视频立体匹配中的时序一致性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `立体匹配` `手术视频` `师生学习` `时间一致性` `伪标签` `微创手术` `深度学习`

## 📋 核心要点

1. 现有基于图像级监督的师生学习方法在手术视频立体匹配中缺乏时间一致性，导致视差预测不稳定和闪烁伪影。
2. TiS-TSL提出一种时序可切换的师生学习框架，通过统一模型实现图像预测、前向和后向视频预测，增强时间建模能力。
3. 实验结果表明，TiS-TSL在两个公共数据集上显著优于现有方法，TEPE和EPE分别提高了至少2.11%和4.54%。

## 📝 摘要（中文）

在微创手术(MIS)中，立体匹配对于下一代导航和增强现实至关重要。然而，由于解剖结构的限制，获取密集的视差监督几乎是不可能的，通常只能获得内窥镜进入深层体腔之前的一些图像级标签。师生学习(TSL)通过利用在稀疏标签上训练的教师网络，从大量未标记的手术视频中生成伪标签和相关的置信度图，提供了一个有希望的解决方案。然而，现有的TSL方法仅限于图像级监督，只提供空间置信度，缺乏时间一致性估计。这种时空可靠性的缺失导致不稳定的视差预测和视频帧之间的严重闪烁伪影。为了克服这些挑战，我们提出了一种新的时序可切换的师生学习框架TiS-TSL，用于在最小监督下进行视频立体匹配。其核心是一个统一的模型，该模型在三种不同的模式下运行：图像预测(IP)、前向视频预测(FVP)和后向视频预测(BVP)，从而在单个架构中实现灵活的时间建模。在这种统一模型的支持下，TiS-TSL采用两阶段学习策略。图像到视频(I2V)阶段将稀疏的图像级知识转移到时间建模的初始化。随后的视频到视频(V2V)阶段通过比较前向和后向预测来计算双向时空一致性，从而细化时间视差预测。这种一致性识别跨帧的不可靠区域，过滤嘈杂的视频级伪标签，并强制执行时间连贯性。在两个公共数据集上的实验结果表明，TiS-TSL超过了其他基于图像的state-of-the-arts方法，TEPE和EPE分别提高了至少2.11%和4.54%。

## 🔬 方法详解

**问题定义**：论文旨在解决微创手术视频立体匹配中，由于缺乏密集的视差标注，以及现有方法缺乏时间一致性建模而导致的视差预测不稳定和闪烁伪影问题。现有方法主要依赖图像级别的监督，无法有效利用视频中的时间信息，导致预测结果在时间维度上不连贯。

**核心思路**：论文的核心思路是利用时序可切换的师生学习框架，通过统一的模型同时进行图像预测、前向视频预测和后向视频预测，从而在时间维度上建立一致性约束。通过比较前向和后向预测结果，可以识别并过滤掉不可靠的伪标签，从而提高视差预测的准确性和稳定性。

**技术框架**：TiS-TSL框架包含两个主要阶段：图像到视频(I2V)阶段和视频到视频(V2V)阶段。在I2V阶段，利用图像级别的稀疏标注训练教师网络，并用其生成视频帧的伪标签，初始化学生网络的时间建模能力。在V2V阶段，学生网络同时进行前向和后向视频预测，并计算双向时空一致性。该一致性用于过滤伪标签中的噪声，并进一步优化学生网络的参数。整个框架采用统一的模型结构，通过切换不同的模式（IP、FVP、BVP）来实现不同的预测任务。

**关键创新**：论文最重要的技术创新在于提出了时序可切换的统一模型，该模型能够同时进行图像预测、前向视频预测和后向视频预测。这种设计使得模型能够有效地利用视频中的时间信息，并建立时间一致性约束。与现有方法相比，TiS-TSL能够更好地处理手术视频中的噪声和遮挡，从而提高视差预测的准确性和鲁棒性。

**关键设计**：在V2V阶段，论文设计了双向时空一致性损失函数，用于衡量前向和后向预测结果之间的一致性。该损失函数能够有效地惩罚不一致的预测结果，并引导学生网络学习更加准确和稳定的视差图。此外，论文还采用了自适应的伪标签过滤策略，根据一致性得分动态调整伪标签的权重，从而减少噪声伪标签对训练的影响。

## 📊 实验亮点

实验结果表明，TiS-TSL在两个公共数据集上均取得了显著的性能提升。与现有的基于图像的state-of-the-art方法相比，TiS-TSL在TEPE指标上至少提高了2.11%，在EPE指标上至少提高了4.54%。这些结果证明了TiS-TSL在手术视频立体匹配任务中的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于微创手术机器人导航、增强现实手术辅助系统等领域。通过提供准确和稳定的立体视觉信息，可以帮助医生更好地进行手术操作，提高手术精度和安全性，减少手术风险，并有望推动下一代智能手术系统的发展。

## 📄 摘要（原文）

> Stereo matching in minimally invasive surgery (MIS) is essential for next-generation navigation and augmented reality. Yet, dense disparity supervision is nearly impossible due to anatomical constraints, typically limiting annotations to only a few image-level labels acquired before the endoscope enters deep body cavities. Teacher-Student Learning (TSL) offers a promising solution by leveraging a teacher trained on sparse labels to generate pseudo labels and associated confidence maps from abundant unlabeled surgical videos. However, existing TSL methods are confined to image-level supervision, providing only spatial confidence and lacking temporal consistency estimation. This absence of spatio-temporal reliability results in unstable disparity predictions and severe flickering artifacts across video frames. To overcome these challenges, we propose TiS-TSL, a novel time-switchable teacher-student learning framework for video stereo matching under minimal supervision. At its core is a unified model that operates in three distinct modes: Image-Prediction (IP), Forward Video-Prediction (FVP), and Backward Video-Prediction (BVP), enabling flexible temporal modeling within a single architecture. Enabled by this unified model, TiS-TSL adopts a two-stage learning strategy. The Image-to-Video (I2V) stage transfers sparse image-level knowledge to initialize temporal modeling. The subsequent Video-to-Video (V2V) stage refines temporal disparity predictions by comparing forward and backward predictions to calculate bidirectional spatio-temporal consistency. This consistency identifies unreliable regions across frames, filters noisy video-level pseudo labels, and enforces temporal coherence. Experimental results on two public datasets demonstrate that TiS-TSL exceeds other image-based state-of-the-arts by improving TEPE and EPE by at least 2.11% and 4.54%, respectively.

