---
layout: default
title: Evaluating Dataset Watermarking for Fine-tuning Traceability of Customized Diffusion Models: A Comprehensive Benchmark and Removal Approach
---

# Evaluating Dataset Watermarking for Fine-tuning Traceability of Customized Diffusion Models: A Comprehensive Benchmark and Removal Approach

**arXiv**: [2511.19316v1](https://arxiv.org/abs/2511.19316) | [PDF](https://arxiv.org/pdf/2511.19316.pdf)

**作者**: Xincheng Wang, Hanchi Sun, Wenjun Sun, Kejun Xue, Wangqiu Zhou, Jianbo Zhang, Wei Sun, Dandan Zhu, Xiongkuo Min, Jun Jia, Zhijun Fang

---

## 💡 一句话要点

**提出数据集水印评估框架与移除方法以解决定制扩散模型微调溯源问题**

**关键词**: `数据集水印` `扩散模型` `微调溯源` `评估框架` `水印移除` `版权保护`

## 📋 核心要点

1. 核心问题：扩散模型微调可复制特定图像集，但带来版权和安全风险，缺乏统一水印评估标准。
2. 方法要点：建立通用威胁模型和评估框架，涵盖通用性、可传递性和鲁棒性指标。
3. 实验或效果：现有方法在通用性和可传递性表现良好，但对真实威胁鲁棒性不足，提出有效移除方法。

## 📄 摘要（原文）

> Recent fine-tuning techniques for diffusion models enable them to reproduce specific image sets, such as particular faces or artistic styles, but also introduce copyright and security risks. Dataset watermarking has been proposed to ensure traceability by embedding imperceptible watermarks into training images, which remain detectable in outputs even after fine-tuning. However, current methods lack a unified evaluation framework. To address this, this paper establishes a general threat model and introduces a comprehensive evaluation framework encompassing Universality, Transmissibility, and Robustness. Experiments show that existing methods perform well in universality and transmissibility, and exhibit some robustness against common image processing operations, yet still fall short under real-world threat scenarios. To reveal these vulnerabilities, the paper further proposes a practical watermark removal method that fully eliminates dataset watermarks without affecting fine-tuning, highlighting a key challenge for future research.

