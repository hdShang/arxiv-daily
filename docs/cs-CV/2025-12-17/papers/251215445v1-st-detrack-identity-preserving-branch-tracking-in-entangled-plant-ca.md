---
layout: default
title: ST-DETrack: Identity-Preserving Branch Tracking in Entangled Plant Canopies via Dual Spatiotemporal Evidence
---

# ST-DETrack: Identity-Preserving Branch Tracking in Entangled Plant Canopies via Dual Spatiotemporal Evidence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15445" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15445v1</a>
  <a href="https://arxiv.org/pdf/2512.15445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15445v1" onclick="toggleFavorite(this, '2512.15445v1', 'ST-DETrack: Identity-Preserving Branch Tracking in Entangled Plant Canopies via Dual Spatiotemporal Evidence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yueqianji Chen, Kevin Williams, John H. Doonan, Paolo Remagnino, Jo Hepworth

**分类**: cs.CV

**发布日期**: 2025-12-17

**备注**: Under Review at IEEE Transactions on Image Processing

---

## 💡 一句话要点

**ST-DETrack：利用时空双重证据，解决复杂植物冠层中分支的身份保持跟踪问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `植物表型分析` `分支跟踪` `时空融合` `双解码器网络` `自适应门控` `高通量` `计算机视觉`

## 📋 核心要点

1. 现有方法难以应对植物生长过程中的非刚性和复杂遮挡，导致分支身份跟踪出现碎片化问题。
2. ST-DETrack融合空间几何先验和时间运动一致性，利用双解码器网络保持分支身份。
3. 实验表明，ST-DETrack在分支匹配精度上显著优于现有方法，提升了长期身份跟踪的鲁棒性。

## 📝 摘要（中文）

本文提出了一种名为ST-DETrack的时空融合双解码器网络，旨在解决高通量表型分析中，由于植物非刚性生长和复杂冠层遮挡导致的分支身份碎片化问题。该网络通过融合空间和时间信息，实现从萌芽到开花的植物分支身份保持跟踪。ST-DETrack包含一个利用位置和角度等几何先验进行早期跟踪的空间解码器，以及一个利用运动一致性解决后期遮挡的时间解码器。自适应门控机制动态调整对空间和时间线索的依赖，而基于负向重力性的生物约束则缓解了垂直生长方向的歧义。在甘蓝型油菜数据集上的验证表明，ST-DETrack的分支匹配精度（BMA）达到93.6%，显著优于空间和时间基线方法，分别提升了28.9和3.3个百分点。实验结果证明了该方法在复杂、动态的植物结构中保持长期身份一致性的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决植物表型分析中，由于植物分支的非刚性生长和相互缠绕遮挡，导致难以准确跟踪单个分支身份的问题。现有方法在处理复杂植物冠层时，容易出现身份碎片化，无法实现长期、稳定的分支跟踪。

**核心思路**：论文的核心思路是融合空间和时间信息，利用植物分支在不同生长阶段的特性，设计一个双解码器网络。空间解码器侧重于利用早期阶段的几何信息，时间解码器侧重于利用后期阶段的运动信息，通过自适应门控机制动态调整二者的权重，从而实现更鲁棒的身份跟踪。

**技术框架**：ST-DETrack网络包含一个空间解码器和一个时间解码器。空间解码器利用分支的位置和角度等几何先验信息进行早期跟踪；时间解码器利用分支的运动一致性信息解决后期遮挡问题。一个自适应门控机制动态调整两个解码器的输出权重。此外，还引入了基于负向重力性的生物约束，以减少垂直生长方向的歧义。

**关键创新**：该方法最重要的创新点在于时空信息的融合以及自适应门控机制的设计。通过融合空间几何先验和时间运动一致性，可以更全面地捕捉分支的特征。自适应门控机制能够根据植物的生长阶段动态调整对不同信息的依赖，从而提高跟踪的鲁棒性。

**关键设计**：自适应门控机制的设计是关键。具体实现方式未知，但其核心作用是根据输入数据动态调整空间和时间解码器的权重。负向重力性约束的具体实现方式也未知，但其目的是减少垂直方向上的跟踪歧义。损失函数的设计可能包含分支匹配损失、身份保持损失等，以确保跟踪的准确性和一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15445v1/first.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15445v1/Frame.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15445v1/annotation_tool.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ST-DETrack在甘蓝型油菜数据集上取得了显著的性能提升。实验结果表明，ST-DETrack的分支匹配精度（BMA）达到了93.6%，相比于仅使用空间信息的基线方法提升了28.9个百分点，相比于仅使用时间信息的基线方法提升了3.3个百分点。这些结果充分证明了ST-DETrack在复杂植物冠层中进行分支跟踪的有效性和鲁棒性。

## 🎯 应用场景

该研究成果可应用于高通量植物表型分析，例如精准农业、植物育种等领域。通过自动提取和跟踪植物分支，可以更高效地获取植物的生长状态、形态特征等信息，为植物生长调控、品种改良提供数据支持，并最终提高农业生产效率和作物产量。

## 📄 摘要（原文）

> Automated extraction of individual plant branches from time-series imagery is essential for high-throughput phenotyping, yet it remains computationally challenging due to non-rigid growth dynamics and severe identity fragmentation within entangled canopies. To overcome these stage-dependent ambiguities, we propose ST-DETrack, a spatiotemporal-fusion dual-decoder network designed to preserve branch identity from budding to flowering. Our architecture integrates a spatial decoder, which leverages geometric priors such as position and angle for early-stage tracking, with a temporal decoder that exploits motion consistency to resolve late-stage occlusions. Crucially, an adaptive gating mechanism dynamically shifts reliance between these spatial and temporal cues, while a biological constraint based on negative gravitropism mitigates vertical growth ambiguities. Validated on a Brassica napus dataset, ST-DETrack achieves a Branch Matching Accuracy (BMA) of 93.6%, significantly outperforming spatial and temporal baselines by 28.9 and 3.3 percentage points, respectively. These results demonstrate the method's robustness in maintaining long-term identity consistency amidst complex, dynamic plant architectures.

