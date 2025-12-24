---
layout: default
title: DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning
---

# DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20409" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20409v1</a>
  <a href="https://arxiv.org/pdf/2512.20409.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20409v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20409v1', 'DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junho Yoon, Jaemo Jung, Hyunju Kim, Dongman Lee

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出DETACH框架，通过解耦时空对齐解决外中心视频与环境传感器融合问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `外中心视频` `环境传感器` `时空对齐` `对比学习` `行为识别`

## 📋 核心要点

1. 现有方法难以捕捉外中心视频与环境传感器融合中的局部细节和空间语义信息。
2. DETACH框架通过解耦时空特征，并利用在线聚类发现传感器-空间特征，实现上下文感知的对齐。
3. 在Opportunity++和HWU-USP数据集上的实验表明，DETACH显著优于现有方法。

## 📝 摘要（中文）

将以自我为中心的视频与可穿戴传感器对齐已显示出在人类行为识别方面的潜力，但面临用户不适、隐私问题和可扩展性等实际限制。我们探索以外中心视频与环境传感器作为一种非侵入式、可扩展的替代方案。以往的以自我为中心的可穿戴设备研究主要采用全局对齐，通过将整个序列编码为统一的表示，但由于两个问题，这种方法在外中心-环境设置中失败：（P1）无法捕捉局部细节，例如细微的动作，以及（P2）过度依赖模态不变的时间模式，导致在具有相似时间模式但具有不同空间语义上下文的动作之间出现错位。为了解决这些问题，我们提出了DETACH，一个解耦的时空框架。这种显式分解保留了局部细节，而我们通过在线聚类发现的新型传感器-空间特征为上下文感知的对齐提供了语义基础。为了对齐分解的特征，我们的两阶段方法通过相互监督建立空间对应关系，然后通过空间-时间加权对比损失执行时间对齐，该损失自适应地处理简单负样本、困难负样本和假负样本。在Opportunity++和HWU-USP数据集上进行的下游任务的综合实验表明，与改编的以自我为中心的可穿戴设备基线相比，性能有了显著提高。

## 🔬 方法详解

**问题定义**：论文旨在解决外中心视频与环境传感器融合中的对齐问题。现有方法，特别是那些从以自我为中心的可穿戴设备研究中改编的方法，通常采用全局对齐策略，即将整个序列编码成统一的表示。这种方法的痛点在于：1) 无法捕捉到细微的局部动作细节；2) 过度依赖时间模式，导致具有相似时间模式但空间语义不同的动作之间产生错位。

**核心思路**：论文的核心思路是将时空对齐问题解耦，分别处理空间和时间上的对齐。通过显式地分解时空特征，保留了局部细节。此外，利用在线聚类方法发现传感器-空间特征，为上下文感知的对齐提供了语义基础。这种解耦和语义增强的设计旨在克服现有全局对齐方法的局限性。

**技术框架**：DETACH框架包含两个主要阶段：空间对齐和时间对齐。首先，通过在线聚类提取传感器-空间特征。然后，利用互监督机制建立视频帧和传感器特征之间的空间对应关系。最后，使用空间-时间加权对比损失进行时间对齐，该损失能够自适应地处理不同类型的负样本（简单负样本、困难负样本和假负样本）。

**关键创新**：DETACH的关键创新在于其解耦的时空对齐框架和自适应的对比学习损失。与以往的全局对齐方法不同，DETACH显式地分解了时空特征，从而能够更好地捕捉局部细节和空间语义信息。此外，自适应的对比学习损失能够更有效地学习到鲁棒的时空表示。

**关键设计**：DETACH的关键设计包括：1) 使用在线聚类方法提取传感器-空间特征，这使得模型能够适应不同的环境和传感器配置；2) 采用互监督机制进行空间对齐，这能够有效地建立视频帧和传感器特征之间的对应关系；3) 设计空间-时间加权对比损失，该损失能够自适应地调整不同负样本的权重，从而提高模型的学习效率和泛化能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20409v1/Figure/Intro_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20409v1/Figure/Intro_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20409v1/Figure/Method_Architecture.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在Opportunity++和HWU-USP数据集上的实验结果表明，DETACH框架显著优于现有的以自我为中心的可穿戴设备基线方法。具体而言，DETACH在两个数据集上的下游任务中均取得了显著的性能提升，证明了其在外中心视频与环境传感器融合方面的有效性。实验结果验证了解耦时空对齐和自适应对比学习损失的优势。

## 🎯 应用场景

该研究成果可应用于智能家居、智能工厂、医疗健康等领域。例如，通过融合外中心视频和环境传感器数据，可以实现对老年人跌倒的自动检测和预警，或者对工厂生产线上工人操作行为的监控和分析，从而提高生产效率和安全性。该研究为构建更加智能和安全的监控系统提供了新的思路。

## 📄 摘要（原文）

> Aligning egocentric video with wearable sensors have shown promise for human action recognition, but face practical limitations in user discomfort, privacy concerns, and scalability. We explore exocentric video with ambient sensors as a non-intrusive, scalable alternative. While prior egocentric-wearable works predominantly adopt Global Alignment by encoding entire sequences into unified representations, this approach fails in exocentric-ambient settings due to two problems: (P1) inability to capture local details such as subtle motions, and (P2) over-reliance on modality-invariant temporal patterns, causing misalignment between actions sharing similar temporal patterns with different spatio-semantic contexts. To resolve these problems, we propose DETACH, a decomposed spatio-temporal framework. This explicit decomposition preserves local details, while our novel sensor-spatial features discovered via online clustering provide semantic grounding for context-aware alignment. To align the decomposed features, our two-stage approach establishes spatial correspondence through mutual supervision, then performs temporal alignment via a spatial-temporal weighted contrastive loss that adaptively handles easy negatives, hard negatives, and false negatives. Comprehensive experiments with downstream tasks on Opportunity++ and HWU-USP datasets demonstrate substantial improvements over adapted egocentric-wearable baselines.

