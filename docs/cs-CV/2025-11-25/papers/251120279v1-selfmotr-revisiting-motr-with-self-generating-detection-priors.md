---
layout: default
title: SelfMOTR: Revisiting MOTR with Self-Generating Detection Priors
---

# SelfMOTR: Revisiting MOTR with Self-Generating Detection Priors

**arXiv**: [2511.20279v1](https://arxiv.org/abs/2511.20279) | [PDF](https://arxiv.org/pdf/2511.20279.pdf)

**作者**: Fabian Gülhan, Emil Mededovic, Yuli Wu, Johannes Stegmaier

---

## 💡 一句话要点

**提出SelfMOTR，利用自生成检测先验解决端到端跟踪中检测与关联冲突问题**

**关键词**: `端到端跟踪` `检测先验` `自生成模型` `MOTR改进` `跟踪性能提升`

## 📋 核心要点

1. 端到端跟踪中检测性能差及检测与关联冲突是核心问题
2. 方法基于MOTR隐藏检测能力，自生成检测先验提升跟踪
3. 在DanceTrack上表现优异，与先进端到端方法竞争

## 📄 摘要（原文）

> Despite progress toward end-to-end tracking with transformer architectures, poor detection performance and the conflict between detection and association in a joint architecture remain critical concerns. Recent approaches aim to mitigate these issues by (i) employing advanced denoising or label assignment strategies, or (ii) incorporating detection priors from external object detectors via distillation or anchor proposal techniques. Inspired by the success of integrating detection priors and by the key insight that MOTR-like models are secretly strong detection models, we introduce SelfMOTR, a novel tracking transformer that relies on self-generated detection priors. Through extensive analysis and ablation studies, we uncover and demonstrate the hidden detection capabilities of MOTR-like models, and present a practical set of tools for leveraging them effectively. On DanceTrack, SelfMOTR achieves strong performance, competing with recent state-of-the-art end-to-end tracking methods.

