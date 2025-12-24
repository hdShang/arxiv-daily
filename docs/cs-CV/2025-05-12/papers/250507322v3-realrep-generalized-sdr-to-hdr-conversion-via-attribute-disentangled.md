---
layout: default
title: "RealRep: Generalized SDR-to-HDR Conversion via Attribute-Disentangled Representation Learning"
---

# RealRep: Generalized SDR-to-HDR Conversion via Attribute-Disentangled Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07322" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07322v3</a>
  <a href="https://arxiv.org/pdf/2505.07322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07322v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07322v3', 'RealRep: Generalized SDR-to-HDR Conversion via Attribute-Disentangled Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Li Xu, Siqi Wang, Kepeng Xu, Gang He, Lin Zhang, Weiran Wang, Yu-Wing Tai

**分类**: cs.CV

**发布日期**: 2025-05-12 (更新: 2025-11-11)

**备注**: Published on AAAI'26(Oral): The Annual AAAI Conference on Artificial Intelligence

---

## 💡 一句话要点

**提出RealRep以解决SDR到HDR转换中的表现多样性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `高动态范围` `标准动态范围` `图像转换` `属性解耦` `深度学习` `视觉质量` `对比学习`

## 📋 核心要点

1. 现有SDR到HDR转换方法依赖固定色调映射，难以适应真实世界中多样的内容和退化情况。
2. 本文提出RealRep框架，通过属性解耦表示学习，明确分离亮度和色度，增强鲁棒性。
3. 实验结果表明，RealRep在HDR色域重建方面显著优于现有方法，提升了泛化能力和感知质量。

## 📝 摘要（中文）

高动态范围宽色域（HDR-WCG）技术日益普及，导致对标准动态范围（SDR）内容转换为HDR的需求增加。现有方法主要依赖固定的色调映射操作，难以处理真实世界SDR内容中的多样外观和退化问题。为了解决这一局限性，本文提出了一种通用的SDR到HDR框架，通过学习属性解耦表示来增强鲁棒性。核心方法为现实属性解耦表示学习（RealRep），明确解耦亮度和色度分量，以捕捉不同SDR分布中的内在内容变化。此外，设计了一种亮度/色度感知的负例生成策略，有效建模SDR风格间的色调差异。通过这些属性级先验，提出了轻量级的两阶段框架DDACMNet，能够通过控制感知归一化机制进行自适应分层映射。实验表明，RealRep在泛化能力和感知HDR色域重建方面均优于现有最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决SDR到HDR转换中，现有方法因依赖固定色调映射而无法处理多样化外观和退化的问题。

**核心思路**：提出RealRep框架，通过属性解耦表示学习，明确分离亮度和色度分量，以捕捉不同SDR内容的内在变化，从而增强转换的鲁棒性。

**技术框架**：整体架构包括两个主要模块：1) 现实属性解耦表示学习（RealRep），用于解耦亮度和色度；2) 退化域感知控制映射网络（DDACMNet），通过控制感知归一化机制进行自适应映射。

**关键创新**：最重要的创新在于引入了亮度/色度感知的负例生成策略，构建退化敏感的对比对，有效建模SDR风格间的色调差异，这与现有方法的固定映射机制有本质区别。

**关键设计**：在网络结构上，DDACMNet采用轻量级设计，包含两阶段映射过程，动态调节映射过程，利用退化条件特征进行控制，确保在不同退化域间的适应性。

## 📊 实验亮点

实验结果显示，RealRep在HDR色域重建任务中，相较于现有最先进方法，泛化能力提升显著，具体表现为在多种SDR样本上均能实现更高的色彩保真度和视觉质量，提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括影视制作、游戏开发和虚拟现实等需要高质量图像处理的场景。通过提升SDR到HDR的转换质量，能够为用户提供更丰富的视觉体验，推动相关技术的发展和应用。

## 📄 摘要（原文）

> High-Dynamic-Range Wide-Color-Gamut (HDR-WCG) technology is becoming increasingly widespread, driving a growing need for converting Standard Dynamic Range (SDR) content to HDR. Existing methods primarily rely on fixed tone mapping operators, which struggle to handle the diverse appearances and degradations commonly present in real-world SDR content. To address this limitation, we propose a generalized SDR-to-HDR framework that enhances robustness by learning attribute-disentangled representations. Central to our approach is Realistic Attribute-Disentangled Representation Learning (RealRep), which explicitly disentangles luminance and chrominance components to capture intrinsic content variations across different SDR distributions. Furthermore, we design a Luma-/Chroma-aware negative exemplar generation strategy that constructs degradation-sensitive contrastive pairs, effectively modeling tone discrepancies across SDR styles. Building on these attribute-level priors, we introduce the Degradation-Domain Aware Controlled Mapping Network (DDACMNet), a lightweight, two-stage framework that performs adaptive hierarchical mapping guided by a control-aware normalization mechanism. DDACMNet dynamically modulates the mapping process via degradation-conditioned features, enabling robust adaptation across diverse degradation domains. Extensive experiments demonstrate that RealRep consistently outperforms state-of-the-art methods in both generalization and perceptually faithful HDR color gamut reconstruction.

