---
layout: default
title: VLA-0: Building State-of-the-Art VLAs with Zero Modification
---

# VLA-0: Building State-of-the-Art VLAs with Zero Modification

**arXiv**: [2510.13054v1](https://arxiv.org/abs/2510.13054) | [PDF](https://arxiv.org/pdf/2510.13054.pdf)

**作者**: Ankit Goyal, Hugo Hadfield, Xuning Yang, Valts Blukis, Fabio Ramos

---

## 💡 一句话要点

**提出VLA-0方法，以文本表示动作构建高性能视觉语言动作模型。**

**关键词**: `视觉语言动作模型` `文本动作表示` `机器人操作` `模型构建方法` `基准测试`

## 📋 核心要点

1. 核心问题：视觉语言动作模型构建方法复杂，简单文本动作表示未被充分探索。
2. 方法要点：直接使用文本表示动作，无需修改视觉语言模型词汇或添加特殊头。
3. 实验效果：在LIBERO基准上超越现有方法，并在真实世界表现优异。

## 📄 摘要（原文）

> Vision-Language-Action models (VLAs) hold immense promise for enabling
> generalist robot manipulation. However, the best way to build them remains an
> open question. Current approaches often add complexity, such as modifying the
> existing vocabulary of a Vision-Language Model (VLM) with action tokens or
> introducing special action heads. Curiously, the simplest strategy of
> representing actions directly as text has remained largely unexplored. This
> work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only
> effective; it is surprisingly powerful. With the right design, VLA-0
> outperforms more involved models. On LIBERO, a popular benchmark for evaluating
> VLAs, VLA-0 outperforms all existing methods trained on the same robotic data,
> including $\pi_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without
> large-scale robotics-specific training, it outperforms methods trained on
> large-scale robotic data, like $\pi_0.5$-KI, $\pi_0$, GR00T-N1 and MolmoAct.
> These findings also translate to the real world, where VLA-0 outperforms
> SmolVLA, a VLA model pre-trained on large-scale real data. This paper
> summarizes our unexpected findings and spells out the specific techniques
> required to unlock the high performance of this simple yet potent VLA design.
> Visual results, code, and trained models are provided here:
> https://vla0.github.io/.

