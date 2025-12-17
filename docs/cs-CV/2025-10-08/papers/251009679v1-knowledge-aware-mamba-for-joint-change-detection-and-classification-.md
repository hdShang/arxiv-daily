---
layout: default
title: Knowledge-Aware Mamba for Joint Change Detection and Classification from MODIS Times Series
---

# Knowledge-Aware Mamba for Joint Change Detection and Classification from MODIS Times Series

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.09679" target="_blank" class="toolbar-btn">arXiv: 2510.09679v1</a>
    <a href="https://arxiv.org/pdf/2510.09679.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09679v1" 
            onclick="toggleFavorite(this, '2510.09679v1', 'Knowledge-Aware Mamba for Joint Change Detection and Classification from MODIS Times Series')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhengsen Xu, Yimin Zhu, Zack Dewis, Mabel Heffring, Motasem Alkayid, Saeid Taleghanidoozdoozan, Lincoln Linlin Xu

**分类**: cs.CV

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**提出知识驱动的Mamba以解决MODIS时间序列变化检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `变化检测` `MODIS` `知识驱动` `多任务学习` `遥感` `土地利用分类` `空间-光谱-时间`

## 📋 核心要点

1. 现有MODIS变化检测方法面临混合像素和信息耦合等挑战，导致检测准确性不足。
2. 提出的KAMamba方法通过知识驱动的转移矩阵和多任务学习来提升变化检测和分类性能。
3. 在加拿大萨斯喀彻温省的MODIS时间序列数据集上，方法在变化检测和LULC分类上均取得显著提升。

## 📝 摘要（中文）

尽管使用MODIS时间序列进行变化检测对环境监测至关重要，但由于混合像素、空间-光谱-时间信息耦合效应和背景类别异质性等关键问题，这是一项极具挑战性的任务。本文提出了一种新颖的知识驱动Mamba（KAMamba）方法，以增强MODIS变化检测。首先，设计了一种知识驱动的转移矩阵引导方法，提出了知识感知转移损失（KAT-loss），以提高检测准确性。其次，采用多任务学习方法，通过预变化分类损失、后变化分类损失和变化检测损失来改善模型学习。最后，设计了新颖的空间-光谱-时间Mamba（SSTMamba）模块，并使用稀疏可变形Mamba（SDMamba）骨干网络来提高模型效率并降低计算成本。实验结果表明，该方法在土地覆盖变化检测上比基线提高了约1.5-6%的平均F1值，在LULC分类上提高了约2%的总体精度、平均精度和Kappa值。

## 🔬 方法详解

**问题定义**：本文旨在解决使用MODIS时间序列进行变化检测时面临的混合像素、空间-光谱-时间信息耦合及背景类别异质性等问题。这些问题导致现有方法的检测准确性不足。

**核心思路**：论文提出了一种知识驱动的Mamba（KAMamba）方法，通过设计知识感知转移损失（KAT-loss）和多任务学习策略，来有效利用类别转移知识，从而提升变化检测和分类的准确性。

**技术框架**：KAMamba的整体架构包括多个模块：首先是知识驱动的转移矩阵引导模块，其次是多任务学习模块，最后是空间-光谱-时间Mamba（SSTMamba）模块，结合稀疏可变形Mamba（SDMamba）骨干网络以提高效率。

**关键创新**：最重要的技术创新在于引入知识感知转移损失（KAT-loss），通过利用类别转移知识来增强模型的学习能力。此外，设计的SSTMamba模块有效解耦了MODIS时间序列中的信息耦合。

**关键设计**：论文中采用了三种损失函数：预变化分类损失（PreC-loss）、后变化分类损失（PostC-loss）和变化检测损失（Chg-loss），以实现多任务学习。同时，SDMamba骨干网络的设计旨在降低计算成本并提高模型效率。

## 📊 实验亮点

实验结果表明，KAMamba在变化检测任务中相较于基线方法提升了约1.5-6%的平均F1值，在LULC分类任务中提升了约2%的总体精度、平均精度和Kappa值，显示出其在实际应用中的有效性和优势。

## 🎯 应用场景

该研究在环境监测、土地利用变化分析和生态系统管理等领域具有广泛的应用潜力。通过提高MODIS时间序列变化检测的准确性，能够为政策制定者和研究人员提供更可靠的数据支持，促进可持续发展和资源管理。未来，该方法还可扩展到其他遥感数据集的变化检测任务中。

## 📄 摘要（原文）

> Although change detection using MODIS time series is critical for environmental monitoring, it is a highly challenging task due to key MODIS difficulties, e.g., mixed pixels, spatial-spectral-temporal information coupling effect, and background class heterogeneity. This paper presents a novel knowledge-aware Mamba (KAMamba) for enhanced MODIS change detection, with the following contributions. First, to leverage knowledge regarding class transitions, we design a novel knowledge-driven transition-matrix-guided approach, leading to a knowledge-aware transition loss (KAT-loss) that can enhance detection accuracies. Second, to improve model constraints, a multi-task learning approach is designed, where three losses, i.e., pre-change classification loss (PreC-loss), post-change classification loss (PostC-loss), and change detection loss (Chg-loss) are used for improve model learning. Third, to disentangle information coupling in MODIS time series, novel spatial-spectral-temporal Mamba (SSTMamba) modules are designed. Last, to improve Mamba model efficiency and remove computational cost, a sparse and deformable Mamba (SDMamba) backbone is used in SSTMamba. On the MODIS time-series dataset for Saskatchewan, Canada, we evaluate the method on land-cover change detection and LULC classification; results show about 1.5-6% gains in average F1 for change detection over baselines, and about 2% improvements in OA, AA, and Kappa for LULC classification.

