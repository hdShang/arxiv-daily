---
layout: default
title: DualGazeNet: A Biologically Inspired Dual-Gaze Query Network for Salient Object Detection
---

# DualGazeNet: A Biologically Inspired Dual-Gaze Query Network for Salient Object Detection

**arXiv**: [2511.18865v1](https://arxiv.org/abs/2511.18865) | [PDF](https://arxiv.org/pdf/2511.18865.pdf)

**作者**: Yu Zhang, Haoan Ping, Yuchen Li, Zhenshan Bing, Fuchun Sun, Alois Knoll

---

## 💡 一句话要点

**提出DualGazeNet以简化显著目标检测架构并提升性能**

**关键词**: `显著目标检测` `Transformer架构` `生物启发模型` `计算效率` `跨域泛化`

## 📋 核心要点

1. 核心问题：复杂SOD方法导致特征冗余和性能瓶颈
2. 方法要点：基于Transformer模拟人类视觉双通路处理机制
3. 实验或效果：在多个基准上超越25种方法，速度和效率显著提升

## 📄 摘要（原文）

> Recent salient object detection (SOD) methods aim to improve performance in four key directions: semantic enhancement, boundary refinement, auxiliary task supervision, and multi-modal fusion. In pursuit of continuous gains, these approaches have evolved toward increasingly sophisticated architectures with multi-stage pipelines, specialized fusion modules, edge-guided learning, and elaborate attention mechanisms. However, this complexity paradoxically introduces feature redundancy and cross-component interference that obscure salient cues, ultimately reaching performance bottlenecks. In contrast, human vision achieves efficient salient object identification without such architectural complexity. This contrast raises a fundamental question: can we design a biologically grounded yet architecturally simple SOD framework that dispenses with most of this engineering complexity, while achieving state-of-the-art accuracy, computational efficiency, and interpretability? In this work, we answer this question affirmatively by introducing DualGazeNet, a biologically inspired pure Transformer framework that models the dual biological principles of robust representation learning and magnocellular-parvocellular dual-pathway processing with cortical attention modulation in the human visual system. Extensive experiments on five RGB SOD benchmarks show that DualGazeNet consistently surpasses 25 state-of-the-art CNN- and Transformer-based methods. On average, DualGazeNet achieves about 60\% higher inference speed and 53.4\% fewer FLOPs than four Transformer-based baselines of similar capacity (VST++, MDSAM, Sam2unet, and BiRefNet). Moreover, DualGazeNet exhibits strong cross-domain generalization, achieving leading or highly competitive performance on camouflaged and underwater SOD benchmarks without relying on additional modalities.

