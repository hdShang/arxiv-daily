---
layout: default
title: Log NeRF: Comparing Spaces for Learning Radiance Fields
---

# Log NeRF: Comparing Spaces for Learning Radiance Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09375" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09375v1</a>
  <a href="https://arxiv.org/pdf/2512.09375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09375v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09375v1', 'Log NeRF: Comparing Spaces for Learning Radiance Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sihe Chen, Luv Verma, Bruce A. Maxwell

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-10

**备注**: The 36th British Machine Vision Conference

---

## 💡 一句话要点

**Log NeRF：通过比较不同色彩空间，提升神经辐射场的学习效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经辐射场` `色彩空间` `novel view synthesis` `log RGB` `渲染质量` `低光照` `表征学习` `光照反射`

## 📋 核心要点

1. 现有 NeRF 方法主要使用 sRGB 色彩空间，忽略了色彩空间对辐射场表示学习的影响。
2. 该论文提出在 log RGB 色彩空间中学习辐射场，利用对数变换简化光照和反射率分离，提升场景外观表示的紧凑性和有效性。
3. 实验结果表明，log RGB 色彩空间能够提高渲染质量，增强鲁棒性，尤其在低光照条件下表现出色，且具有良好的泛化性。

## 📝 摘要（中文）

神经辐射场（NeRF）在 novel view synthesis 方面取得了显著成果，通常使用 sRGB 图像进行监督。然而，很少有研究关注网络学习辐射场表示时所使用的色彩空间。受 BiIlluminant Dichromatic Reflection (BIDR) 模型的启发，该模型表明对数变换简化了光照和反射率的分离，我们假设 log RGB 空间使 NeRF 能够学习更紧凑和有效的场景外观表示。为了验证这一点，我们使用 GoPro 相机拍摄了大约 30 个视频，通过逆编码确保线性数据恢复。我们通过将每个网络输出转换为通用色彩空间，然后在渲染和损失计算之前，在不同的色彩空间（线性、sRGB、GPLog 和 log RGB）下训练 NeRF 模型，从而在不同的色彩空间中强制进行表征学习。定量和定性评估表明，使用 log RGB 色彩空间始终可以提高渲染质量，在各种场景中表现出更大的鲁棒性，并且在低光照条件下表现特别好，同时使用相同位深度的输入图像。对不同网络大小和 NeRF 变体的进一步分析证实了 log 空间优势的泛化性和稳定性。

## 🔬 方法详解

**问题定义**：现有 NeRF 方法在 novel view synthesis 任务中取得了显著进展，但大多采用 sRGB 色彩空间作为监督信号，忽略了色彩空间本身对辐射场表示学习的影响。不同的色彩空间可能影响网络学习场景几何和外观的效率和质量。因此，如何选择合适的色彩空间以优化 NeRF 的性能是一个关键问题。

**核心思路**：该论文的核心思路是借鉴 BiIlluminant Dichromatic Reflection (BIDR) 模型的启示，认为在 log RGB 色彩空间中，光照和反射率更容易分离。因此，在 log RGB 空间中学习辐射场可以帮助 NeRF 学习到更紧凑、更有效的场景外观表示。通过在不同色彩空间中训练 NeRF 模型，并比较其渲染质量，验证 log RGB 空间的优势。

**技术框架**：该论文的技术框架主要包括以下几个步骤：1) 数据采集：使用 GoPro 相机拍摄视频，并通过逆编码确保线性数据恢复。2) 色彩空间转换：将输入图像转换为不同的色彩空间，包括线性、sRGB、GPLog 和 log RGB。3) NeRF 模型训练：在不同的色彩空间中训练 NeRF 模型。4) 渲染和损失计算：将每个网络输出转换为通用色彩空间，然后在该空间中进行渲染和损失计算。5) 评估：通过定量和定性评估比较不同色彩空间下 NeRF 模型的渲染质量。

**关键创新**：该论文最重要的技术创新点在于将 log RGB 色彩空间引入 NeRF 的训练过程中，并证明了其在提高渲染质量、增强鲁棒性以及在低光照条件下表现方面的优势。与现有方法相比，该方法关注了色彩空间对辐射场表示学习的影响，并提供了一种新的色彩空间选择策略。

**关键设计**：在实验中，作者使用了 GoPro 相机采集数据，并通过逆编码确保线性数据恢复。在色彩空间转换方面，作者实现了线性、sRGB、GPLog 和 log RGB 等多种色彩空间的转换。在 NeRF 模型训练方面，作者使用了标准的 NeRF 架构，并针对不同的色彩空间进行了相应的调整。在损失函数方面，作者使用了常用的 L2 损失函数。此外，作者还对不同网络大小和 NeRF 变体进行了实验，以验证 log 空间优势的泛化性和稳定性。

## 📊 实验亮点

实验结果表明，使用 log RGB 色彩空间训练的 NeRF 模型在渲染质量方面始终优于其他色彩空间，尤其是在低光照条件下表现更加出色。定量评估结果显示，log RGB 空间在 PSNR、SSIM 和 LPIPS 等指标上均取得了显著提升。此外，该方法在不同场景和不同网络大小下均表现出良好的鲁棒性和泛化性。

## 🎯 应用场景

该研究成果可应用于 novel view synthesis、3D 重建、虚拟现实、增强现实等领域。通过选择合适的色彩空间，可以提高渲染质量，增强场景的真实感和沉浸感。尤其是在低光照条件下，该方法能够显著提升渲染效果，具有重要的实际应用价值。未来，该研究可以进一步扩展到其他类型的场景和数据集，并与其他 NeRF 改进方法相结合，以实现更好的性能。

## 📄 摘要（原文）

> Neural Radiance Fields (NeRF) have achieved remarkable results in novel view synthesis, typically using sRGB images for supervision. However, little attention has been paid to the color space in which the network is learning the radiance field representation. Inspired by the BiIlluminant Dichromatic Reflection (BIDR) model, which suggests that a logarithmic transformation simplifies the separation of illumination and reflectance, we hypothesize that log RGB space enables NeRF to learn a more compact and effective representation of scene appearance. To test this, we captured approximately 30 videos using a GoPro camera, ensuring linear data recovery through inverse encoding. We trained NeRF models under various color space interpretations linear, sRGB, GPLog, and log RGB by converting each network output to a common color space before rendering and loss computation, enforcing representation learning in different color spaces. Quantitative and qualitative evaluations demonstrate that using a log RGB color space consistently improves rendering quality, exhibits greater robustness across scenes, and performs particularly well in low light conditions while using the same bit-depth input images. Further analysis across different network sizes and NeRF variants confirms the generalization and stability of the log space advantage.

