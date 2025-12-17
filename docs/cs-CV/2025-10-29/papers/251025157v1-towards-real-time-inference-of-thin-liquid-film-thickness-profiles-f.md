---
layout: default
title: Towards Real-Time Inference of Thin Liquid Film Thickness Profiles from Interference Patterns Using Vision Transformers
---

# Towards Real-Time Inference of Thin Liquid Film Thickness Profiles from Interference Patterns Using Vision Transformers

**arXiv**: [2510.25157v1](https://arxiv.org/abs/2510.25157) | [PDF](https://arxiv.org/pdf/2510.25157.pdf)

**作者**: Gautam A. Viruthagiri, Arnuv Tandon, Gerald G. Fuller, Vinny Chandran Suja

---

## 💡 一句话要点

**提出基于视觉变换器的实时薄膜厚度推断方法，以解决眼科干涉图重建难题。**

**关键词**: `视觉变换器` `薄膜干涉测量` `实时推断` `厚度重建` `眼科应用` `相位解析`

## 📋 核心要点

1. 核心问题：干涉图重建为不适定逆问题，受相位周期性和噪声影响，传统方法计算密集或需专家分析。
2. 方法要点：使用视觉变换器模型，利用长程空间相关性解析相位模糊，从动态干涉图直接推断厚度。
3. 实验或效果：在合成和实验泪膜数据上训练，实现实时重建，优于传统方法，适用于干眼症诊断。

## 📄 摘要（原文）

> Thin film interferometry is a powerful technique for non-invasively measuring
> liquid film thickness with applications in ophthalmology, but its clinical
> translation is hindered by the challenges in reconstructing thickness profiles
> from interference patterns - an ill-posed inverse problem complicated by phase
> periodicity, imaging noise and ambient artifacts. Traditional reconstruction
> methods are either computationally intensive, sensitive to noise, or require
> manual expert analysis, which is impractical for real-time diagnostics. To
> address this challenge, here we present a vision transformer-based approach for
> real-time inference of thin liquid film thickness profiles directly from
> isolated interferograms. Trained on a hybrid dataset combining
> physiologically-relevant synthetic and experimental tear film data, our model
> leverages long-range spatial correlations to resolve phase ambiguities and
> reconstruct temporally coherent thickness profiles in a single forward pass
> from dynamic interferograms acquired in vivo and ex vivo. The network
> demonstrates state-of-the-art performance on noisy, rapidly-evolving films with
> motion artifacts, overcoming limitations of conventional phase-unwrapping and
> iterative fitting methods. Our data-driven approach enables automated,
> consistent thickness reconstruction at real-time speeds on consumer hardware,
> opening new possibilities for continuous monitoring of pre-lens ocular tear
> films and non-invasive diagnosis of conditions such as the dry eye disease.

