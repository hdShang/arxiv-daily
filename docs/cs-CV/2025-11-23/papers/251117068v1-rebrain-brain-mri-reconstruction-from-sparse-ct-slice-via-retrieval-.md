---
layout: default
title: ReBrain: Brain MRI Reconstruction from Sparse CT Slice via Retrieval-Augmented Diffusion
---

# ReBrain: Brain MRI Reconstruction from Sparse CT Slice via Retrieval-Augmented Diffusion

**arXiv**: [2511.17068v1](https://arxiv.org/abs/2511.17068) | [PDF](https://arxiv.org/pdf/2511.17068.pdf)

**作者**: Junming Liu, Yifei Sun, Weihua Cheng, Yujin Kang, Yirong Chen, Ding Wang, Guosun Zeng

---

## 💡 一句话要点

**提出ReBrain框架，通过检索增强扩散从稀疏CT重建脑MRI**

**关键词**: `脑MRI重建` `跨模态合成` `扩散模型` `检索增强` `稀疏CT` `ControlNet`

## 📋 核心要点

1. 核心问题：稀疏CT体积导致脑MRI重建困难，影响疾病诊断。
2. 方法要点：使用BBDM合成MRI，结合检索CT通过ControlNet引导生成。
3. 实验或效果：在SynthRAD2023和BraTS数据集上实现先进性能。

## 📄 摘要（原文）

> Magnetic Resonance Imaging (MRI) plays a crucial role in brain disease diagnosis, but it is not always feasible for certain patients due to physical or clinical constraints. Recent studies attempt to synthesize MRI from Computed Tomography (CT) scans; however, low-dose protocols often result in highly sparse CT volumes with poor through-plane resolution, making accurate reconstruction of the full brain MRI volume particularly challenging. To address this, we propose ReBrain, a retrieval-augmented diffusion framework for brain MRI reconstruction. Given any 3D CT scan with limited slices, we first employ a Brownian Bridge Diffusion Model (BBDM) to synthesize MRI slices along the 2D dimension. Simultaneously, we retrieve structurally and pathologically similar CT slices from a comprehensive prior database via a fine-tuned retrieval model. These retrieved slices are used as references, incorporated through a ControlNet branch to guide the generation of intermediate MRI slices and ensure structural continuity. We further account for rare retrieval failures when the database lacks suitable references and apply spherical linear interpolation to provide supplementary guidance. Extensive experiments on SynthRAD2023 and BraTS demonstrate that ReBrain achieves state-of-the-art performance in cross-modal reconstruction under sparse conditions.

