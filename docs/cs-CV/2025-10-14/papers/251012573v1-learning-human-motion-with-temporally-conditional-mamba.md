---
layout: default
title: Learning Human Motion with Temporally Conditional Mamba
---

# Learning Human Motion with Temporally Conditional Mamba

**arXiv**: [2510.12573v1](https://arxiv.org/abs/2510.12573) | [PDF](https://arxiv.org/pdf/2510.12573.pdf)

**作者**: Quang Nguyen, Tri Le, Baoru Huang, Minh Nhat Vu, Ngan Le, Thieu Vo, Anh Nguyen

---

## 💡 一句话要点

**提出Temporally Conditional Mamba以解决时间条件人类运动生成中的对齐问题**

**关键词**: `人类运动生成` `时间条件建模` `Mamba模型` `时间对齐` `运动估计`

## 📋 核心要点

1. 核心问题：现有方法依赖跨注意力机制，难以保持时间步对齐。
2. 方法要点：将条件信息集成到Mamba块的循环动态中，提升时间对齐。
3. 实验或效果：在多种任务中验证，显著改进对齐、真实性和条件一致性。

## 📄 摘要（原文）

> Learning human motion based on a time-dependent input signal presents a
> challenging yet impactful task with various applications. The goal of this task
> is to generate or estimate human movement that consistently reflects the
> temporal patterns of conditioning inputs. Existing methods typically rely on
> cross-attention mechanisms to fuse the condition with motion. However, this
> approach primarily captures global interactions and struggles to maintain
> step-by-step temporal alignment. To address this limitation, we introduce
> Temporally Conditional Mamba, a new mamba-based model for human motion
> generation. Our approach integrates conditional information into the recurrent
> dynamics of the Mamba block, enabling better temporally aligned motion. To
> validate the effectiveness of our method, we evaluate it on a variety of human
> motion tasks. Extensive experiments demonstrate that our model significantly
> improves temporal alignment, motion realism, and condition consistency over
> state-of-the-art approaches. Our project page is available at
> https://zquang2202.github.io/TCM.

