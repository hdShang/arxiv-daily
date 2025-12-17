---
layout: default
title: EvoIR: Towards All-in-One Image Restoration via Evolutionary Frequency Modulation
---

# EvoIR: Towards All-in-One Image Restoration via Evolutionary Frequency Modulation

**arXiv**: [2512.05104v1](https://arxiv.org/abs/2512.05104) | [PDF](https://arxiv.org/pdf/2512.05104.pdf)

**作者**: Jiaqi Ma, Shengkai Hu, Jun Wan, Jiaxing Huang, Lefei Zhang, Salman Khan

---

## 💡 一句话要点

**提出EvoIR框架，通过进化频率调制解决全场景图像恢复中的异构退化问题。**

**关键词**: `全场景图像恢复` `频率调制` `进化优化` `异构退化` `结构保真度` `感知质量`

## 📋 核心要点

1. 核心问题：现有全场景图像恢复方法缺乏显式频率建模和自适应优化，限制跨异构退化的泛化能力。
2. 方法要点：引入频率调制模块显式分解高低频特征，结合进化优化策略动态调整目标以平衡结构准确性和感知保真度。
3. 实验或效果：在多个基准测试中优于现有先进方法，验证了框架的有效性和互补性。

## 📄 摘要（原文）

> All-in-One Image Restoration (AiOIR) tasks often involve diverse degradation that require robust and versatile strategies. However, most existing approaches typically lack explicit frequency modeling and rely on fixed or heuristic optimization schedules, which limit the generalization across heterogeneous degradation. To address these limitations, we propose EvoIR, an AiOIR-specific framework that introduces evolutionary frequency modulation for dynamic and adaptive image restoration. Specifically, EvoIR employs the Frequency-Modulated Module (FMM) that decomposes features into high- and low-frequency branches in an explicit manner and adaptively modulates them to enhance both structural fidelity and fine-grained details. Central to EvoIR, an Evolutionary Optimization Strategy (EOS) iteratively adjusts frequency-aware objectives through a population-based evolutionary process, dynamically balancing structural accuracy and perceptual fidelity. Its evolutionary guidance further mitigates gradient conflicts across degradation and accelerates convergence. By synergizing FMM and EOS, EvoIR yields greater improvements than using either component alone, underscoring their complementary roles. Extensive experiments on multiple benchmarks demonstrate that EvoIR outperforms state-of-the-art AiOIR methods.

