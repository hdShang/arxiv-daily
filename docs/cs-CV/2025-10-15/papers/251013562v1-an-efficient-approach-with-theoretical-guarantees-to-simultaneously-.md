---
layout: default
title: An efficient approach with theoretical guarantees to simultaneously reconstruct activity and attenuation sinogram for TOF-PET
---

# An efficient approach with theoretical guarantees to simultaneously reconstruct activity and attenuation sinogram for TOF-PET

**arXiv**: [2510.13562v1](https://arxiv.org/abs/2510.13562) | [PDF](https://arxiv.org/pdf/2510.13562.pdf)

**作者**: Liyang Hu, Chong Chen

---

## 💡 一句话要点

**提出基于最大似然估计的模型，从TOF-PET发射数据同时重建活性和衰减正弦图**

**关键词**: `正电子发射断层成像` `衰减校正` `最大似然估计` `时间飞行PET` `正弦图重建` `交替更新算法`

## 📋 核心要点

1. 核心问题：PET中衰减校正依赖额外扫描，导致辐射、时间和运动错位问题
2. 方法要点：利用衰减校正因子的指数形式，结合活动总量约束，证明解的存在唯一性
3. 实验或效果：数值实验显示方法收敛、抗噪，在精度和效率上优于现有方法

## 📄 摘要（原文）

> In positron emission tomography (PET), it is indispensable to perform
> attenuation correction in order to obtain the quantitatively accurate activity
> map (tracer distribution) in the body. Generally, this is carried out based on
> the estimated attenuation map obtained from computed tomography or magnetic
> resonance imaging. However, except for errors in the attenuation correction
> factors obtained, the additional scan not only brings in new radiation doses
> and/or increases the scanning time but also leads to severe misalignment
> induced by various motions during and between the two sequential scans. To
> address these issues, based on maximum likelihood estimation, we propose a new
> mathematical model for simultaneously reconstructing the activity and
> attenuation sinogram from the time-of-flight (TOF)-PET emission data only.
> Particularly, we make full use of the exclusively exponential form for the
> attenuation correction factors, and consider the constraint of a total amount
> of the activity in some mask region in the proposed model. Furthermore, we
> prove its well-posedness, including the existence, uniqueness and stability of
> the solution. We propose an alternating update algorithm to solve the model,
> and also analyze its convergence. Finally, numerical experiments with various
> TOF-PET emission data demonstrate that the proposed method is of numerical
> convergence and robust to noise, and outperforms some state-of-the-art methods
> in terms of accuracy and efficiency, and has the capability of autonomous
> attenuation correction.

