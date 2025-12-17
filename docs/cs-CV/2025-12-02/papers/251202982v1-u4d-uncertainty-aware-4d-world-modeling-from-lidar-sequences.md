---
layout: default
title: U4D: Uncertainty-Aware 4D World Modeling from LiDAR Sequences
---

# U4D: Uncertainty-Aware 4D World Modeling from LiDAR Sequences

**arXiv**: [2512.02982v1](https://arxiv.org/abs/2512.02982) | [PDF](https://arxiv.org/pdf/2512.02982.pdf)

**作者**: Xiang Xu, Ao Liang, Youquan Liu, Linfeng Li, Lingdong Kong, Ziwei Liu, Qingshan Liu

---

## 💡 一句话要点

**提出U4D框架，通过不确定性感知建模解决LiDAR序列4D世界生成中的几何失真与时间不一致问题。**

**关键词**: `4D世界建模` `不确定性感知` `LiDAR序列生成` `时空一致性` `扩散模型` `自动驾驶仿真`

## 📋 核心要点

1. 核心问题：现有方法均匀处理空间区域，忽略场景不确定性，导致复杂区域生成失真和时间稳定性不足。
2. 方法要点：基于预训练分割模型估计空间不确定性图，采用“难到易”两阶段生成，并引入时空混合块增强时间一致性。
3. 实验或效果：实验表明U4D能生成几何保真且时间一致的LiDAR序列，提升自动驾驶感知与仿真的可靠性。

## 📄 摘要（原文）

> Modeling dynamic 3D environments from LiDAR sequences is central to building reliable 4D worlds for autonomous driving and embodied AI. Existing generative frameworks, however, often treat all spatial regions uniformly, overlooking the varying uncertainty across real-world scenes. This uniform generation leads to artifacts in complex or ambiguous regions, limiting realism and temporal stability. In this work, we present U4D, an uncertainty-aware framework for 4D LiDAR world modeling. Our approach first estimates spatial uncertainty maps from a pretrained segmentation model to localize semantically challenging regions. It then performs generation in a "hard-to-easy" manner through two sequential stages: (1) uncertainty-region modeling, which reconstructs high-entropy regions with fine geometric fidelity, and (2) uncertainty-conditioned completion, which synthesizes the remaining areas under learned structural priors. To further ensure temporal coherence, U4D incorporates a mixture of spatio-temporal (MoST) block that adaptively fuses spatial and temporal representations during diffusion. Extensive experiments show that U4D produces geometrically faithful and temporally consistent LiDAR sequences, advancing the reliability of 4D world modeling for autonomous perception and simulation.

