---
layout: default
title: GLYPH-SR: Can We Achieve Both High-Quality Image Super-Resolution and High-Fidelity Text Recovery via VLM-guided Latent Diffusion Model?
---

# GLYPH-SR: Can We Achieve Both High-Quality Image Super-Resolution and High-Fidelity Text Recovery via VLM-guided Latent Diffusion Model?

**arXiv**: [2510.26339v1](https://arxiv.org/abs/2510.26339) | [PDF](https://arxiv.org/pdf/2510.26339.pdf)

**作者**: Mingyu Sung, Seungjae Ham, Kangwoo Kim, Yeokyoung Yoon, Sangseok Yun, Il-Min Kim, Jae-Mo Kang

---

## 💡 一句话要点

**提出GLYPH-SR，通过VLM引导的潜在扩散模型实现高质量图像超分与高保真文本恢复。**

**关键词**: `图像超分辨率` `场景文本恢复` `潜在扩散模型` `视觉语言模型` `OCR引导` `融合控制网络`

## 📋 核心要点

1. 核心问题：现有超分方法对场景文本恢复不敏感，导致OCR失败。
2. 方法要点：使用文本-场景融合ControlNet和乒乓调度器，结合OCR数据引导。
3. 实验效果：在多个数据集上显著提升OCR F1分数，同时保持感知质量。

## 📄 摘要（原文）

> Image super-resolution(SR) is fundamental to many vision system-from
> surveillance and autonomy to document analysis and retail analytics-because
> recovering high-frequency details, especially scene-text, enables reliable
> downstream perception. Scene-text, i.e., text embedded in natural images such
> as signs, product labels, and storefronts, often carries the most actionable
> information; when characters are blurred or hallucinated, optical character
> recognition(OCR) and subsequent decisions fail even if the rest of the image
> appears sharp. Yet previous SR research has often been tuned to distortion
> (PSNR/SSIM) or learned perceptual metrics (LIPIS, MANIQA, CLIP-IQA, MUSIQ) that
> are largely insensitive to character-level errors. Furthermore, studies that do
> address text SR often focus on simplified benchmarks with isolated characters,
> overlooking the challenges of text within complex natural scenes. As a result,
> scene-text is effectively treated as generic texture. For SR to be effective in
> practical deployments, it is therefore essential to explicitly optimize for
> both text legibility and perceptual quality. We present GLYPH-SR, a
> vision-language-guided diffusion framework that aims to achieve both objectives
> jointly. GLYPH-SR utilizes a Text-SR Fusion ControlNet(TS-ControlNet) guided by
> OCR data, and a ping-pong scheduler that alternates between text- and
> scene-centric guidance. To enable targeted text restoration, we train these
> components on a synthetic corpus while keeping the main SR branch frozen.
> Across SVT, SCUT-CTW1500, and CUTE80 at x4, and x8, GLYPH-SR improves OCR F1 by
> up to +15.18 percentage points over diffusion/GAN baseline (SVT x8, OpenOCR)
> while maintaining competitive MANIQA, CLIP-IQA, and MUSIQ. GLYPH-SR is designed
> to satisfy both objectives simultaneously-high readability and high visual
> realism-delivering SR that looks right and reds right.

