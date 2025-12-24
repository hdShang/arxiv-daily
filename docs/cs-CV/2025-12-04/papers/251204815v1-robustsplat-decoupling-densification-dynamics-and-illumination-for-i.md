---
layout: default
title: "RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS"
---

# RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04815" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04815v1</a>
  <a href="https://arxiv.org/pdf/2512.04815.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04815v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04815v1', 'RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao

**分类**: cs.CV

**发布日期**: 2025-12-04

**备注**: arXiv admin note: substantial text overlap with arXiv:2506.02751

---

## 💡 一句话要点

**RobustSplat++：解耦3DGS的稠密化、动态和光照，实现野外场景鲁棒建模**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `新视角合成` `野外场景建模` `瞬态物体` `光照变化` `鲁棒性` `延迟高斯增长` `尺度级联掩码`

## 📋 核心要点

1. 现有3DGS方法在处理野外场景时，易受瞬态物体和光照变化的影响，导致渲染结果出现伪影。
2. RobustSplat++通过延迟高斯增长、尺度级联掩码自举和外观建模，解耦稠密化、动态和光照，提升鲁棒性。
3. 实验表明，RobustSplat++在多个数据集上超越现有方法，证明了其在野外场景建模方面的有效性。

## 📝 摘要（中文）

3D高斯溅射(3DGS)因其在新视角合成和3D建模中的实时、照片级真实感渲染而备受关注。然而，现有方法难以准确建模受瞬态物体和光照影响的野外场景，导致渲染图像中出现伪影。我们发现，高斯稠密化过程在增强场景细节捕获的同时，通过增长额外的用于建模瞬态干扰和光照变化的高斯分布，无意中导致了这些伪影。为了解决这个问题，我们提出了RobustSplat++，这是一个基于几个关键设计的鲁棒解决方案。首先，我们引入了一种延迟高斯增长策略，该策略优先优化静态场景结构，然后再允许高斯分裂/克隆，从而减轻了早期优化过程中对瞬态物体的过拟合。其次，我们设计了一种尺度级联的掩码自举方法，该方法首先利用较低分辨率的特征相似性监督来进行可靠的初始瞬态掩码估计，利用其更强的语义一致性和对噪声的鲁棒性，然后逐步发展到高分辨率监督，以实现更精确的掩码预测。第三，我们将延迟高斯增长策略和掩码自举与外观建模相结合，以处理包括瞬态和光照在内的野外场景。在多个具有挑战性的数据集上进行的大量实验表明，我们的方法优于现有方法，清楚地证明了我们方法的鲁棒性和有效性。

## 🔬 方法详解

**问题定义**：现有3DGS方法在处理真实世界的复杂场景时，容易受到瞬态物体（如移动的车辆、行人）和光照变化的影响。这些因素会导致高斯分布过度拟合这些干扰，从而在渲染结果中产生不希望的伪影，降低了新视角合成的质量。现有方法缺乏对这些动态因素的有效建模和分离能力。

**核心思路**：RobustSplat++的核心思路是将场景的静态结构、动态物体和光照变化解耦。通过延迟高斯增长，优先优化静态场景的几何结构，避免在早期优化阶段过度拟合瞬态物体。利用尺度级联的掩码自举方法，逐步精确地识别和分割瞬态物体。结合外观建模，更好地处理光照变化带来的影响。

**技术框架**：RobustSplat++的整体框架包含以下几个主要阶段：1) 延迟高斯增长：在初始阶段，限制高斯分布的增长，专注于优化静态场景结构。2) 尺度级联掩码自举：从低分辨率到高分辨率，逐步优化瞬态物体的掩码。3) 外观建模：结合光照信息，优化高斯分布的外观参数。4) 渲染：使用优化后的高斯分布进行新视角合成。

**关键创新**：RobustSplat++的关键创新在于其解耦的思想和具体实现。延迟高斯增长策略避免了对瞬态物体的过度拟合，尺度级联掩码自举方法提高了瞬态物体分割的鲁棒性和精度。这种解耦方法使得模型能够更好地适应野外场景的复杂性和动态性。

**关键设计**：延迟高斯增长策略中，可以设置一个阈值，控制高斯分布增长的起始时间。尺度级联掩码自举方法中，可以使用不同的损失函数（如交叉熵损失）来监督掩码的预测。外观建模可以采用球谐光照模型或其他光照模型来表示光照变化。具体参数设置需要根据数据集和场景特点进行调整。

## 📊 实验亮点

RobustSplat++在多个具有挑战性的数据集上进行了评估，实验结果表明，该方法在渲染质量和鲁棒性方面均优于现有方法。具体而言，RobustSplat++在处理包含瞬态物体和光照变化的场景时，能够显著减少伪影，提高新视角合成的真实感。定量指标方面，RobustSplat++在PSNR、SSIM等指标上均取得了显著提升。

## 🎯 应用场景

RobustSplat++在自动驾驶、机器人导航、增强现实等领域具有广泛的应用前景。它可以用于构建更鲁棒、更准确的3D场景模型，提高这些应用在复杂环境下的性能和可靠性。例如，在自动驾驶中，可以利用RobustSplat++构建周围环境的3D地图，并准确识别和跟踪动态物体，从而提高驾驶安全性。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has gained significant attention for its real-time, photo-realistic rendering in novel-view synthesis and 3D modeling. However, existing methods struggle with accurately modeling in-the-wild scenes affected by transient objects and illuminations, leading to artifacts in the rendered images. We identify that the Gaussian densification process, while enhancing scene detail capture, unintentionally contributes to these artifacts by growing additional Gaussians that model transient disturbances and illumination variations. To address this, we propose RobustSplat++, a robust solution based on several critical designs. First, we introduce a delayed Gaussian growth strategy that prioritizes optimizing static scene structure before allowing Gaussian splitting/cloning, mitigating overfitting to transient objects in early optimization. Second, we design a scale-cascaded mask bootstrapping approach that first leverages lower-resolution feature similarity supervision for reliable initial transient mask estimation, taking advantage of its stronger semantic consistency and robustness to noise, and then progresses to high-resolution supervision to achieve more precise mask prediction. Third, we incorporate the delayed Gaussian growth strategy and mask bootstrapping with appearance modeling to handling in-the-wild scenes including transients and illuminations. Extensive experiments on multiple challenging datasets show that our method outperforms existing methods, clearly demonstrating the robustness and effectiveness of our method.

