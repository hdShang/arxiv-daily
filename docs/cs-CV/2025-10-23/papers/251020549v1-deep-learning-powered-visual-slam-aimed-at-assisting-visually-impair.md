---
layout: default
title: Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation
---

# Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20549" target="_blank" class="toolbar-btn">arXiv: 2510.20549v1</a>
    <a href="https://arxiv.org/pdf/2510.20549.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20549v1" 
            onclick="toggleFavorite(this, '2510.20549v1', 'Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Marziyeh Bamdad, Hans-Peter Hutter, Alireza Darvishy

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-23

**备注**: 8 pages, 7 figures, 4 tables

**DOI**: [10.5220/0013338200003912](https://doi.org/10.5220/0013338200003912)

---

## 💡 一句话要点

**提出SELM-SLAM3，利用深度学习增强视觉SLAM，辅助视障人士导航。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉SLAM` `深度学习` `特征提取` `特征匹配` `视障辅助导航` `机器人导航` `SuperPoint` `LightGlue`

## 📋 核心要点

1. 现有SLAM技术在低纹理、运动模糊等复杂环境下鲁棒性不足，限制了其在视障辅助导航等领域的应用。
2. SELM-SLAM3通过集成SuperPoint和LightGlue，利用深度学习提升特征提取和匹配的鲁棒性，从而提高SLAM的整体性能。
3. 实验结果表明，SELM-SLAM3在多个数据集上显著优于ORB-SLAM3和其他先进的RGB-D SLAM系统，尤其是在挑战性场景下。

## 📝 摘要（中文）

本文提出了一种基于深度学习的视觉SLAM框架SELM-SLAM3，旨在解决低纹理、运动模糊或复杂光照等挑战性条件下SLAM的鲁棒性问题。这些问题在视障人士辅助导航等应用中尤为常见，会降低定位精度和跟踪稳定性，从而影响导航的可靠性和安全性。SELM-SLAM3集成了SuperPoint和LightGlue，以实现稳健的特征提取和匹配。在TUM RGB-D、ICL-NUIM和TartanAir数据集上的评估结果表明，SELM-SLAM3的性能优于传统的ORB-SLAM3，平均提升87.84%，并且超过了最先进的RGB-D SLAM系统36.77%。该框架在低纹理场景和快速运动等挑战性条件下表现出增强的性能，为开发视障人士导航辅助工具提供了一个可靠的平台。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉SLAM在具有挑战性的环境条件下的鲁棒性问题，尤其是在低纹理、运动模糊和复杂光照等场景中。现有的SLAM方法在这些条件下容易出现定位精度下降和跟踪不稳定的问题，从而影响导航的可靠性和安全性。这些问题对于视障人士辅助导航等应用来说尤为关键。

**核心思路**：论文的核心思路是利用深度学习来增强视觉SLAM的特征提取和匹配能力。通过使用SuperPoint进行特征点检测，并使用LightGlue进行特征匹配，可以提高SLAM系统在具有挑战性的环境条件下的鲁棒性。这种方法旨在克服传统特征提取和匹配算法在这些条件下的局限性。

**技术框架**：SELM-SLAM3的整体框架基于视觉SLAM系统，并集成了深度学习模块。该框架包含以下主要模块：1) 使用SuperPoint进行特征点检测；2) 使用LightGlue进行特征匹配；3) 基于提取的特征和匹配结果进行位姿估计和地图构建。整个流程旨在实现更准确和鲁棒的SLAM性能。

**关键创新**：该论文的关键创新在于将SuperPoint和LightGlue集成到视觉SLAM系统中，以提高特征提取和匹配的鲁棒性。与传统的基于手工设计的特征提取器（如ORB）相比，SuperPoint能够学习到更具判别性的特征，从而在低纹理和光照变化等条件下表现更好。LightGlue则利用图神经网络进行特征匹配，能够更好地处理噪声和异常值。

**关键设计**：论文中没有详细说明关键的参数设置、损失函数或网络结构等技术细节。SuperPoint和LightGlue是预训练好的模型，直接应用于SLAM框架中。具体如何将这些模块与SLAM系统的其他部分集成，以及如何优化整个系统的性能，需要在后续研究中进一步探索。

## 📊 实验亮点

SELM-SLAM3在TUM RGB-D、ICL-NUIM和TartanAir数据集上进行了评估，结果表明其性能显著优于传统的ORB-SLAM3，平均提升87.84%，并且超过了最先进的RGB-D SLAM系统36.77%。这些结果表明，SELM-SLAM3在挑战性条件下具有更强的鲁棒性和更高的精度。

## 🎯 应用场景

该研究成果可应用于视障人士辅助导航系统，提升其在复杂环境下的定位和导航能力，增强出行安全性和便利性。此外，该方法还可应用于机器人导航、自动驾驶等领域，提高机器人在光照不足、纹理缺失等挑战性环境下的自主导航能力。未来，该技术有望在智能家居、工业自动化等领域发挥重要作用。

## 📄 摘要（原文）

> Despite advancements in SLAM technologies, robust operation under challenging conditions such as low-texture, motion-blur, or challenging lighting remains an open challenge. Such conditions are common in applications such as assistive navigation for the visually impaired. These challenges undermine localization accuracy and tracking stability, reducing navigation reliability and safety. To overcome these limitations, we present SELM-SLAM3, a deep learning-enhanced visual SLAM framework that integrates SuperPoint and LightGlue for robust feature extraction and matching. We evaluated our framework using TUM RGB-D, ICL-NUIM, and TartanAir datasets, which feature diverse and challenging scenarios. SELM-SLAM3 outperforms conventional ORB-SLAM3 by an average of 87.84% and exceeds state-of-the-art RGB-D SLAM systems by 36.77%. Our framework demonstrates enhanced performance under challenging conditions, such as low-texture scenes and fast motion, providing a reliable platform for developing navigation aids for the visually impaired.

