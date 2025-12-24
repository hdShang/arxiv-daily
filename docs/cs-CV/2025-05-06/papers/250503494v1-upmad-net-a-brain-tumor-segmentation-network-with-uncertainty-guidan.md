---
layout: default
title: UPMAD-Net: A Brain Tumor Segmentation Network with Uncertainty Guidance and Adaptive Multimodal Feature Fusion
---

# UPMAD-Net: A Brain Tumor Segmentation Network with Uncertainty Guidance and Adaptive Multimodal Feature Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03494" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03494v1</a>
  <a href="https://arxiv.org/pdf/2505.03494.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03494v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03494v1', 'UPMAD-Net: A Brain Tumor Segmentation Network with Uncertainty Guidance and Adaptive Multimodal Feature Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhanyuan Jia, Ni Yao, Danyang Sun, Chuang Han, Yanting Li, Jiaofen Nan, Fubao Zhu, Chen Zhao, Weihua Zhou

**分类**: cs.CV

**发布日期**: 2025-05-06

**备注**: 21 pages, 7 figures

**🔗 代码/项目**: [GITHUB](https://github.com/chenzhao2023/UPMAD_Net_BrainSeg)

---

## 💡 一句话要点

**提出UPMAD-Net以解决脑肿瘤分割中的不确定性与多模态特征融合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑肿瘤分割` `深度学习` `多模态特征融合` `不确定性估计` `U-Net` `医学影像分析` `蒙特卡洛Dropout`

## 📋 核心要点

1. 现有脑肿瘤分割方法在处理不规则形状和模糊边界时面临挑战，导致分割精度不足。
2. 本文提出的UPMAD-Net结合深度学习与区域生长算法，通过多尺度特征融合和自适应注意机制提升分割性能。
3. 在BraTS2021和BraTS2019数据集上，UPMAD-Net在增强肿瘤、整体肿瘤和肿瘤核心分割任务中均取得了优异的Dice分数，验证了方法的有效性。

## 📝 摘要（中文）

脑肿瘤分割对脑肿瘤的诊断和治疗具有重要影响。然而，由于肿瘤形状不规则、边界模糊及高度变异，准确的分割仍然具有挑战性。本文提出了一种结合深度学习与区域生长算法先验知识的脑肿瘤分割方法。该方法利用多尺度特征融合模块和自适应注意机制提取多尺度特征，并捕获全局上下文信息。通过蒙特卡洛Dropout策略进行不确定性估计，增强模型在低置信区域的鲁棒性。实验结果表明，该方法在BraTS数据集上表现优越，显著超越多种最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决脑肿瘤分割中存在的形状不规则、边界模糊及高变异性等问题。现有方法在低置信区域的鲁棒性不足，导致分割精度不高。

**核心思路**：UPMAD-Net通过结合深度学习与区域生长算法的先验知识，利用多尺度特征融合和自适应注意机制来提取特征并捕获全局上下文信息，从而提高分割的准确性和鲁棒性。

**技术框架**：该方法基于U-Net架构，主要包括多尺度特征融合模块（MSFF）、自适应注意机制（AAM）和蒙特卡洛Dropout（MC Dropout）策略。MSFF用于提取多尺度特征，AAM用于增强特征的上下文信息，而MC Dropout则用于不确定性估计。

**关键创新**：最重要的创新在于将不确定性估计与深度学习相结合，利用MC Dropout增强模型在低置信区域的鲁棒性。这一设计使得模型在处理复杂的脑肿瘤分割任务时表现更为出色。

**关键设计**：模型的损失函数设计考虑了分割精度与不确定性估计的平衡，网络结构采用U-Net的编码-解码架构，结合了多尺度特征提取和自适应注意机制，以确保特征的有效融合和利用。具体参数设置和训练细节在实验部分进行了详细说明。

## 📊 实验亮点

在BraTS2021数据集中，UPMAD-Net在增强肿瘤、整体肿瘤和肿瘤核心分割任务中分别取得了89.18%、93.67%和91.23%的Dice分数；在BraTS2019验证集中，Dice分数为87.43%、90.92%和90.40%。这些结果显著优于多种现有最先进方法，验证了模型的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、脑肿瘤诊断与治疗规划等。通过提高脑肿瘤分割的准确性，UPMAD-Net能够为临床医生提供更可靠的决策支持，进而改善患者的治疗效果。未来，该方法还可扩展到其他类型的医学图像分割任务中，具有广泛的应用前景。

## 📄 摘要（原文）

> Background: Brain tumor segmentation has a significant impact on the diagnosis and treatment of brain tumors. Accurate brain tumor segmentation remains challenging due to their irregular shapes, vague boundaries, and high variability. Objective: We propose a brain tumor segmentation method that combines deep learning with prior knowledge derived from a region-growing algorithm. Methods: The proposed method utilizes a multi-scale feature fusion (MSFF) module and adaptive attention mechanisms (AAM) to extract multi-scale features and capture global contextual information. To enhance the model's robustness in low-confidence regions, the Monte Carlo Dropout (MC Dropout) strategy is employed for uncertainty estimation. Results: Extensive experiments demonstrate that the proposed method achieves superior performance on Brain Tumor Segmentation (BraTS) datasets, significantly outperforming various state-of-the-art methods. On the BraTS2021 dataset, the test Dice scores are 89.18% for Enhancing Tumor (ET) segmentation, 93.67% for Whole Tumor (WT) segmentation, and 91.23% for Tumor Core (TC) segmentation. On the BraTS2019 validation set, the validation Dice scores are 87.43%, 90.92%, and 90.40% for ET, WT, and TC segmentation, respectively. Ablation studies further confirmed the contribution of each module to segmentation accuracy, indicating that each component played a vital role in overall performance improvement. Conclusion: This study proposed a novel 3D brain tumor segmentation network based on the U-Net architecture. By incorporating the prior knowledge and employing the uncertainty estimation method, the robustness and performance were improved. The code for the proposed method is available at https://github.com/chenzhao2023/UPMAD_Net_BrainSeg.

