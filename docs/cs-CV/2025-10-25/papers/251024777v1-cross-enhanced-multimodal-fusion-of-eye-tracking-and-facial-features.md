---
layout: default
title: "Cross-Enhanced Multimodal Fusion of Eye-Tracking and Facial Features for Alzheimer's Disease Diagnosis"
---

# Cross-Enhanced Multimodal Fusion of Eye-Tracking and Facial Features for Alzheimer's Disease Diagnosis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.24777" class="toolbar-btn" target="_blank">📄 arXiv: 2510.24777v1</a>
  <a href="https://arxiv.org/pdf/2510.24777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.24777v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.24777v1', 'Cross-Enhanced Multimodal Fusion of Eye-Tracking and Facial Features for Alzheimer\'s Disease Diagnosis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujie Nie, Jianzhang Ni, Yonglong Ye, Yuan-Ting Zhang, Yun Kwok Wing, Xiangqing Xu, Xin Ma, Lizhou Fan

**分类**: cs.CV, cs.AI, eess.IV

**发布日期**: 2025-10-25

**备注**: 35 pages, 8 figures, and 7 tables

---

## 💡 一句话要点

**提出一种交叉增强的多模态融合框架，用于眼动追踪和面部特征的阿尔茨海默病诊断。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿尔茨海默病诊断` `多模态融合` `眼动追踪` `面部特征` `交叉注意力` `方向感知卷积`

## 📋 核心要点

1. 现有方法在阿尔茨海默病辅助诊断中，较少探索眼动追踪和面部特征的联合集成，限制了诊断的准确性。
2. 提出一种交叉增强的多模态融合框架，通过交叉注意力和方向感知卷积，自适应地学习判别性表征。
3. 在自建的多模态数据集上，该框架超越了传统方法，实现了95.11%的分类准确率，提升了诊断性能。

## 📝 摘要（中文）

本研究提出了一种多模态交叉增强融合框架，旨在协同利用眼动追踪和面部特征进行阿尔茨海默病（AD）检测，从而实现及时干预并延缓疾病进展。该框架包含两个关键模块：(a) 交叉增强融合注意力模块（CEFAM），通过交叉注意力和全局增强来建模模态间交互；(b) 方向感知卷积模块（DACM），通过水平-垂直感受野捕获细粒度的方向性面部特征。这些模块共同实现了自适应和判别性的多模态表征学习。为了支持这项工作，我们构建了一个同步的多模态数据集，包括25名AD患者和25名健康对照者（HC），通过在视觉记忆搜索范式中记录对齐的面部视频和眼动追踪序列，为评估集成策略提供了一个生态有效的资源。大量实验表明，我们的框架优于传统的后期融合和特征连接方法，在区分AD和HC方面实现了95.11%的分类准确率，突出了通过显式建模模态间依赖性和模态特定贡献所实现的卓越鲁棒性和诊断性能。

## 🔬 方法详解

**问题定义**：阿尔茨海默病（AD）的早期诊断对于及时干预至关重要。现有的诊断方法，特别是基于单一模态的方法，可能无法充分捕捉AD患者在认知和行为上的复杂变化。虽然眼动追踪和面部特征是重要的认知功能指标，但很少有研究探索如何有效地将它们融合用于AD诊断。传统的后期融合和特征连接方法无法充分利用模态间的互补信息和依赖关系，导致诊断性能受限。

**核心思路**：本研究的核心思路是设计一个能够显式建模眼动追踪和面部特征之间交互的框架，从而提取更具判别性的多模态表征。通过引入交叉注意力机制，框架可以自适应地学习不同模态的权重，并捕捉它们之间的依赖关系。同时，利用方向感知卷积模块提取细粒度的面部特征，增强模型对AD相关面部变化的敏感性。

**技术框架**：该框架主要包含两个关键模块：交叉增强融合注意力模块（CEFAM）和方向感知卷积模块（DACM）。首先，分别提取眼动追踪和面部特征。然后，CEFAM模块利用交叉注意力机制建模模态间的交互，并通过全局增强来提升特征的表达能力。DACM模块则通过水平和垂直方向的卷积核提取细粒度的方向性面部特征。最后，将两个模块的输出进行融合，并使用分类器进行AD诊断。

**关键创新**：该研究的关键创新在于提出了CEFAM和DACM两个模块，以及将它们集成到一个统一的框架中。CEFAM通过交叉注意力机制显式地建模了模态间的交互，克服了传统融合方法忽略模态间依赖关系的缺点。DACM则通过方向感知卷积提取了更具判别性的面部特征，增强了模型对AD相关面部变化的敏感性。

**关键设计**：CEFAM模块使用多头注意力机制来实现交叉注意力，允许模型从不同的角度关注不同模态的信息。全局增强采用残差连接的方式，避免了梯度消失问题。DACM模块使用两个方向（水平和垂直）的卷积核，分别提取水平和垂直方向的梯度信息。损失函数采用交叉熵损失函数，用于训练分类器。

## 📊 实验亮点

实验结果表明，该框架在自建的多模态数据集上实现了95.11%的分类准确率，显著优于传统的后期融合和特征连接方法。与仅使用眼动追踪或面部特征的单模态方法相比，该框架的性能也得到了显著提升，验证了多模态融合的有效性。消融实验进一步证明了CEFAM和DACM模块的有效性。

## 🎯 应用场景

该研究成果可应用于阿尔茨海默病的早期辅助诊断，帮助医生更准确地识别高风险人群，从而进行早期干预和管理。此外，该多模态融合框架也可扩展到其他神经退行性疾病的诊断，具有广阔的应用前景。未来，结合可穿戴设备，有望实现AD的远程监测和个性化管理。

## 📄 摘要（原文）

> Accurate diagnosis of Alzheimer's disease (AD) is essential for enabling timely intervention and slowing disease progression. Multimodal diagnostic approaches offer considerable promise by integrating complementary information across behavioral and perceptual domains. Eye-tracking and facial features, in particular, are important indicators of cognitive function, reflecting attentional distribution and neurocognitive state. However, few studies have explored their joint integration for auxiliary AD diagnosis. In this study, we propose a multimodal cross-enhanced fusion framework that synergistically leverages eye-tracking and facial features for AD detection. The framework incorporates two key modules: (a) a Cross-Enhanced Fusion Attention Module (CEFAM), which models inter-modal interactions through cross-attention and global enhancement, and (b) a Direction-Aware Convolution Module (DACM), which captures fine-grained directional facial features via horizontal-vertical receptive fields. Together, these modules enable adaptive and discriminative multimodal representation learning. To support this work, we constructed a synchronized multimodal dataset, including 25 patients with AD and 25 healthy controls (HC), by recording aligned facial video and eye-tracking sequences during a visual memory-search paradigm, providing an ecologically valid resource for evaluating integration strategies. Extensive experiments on this dataset demonstrate that our framework outperforms traditional late fusion and feature concatenation methods, achieving a classification accuracy of 95.11% in distinguishing AD from HC, highlighting superior robustness and diagnostic performance by explicitly modeling inter-modal dependencies and modality-specific contributions.

