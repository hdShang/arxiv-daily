---
layout: default
title: SCAIL: Towards Studio-Grade Character Animation via In-Context Learning of 3D-Consistent Pose Representations
---

# SCAIL: Towards Studio-Grade Character Animation via In-Context Learning of 3D-Consistent Pose Representations

**arXiv**: [2512.05905v1](https://arxiv.org/abs/2512.05905) | [PDF](https://arxiv.org/pdf/2512.05905.pdf)

**作者**: Wenhao Yan, Sheng Ye, Zhuoyi Yang, Jiayan Teng, ZhenHui Dong, Kairui Wen, Xiaotao Gu, Yong-Jin Liu, Jie Tang

---

## 💡 一句话要点

**提出SCAIL框架，通过上下文学习3D一致姿态表示以实现工作室级角色动画**

**关键词**: `角色动画` `3D姿态表示` `上下文学习` `扩散变换器` `时空一致性` `工作室级动画`

## 📋 核心要点

1. 现有方法在复杂运动和跨身份动画中难以保持结构保真度和时间一致性
2. 引入3D姿态表示和全上下文姿态注入机制，提升运动信号的鲁棒性和时空推理能力
3. 实验表明SCAIL在系统评估中达到先进性能，推动动画向工作室级可靠性和真实感发展

## 📄 摘要（原文）

> Achieving character animation that meets studio-grade production standards remains challenging despite recent progress. Existing approaches can transfer motion from a driving video to a reference image, but often fail to preserve structural fidelity and temporal consistency in wild scenarios involving complex motion and cross-identity animations. In this work, we present \textbf{SCAIL} (\textbf{S}tudio-grade \textbf{C}haracter \textbf{A}nimation via \textbf{I}n-context \textbf{L}earning), a framework designed to address these challenges from two key innovations. First, we propose a novel 3D pose representation, providing a more robust and flexible motion signal. Second, we introduce a full-context pose injection mechanism within a diffusion-transformer architecture, enabling effective spatio-temporal reasoning over full motion sequences. To align with studio-level requirements, we develop a curated data pipeline ensuring both diversity and quality, and establish a comprehensive benchmark for systematic evaluation. Experiments show that \textbf{SCAIL} achieves state-of-the-art performance and advances character animation toward studio-grade reliability and realism.

