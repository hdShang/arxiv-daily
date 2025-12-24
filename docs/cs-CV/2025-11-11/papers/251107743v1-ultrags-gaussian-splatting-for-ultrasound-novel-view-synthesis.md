---
layout: default
title: "UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis"
---

# UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07743" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07743v1</a>
  <a href="https://arxiv.org/pdf/2511.07743.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07743v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.07743v1', 'UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-11

**备注**: Under Review

**🔗 代码/项目**: [GITHUB](https://github.com/Bean-Young/UltraGS)

---

## 💡 一句话要点

**UltraGS：用于超声新视角合成的高斯溅射方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `超声成像` `新视角合成` `高斯溅射` `深度感知` `医学影像`

## 📋 核心要点

1. 超声成像视野有限，难以进行新视角合成，限制了临床应用。
2. UltraGS通过深度感知高斯溅射和超声物理建模，实现高质量新视角合成。
3. 实验表明，UltraGS在PSNR、SSIM和MSE指标上优于现有方法，并能实时渲染。

## 📝 摘要（中文）

超声成像是非侵入性临床诊断的基石，但其有限的视野使得新视角合成变得复杂。我们提出了UltraGS，一个为超声成像优化的高斯溅射框架。首先，我们引入了一种深度感知的高斯溅射策略，其中每个高斯被分配一个可学习的视野，从而实现精确的深度预测和精确的结构表示。其次，我们设计了SH-DARS，一个轻量级的渲染函数，它结合了低阶球谐函数与超声特有的波物理，包括深度衰减、反射和散射，以准确地模拟组织强度。第三，我们贡献了临床超声检查数据集，这是一个基准，用于捕获真实临床协议下的各种解剖扫描。在三个数据集上的大量实验表明了UltraGS的优越性，在PSNR（高达29.55）、SSIM（高达0.89）和MSE（低至0.002）方面取得了最先进的结果，同时实现了64.69 fps的实时合成。

## 🔬 方法详解

**问题定义**：超声成像在临床诊断中至关重要，但其视野范围有限，难以从不同角度观察组织结构。现有方法在新视角合成方面存在精度不足的问题，无法准确重建组织结构和强度信息。

**核心思路**：UltraGS的核心思路是将高斯溅射技术与超声成像的物理特性相结合，通过学习每个高斯粒子的深度信息和视野范围，以及模拟超声波的传播特性（如衰减、反射和散射），从而实现更精确的新视角合成。

**技术框架**：UltraGS框架主要包含以下几个模块：1) 深度感知高斯溅射：使用可学习的视野范围来增强高斯粒子的深度表达能力。2) SH-DARS渲染函数：结合低阶球谐函数和超声波物理模型，模拟组织强度。3) 优化过程：通过最小化渲染图像与真实图像之间的差异来优化高斯粒子的参数。

**关键创新**：UltraGS的关键创新在于：1) 引入了深度感知的高斯溅射策略，使得每个高斯粒子能够学习其视野范围，从而更准确地预测深度信息。2) 设计了SH-DARS渲染函数，将超声波的物理特性融入到渲染过程中，从而更真实地模拟组织强度。

**关键设计**：1) 深度感知高斯溅射：每个高斯粒子除了位置、颜色等参数外，还包含一个可学习的视野范围参数。2) SH-DARS渲染函数：使用低阶球谐函数来表示方向依赖的反射和散射，并根据深度信息模拟超声波的衰减。3) 损失函数：主要包括渲染图像与真实图像之间的L1损失、SSIM损失和深度一致性损失。

## 📊 实验亮点

UltraGS在三个数据集上进行了广泛的实验，结果表明，该方法在PSNR、SSIM和MSE等指标上均优于现有方法，PSNR最高提升至29.55，SSIM最高提升至0.89，MSE最低降至0.002。此外，UltraGS还实现了64.69 fps的实时渲染速度，使其能够应用于实时临床场景。

## 🎯 应用场景

UltraGS可应用于医学影像分析、手术导航、远程医疗等领域。通过生成任意视角的超声图像，医生可以更全面地了解患者的病情，提高诊断的准确性和效率。此外，该技术还可用于培训医生，帮助他们更好地掌握超声成像技术。

## 📄 摘要（原文）

> Ultrasound imaging is a cornerstone of non-invasive clinical diagnostics, yet its limited field of view complicates novel view synthesis. We propose \textbf{UltraGS}, a Gaussian Splatting framework optimized for ultrasound imaging. First, we introduce a depth-aware Gaussian splatting strategy, where each Gaussian is assigned a learnable field of view, enabling accurate depth prediction and precise structural representation. Second, we design SH-DARS, a lightweight rendering function combining low-order spherical harmonics with ultrasound-specific wave physics, including depth attenuation, reflection, and scattering, to model tissue intensity accurately. Third, we contribute the Clinical Ultrasound Examination Dataset, a benchmark capturing diverse anatomical scans under real-world clinical protocols. Extensive experiments on three datasets demonstrate UltraGS's superiority, achieving state-of-the-art results in PSNR (up to 29.55), SSIM (up to 0.89), and MSE (as low as 0.002) while enabling real-time synthesis at 64.69 fps. The code and dataset are open-sourced at: https://github.com/Bean-Young/UltraGS.

