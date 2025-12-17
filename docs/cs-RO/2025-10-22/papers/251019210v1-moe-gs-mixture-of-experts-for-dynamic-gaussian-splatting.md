---
layout: default
title: MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting
---

# MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting

**arXiv**: [2510.19210v1](https://arxiv.org/abs/2510.19210) | [PDF](https://arxiv.org/pdf/2510.19210.pdf)

**作者**: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong

---

## 💡 一句话要点

**提出MoE-GS框架以解决动态场景重建中性能不一致问题**

**关键词**: `动态场景重建` `高斯泼溅` `专家混合` `体积感知路由` `模型蒸馏` `渲染效率`

## 📋 核心要点

1. 动态场景重建中现有方法性能不一致，缺乏统一处理动态挑战的方案
2. 集成多个专家模型，通过体积感知像素路由器自适应混合输出
3. 实验显示在N3V和Technicolor数据集上优于现有方法，效率提升

## 📄 摘要（原文）

> Recent advances in dynamic scene reconstruction have significantly benefited
> from 3D Gaussian Splatting, yet existing methods show inconsistent performance
> across diverse scenes, indicating no single approach effectively handles all
> dynamic challenges. To overcome these limitations, we propose Mixture of
> Experts for Dynamic Gaussian Splatting (MoE-GS), a unified framework
> integrating multiple specialized experts via a novel Volume-aware Pixel Router.
> Our router adaptively blends expert outputs by projecting volumetric
> Gaussian-level weights into pixel space through differentiable weight
> splatting, ensuring spatially and temporally coherent results. Although MoE-GS
> improves rendering quality, the increased model capacity and reduced FPS are
> inherent to the MoE architecture. To mitigate this, we explore two
> complementary directions: (1) single-pass multi-expert rendering and gate-aware
> Gaussian pruning, which improve efficiency within the MoE framework, and (2) a
> distillation strategy that transfers MoE performance to individual experts,
> enabling lightweight deployment without architectural changes. To the best of
> our knowledge, MoE-GS is the first approach incorporating Mixture-of-Experts
> techniques into dynamic Gaussian splatting. Extensive experiments on the N3V
> and Technicolor datasets demonstrate that MoE-GS consistently outperforms
> state-of-the-art methods with improved efficiency. Video demonstrations are
> available at https://anonymous.4open.science/w/MoE-GS-68BA/.

