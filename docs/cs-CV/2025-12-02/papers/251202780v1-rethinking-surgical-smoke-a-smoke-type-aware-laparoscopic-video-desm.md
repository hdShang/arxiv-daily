---
layout: default
title: Rethinking Surgical Smoke: A Smoke-Type-Aware Laparoscopic Video Desmoking Method and Dataset
---

# Rethinking Surgical Smoke: A Smoke-Type-Aware Laparoscopic Video Desmoking Method and Dataset

**arXiv**: [2512.02780v1](https://arxiv.org/abs/2512.02780) | [PDF](https://arxiv.org/pdf/2512.02780.pdf)

**作者**: Qifan Liang, Junlin Li, Zhen Han, Xihao Wang, Zhongyuan Wang, Bin Mei

---

## 💡 一句话要点

**提出烟雾类型感知的腹腔镜视频去烟网络STANet，以解决手术烟雾对视频引导的干扰问题。**

**关键词**: `腹腔镜视频去烟` `烟雾类型感知` `掩码分割` `视频重建` `合成数据集` `手术视觉引导`

## 📋 核心要点

1. 核心问题：手术烟雾根据运动模式分为扩散烟雾和环境烟雾，现有去烟方法未考虑烟雾类型差异。
2. 方法要点：设计烟雾掩码分割子网络预测烟雾类型和掩码，嵌入粗到细解缠模块处理烟雾类型纠缠。
3. 实验或效果：构建首个大规模合成视频去烟数据集，实验显示方法在质量评估和下游任务泛化性上优于现有方法。

## 📄 摘要（原文）

> Electrocautery or lasers will inevitably generate surgical smoke, which hinders the visual guidance of laparoscopic videos for surgical procedures. The surgical smoke can be classified into different types based on its motion patterns, leading to distinctive spatio-temporal characteristics across smoky laparoscopic videos. However, existing desmoking methods fail to account for such smoke-type-specific distinctions. Therefore, we propose the first Smoke-Type-Aware Laparoscopic Video Desmoking Network (STANet) by introducing two smoke types: Diffusion Smoke and Ambient Smoke. Specifically, a smoke mask segmentation sub-network is designed to jointly conduct smoke mask and smoke type predictions based on the attention-weighted mask aggregation, while a smokeless video reconstruction sub-network is proposed to perform specially desmoking on smoky features guided by two types of smoke mask. To address the entanglement challenges of two smoke types, we further embed a coarse-to-fine disentanglement module into the mask segmentation sub-network, which yields more accurate disentangled masks through the smoke-type-aware cross attention between non-entangled and entangled regions. In addition, we also construct the first large-scale synthetic video desmoking dataset with smoke type annotations. Extensive experiments demonstrate that our method not only outperforms state-of-the-art approaches in quality evaluations, but also exhibits superior generalization across multiple downstream surgical tasks.

