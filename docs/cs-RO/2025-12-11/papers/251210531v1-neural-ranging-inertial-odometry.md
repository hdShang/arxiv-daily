---
layout: default
title: Neural Ranging Inertial Odometry
---

# Neural Ranging Inertial Odometry

**arXiv**: [2512.10531v1](https://arxiv.org/abs/2512.10531) | [PDF](https://arxiv.org/pdf/2512.10531.pdf)

**作者**: Si Wang, Bingqi Shen, Fei Wang, Yanjun Cao, Rong Xiong, Yue Wang

---

## 💡 一句话要点

**提出神经融合框架IR-ULSG，结合图注意力UWB网络和循环神经惯性网络，以解决GPS缺失环境下UWB定位精度受限问题。**

**关键词**: `UWB定位` `神经融合框架` `图注意力网络` `惯性里程计` `GPS缺失环境` `多径干扰`

## 📋 核心要点

1. 核心问题：UWB定位在真实场景中因传感器布置敏感性和多径干扰导致精度受限，尤其在长隧道等环境中。
2. 方法要点：设计图注意力网络学习场景相关测距模式，适应任意锚点或标签数，无需校准；集成最小二乘法和名义帧提升性能与可扩展性。
3. 实验或效果：在公共和自收集数据集上验证，涵盖室内、室外和隧道环境，显示在凸包外和单锚点等挑战条件下具有优越性。

## 📄 摘要（原文）

> Ultra-wideband (UWB) has shown promising potential in GPS-denied localization thanks to its lightweight and drift-free characteristics, while the accuracy is limited in real scenarios due to its sensitivity to sensor arrangement and non-Gaussian pattern induced by multi-path or multi-signal interference, which commonly occurs in many typical applications like long tunnels. We introduce a novel neural fusion framework for ranging inertial odometry which involves a graph attention UWB network and a recurrent neural inertial network. Our graph net learns scene-relevant ranging patterns and adapts to any number of anchors or tags, realizing accurate positioning without calibration. Additionally, the integration of least squares and the incorporation of nominal frame enhance overall performance and scalability. The effectiveness and robustness of our methods are validated through extensive experiments on both public and self-collected datasets, spanning indoor, outdoor, and tunnel environments. The results demonstrate the superiority of our proposed IR-ULSG in handling challenging conditions, including scenarios outside the convex envelope and cases where only a single anchor is available.

