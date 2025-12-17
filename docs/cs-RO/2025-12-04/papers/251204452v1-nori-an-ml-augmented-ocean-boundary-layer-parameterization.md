---
layout: default
title: NORi: An ML-Augmented Ocean Boundary Layer Parameterization
---

# NORi: An ML-Augmented Ocean Boundary Layer Parameterization

**arXiv**: [2512.04452v1](https://arxiv.org/abs/2512.04452) | [PDF](https://arxiv.org/pdf/2512.04452.pdf)

**作者**: Xin Kai Lee, Ali Ramadhan, Andre Souza, Gregory LeClaire Wagner, Simone Silvestri, John Marshall, Raffaele Ferrari

---

## 💡 一句话要点

**提出NORi以增强海洋边界层湍流参数化，结合物理模型与神经网络提升气候模型性能。**

**关键词**: `海洋边界层参数化` `神经网络增强` `物理引导机器学习` `气候模型` `数值稳定性` `夹带模拟`

## 📋 核心要点

1. 核心问题：传统局部扩散闭合无法准确模拟海洋边界层底部的夹带过程。
2. 方法要点：基于Richardson数的物理参数化，通过NODEs训练捕获夹带，采用后验校准减少噪声影响。
3. 实验或效果：在多种海洋条件下表现优异，数值稳定，可长期模拟，减少数据需求并优化推理性能。

## 📄 摘要（原文）

> NORi is a machine-learned (ML) parameterization of ocean boundary layer turbulence that is physics-based and augmented with neural networks. NORi stands for neural ordinary differential equations (NODEs) Richardson number (Ri) closure. The physical parameterization is controlled by a Richardson number-dependent diffusivity and viscosity. The NODEs are trained to capture the entrainment through the base of the boundary layer, which cannot be represented with a local diffusive closure. The parameterization is trained using large-eddy simulations in an "a posteriori" fashion, where parameters are calibrated with a loss function that explicitly depends on the actual time-integrated variables of interest rather than the instantaneous subgrid fluxes, which are inherently noisy. NORi is designed for the realistic nonlinear equation of state of seawater and demonstrates excellent prediction and generalization capabilities in capturing entrainment dynamics under different convective strengths, oceanic background stratifications, rotation strengths, and surface wind forcings. NORi is numerically stable for at least 100 years of integration time in large-scale simulations, despite only being trained on 2-day horizons, and can be run with time steps as long as one hour. The highly expressive neural networks, combined with a physically-rigorous base closure, prove to be a robust paradigm for designing parameterizations for climate models where data requirements are drastically reduced, inference performance can be directly targeted and optimized, and numerical stability is implicitly encouraged during training.

