---
layout: default
title: Robust HRRP Recognition under Interrupted Sampling Repeater Jamming using a Prior Jamming Information-Guided Network
---

# Robust HRRP Recognition under Interrupted Sampling Repeater Jamming using a Prior Jamming Information-Guided Network

**arXiv**: [2511.23256v1](https://arxiv.org/abs/2511.23256) | [PDF](https://arxiv.org/pdf/2511.23256.pdf)

**作者**: Guozheng Sun, Lei Wang, Yanhao Wang, Jie Wang, Yimin Liu

---

## 💡 一句话要点

**提出基于先验干扰信息引导的网络，以解决中断采样转发干扰下的稳健HRRP识别问题。**

**关键词**: `高分辨率距离像识别` `中断采样转发干扰` `先验信息引导` `稳健特征学习` `雷达自动目标识别`

## 📋 核心要点

1. 核心问题：中断采样转发干扰导致HRRP特征严重失真，影响雷达自动目标识别。
2. 方法要点：利用点扩散函数作为先验信息建模干扰失真，设计引导特征交互模块和混合损失函数。
3. 实验或效果：模拟和实测数据实验显示，方法优于现有技术，对未见干扰参数具有强泛化能力。

## 📄 摘要（原文）

> Radar automatic target recognition (RATR) based on high-resolution range profile (HRRP) has attracted increasing attention due to its ability to capture fine-grained structural features. However, recognizing targets under electronic countermeasures (ECM), especially the mainstream interrupted-sampling repeater jamming (ISRJ), remains a significant challenge, as HRRPs often suffer from serious feature distortion. To address this, we propose a robust HRRP recognition method guided by prior jamming information. Specifically, we introduce a point spread function (PSF) as prior information to model the HRRP distortion induced by ISRJ. Based on this, we design a recognition network that leverages this prior through a prior-guided feature interaction module and a hybrid loss function to enhance the model's discriminative capability. With the aid of prior information, the model can learn invariant features within distorted HRRP under different jamming parameters. Both the simulated and measured-data experiments demonstrate that our method consistently outperforms state-of-the-art approaches and exhibits stronger generalization capabilities when facing unseen jamming parameters.

