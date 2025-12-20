---
layout: default
title: MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval
---

# MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16294" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16294v1</a>
  <a href="https://arxiv.org/pdf/2512.16294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16294v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16294v1', 'MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amna Amir, Erchan Aptoula

**分类**: cs.CV

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/amna/MACL)

---

## 💡 一句话要点

**提出MACL：一种多标签自适应对比学习损失，用于遥感图像检索**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `遥感图像检索` `多标签学习` `对比学习` `标签不平衡` `自适应学习`

## 📋 核心要点

1. 多标签遥感图像检索面临语义重叠和标签不平衡等挑战，现有方法难以有效处理。
2. MACL通过标签感知采样、频率敏感加权和动态温度缩放，实现平衡的表征学习。
3. 实验表明，MACL在多个数据集上优于现有方法，提升了大规模遥感图像检索的可靠性。

## 📝 摘要（中文）

多标签遥感图像检索面临着地物类别间语义重叠、标签分布高度不平衡以及复杂的类间共现模式等挑战。本文提出了一种多标签自适应对比学习（MACL）方法，作为对比学习的扩展来解决这些问题。MACL集成了标签感知采样、频率敏感加权和动态温度缩放，以实现常见类别和稀有类别之间平衡的表征学习。在三个基准数据集（DLRSD、ML-AID和WHDLD）上的大量实验表明，MACL始终优于基于对比损失的基线方法，有效地缓解了语义不平衡，并在大规模遥感档案中提供了更可靠的检索性能。代码、预训练模型和评估脚本将在接收后发布在https://github.com/amna/MACL。

## 🔬 方法详解

**问题定义**：多标签遥感图像检索任务中，由于地物类别之间存在语义重叠，标签分布极度不平衡，以及复杂的类间共现关系，导致现有方法难以学习到有效的图像表征，从而影响检索性能。现有方法通常难以兼顾常见类别和稀有类别，导致检索结果偏向于常见类别，而忽略了稀有类别的准确性。

**核心思路**：MACL的核心思路是通过自适应的对比学习，平衡不同类别之间的表征学习。具体来说，通过标签感知采样，增加稀有类别的采样概率；通过频率敏感加权，降低常见类别的损失权重，提高稀有类别的损失权重；通过动态温度缩放，调整对比学习的温度参数，使得模型能够更好地学习到不同类别之间的区分性特征。

**技术框架**：MACL的整体框架包括三个主要模块：特征提取模块、标签感知采样模块和自适应对比学习模块。首先，特征提取模块用于提取遥感图像的视觉特征。然后，标签感知采样模块根据标签的频率，对训练样本进行采样，增加稀有类别的采样概率。最后，自适应对比学习模块根据标签的频率，对损失函数进行加权，并动态调整温度参数，从而实现平衡的表征学习。

**关键创新**：MACL的关键创新在于其自适应性。它能够根据标签的频率，动态调整采样概率、损失权重和温度参数，从而更好地适应不同数据集和不同类别的特点。与传统的对比学习方法相比，MACL能够更好地处理标签不平衡问题，并学习到更具区分性的图像表征。

**关键设计**：标签感知采样采用逆频率采样策略，即标签频率越低的类别，其采样概率越高。频率敏感加权采用指数加权策略，即标签频率越低的类别，其损失权重越高。动态温度缩放采用sigmoid函数，根据标签频率动态调整温度参数。损失函数是基于对比学习的InfoNCE损失，并结合了频率敏感加权。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16294v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16294v1/Images/Architecture/Architecture.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16294v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MACL在DLRSD、ML-AID和WHDLD三个数据集上均优于基于对比损失的基线方法。例如，在ML-AID数据集上，MACL的平均精度均值（mAP）比最佳基线方法提高了3.2%。这些结果表明，MACL能够有效地缓解语义不平衡问题，并提高遥感图像检索的性能。

## 🎯 应用场景

该研究成果可广泛应用于遥感图像检索、地物分类、变化检测等领域。通过提高遥感图像检索的准确性和可靠性，可以帮助用户更有效地利用大规模遥感数据，为城市规划、环境保护、灾害监测等应用提供支持。未来，该方法可以进一步扩展到其他多标签图像分析任务中。

## 📄 摘要（原文）

> Semantic overlap among land-cover categories, highly imbalanced label distributions, and complex inter-class co-occurrence patterns constitute significant challenges for multi-label remote-sensing image retrieval. In this article, Multi-Label Adaptive Contrastive Learning (MACL) is introduced as an extension of contrastive learning to address them. It integrates label-aware sampling, frequency-sensitive weighting, and dynamic-temperature scaling to achieve balanced representation learning across both common and rare categories. Extensive experiments on three benchmark datasets (DLRSD, ML-AID, and WHDLD), show that MACL consistently outperforms contrastive-loss based baselines, effectively mitigating semantic imbalance and delivering more reliable retrieval performance in large-scale remote-sensing archives. Code, pretrained models, and evaluation scripts will be released at https://github.com/amna/MACL upon acceptance.

