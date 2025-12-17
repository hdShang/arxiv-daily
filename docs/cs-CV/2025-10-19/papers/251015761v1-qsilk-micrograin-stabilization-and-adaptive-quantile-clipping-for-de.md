---
layout: default
title: QSilk: Micrograin Stabilization and Adaptive Quantile Clipping for Detail-Friendly Latent Diffusion
---

# QSilk: Micrograin Stabilization and Adaptive Quantile Clipping for Detail-Friendly Latent Diffusion

**arXiv**: [2510.15761v1](https://arxiv.org/abs/2510.15761) | [PDF](https://arxiv.org/pdf/2510.15761.pdf)

**作者**: Denis Rychkovskiy

---

## 💡 一句话要点

**提出QSilk稳定层以提升潜在扩散模型的高频保真度并抑制激活尖峰**

**关键词**: `潜在扩散模型` `图像稳定` `高频保真` `自适应裁剪` `无训练优化`

## 📋 核心要点

1. 核心问题：潜在扩散模型在高频细节保真和抑制罕见激活尖峰方面存在不足
2. 方法要点：结合微粒度钳位和自适应分位数裁剪，无需训练即可稳定输出
3. 实验或效果：在SD/SDXL上实现更清晰结果，低步数和高分辨率下开销可忽略

## 📄 摘要（原文）

> We present QSilk, a lightweight, always-on stabilization layer for latent
> diffusion that improves high-frequency fidelity while suppressing rare
> activation spikes. QSilk combines (i) a per-sample micro clamp that gently
> limits extreme values without washing out texture, and (ii) Adaptive Quantile
> Clip (AQClip), which adapts the allowed value corridor per region. AQClip can
> operate in a proxy mode using local structure statistics or in an attention
> entropy guided mode (model confidence). Integrated into the CADE 2.5 rendering
> pipeline, QSilk yields cleaner, sharper results at low step counts and
> ultra-high resolutions with negligible overhead. It requires no training or
> fine-tuning and exposes minimal user controls. We report consistent qualitative
> improvements across SD/SDXL backbones and show synergy with CFG/Rescale,
> enabling slightly higher guidance without artifacts.

