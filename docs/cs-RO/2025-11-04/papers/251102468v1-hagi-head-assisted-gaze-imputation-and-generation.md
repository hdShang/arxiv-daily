---
layout: default
title: HAGI++: Head-Assisted Gaze Imputation and Generation
---

# HAGI++: Head-Assisted Gaze Imputation and Generation

**arXiv**: [2511.02468v1](https://arxiv.org/abs/2511.02468) | [PDF](https://arxiv.org/pdf/2511.02468.pdf)

**作者**: Chuhan Jiao, Zhiming Hu, Andreas Bulling

---

## 💡 一句话要点

**提出HAGI++方法，利用头向传感器解决移动眼动追踪中缺失值问题**

**关键词**: `眼动追踪` `数据填补` `多模态学习` `扩散模型` `头眼相关性`

## 📋 核心要点

1. 移动眼动追踪中，眨眼或检测错误导致缺失值，影响数据分析
2. 采用多模态扩散模型，结合头眼运动相关性进行数据填补
3. 在多个数据集上优于传统方法，生成更真实的眼动速度分布

## 📄 摘要（原文）

> Mobile eye tracking plays a vital role in capturing human visual attention
> across both real-world and extended reality (XR) environments, making it an
> essential tool for applications ranging from behavioural research to
> human-computer interaction. However, missing values due to blinks, pupil
> detection errors, or illumination changes pose significant challenges for
> further gaze data analysis. To address this challenge, we introduce HAGI++ - a
> multi-modal diffusion-based approach for gaze data imputation that, for the
> first time, uses the integrated head orientation sensors to exploit the
> inherent correlation between head and eye movements. HAGI++ employs a
> transformer-based diffusion model to learn cross-modal dependencies between eye
> and head representations and can be readily extended to incorporate additional
> body movements. Extensive evaluations on the large-scale Nymeria, Ego-Exo4D,
> and HOT3D datasets demonstrate that HAGI++ consistently outperforms
> conventional interpolation methods and deep learning-based time-series
> imputation baselines in gaze imputation. Furthermore, statistical analyses
> confirm that HAGI++ produces gaze velocity distributions that closely match
> actual human gaze behaviour, ensuring more realistic gaze imputations.
> Moreover, by incorporating wrist motion captured from commercial wearable
> devices, HAGI++ surpasses prior methods that rely on full-body motion capture
> in the extreme case of 100% missing gaze data (pure gaze generation). Our
> method paves the way for more complete and accurate eye gaze recordings in
> real-world settings and has significant potential for enhancing gaze-based
> analysis and interaction across various application domains.

