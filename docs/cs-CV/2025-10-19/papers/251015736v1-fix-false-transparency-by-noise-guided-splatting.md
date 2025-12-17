---
layout: default
title: Fix False Transparency by Noise Guided Splatting
---

# Fix False Transparency by Noise Guided Splatting

**arXiv**: [2510.15736v1](https://arxiv.org/abs/2510.15736) | [PDF](https://arxiv.org/pdf/2510.15736.pdf)

**作者**: Aly El Hakie, Yiren Lu, Yu Yin, Michael Jenkins, Yehe Liu

---

## 💡 一句话要点

**提出噪声引导溅射以解决3D高斯溅射中的虚假透明问题**

**关键词**: `3D高斯溅射` `虚假透明` `噪声引导优化` `表面不透明度` `交互式查看` `重建评估`

## 📋 核心要点

1. 核心问题：3D高斯溅射优化中缺乏表面不透明度约束，导致不透明物体出现虚假透明
2. 方法要点：通过注入不透明噪声高斯，鼓励表面高斯采用更高不透明度
3. 实验或效果：在多个数据集上显著减少虚假透明，保持标准渲染指标竞争力

## 📄 摘要（原文）

> Opaque objects reconstructed by 3DGS often exhibit a falsely transparent
> surface, leading to inconsistent background and internal patterns under camera
> motion in interactive viewing. This issue stems from the ill-posed optimization
> in 3DGS. During training, background and foreground Gaussians are blended via
> alpha-compositing and optimized solely against the input RGB images using a
> photometric loss. As this process lacks an explicit constraint on surface
> opacity, the optimization may incorrectly assign transparency to opaque
> regions, resulting in view-inconsistent and falsely transparent. This issue is
> difficult to detect in standard evaluation settings but becomes particularly
> evident in object-centric reconstructions under interactive viewing. Although
> other causes of view-inconsistency have been explored recently, false
> transparency has not been explicitly identified. To the best of our knowledge,
> we are the first to identify, characterize, and develop solutions for this
> artifact, an underreported artifact in 3DGS. Our strategy, NGS, encourages
> surface Gaussians to adopt higher opacity by injecting opaque noise Gaussians
> in the object volume during training, requiring only minimal modifications to
> the existing splatting process. To quantitatively evaluate false transparency
> in static renderings, we propose a transmittance-based metric that measures the
> severity of this artifact. In addition, we introduce a customized, high-quality
> object-centric scan dataset exhibiting pronounced transparency issues, and we
> augment popular existing datasets with complementary infill noise specifically
> designed to assess the robustness of 3D reconstruction methods to false
> transparency. Experiments across multiple datasets show that NGS substantially
> reduces false transparency while maintaining competitive performance on
> standard rendering metrics, demonstrating its overall effectiveness.

