---
layout: default
title: Audio-sync Video Instance Editing with Granularity-Aware Mask Refiner
---

# Audio-sync Video Instance Editing with Granularity-Aware Mask Refiner

**arXiv**: [2512.10571v1](https://arxiv.org/abs/2512.10571) | [PDF](https://arxiv.org/pdf/2512.10571.pdf)

**作者**: Haojie Zheng, Shuchen Weng, Jingqi Liu, Siqi Yang, Boxin Shi, Xinlong Wang

---

## 💡 一句话要点

**提出AVI-Edit框架，通过粒度感知掩码精炼器和自反馈音频代理实现音频同步的视频实例编辑。**

**关键词**: `视频实例编辑` `音频-视觉同步` `掩码精炼` `自反馈代理` `数据集构建`

## 📋 核心要点

1. 现有视频编辑方法忽视音频-视觉同步，缺乏实例级精细控制。
2. 引入粒度感知掩码精炼器迭代优化掩码，自反馈音频代理提供高质量音频引导。
3. 实验表明AVI-Edit在视觉质量、条件遵循和音频-视觉同步方面优于现有方法。

## 📄 摘要（原文）

> Recent advancements in video generation highlight that realistic audio-visual synchronization is crucial for engaging content creation. However, existing video editing methods largely overlook audio-visual synchronization and lack the fine-grained spatial and temporal controllability required for precise instance-level edits. In this paper, we propose AVI-Edit, a framework for audio-sync video instance editing. We propose a granularity-aware mask refiner that iteratively refines coarse user-provided masks into precise instance-level regions. We further design a self-feedback audio agent to curate high-quality audio guidance, providing fine-grained temporal control. To facilitate this task, we additionally construct a large-scale dataset with instance-centric correspondence and comprehensive annotations. Extensive experiments demonstrate that AVI-Edit outperforms state-of-the-art methods in visual quality, condition following, and audio-visual synchronization. Project page: https://hjzheng.net/projects/AVI-Edit/.

