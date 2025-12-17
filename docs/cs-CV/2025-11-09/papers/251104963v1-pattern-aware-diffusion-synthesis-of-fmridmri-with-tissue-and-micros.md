---
layout: default
title: Pattern-Aware Diffusion Synthesis of fMRI/dMRI with Tissue and Microstructural Refinement
---

# Pattern-Aware Diffusion Synthesis of fMRI/dMRI with Tissue and Microstructural Refinement

**arXiv**: [2511.04963v1](https://arxiv.org/abs/2511.04963) | [PDF](https://arxiv.org/pdf/2511.04963.pdf)

**作者**: Xiongri Shen, Jiaqi Wang, Yi Zhong, Zhenxi Song, Leilei Zhao, Yichen Wei, Lingyan Liang, Shuqiang Wang, Baiying Lei, Demao Deng, Zhiguo Zhang

---

## 💡 一句话要点

**提出PDS方法以解决fMRI和dMRI模态缺失问题，通过模式感知扩散框架提升合成质量。**

**关键词**: `fMRI合成` `dMRI合成` `扩散模型` `模式感知` `组织细化` `微结构细化`

## 📋 核心要点

1. 核心问题：fMRI和dMRI模态缺失，且信号差异大，现有方法难以有效合成。
2. 方法要点：引入模式感知双模态3D扩散框架和组织与微结构细化网络。
3. 实验或效果：在多个数据集上PSNR/SSIM指标领先，临床诊断准确率达67.92%。

## 📄 摘要（原文）

> Magnetic resonance imaging (MRI), especially functional MRI (fMRI) and
> diffusion MRI (dMRI), is essential for studying neurodegenerative diseases.
> However, missing modalities pose a major barrier to their clinical use.
> Although GAN- and diffusion model-based approaches have shown some promise in
> modality completion, they remain limited in fMRI-dMRI synthesis due to (1)
> significant BOLD vs. diffusion-weighted signal differences between fMRI and
> dMRI in time/gradient axis, and (2) inadequate integration of disease-related
> neuroanatomical patterns during generation. To address these challenges, we
> propose PDS, introducing two key innovations: (1) a pattern-aware dual-modal 3D
> diffusion framework for cross-modality learning, and (2) a tissue refinement
> network integrated with a efficient microstructure refinement to maintain
> structural fidelity and fine details. Evaluated on OASIS-3, ADNI, and in-house
> datasets, our method achieves state-of-the-art results, with PSNR/SSIM scores
> of 29.83 dB/90.84\% for fMRI synthesis (+1.54 dB/+4.12\% over baselines) and
> 30.00 dB/77.55\% for dMRI synthesis (+1.02 dB/+2.2\%). In clinical validation,
> the synthesized data show strong diagnostic performance, achieving
> 67.92\%/66.02\%/64.15\% accuracy (NC vs. MCI vs. AD) in hybrid real-synthetic
> experiments. Code is available in \href{https://github.com/SXR3015/PDS}{PDS
> GitHub Repository}

