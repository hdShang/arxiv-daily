---
layout: default
title: FREE: Uncertainty-Aware Autoregression for Parallel Diffusion Transformers
---

# FREE: Uncertainty-Aware Autoregression for Parallel Diffusion Transformers

**arXiv**: [2511.20390v1](https://arxiv.org/abs/2511.20390) | [PDF](https://arxiv.org/pdf/2511.20390.pdf)

**作者**: Xinwan Wen, Bowen Li, Jiajun Luo, Ye Li, Zhi Wang

---

## 💡 一句话要点

**提出FREE框架以加速扩散变换器推理，通过特征级自回归和不确定性引导松弛策略**

**关键词**: `扩散变换器` `并行采样` `特征自回归` `不确定性引导` `无损加速` `推理优化`

## 📋 核心要点

1. 扩散变换器推理延迟高，因长序列去噪轨迹和草稿准确性不足
2. FREE使用轻量级草稿器进行特征级自回归，结合并行验证实现无损加速
3. 实验在ImageNet-512²上，FREE加速1.86倍，FREE(relax)达2.25倍，保持生成质量

## 📄 摘要（原文）

> Diffusion Transformers (DiTs) achieve state-of-the-art generation quality but require long sequential denoising trajectories, leading to high inference latency. Recent speculative inference methods enable lossless parallel sampling in U-Net-based diffusion models via a drafter-verifier scheme, but their acceleration is limited on DiTs due to insufficient draft accuracy during verification. To address this limitation, we analyze the DiTs' feature dynamics and find the features of the final transformer layer (top-block) exhibit strong temporal consistency and rich semantic abstraction. Based on this insight, we propose FREE, a novel framework that employs a lightweight drafter to perform feature-level autoregression with parallel verification, guaranteeing lossless acceleration with theoretical and empirical support. Meanwhile, prediction variance (uncertainty) of DiTs naturally increases in later denoising steps, reducing acceptance rates under speculative sampling. To mitigate this effect, we further introduce an uncertainty-guided relaxation strategy, forming FREE (relax), which dynamically adjusts the acceptance probability in response to uncertainty levels. Experiments on ImageNet-$512^2$ show that FREE achieves up to $1.86 \times$ acceleration, and FREE (relax) further reaches $2.25 \times$ speedup while maintaining high perceptual and quantitative fidelity in generation quality.

