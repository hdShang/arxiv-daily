---
layout: default
title: "RTGMFF: Enhanced fMRI-based Brain Disorder Diagnosis via ROI-driven Text Generation and Multimodal Feature Fusion"
---

# RTGMFF: Enhanced fMRI-based Brain Disorder Diagnosis via ROI-driven Text Generation and Multimodal Feature Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03214" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03214v1</a>
  <a href="https://arxiv.org/pdf/2509.03214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03214v1', 'RTGMFF: Enhanced fMRI-based Brain Disorder Diagnosis via ROI-driven Text Generation and Multimodal Feature Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao Jia, Yifei Sun, Yunyou Liu, Cheng Yang, Changmiao Wang, Feiwei Qin, Yong Peng, Wenwen Min

**分类**: cs.CV

**发布日期**: 2025-09-03

**🔗 代码/项目**: [GITHUB](https://github.com/BeistMedAI/RTGMFF)

---

## 💡 一句话要点

**提出RTGMFF框架以提升fMRI脑部疾病诊断准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `fMRI` `脑部疾病诊断` `多模态特征融合` `文本生成` `深度学习` `神经科学` `机器学习`

## 📋 核心要点

1. 现有fMRI诊断方法面临信噪比低和个体差异大的挑战，影响了临床应用的可靠性。
2. RTGMFF框架通过ROI驱动的文本生成和多模态特征融合，提供了一种新的脑部疾病诊断方法。
3. 在ADHD-200和ABIDE基准测试中，RTGMFF显著提高了诊断准确性，敏感性和特异性均有显著提升。

## 📝 摘要（中文）

功能性磁共振成像（fMRI）是一种强大的脑功能探测工具，但由于信噪比低、个体间差异大以及现有CNN和Transformer模型的频率感知能力有限，临床诊断的可靠性受到影响。此外，大多数fMRI数据集缺乏文本注释，无法为区域激活和连接模式提供背景信息。本文提出RTGMFF框架，将自动ROI级文本生成与多模态特征融合结合，用于脑部疾病诊断。RTGMFF包括三个组件：ROI驱动的fMRI文本生成、混合频率-空间编码器和自适应语义对齐模块。大量实验表明，RTGMFF在ADHD-200和ABIDE基准测试中超越了现有方法，显著提高了敏感性、特异性和ROC曲线下面积。

## 🔬 方法详解

**问题定义**：本文旨在解决fMRI在脑部疾病诊断中的低信噪比和个体差异问题，现有方法在频率感知和文本注释方面存在不足。

**核心思路**：RTGMFF框架通过结合ROI驱动的文本生成与多模态特征融合，旨在提高诊断的准确性和可靠性。该设计能够有效整合不同模态的信息，提供更全面的诊断依据。

**技术框架**：RTGMFF由三个主要模块组成：1) ROI驱动的fMRI文本生成，2) 混合频率-空间编码器，3) 自适应语义对齐模块。每个模块协同工作，形成一个完整的诊断流程。

**关键创新**：最重要的创新在于将文本生成与多模态特征融合相结合，特别是通过自适应语义对齐模块来缩小不同模态之间的差距，这在现有方法中尚未见到。

**关键设计**：在技术细节上，采用了正则化余弦相似度损失函数来优化模态对齐，同时混合频率-空间编码器结合了层次小波变换和跨尺度Transformer编码器，以捕捉频域结构和长距离空间依赖。

## 📊 实验亮点

在ADHD-200和ABIDE基准测试中，RTGMFF的诊断准确性显著高于现有方法，敏感性和特异性均有显著提升，ROC曲线下面积也得到了显著改善，展示了该框架在脑部疾病诊断中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括精神疾病的早期诊断和个性化治疗方案的制定。通过提高fMRI数据的解读能力，RTGMFF能够为临床医生提供更可靠的诊断工具，推动神经科学研究的发展。未来，该框架有望扩展到其他类型的脑部疾病诊断中，具有广泛的实际价值。

## 📄 摘要（原文）

> Functional magnetic resonance imaging (fMRI) is a powerful tool for probing brain function, yet reliable clinical diagnosis is hampered by low signal-to-noise ratios, inter-subject variability, and the limited frequency awareness of prevailing CNN- and Transformer-based models. Moreover, most fMRI datasets lack textual annotations that could contextualize regional activation and connectivity patterns. We introduce RTGMFF, a framework that unifies automatic ROI-level text generation with multimodal feature fusion for brain-disorder diagnosis. RTGMFF consists of three components: (i) ROI-driven fMRI text generation deterministically condenses each subject's activation, connectivity, age, and sex into reproducible text tokens; (ii) Hybrid frequency-spatial encoder fuses a hierarchical wavelet-mamba branch with a cross-scale Transformer encoder to capture frequency-domain structure alongside long-range spatial dependencies; and (iii) Adaptive semantic alignment module embeds the ROI token sequence and visual features in a shared space, using a regularized cosine-similarity loss to narrow the modality gap. Extensive experiments on the ADHD-200 and ABIDE benchmarks show that RTGMFF surpasses current methods in diagnostic accuracy, achieving notable gains in sensitivity, specificity, and area under the ROC curve. Code is available at https://github.com/BeistMedAI/RTGMFF.

