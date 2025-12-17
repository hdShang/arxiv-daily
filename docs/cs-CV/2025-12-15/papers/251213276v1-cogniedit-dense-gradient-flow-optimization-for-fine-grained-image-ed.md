---
layout: default
title: CogniEdit: Dense Gradient Flow Optimization for Fine-Grained Image Editing
---

# CogniEdit: Dense Gradient Flow Optimization for Fine-Grained Image Editing

**arXiv**: [2512.13276v1](https://arxiv.org/abs/2512.13276) | [PDF](https://arxiv.org/pdf/2512.13276.pdf)

**作者**: Yan Li, Lin Liu, Xiaopeng Zhang, Wei Xue, Wenhan Luo, Yike Guo, Qi Tian

---

## 💡 一句话要点

**提出CogniEdit框架，通过密集梯度流优化解决扩散模型在细粒度图像编辑中的指令遵循问题**

**关键词**: `细粒度图像编辑` `扩散模型` `梯度流优化` `多模态推理` `指令遵循`

## 📋 核心要点

1. 现有方法在遵循细粒度指令（如颜色、位置）时存在稀疏反馈限制轨迹级控制的问题
2. CogniEdit结合多模态推理与密集奖励优化，在去噪步骤间传播梯度以实现轨迹级监督
3. 实验表明CogniEdit在基准数据集上实现了细粒度指令遵循与视觉质量、可编辑性保持的平衡

## 📄 摘要（原文）

> Instruction-based image editing with diffusion models has achieved impressive results, yet existing methods strug- gle with fine-grained instructions specifying precise attributes such as colors, positions, and quantities. While recent approaches employ Group Relative Policy Optimization (GRPO) for alignment, they optimize only at individual sampling steps, providing sparse feedback that limits trajectory-level control. We propose a unified framework CogniEdit, combining multi-modal reasoning with dense reward optimization that propagates gradients across con- secutive denoising steps, enabling trajectory-level gradient flow through the sampling process. Our method comprises three components: (1) Multi-modal Large Language Models for decomposing complex instructions into actionable directives, (2) Dynamic Token Focus Relocation that adaptively emphasizes fine-grained attributes, and (3) Dense GRPO-based optimization that propagates gradients across consecutive steps for trajectory-level supervision. Extensive experiments on benchmark datasets demonstrate that our CogniEdit achieves state-of-the-art performance in balancing fine-grained instruction following with visual quality and editability preservation

