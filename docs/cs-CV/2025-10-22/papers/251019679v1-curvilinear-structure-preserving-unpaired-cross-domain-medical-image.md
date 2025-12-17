---
layout: default
title: Curvilinear Structure-preserving Unpaired Cross-domain Medical Image Translation
---

# Curvilinear Structure-preserving Unpaired Cross-domain Medical Image Translation

**arXiv**: [2510.19679v1](https://arxiv.org/abs/2510.19679) | [PDF](https://arxiv.org/pdf/2510.19679.pdf)

**作者**: Zihao Chen, Yi Zhou, Xudong Jiang, Li Chen, Leopold Schmetterer, Bingyao Tan, Jun Cheng

---

## 💡 一句话要点

**提出CST框架以解决医学图像无配对翻译中细曲线结构失真问题**

**关键词**: `医学图像翻译` `曲线结构保留` `无配对学习` `拓扑监督` `跨域合成`

## 📋 核心要点

1. 现有方法在医学图像无配对翻译中易扭曲细曲线结构，影响诊断可靠性
2. CST通过集成曲线提取模块和拓扑监督，增强结构一致性
3. 在多种成像模态实验中，CST提升翻译保真度并达到先进性能

## 📄 摘要（原文）

> Unpaired image-to-image translation has emerged as a crucial technique in
> medical imaging, enabling cross-modality synthesis, domain adaptation, and data
> augmentation without costly paired datasets. Yet, existing approaches often
> distort fine curvilinear structures, such as microvasculature, undermining both
> diagnostic reliability and quantitative analysis. This limitation is
> consequential in ophthalmic and vascular imaging, where subtle morphological
> changes carry significant clinical meaning. We propose Curvilinear
> Structure-preserving Translation (CST), a general framework that explicitly
> preserves fine curvilinear structures during unpaired translation by
> integrating structure consistency into the training. Specifically, CST augments
> baseline models with a curvilinear extraction module for topological
> supervision. It can be seamlessly incorporated into existing methods. We
> integrate it into CycleGAN and UNSB as two representative backbones.
> Comprehensive evaluation across three imaging modalities: optical coherence
> tomography angiography, color fundus and X-ray coronary angiography
> demonstrates that CST improves translation fidelity and achieves
> state-of-the-art performance. By reinforcing geometric integrity in learned
> mappings, CST establishes a principled pathway toward curvilinear
> structure-aware cross-domain translation in medical imaging.

