---
layout: default
title: Planning with Sketch-Guided Verification for Physics-Aware Video Generation
---

# Planning with Sketch-Guided Verification for Physics-Aware Video Generation

**arXiv**: [2511.17450v1](https://arxiv.org/abs/2511.17450) | [PDF](https://arxiv.org/pdf/2511.17450.pdf)

**作者**: Yidong Huang, Zun Wang, Han Lin, Dong-Ki Kim, Shayegan Omidshafiei, Jaehong Yoon, Yue Zhang, Mohit Bansal

---

## 💡 一句话要点

**提出SketchVerify框架，通过草图验证规划提升物理感知视频生成的动态一致性。**

**关键词**: `视频生成` `运动规划` `物理感知` `草图验证` `训练免费方法` `动态一致性`

## 📋 核心要点

1. 核心问题：现有视频生成方法依赖单次或迭代规划，导致运动简单或计算成本高。
2. 方法要点：训练免费，基于草图验证循环预测、排序候选运动计划，确保语义对齐与物理合理性。
3. 实验或效果：在基准测试中显著提升运动质量、物理真实性和长期一致性，且效率更高。

## 📄 摘要（原文）

> Recent video generation approaches increasingly rely on planning intermediate control signals such as object trajectories to improve temporal coherence and motion fidelity. However, these methods mostly employ single-shot plans that are typically limited to simple motions, or iterative refinement which requires multiple calls to the video generator, incuring high computational cost. To overcome these limitations, we propose SketchVerify, a training-free, sketch-verification-based planning framework that improves motion planning quality with more dynamically coherent trajectories (i.e., physically plausible and instruction-consistent motions) prior to full video generation by introducing a test-time sampling and verification loop. Given a prompt and a reference image, our method predicts multiple candidate motion plans and ranks them using a vision-language verifier that jointly evaluates semantic alignment with the instruction and physical plausibility. To efficiently score candidate motion plans, we render each trajectory as a lightweight video sketch by compositing objects over a static background, which bypasses the need for expensive, repeated diffusion-based synthesis while achieving comparable performance. We iteratively refine the motion plan until a satisfactory one is identified, which is then passed to the trajectory-conditioned generator for final synthesis. Experiments on WorldModelBench and PhyWorldBench demonstrate that our method significantly improves motion quality, physical realism, and long-term consistency compared to competitive baselines while being substantially more efficient. Our ablation study further shows that scaling up the number of trajectory candidates consistently enhances overall performance.

