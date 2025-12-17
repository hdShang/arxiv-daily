---
layout: default
title: Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers
---

# Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers

**arXiv**: [2511.17209v1](https://arxiv.org/abs/2511.17209) | [PDF](https://arxiv.org/pdf/2511.17209.pdf)

**作者**: Cris Claessens, Christiaan Viviers, Giacomo D'Amicantonio, Egor Bondarev, Fons van der Sommen

---

## 💡 一句话要点

**提出SPECTRE基础模型，通过自监督与跨模态预训练解决体积CT表示学习挑战**

**关键词**: `体积CT表示学习` `自监督预训练` `跨模态对齐` `3D视觉Transformer` `医学影像基础模型`

## 📋 核心要点

1. 核心问题：体积CT存在令牌扩展、几何各向异性及弱监督，标准Transformer方法不适用
2. 方法要点：联合优化局部和全局Transformer，结合DINO自蒸馏与SigLIP跨模态对齐
3. 实验或效果：在多个CT基准测试中，零样本和微调设置下均优于先前模型

## 📄 摘要（原文）

> We introduce SPECTRE, a fully transformer-based foundation model for volumetric computed tomography (CT). Our Self-Supervised & Cross-Modal Pretraining for CT Representation Extraction (SPECTRE) approach utilizes scalable 3D Vision Transformer architectures and modern self-supervised and vision-language pretraining strategies to learn general-purpose CT representations. Volumetric CT poses unique challenges, such as extreme token scaling, geometric anisotropy, and weak or noisy clinical supervision, that make standard transformer and contrastive learning recipes ineffective out of the box. The framework jointly optimizes a local transformer for high-resolution volumetric feature extraction and a global transformer for whole-scan context modeling, making large-scale 3D attention computationally tractable. Notably, SPECTRE is trained exclusively on openly available CT datasets, demonstrating that high-performing, generalizable representations can be achieved without relying on private data. Pretraining combines DINO-style self-distillation with SigLIP-based vision-language alignment using paired radiology reports, yielding features that are both geometrically consistent and clinically meaningful. Across multiple CT benchmarks, SPECTRE consistently outperforms prior CT foundation models in both zero-shot and fine-tuned settings, establishing SPECTRE as a scalable, open, and fully transformer-based foundation model for 3D medical imaging.

