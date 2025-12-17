---
layout: default
title: Towards Unified Co-Speech Gesture Generation via Hierarchical Implicit Periodicity Learning
---

# Towards Unified Co-Speech Gesture Generation via Hierarchical Implicit Periodicity Learning

**arXiv**: [2512.13131v1](https://arxiv.org/abs/2512.13131) | [PDF](https://arxiv.org/pdf/2512.13131.pdf)

**作者**: Xin Guo, Yifan Zhao, Jia Li

---

## 💡 一句话要点

**提出分层隐式周期性学习以统一生成语音驱动的3D手势，解决运动单元间协调性问题。**

**关键词**: `语音驱动手势生成` `分层隐式周期性学习` `3D运动生成` `周期性自编码器` `多模态协调`

## 📋 核心要点

1. 核心问题：现有端到端方法难以建模头、身体和手部运动单元间的内在关联，导致不自然运动。
2. 方法要点：通过周期性自编码器探索手势运动相位流形，结合级联引导建模分层关系，增强多样性和协调性。
3. 实验或效果：在3D虚拟人上验证，定量和定性评估均优于当前最优方法，代码和模型将公开。

## 📄 摘要（原文）

> Generating 3D-based body movements from speech shows great potential in extensive downstream applications, while it still suffers challenges in imitating realistic human movements. Predominant research efforts focus on end-to-end generation schemes to generate co-speech gestures, spanning GANs, VQ-VAE, and recent diffusion models. As an ill-posed problem, in this paper, we argue that these prevailing learning schemes fail to model crucial inter- and intra-correlations across different motion units, i.e. head, body, and hands, thus leading to unnatural movements and poor coordination. To delve into these intrinsic correlations, we propose a unified Hierarchical Implicit Periodicity (HIP) learning approach for audio-inspired 3D gesture generation. Different from predominant research, our approach models this multi-modal implicit relationship by two explicit technique insights: i) To disentangle the complicated gesture movements, we first explore the gesture motion phase manifolds with periodic autoencoders to imitate human natures from realistic distributions while incorporating non-period ones from current latent states for instance-level diversities. ii) To model the hierarchical relationship of face motions, body gestures, and hand movements, driving the animation with cascaded guidance during learning. We exhibit our proposed approach on 3D avatars and extensive experiments show our method outperforms the state-of-the-art co-speech gesture generation methods by both quantitative and qualitative evaluations. Code and models will be publicly available.

