---
layout: default
title: MEIcoder: Decoding Visual Stimuli from Neural Activity by Leveraging Most Exciting Inputs
---

# MEIcoder: Decoding Visual Stimuli from Neural Activity by Leveraging Most Exciting Inputs

**arXiv**: [2510.20762v1](https://arxiv.org/abs/2510.20762) | [PDF](https://arxiv.org/pdf/2510.20762.pdf)

**作者**: Jan Sobotka, Luca Baroni, Ján Antolík

---

## 💡 一句话要点

**提出MEIcoder方法，利用最兴奋输入解码视觉刺激，解决小数据集下神经活动解码难题。**

**关键词**: `视觉刺激解码` `神经活动分析` `小数据集学习` `对抗训练` `结构相似性损失`

## 📋 核心要点

1. 核心问题：灵长类或人类神经数据稀缺，限制深度学习解码视觉刺激的应用。
2. 方法要点：结合最兴奋输入、结构相似性损失和对抗训练，提升解码性能。
3. 实验或效果：在V1区单细胞活动解码中表现优异，支持少量神经元和训练数据。

## 📄 摘要（原文）

> Decoding visual stimuli from neural population activity is crucial for
> understanding the brain and for applications in brain-machine interfaces.
> However, such biological data is often scarce, particularly in primates or
> humans, where high-throughput recording techniques, such as two-photon imaging,
> remain challenging or impossible to apply. This, in turn, poses a challenge for
> deep learning decoding techniques. To overcome this, we introduce MEIcoder, a
> biologically informed decoding method that leverages neuron-specific most
> exciting inputs (MEIs), a structural similarity index measure loss, and
> adversarial training. MEIcoder achieves state-of-the-art performance in
> reconstructing visual stimuli from single-cell activity in primary visual
> cortex (V1), especially excelling on small datasets with fewer recorded
> neurons. Using ablation studies, we demonstrate that MEIs are the main drivers
> of the performance, and in scaling experiments, we show that MEIcoder can
> reconstruct high-fidelity natural-looking images from as few as 1,000-2,500
> neurons and less than 1,000 training data points. We also propose a unified
> benchmark with over 160,000 samples to foster future research. Our results
> demonstrate the feasibility of reliable decoding in early visual system and
> provide practical insights for neuroscience and neuroengineering applications.

