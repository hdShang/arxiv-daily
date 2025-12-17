---
layout: default
title: Lost in Time? A Meta-Learning Framework for Time-Shift-Tolerant Physiological Signal Transformation
---

# Lost in Time? A Meta-Learning Framework for Time-Shift-Tolerant Physiological Signal Transformation

**arXiv**: [2511.21500v1](https://arxiv.org/abs/2511.21500) | [PDF](https://arxiv.org/pdf/2511.21500.pdf)

**作者**: Qian Hong, Cheng Bian, Xiao Zhou, Xiaoyu Li, Yelei Li, Zijing Zeng

---

## 💡 一句话要点

**提出ShiftSyncNet以解决生理信号转换中的时间偏移问题**

**关键词**: `生理信号转换` `时间偏移校正` `元学习` `多模态信号` `傅里叶相位偏移`

## 📋 核心要点

1. 核心问题：多模态生理信号转换中时间错位降低准确性，如ABP峰值捕捉。
2. 方法要点：基于元学习的双层优化框架，包含TransNet和SyncNet，自动校正时间偏移。
3. 实验或效果：在真实和公共数据集上，性能提升达9.4%、6.0%和12.8%。

## 📄 摘要（原文）

> Translating non-invasive signals such as photoplethysmography (PPG) and ballistocardiography (BCG) into clinically meaningful signals like arterial blood pressure (ABP) is vital for continuous, low-cost healthcare monitoring. However, temporal misalignment in multimodal signal transformation impairs transformation accuracy, especially in capturing critical features like ABP peaks. Conventional synchronization methods often rely on strong similarity assumptions or manual tuning, while existing Learning with Noisy Labels (LNL) approaches are ineffective under time-shifted supervision, either discarding excessive data or failing to correct label shifts. To address this challenge, we propose ShiftSyncNet, a meta-learning-based bi-level optimization framework that automatically mitigates performance degradation due to time misalignment. It comprises a transformation network (TransNet) and a time-shift correction network (SyncNet), where SyncNet learns time offsets between training pairs and applies Fourier phase shifts to align supervision signals. Experiments on one real-world industrial dataset and two public datasets show that ShiftSyncNet outperforms strong baselines by 9.4%, 6.0%, and 12.8%, respectively. The results highlight its effectiveness in correcting time shifts, improving label quality, and enhancing transformation accuracy across diverse misalignment scenarios, pointing toward a unified direction for addressing temporal inconsistencies in multimodal physiological transformation.

