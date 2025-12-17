---
layout: default
title: Dedelayed: Deleting remote inference delay via on-device correction
---

# Dedelayed: Deleting remote inference delay via on-device correction

**arXiv**: [2510.13714v1](https://arxiv.org/abs/2510.13714) | [PDF](https://arxiv.org/pdf/2510.13714.pdf)

**作者**: Dan Jacobellis, Mateen Ulhaq, Fabien Racapé, Hyomin Choi, Neeraja J. Yadwadkar

---

## 💡 一句话要点

**提出Dedelayed方法，通过本地校正缓解远程推理延迟，实现实时输出。**

**关键词**: `远程推理` `延迟校正` `实时系统` `语义分割` `特征融合`

## 📋 核心要点

1. 远程推理因网络延迟导致预测过时，不适用于实时任务。
2. 使用轻量本地模型融合当前帧与远程模型历史特征，校正延迟。
3. 在BDD100K数据集上，延迟100ms时精度提升6.4 mIoU，优势随延迟和运动增强。

## 📄 摘要（原文）

> Remote inference allows lightweight devices to leverage powerful cloud
> models. However, communication network latency makes predictions stale and
> unsuitable for real-time tasks. To address this, we introduce Dedelayed, a
> delay-corrective method that mitigates arbitrary remote inference delays,
> allowing the local device to produce low-latency outputs in real time. Our
> method employs a lightweight local model that processes the current frame and
> fuses in features that a heavyweight remote model computes from past frames. On
> video from the BDD100K driving dataset, Dedelayed improves semantic
> segmentation accuracy over the stronger of the local-only and remote-only
> baselines across all realistic communication network delays beyond 33 ms.
> Without incurring additional delay, it improves accuracy by 6.4 mIoU compared
> to fully local inference and 9.8 mIoU compared to remote inference, for a
> round-trip delay of 100 ms. The advantage grows under longer delays and
> higher-motion scenes, as delay-mitigated split inference sustains accuracy more
> effectively, providing clear advantages for real-time tasks that must remain
> aligned with the current world state.

