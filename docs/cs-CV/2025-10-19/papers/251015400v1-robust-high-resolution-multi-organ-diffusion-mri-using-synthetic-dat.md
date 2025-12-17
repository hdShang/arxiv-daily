---
layout: default
title: Robust High-Resolution Multi-Organ Diffusion MRI Using Synthetic-Data-Tuned Prompt Learning
---

# Robust High-Resolution Multi-Organ Diffusion MRI Using Synthetic-Data-Tuned Prompt Learning

**arXiv**: [2510.15400v1](https://arxiv.org/abs/2510.15400) | [PDF](https://arxiv.org/pdf/2510.15400.pdf)

**作者**: Chen Qian, Haoyu Zhang, Junnan Ma, Liuhong Zhu, Qingrui Cai, Yu Wang, Ruibo Song, Lv Li, Lin Mei, Xianwang Jiang, Qin Xu, Boyu Jiang, Ran Tao, Chunmiao Chen, Shufang Chen, Dongyun Liang, Qiu Guo, Jianzhong Lin, Taishan Kang, Mengtian Lu, Liyuan Fu, Ruibin Huang, Huijuan Wan, Xu Huang, Jianhua Wang, Di Guo, Hai Zhong, Jianjun Zhou, Xiaobo Qu

---

## 💡 一句话要点

**提出LoSP-Prompt框架以解决多器官扩散MRI中运动伪影问题**

**关键词**: `扩散加权成像` `运动伪影抑制` `提示学习` `多器官重建` `合成数据训练`

## 📋 核心要点

1. 核心问题：多器官扩散MRI受呼吸等运动伪影影响，限制临床应用。
2. 方法要点：结合局部平滑相位建模与合成数据驱动的提示学习进行重建。
3. 实验或效果：在临床图像中实现高分辨率，提升图像质量并泛化多器官。

## 📄 摘要（原文）

> Clinical adoption of multi-shot diffusion-weighted magnetic resonance imaging
> (multi-shot DWI) for body-wide tumor diagnostics is limited by severe
> motion-induced phase artifacts from respiration, peristalsis, and so on,
> compounded by multi-organ, multi-slice, multi-direction and multi-b-value
> complexities. Here, we introduce a reconstruction framework, LoSP-Prompt, that
> overcomes these challenges through physics-informed modeling and
> synthetic-data-driven prompt learning. We model inter-shot phase variations as
> a high-order Locally Smooth Phase (LoSP), integrated into a low-rank Hankel
> matrix reconstruction. Crucially, the algorithm's rank parameter is
> automatically set via prompt learning trained exclusively on synthetic
> abdominal DWI data emulating physiological motion. Validated across 10,000+
> clinical images (43 subjects, 4 scanner models, 5 centers), LoSP-Prompt: (1)
> Achieved twice the spatial resolution of clinical single-shot DWI, enhancing
> liver lesion conspicuity; (2) Generalized to seven diverse anatomical regions
> (liver, kidney, sacroiliac, pelvis, knee, spinal cord, brain) with a single
> model; (3) Outperformed state-of-the-art methods in image quality, artifact
> suppression, and noise reduction (11 radiologists' evaluations on a 5-point
> scale, $p<0.05$), achieving 4-5 points (excellent) on kidney DWI, 4 points
> (good to excellent) on liver, sacroiliac and spinal cord DWI, and 3-4 points
> (good) on knee and tumor brain. The approach eliminates navigator signals and
> realistic data supervision, providing an interpretable, robust solution for
> high-resolution multi-organ multi-shot DWI. Its scanner-agnostic performance
> signifies transformative potential for precision oncology.

