---
layout: default
title: Dynamic Caustics by Ultrasonically Modulated Liquid Surface
---

# Dynamic Caustics by Ultrasonically Modulated Liquid Surface

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16397" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16397v1</a>
  <a href="https://arxiv.org/pdf/2505.16397.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16397v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16397v1', 'Dynamic Caustics by Ultrasonically Modulated Liquid Surface')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Koki Nagakura, Tatsuki Fushimi, Ayaka Tsutsui, Yoichi Ochiai

**分类**: cs.GR, cs.HC

**发布日期**: 2025-05-22

**DOI**: [10.1038/s41598-025-16190-3](https://doi.org/10.1038/s41598-025-16190-3)

---

## 💡 一句话要点

**提出动态光斑生成方法以解决液体表面操控难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `动态光斑` `液体表面` `超声波操控` `数字双胞胎` `实时反馈` `光学显示` `计算机视觉`

## 📋 核心要点

1. 现有的光斑生成方法在动态操控液体表面方面存在挑战，难以实现高频率和复杂图案的实时生成。
2. 论文提出通过超声波直接操控液体表面，结合数字双胞胎框架，实现动态光斑的生成与优化。
3. 实验结果表明，该方法能够生成连续动画和复杂光斑图案，尽管在对比度和分辨率上有所不足，但实时适应性显著提升。

## 📝 摘要（中文）

本文提出了一种通过利用双优化全息场与相控阵换能器（PAT）生成动态光斑图案的方法。基于静态光斑优化和超声操控的前期研究，该方法采用计算技术动态塑造液体表面，从而创建可控的实时光斑图像。系统采用数字双胞胎框架，支持迭代反馈和优化，提升了光斑图案的准确性和质量。尽管与固体表面方法相比在对比度和分辨率上存在局限性，但该方法在实时适应性和可扩展性方面具有优势，未来可广泛应用于互动显示、艺术装置和教育工具等领域。

## 🔬 方法详解

**问题定义**：本文旨在解决现有光斑生成方法在动态液体表面操控中的不足，特别是在高频率和复杂图案生成方面的挑战。

**核心思路**：通过结合超声波技术与数字双胞胎框架，动态塑造液体表面以生成可控的光斑图案，从而实现实时反馈与优化。

**技术框架**：系统主要包括超声波换能器、全息场生成模块和数字双胞胎反馈机制。超声波换能器用于操控液体表面，全息场生成模块负责光斑图案的创建，而数字双胞胎框架则支持实时调整与优化。

**关键创新**：本研究的主要创新在于将液体表面作为折射介质进行动态光斑生成，利用超声波直接操控液体表面，显著提升了光斑生成的灵活性与实时性。

**关键设计**：在技术细节上，采用了优化的超声波频率和相位设置，以实现最佳的液体表面形状，同时设计了适应性强的损失函数，以提高光斑图案的质量和准确性。

## 📊 实验亮点

实验结果显示，该方法能够以高频率生成连续动画和复杂光斑图案，尽管在对比度和分辨率上与固体表面方法相比存在局限性，但在实时适应性和可扩展性方面表现出显著优势，具有广泛的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括互动显示、艺术装置和教育工具等，能够为用户提供更具沉浸感和互动性的体验。未来，随着技术的进一步发展，预计将推动相关领域的创新与应用，提升视觉表现和用户体验。

## 📄 摘要（原文）

> This paper presents a method for generating dynamic caustic patterns by utilising dual-optimised holographic fields with Phased Array Transducer (PAT). Building on previous research in static caustic optimisation and ultrasonic manipulation, this approach employs computational techniques to dynamically shape fluid surfaces, thereby creating controllable and real-time caustic images. The system employs a Digital Twin framework, which enables iterative feedback and refinement, thereby improving the accuracy and quality of the caustic patterns produced. This paper extends the foundational work in caustic generation by integrating liquid surfaces as refractive media. This concept has previously been explored in simulations but not fully realised in practical applications. The utilisation of ultrasound to directly manipulate these surfaces enables the generation of dynamic caustics with a high degree of flexibility. The Digital Twin approach further enhances this process by allowing for precise adjustments and optimisation based on real-time feedback. Experimental results demonstrate the technique's capacity to generate continuous animations and complex caustic patterns at high frequencies. Although there are limitations in contrast and resolution compared to solid-surface methods, this approach offers advantages in terms of real-time adaptability and scalability. This technique has the potential to be applied in a number of areas, including interactive displays, artistic installations and educational tools. This research builds upon the work of previous researchers in the fields of caustics optimisation, ultrasonic manipulation, and computational displays. Future research will concentrate on enhancing the resolution and intricacy of the generated patterns.

