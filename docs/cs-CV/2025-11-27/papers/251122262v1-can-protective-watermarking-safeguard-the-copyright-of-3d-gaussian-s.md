---
layout: default
title: Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?
---

# Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22262" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22262v1</a>
  <a href="https://arxiv.org/pdf/2511.22262.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22262v1" onclick="toggleFavorite(this, '2511.22262v1', 'Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenkai Huang, Yijia Guo, Gaolei Li, Lei Ma, Hang Zhang, Liwen Hu, Jiazheng Wang, Jianhua Li, Tiejun Huang

**分类**: cs.CV

**发布日期**: 2025-11-27

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**提出GSPure框架，针对3D高斯溅射的水印进行有效去除，同时保持场景完整性。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `水印去除` `版权保护` `几何特征聚类` `渲染贡献分析`

## 📋 核心要点

1. 现有3D高斯溅射水印方案缺乏对恶意攻击的系统性评估，其鲁棒性有待考量。
2. GSPure框架通过分析视角相关渲染贡献和几何特征聚类，精确定位并移除水印相关的高斯基元。
3. 实验表明，GSPure能有效去除水印，水印PSNR降低高达16.34dB，同时场景保真度损失小于1dB。

## 📝 摘要（中文）

3D高斯溅射(3DGS)作为一种强大的3D场景表示方法，因其卓越的效率和高保真视觉质量而被广泛采用。鉴于3DGS资产的重要价值，最近的研究引入了专门的水印方案，以确保版权保护和所有权验证。然而，现有的3D高斯水印方法能否真正保证对3D资产的强大保护？本文首次系统地探索和验证了3DGS水印框架可能存在的漏洞。我们证明了为2D图像设计的传统水印去除技术，由于专门的渲染管线和每个高斯基元的独特属性，不能有效地推广到3DGS场景。受此启发，我们提出了GSPure，这是第一个专门为3DGS水印表示设计的水印净化框架。通过分析视角相关的渲染贡献和利用几何精确的特征聚类，GSPure精确地隔离并有效地去除与水印相关的高斯基元，同时保持场景完整性。大量的实验表明，我们的GSPure实现了最佳的水印净化性能，将水印PSNR降低了高达16.34dB，同时将原始场景保真度的降低降至最低，损失小于1dB PSNR。此外，它在有效性和泛化性方面始终优于现有方法。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射水印方案的安全性缺乏充分验证，容易受到攻击。传统的2D图像水印去除方法无法直接应用于3DGS，因为3DGS具有独特的渲染管线和高斯基元属性。因此，如何有效地去除3DGS中的水印，同时保持场景的完整性，是一个亟待解决的问题。

**核心思路**：GSPure的核心思路是利用3DGS的特性，通过分析视角相关的渲染贡献和几何特征，精确定位并去除与水印相关的高斯基元。该方法避免了直接修改高斯参数，而是专注于识别和移除恶意添加的高斯点，从而在去除水印的同时，最大限度地保留原始场景的细节。

**技术框架**：GSPure框架主要包含两个阶段：视角相关渲染贡献分析和几何特征聚类。首先，分析每个高斯基元在不同视角下的渲染贡献，以确定哪些高斯基元对水印的贡献最大。然后，利用几何特征聚类算法，将这些高斯基元进行分组，以便更精确地识别和移除水印相关的高斯基元。最后，将识别出的水印高斯点移除，从而达到净化水印的目的。

**关键创新**：GSPure的关键创新在于其针对3DGS水印的特性，提出了专门的水印净化框架。与传统的2D图像水印去除方法不同，GSPure充分利用了3DGS的渲染管线和高斯基元属性，实现了更精确的水印定位和去除。此外，GSPure还引入了几何特征聚类算法，进一步提高了水印去除的精度和效率。

**关键设计**：GSPure的关键设计包括：1) 视角相关渲染贡献分析，通过计算每个高斯基元在不同视角下的渲染贡献，确定其对水印的影响程度；2) 几何特征聚类，利用高斯基元的几何特征（如位置、法向量等）进行聚类，以便更精确地识别和移除水印相关的高斯基元；3) 自适应阈值设定，根据场景的复杂度和水印的强度，自适应地调整水印去除的阈值，以平衡水印去除效果和场景保真度。

## 📊 实验亮点

实验结果表明，GSPure在水印去除性能方面显著优于现有方法，水印PSNR降低高达16.34dB，同时场景保真度损失小于1dB。GSPure在不同场景和水印强度下均表现出良好的泛化能力。此外，实验还验证了GSPure对不同类型水印攻击的鲁棒性。

## 🎯 应用场景

该研究成果可应用于3D内容版权保护领域，例如游戏资产、虚拟现实场景、建筑模型等。通过GSPure框架，可以有效防止未经授权的3D资产复制和传播，维护创作者的权益。此外，该技术还可以应用于数字取证领域，用于检测和分析3D模型中的恶意水印。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for 3D scenes, widely adopted due to its exceptional efficiency and high-fidelity visual quality. Given the significant value of 3DGS assets, recent works have introduced specialized watermarking schemes to ensure copyright protection and ownership verification. However, can existing 3D Gaussian watermarking approaches genuinely guarantee robust protection of the 3D assets? In this paper, for the first time, we systematically explore and validate possible vulnerabilities of 3DGS watermarking frameworks. We demonstrate that conventional watermark removal techniques designed for 2D images do not effectively generalize to the 3DGS scenario due to the specialized rendering pipeline and unique attributes of each gaussian primitives. Motivated by this insight, we propose GSPure, the first watermark purification framework specifically for 3DGS watermarking representations. By analyzing view-dependent rendering contributions and exploiting geometrically accurate feature clustering, GSPure precisely isolates and effectively removes watermark-related Gaussian primitives while preserving scene integrity. Extensive experiments demonstrate that our GSPure achieves the best watermark purification performance, reducing watermark PSNR by up to 16.34dB while minimizing degradation to original scene fidelity with less than 1dB PSNR loss. Moreover, it consistently outperforms existing methods in both effectiveness and generalization.

