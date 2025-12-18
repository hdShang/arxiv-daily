---
layout: default
title: FMANet: A Novel Dual-Phase Optical Flow Approach with Fusion Motion Attention Network for Robust Micro-expression Recognition
---

# FMANet: A Novel Dual-Phase Optical Flow Approach with Fusion Motion Attention Network for Robust Micro-expression Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07810" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07810v3</a>
  <a href="https://arxiv.org/pdf/2510.07810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07810v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.07810v3', 'FMANet: A Novel Dual-Phase Optical Flow Approach with Fusion Motion Attention Network for Robust Micro-expression Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luu Tu Nguyen, Vu Tram Anh Khuong, Thi Bich Phuong Man, Thi Duyen Ngo, Thanh Ha Le

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-10-15)

---

## 💡 一句话要点

**提出FMANet，利用双阶段光流和融合运动注意力网络提升微表情识别鲁棒性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `微表情识别` `光流` `双阶段分析` `注意力机制` `情感计算`

## 📋 核心要点

1. 现有微表情识别方法主要依赖起始帧到顶点帧的光流，忽略了顶点帧到偏移帧阶段的运动信息。
2. 论文提出幅度调制组合光流（MM-COF）和融合运动注意力网络（FMANet），实现双阶段运动信息融合和显著区域关注。
3. 在多个标准数据集上，FMANet和MM-COF表现优于现有方法，验证了双阶段框架在微表情识别中的有效性。

## 📝 摘要（中文）

面部微表情是真实情感的重要指标，但其细微和短暂的特性使得微表情识别极具挑战。光流因其有效性而被广泛用作输入模态。然而，现有方法通常只计算起始帧和顶点帧之间的光流，忽略了顶点帧到偏移帧阶段的重要运动信息。为了解决这一局限，我们首先提出了一种综合运动表示，称为幅度调制组合光流（MM-COF），它将微表情两个阶段的运动动态整合到一个统一的描述符中，可以直接用于识别网络。在此基础上，我们提出了一种新的端到端神经网络架构FMANet，它将双阶段分析和幅度调制内置到可学习的模块中。这使得网络能够自适应地融合运动线索，并专注于显著的面部区域进行分类。在MMEW、SMIC、CASME-II和SAMM数据集上的实验结果表明，我们提出的MM-COF表示和FMANet优于现有方法，突出了可学习的双阶段框架在推进微表情识别方面的潜力。

## 🔬 方法详解

**问题定义**：微表情识别旨在从细微的面部运动中识别情感。现有方法，尤其是基于光流的方法，通常只关注起始帧到顶点帧的运动信息，忽略了顶点帧到偏移帧阶段的运动，导致信息不完整，影响识别精度。

**核心思路**：核心思路是充分利用微表情的两个阶段（起始到顶点，顶点到偏移）的运动信息。通过结合两个阶段的光流信息，并引入注意力机制，使网络能够自适应地关注重要的面部区域，从而提高微表情识别的准确性和鲁棒性。

**技术框架**：FMANet是一个端到端的神经网络架构，主要包含以下几个模块：1) 双阶段光流计算：分别计算起始帧到顶点帧以及顶点帧到偏移帧的光流。2) 幅度调制组合光流（MM-COF）：将两个阶段的光流信息进行融合，并根据光流幅度进行调制，得到更全面的运动表示。3) 融合运动注意力网络：利用注意力机制，自适应地学习不同面部区域的重要性，并融合不同阶段的运动信息。4) 分类器：根据融合后的特征进行微表情分类。

**关键创新**：关键创新在于：1) 提出了MM-COF，一种综合考虑两个阶段运动信息的表示方法。2) 设计了FMANet，一个可学习的双阶段分析框架，能够自适应地融合运动线索和关注显著区域。3) 将双阶段分析和幅度调制融入到可学习的模块中，使得网络能够更好地适应不同的微表情数据。

**关键设计**：MM-COF通过将两个阶段的光流幅度进行加权组合，并进行归一化处理，从而得到一个统一的运动描述符。融合运动注意力网络采用卷积神经网络提取特征，并利用注意力机制学习不同区域的权重。损失函数采用交叉熵损失函数，用于优化分类器的性能。具体的网络结构和参数设置在论文中有详细描述，但具体数值未知。

## 📊 实验亮点

实验结果表明，提出的MM-COF表示和FMANet在MMEW、SMIC、CASME-II和SAMM等多个标准数据集上均优于现有方法。具体性能提升幅度未知，但论文强调了其优越性，表明该方法在微表情识别方面具有显著的优势。

## 🎯 应用场景

该研究成果可应用于心理学研究、安全监控、行为分析等领域。例如，在心理咨询中，可以辅助识别患者的真实情感；在安全监控中，可以用于检测潜在的犯罪意图；在行为分析中，可以用于评估个体的情绪状态。未来，该技术有望在人机交互、情感计算等领域发挥更大的作用。

## 📄 摘要（原文）

> Facial micro-expressions, characterized by their subtle and brief nature, are valuable indicators of genuine emotions. Despite their significance in psychology, security, and behavioral analysis, micro-expression recognition remains challenging due to the difficulty of capturing subtle facial movements. Optical flow has been widely employed as an input modality for this task due to its effectiveness. However, most existing methods compute optical flow only between the onset and apex frames, thereby overlooking essential motion information in the apex-to-offset phase. To address this limitation, we first introduce a comprehensive motion representation, termed Magnitude-Modulated Combined Optical Flow (MM-COF), which integrates motion dynamics from both micro-expression phases into a unified descriptor suitable for direct use in recognition networks. Building upon this principle, we then propose FMANet, a novel end-to-end neural network architecture that internalizes the dual-phase analysis and magnitude modulation into learnable modules. This allows the network to adaptively fuse motion cues and focus on salient facial regions for classification. Experimental evaluations on the MMEW, SMIC, CASME-II, and SAMM datasets, widely recognized as standard benchmarks, demonstrate that our proposed MM-COF representation and FMANet outperforms existing methods, underscoring the potential of a learnable, dual-phase framework in advancing micro-expression recognition.

