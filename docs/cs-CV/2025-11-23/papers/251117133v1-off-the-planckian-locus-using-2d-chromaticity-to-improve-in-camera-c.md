---
layout: default
title: Off the Planckian Locus: Using 2D Chromaticity to Improve In-Camera Color
---

# Off the Planckian Locus: Using 2D Chromaticity to Improve In-Camera Color

**arXiv**: [2511.17133v1](https://arxiv.org/abs/2511.17133) | [PDF](https://arxiv.org/pdf/2511.17133.pdf)

**作者**: SaiKiran Tedla, Joshua E. Little, Hakki Can Karaimer, Michael S. Brown

---

## 💡 一句话要点

**提出基于2D色度与MLP的色度映射方法，提升非普朗克光源下的色彩准确性**

**关键词**: `相机色彩映射` `2D色度空间` `多层感知机` `非普朗克光源` `LED照明` `实时部署`

## 📋 核心要点

1. 传统相机色彩映射依赖CCT插值，但LED光源偏离普朗克轨迹导致精度不足
2. 使用2D色度空间和轻量MLP替代CCT插值，增强非普朗克光源下的鲁棒性
3. 实验显示LED场景下角度再现误差平均降低22%，保持实时部署与向后兼容

## 📄 摘要（原文）

> Traditional in-camera colorimetric mapping relies on correlated color temperature (CCT)-based interpolation between pre-calibrated transforms optimized for Planckian illuminants such as CIE A and D65. However, modern lighting technologies such as LEDs can deviate substantially from the Planckian locus, exposing the limitations of relying on conventional one-dimensional CCT for illumination characterization. This paper demonstrates that transitioning from 1D CCT (on the Planckian locus) to a 2D chromaticity space (off the Planckian locus) improves colorimetric accuracy across various mapping approaches. In addition, we replace conventional CCT interpolation with a lightweight multi-layer perceptron (MLP) that leverages 2D chromaticity features for robust colorimetric mapping under non-Planckian illuminants. A lightbox-based calibration procedure incorporating representative LED sources is used to train our MLP. Validated across diverse LED lighting, our method reduces angular reproduction error by 22% on average in LED-lit scenes, maintains backward compatibility with traditional illuminants, accommodates multi-illuminant scenes, and supports real-time in-camera deployment with negligible additional computational cost.

