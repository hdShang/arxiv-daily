---
layout: default
title: "MCLPD:Multi-view Contrastive Learning for EEG-based PD Detection Across Datasets"
---

# MCLPD:Multi-view Contrastive Learning for EEG-based PD Detection Across Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14073" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14073v2</a>
  <a href="https://arxiv.org/pdf/2508.14073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14073v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14073v2', 'MCLPD:Multi-view Contrastive Learning for EEG-based PD Detection Across Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qian Zhang, Ruilin Zhang, Jun Xiao, Yifan Liu, Zhe Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-12 (更新: 2025-08-21)

**备注**: Acccepted by European Conference on Artificial Intelligence(ECAI 2025)

---

## 💡 一句话要点

**提出MCLPD以解决跨数据集的帕金森病检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `脑电图` `帕金森病` `半监督学习` `对比学习` `跨数据集检测` `自监督学习` `数据增强`

## 📋 核心要点

1. 现有方法在跨数据集的帕金森病检测中面临数据标注成本高和数据集间差异大的挑战，限制了模型的泛化能力。
2. 本文提出的MCLPD框架通过多视角对比学习和轻量级微调，利用自监督学习和少量标记数据，提升跨数据集检测性能。
3. 实验结果显示，MCLPD在使用1%标记数据时，F1分数达到0.91和0.81，使用5%标记数据时进一步提升至0.97和0.87，显著优于现有方法。

## 📝 摘要（中文）

脑电图（EEG）已被验证为检测帕金森病（PD）的有效技术，尤其是在早期阶段。然而，EEG数据标注的高成本导致数据集规模有限，并且不同数据集之间存在显著差异，这严重阻碍了模型在跨数据集检测场景中的鲁棒性和泛化能力。为了解决这些挑战，本文提出了一种名为MCLPD的半监督学习框架，结合了多视角对比预训练和轻量级监督微调，以增强跨数据集的PD检测性能。在预训练阶段，MCLPD在未标记的UNM数据集上使用自监督学习，通过在时间和频率域进行双重增强来构建对比对，丰富数据并自然融合时频信息。在微调阶段，仅使用来自另外两个数据集（UI和UC）的小部分标记数据进行监督优化。实验结果表明，MCLPD在UI和UC上分别达到了0.91和0.81的F1分数，使用1%的标记数据时，进一步提升至0.97和0.87，显示了所提框架的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决跨数据集的帕金森病检测问题，现有方法因数据标注成本高和数据集间差异大而面临鲁棒性和泛化能力不足的挑战。

**核心思路**：MCLPD框架通过结合多视角对比学习和轻量级监督微调，利用自监督学习在未标记数据集上进行预训练，从而减少对标记数据的依赖。

**技术框架**：MCLPD的整体架构分为两个主要阶段：预训练和微调。在预训练阶段，使用自监督学习构建对比对；在微调阶段，利用少量标记数据进行监督优化。

**关键创新**：MCLPD的创新在于通过双重增强技术在时间和频率域构建对比对，丰富数据表示并提高模型的泛化能力，与现有方法相比显著减少了对标记数据的依赖。

**关键设计**：在预训练阶段，采用自监督学习方法，并通过时间和频率域的双重增强来构建对比对；在微调阶段，仅使用来自UI和UC数据集的小部分标记数据进行优化，确保模型在跨数据集上的有效性。

## 📊 实验亮点

MCLPD在实验中表现出色，使用仅1%的标记数据时，F1分数达到了0.91和0.81，使用5%标记数据时进一步提升至0.97和0.87，显著优于现有方法，展示了其在跨数据集检测中的强大能力和有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在医疗领域的帕金森病早期检测中。通过提高跨数据集的检测性能，MCLPD可以帮助医生更准确地诊断和监测患者的病情，进而改善患者的治疗效果和生活质量。此外，该方法的框架也可以推广到其他神经疾病的检测中，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Electroencephalography has been validated as an effective technique for detecting Parkinson's disease,particularly in its early stages.However,the high cost of EEG data annotation often results in limited dataset size and considerable discrepancies across datasets,including differences in acquisition protocols and subject demographics,significantly hinder the robustness and generalizability of models in cross-dataset detection scenarios.To address such challenges,this paper proposes a semi-supervised learning framework named MCLPD,which integrates multi-view contrastive pre-training with lightweight supervised fine-tuning to enhance cross-dataset PD detection performance.During pre-training,MCLPD uses self-supervised learning on the unlabeled UNM dataset.To build contrastive pairs,it applies dual augmentations in both time and frequency domains,which enrich the data and naturally fuse time-frequency information.In the fine-tuning phase,only a small proportion of labeled data from another two datasets (UI and UC)is used for supervised optimization.Experimental results show that MCLPD achieves F1 scores of 0.91 on UI and 0.81 on UC using only 1%of labeled data,which further improve to 0.97 and 0.87,respectively,when 5%of labeled data is used.Compared to existing methods,MCLPD substantially improves cross-dataset generalization while reducing the dependency on labeled data,demonstrating the effectiveness of the proposed framework.

