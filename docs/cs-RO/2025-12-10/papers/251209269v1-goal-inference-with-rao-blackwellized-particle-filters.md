---
layout: default
title: Goal inference with Rao-Blackwellized Particle Filters
---

# Goal inference with Rao-Blackwellized Particle Filters

**arXiv**: [2512.09269v1](https://arxiv.org/abs/2512.09269) | [PDF](https://arxiv.org/pdf/2512.09269.pdf)

**作者**: Yixuan Wang, Dan P. Guralnik, Warren E. Dixon

---

## 💡 一句话要点

**提出基于Rao-Blackwellized粒子滤波的目标推断方法，用于从噪声轨迹中推断移动代理的最终目标。**

**关键词**: `目标推断` `Rao-Blackwellized粒子滤波` `信息论泄漏` `高斯混合模型` `轨迹分析`

## 📋 核心要点

1. 核心问题：从噪声观测中推断移动代理的最终目标，是基础估计问题。
2. 方法要点：利用Rao-Blackwellized粒子滤波，假设代理行为具有闭环稳定性，通过解析边缘化线性高斯子结构提高样本效率。
3. 实验或效果：实验显示对合规代理能快速准确恢复目标，并量化了推断性能和信息泄漏。

## 📄 摘要（原文）

> Inferring the eventual goal of a mobile agent from noisy observations of its trajectory is a fundamental estimation problem. We initiate the study of such intent inference using a variant of a Rao-Blackwellized Particle Filter (RBPF), subject to the assumption that the agent's intent manifests through closed-loop behavior with a state-of-the-art provable practical stability property. Leveraging the assumed closed-form agent dynamics, the RBPF analytically marginalizes the linear-Gaussian substructure and updates particle weights only, improving sample efficiency over a standard particle filter. Two difference estimators are introduced: a Gaussian mixture model using the RBPF weights and a reduced version confining the mixture to the effective sample. We quantify how well the adversary can recover the agent's intent using information-theoretic leakage metrics and provide computable lower bounds on the Kullback-Leibler (KL) divergence between the true intent distribution and RBPF estimates via Gaussian-mixture KL bounds. We also provide a bound on the difference in performance between the two estimators, highlighting the fact that the reduced estimator performs almost as well as the complete one. Experiments illustrate fast and accurate intent recovery for compliant agents, motivating future work on designing intent-obfuscating controllers.

