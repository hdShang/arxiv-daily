---
layout: default
title: Fix False Transparency by Noise Guided Splatting
---

# Fix False Transparency by Noise Guided Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15736" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15736v1</a>
  <a href="https://arxiv.org/pdf/2510.15736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15736v1" onclick="toggleFavorite(this, '2510.15736v1', 'Fix False Transparency by Noise Guided Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aly El Hakie, Yiren Lu, Yu Yin, Michael Jenkins, Yehe Liu

**分类**: cs.GR, cs.CV

**发布日期**: 2025-10-17

---

## 💡 一句话要点

**提出噪声引导Splatting，解决3DGS重建中虚假透明问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `虚假透明` `三维重建` `噪声引导` `视角一致性`

## 📋 核心要点

1. 3DGS重建不透明物体时，常出现虚假透明，导致视角不一致，原因是缺乏对表面不透明度的显式约束。
2. 论文提出噪声引导Splatting（NGS），通过注入噪声高斯来鼓励表面高斯采用更高的不透明度，解决虚假透明问题。
3. 实验表明，NGS在多个数据集上显著降低了虚假透明度，同时保持了标准渲染指标上的竞争力。

## 📝 摘要（中文）

基于3D高斯（3DGS）重建的不透明物体，在交互式观察中，经常出现虚假的透明表面，导致相机运动时背景和内部图案不一致。这个问题源于3DGS中不适定的优化。在训练期间，背景和前景高斯通过alpha合成混合，并仅使用光度损失针对输入RGB图像进行优化。由于该过程缺乏对表面不透明度的显式约束，因此优化可能会错误地将透明度分配给不透明区域，从而导致视角不一致和虚假透明。为了解决这个问题，论文提出了噪声引导Splatting（NGS），通过在训练期间在对象体积中注入不透明噪声高斯来鼓励表面高斯采用更高的不透明度，只需要对现有的splatting过程进行最小的修改。论文还提出了一种基于透射率的指标来定量评估静态渲染中的虚假透明度，并引入了一个定制的、高质量的以对象为中心的扫描数据集，该数据集表现出明显的透明度问题，并使用专门设计的填充噪声来增强流行的现有数据集，以评估3D重建方法对虚假透明度的鲁棒性。实验表明，NGS在多个数据集上显著降低了虚假透明度，同时保持了标准渲染指标上的竞争性能。

## 🔬 方法详解

**问题定义**：3D高斯溅射（3DGS）重建不透明物体时，由于优化过程中缺乏对表面不透明度的显式约束，容易出现虚假透明的现象。这种虚假透明会导致视角不一致，在交互式观察时表现为背景和内部图案的错误显示。现有方法主要关注视角一致性问题，但未明确识别和解决虚假透明这一特定问题。

**核心思路**：论文的核心思路是通过在训练过程中向物体体积中注入“噪声高斯”，这些噪声高斯具有较高的不透明度，从而引导优化过程，鼓励物体表面的高斯也具有较高的不透明度。这样可以有效地抑制虚假透明现象的产生。

**技术框架**：NGS方法在现有的3DGS训练框架基础上进行改进。主要流程包括：1) 初始化3D高斯；2) 在训练过程中，随机在物体体积内注入具有较高不透明度的噪声高斯；3) 使用光度损失函数优化所有高斯的参数（位置、形状、颜色、不透明度等）；4) 在渲染阶段，使用优化后的高斯进行splatting渲染。

**关键创新**：论文的关键创新在于明确识别并解决了3DGS中的虚假透明问题，并提出了通过注入噪声高斯来解决该问题的方法。与现有方法相比，NGS方法专门针对虚假透明问题进行了优化，而无需对现有的3DGS框架进行大幅修改。

**关键设计**：NGS的关键设计包括：1) 噪声高斯的初始化：噪声高斯的位置在物体体积内随机采样，不透明度设置为较高的值（例如0.9），颜色可以随机初始化或从周围高斯采样。2) 噪声高斯的注入频率：需要根据具体数据集和场景进行调整，以达到最佳效果。3) 损失函数：仍然使用标准的光度损失函数，但噪声高斯的引入会影响损失函数的梯度，从而引导优化过程。

## 📊 实验亮点

实验结果表明，NGS方法在多个数据集上显著降低了虚假透明度，同时保持了标准渲染指标上的竞争力。论文还提出了一个新的基于透射率的指标来定量评估虚假透明度，并构建了一个高质量的以对象为中心的扫描数据集，用于评估3D重建方法对虚假透明度的鲁棒性。这些数据集和评估指标为未来的研究提供了有价值的资源。

## 🎯 应用场景

该研究成果可应用于三维重建、虚拟现实、增强现实等领域。通过减少虚假透明现象，可以提高三维模型的真实感和视觉质量，改善用户在交互式观察中的体验。例如，在游戏开发中，可以利用该技术重建高质量的游戏场景和角色模型；在工业设计中，可以用于创建逼真的产品原型。

## 📄 摘要（原文）

> Opaque objects reconstructed by 3DGS often exhibit a falsely transparent surface, leading to inconsistent background and internal patterns under camera motion in interactive viewing. This issue stems from the ill-posed optimization in 3DGS. During training, background and foreground Gaussians are blended via alpha-compositing and optimized solely against the input RGB images using a photometric loss. As this process lacks an explicit constraint on surface opacity, the optimization may incorrectly assign transparency to opaque regions, resulting in view-inconsistent and falsely transparent. This issue is difficult to detect in standard evaluation settings but becomes particularly evident in object-centric reconstructions under interactive viewing. Although other causes of view-inconsistency have been explored recently, false transparency has not been explicitly identified. To the best of our knowledge, we are the first to identify, characterize, and develop solutions for this artifact, an underreported artifact in 3DGS. Our strategy, NGS, encourages surface Gaussians to adopt higher opacity by injecting opaque noise Gaussians in the object volume during training, requiring only minimal modifications to the existing splatting process. To quantitatively evaluate false transparency in static renderings, we propose a transmittance-based metric that measures the severity of this artifact. In addition, we introduce a customized, high-quality object-centric scan dataset exhibiting pronounced transparency issues, and we augment popular existing datasets with complementary infill noise specifically designed to assess the robustness of 3D reconstruction methods to false transparency. Experiments across multiple datasets show that NGS substantially reduces false transparency while maintaining competitive performance on standard rendering metrics, demonstrating its overall effectiveness.

