---
layout: default
title: CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting
---

# CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20469" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20469v2</a>
  <a href="https://arxiv.org/pdf/2505.20469.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20469v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20469v2', 'CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Tian, Xiaomin Li, Liqian Ma, Hao Yin, Zirui Zheng, Hefei Huang, Taiqing Li, Huchuan Lu, Xu Jia

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-08-14)

**备注**: ICCV 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://epsilontl.github.io/CCL-LGS/)

---

## 💡 一句话要点

**提出CCL-LGS以解决3D语义理解中的视角不一致问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D语义理解` `视角一致性` `多视角学习` `对比学习` `语义编码` `机器人技术` `自动驾驶` `虚拟现实`

## 📋 核心要点

1. 现有方法依赖2D先验，容易受到遮挡和视角变化的影响，导致3D语义理解中的语义不一致问题。
2. CCL-LGS框架通过多视角语义线索的整合，采用零样本跟踪器和CLIP，确保视角一致的语义监督。
3. 实验结果显示，CCL-LGS在3D语义理解任务中超越了现有的最先进方法，提升了语义场的质量。

## 📝 摘要（中文）

近年来，3D重建技术和视觉-语言模型的进展推动了3D语义理解的显著发展，这对于机器人、自动驾驶以及虚拟/增强现实至关重要。然而，依赖于2D先验的方法面临着视角间语义不一致的挑战，尤其是在遮挡、图像模糊和视角依赖变化的情况下。为了解决这一问题，本文提出了CCL-LGS框架，通过整合多视角语义线索来强制执行视角一致的语义监督。具体而言，首先使用零样本跟踪器对一组SAM生成的2D掩码进行对齐，并可靠地识别其对应类别。接着，利用CLIP提取跨视角的稳健语义编码。最后，Contrastive Codebook Learning (CCL)模块通过强制类内紧凑性和类间区分性来提炼判别性语义特征。实验结果表明，CCL-LGS在性能上超越了现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决3D语义理解中的视角不一致问题，现有方法在处理遮挡和视角变化时容易引入语义冲突，影响3D高斯语义场的质量。

**核心思路**：CCL-LGS框架通过整合多视角信息，利用零样本跟踪器和CLIP提取稳健的语义编码，从而实现视角一致的语义监督，减少语义冲突。

**技术框架**：该框架包括三个主要模块：首先，使用零样本跟踪器对SAM生成的2D掩码进行对齐；其次，利用CLIP提取跨视角的语义编码；最后，通过Contrastive Codebook Learning (CCL)模块提炼判别性语义特征。

**关键创新**：最重要的创新在于引入了Contrastive Codebook Learning模块，通过强制类内紧凑性和类间区分性来解决语义冲突，显著提升了语义特征的判别能力。

**关键设计**：在设计中，采用了零样本跟踪器来确保掩码的准确性，CLIP用于提取语义编码，CCL模块则通过特定的损失函数来优化语义特征的分布，确保模型的有效性。

## 📊 实验亮点

实验结果表明，CCL-LGS在多个基准测试中均优于现有最先进的方法，具体性能提升幅度达到XX%，显著提高了3D语义场的质量和一致性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶系统以及虚拟/增强现实环境中的3D场景理解。通过提高3D语义理解的准确性，CCL-LGS能够为这些领域提供更为可靠的支持，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Recent advances in 3D reconstruction techniques and vision-language models have fueled significant progress in 3D semantic understanding, a capability critical to robotics, autonomous driving, and virtual/augmented reality. However, methods that rely on 2D priors are prone to a critical challenge: cross-view semantic inconsistencies induced by occlusion, image blur, and view-dependent variations. These inconsistencies, when propagated via projection supervision, deteriorate the quality of 3D Gaussian semantic fields and introduce artifacts in the rendered outputs. To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues. Specifically, our approach first employs a zero-shot tracker to align a set of SAM-generated 2D masks and reliably identify their corresponding categories. Next, we utilize CLIP to extract robust semantic encodings across views. Finally, our Contrastive Codebook Learning (CCL) module distills discriminative semantic features by enforcing intra-class compactness and inter-class distinctiveness. In contrast to previous methods that directly apply CLIP to imperfect masks, our framework explicitly resolves semantic conflicts while preserving category discriminability. Extensive experiments demonstrate that CCL-LGS outperforms previous state-of-the-art methods. Our project page is available at https://epsilontl.github.io/CCL-LGS/.

