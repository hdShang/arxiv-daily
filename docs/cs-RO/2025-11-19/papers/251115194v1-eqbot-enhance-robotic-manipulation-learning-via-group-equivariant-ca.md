---
layout: default
title: Eq.Bot: Enhance Robotic Manipulation Learning via Group Equivariant Canonicalization
---

# Eq.Bot: Enhance Robotic Manipulation Learning via Group Equivariant Canonicalization

**arXiv**: [2511.15194v1](https://arxiv.org/abs/2511.15194) | [PDF](https://arxiv.org/pdf/2511.15194.pdf)

**作者**: Jian Deng, Yuandong Wang, Yangfu Zhu, Tao Feng, Tianyu Wo, Zhenzhou Shao

---

## 💡 一句话要点

**提出Eq.Bot框架以增强机器人操作学习中的空间等变性**

**关键词**: `机器人操作学习` `空间等变性` `SE(2)群理论` `规范化框架` `模型无关方法`

## 📋 核心要点

1. 现有机器人操作框架缺乏几何一致性保证，难以处理旋转和平移等空间变换
2. 基于SE(2)群等变理论，通过规范化空间转换实现模型无关的空间等变性
3. 实验显示在CNN和Transformer架构上优于现有方法，最高提升50.0%

## 📄 摘要（原文）

> Robotic manipulation systems are increasingly deployed across diverse domains. Yet existing multi-modal learning frameworks lack inherent guarantees of geometric consistency, struggling to handle spatial transformations such as rotations and translations. While recent works attempt to introduce equivariance through bespoke architectural modifications, these methods suffer from high implementation complexity, computational cost, and poor portability. Inspired by human cognitive processes in spatial reasoning, we propose Eq.Bot, a universal canonicalization framework grounded in SE(2) group equivariant theory for robotic manipulation learning. Our framework transforms observations into a canonical space, applies an existing policy, and maps the resulting actions back to the original space. As a model-agnostic solution, Eq.Bot aims to endow models with spatial equivariance without requiring architectural modifications. Extensive experiments demonstrate the superiority of Eq.Bot under both CNN-based (e.g., CLIPort) and Transformer-based (e.g., OpenVLA-OFT) architectures over existing methods on various robotic manipulation tasks, where the most significant improvement can reach 50.0%.

