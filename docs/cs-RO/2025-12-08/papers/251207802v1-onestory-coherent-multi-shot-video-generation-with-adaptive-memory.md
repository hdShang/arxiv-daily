---
layout: default
title: OneStory: Coherent Multi-Shot Video Generation with Adaptive Memory
---

# OneStory: Coherent Multi-Shot Video Generation with Adaptive Memory

**arXiv**: [2512.07802v1](https://arxiv.org/abs/2512.07802) | [PDF](https://arxiv.org/pdf/2512.07802.pdf)

**作者**: Zhaochong An, Menglin Jia, Haonan Qiu, Zijian Zhou, Xiaoke Huang, Zhiheng Liu, Weiming Ren, Kumara Kahatapitiya, Ding Liu, Sen He, Chenyang Zhang, Tao Xiang, Fanny Yang, Serge Belongie, Tian Xie

---

## 💡 一句话要点

**提出OneStory以解决多镜头视频生成中长程跨镜头上下文建模不足的问题**

**关键词**: `多镜头视频生成` `跨镜头上下文建模` `自适应条件器` `下一镜头生成` `叙事连贯性` `长视频生成`

## 📋 核心要点

1. 核心问题：现有方法依赖有限时间窗口或单关键帧条件，难以建模复杂叙事下的跨镜头上下文
2. 方法要点：将多镜头视频生成重构为下一镜头生成任务，引入帧选择模块和自适应条件器进行全局紧凑上下文建模
3. 实验或效果：在自建60K数据集上微调，在文本和图像条件下实现最先进的叙事连贯性，支持可控长视频生成

## 📄 摘要（原文）

> Storytelling in real-world videos often unfolds through multiple shots -- discontinuous yet semantically connected clips that together convey a coherent narrative. However, existing multi-shot video generation (MSV) methods struggle to effectively model long-range cross-shot context, as they rely on limited temporal windows or single keyframe conditioning, leading to degraded performance under complex narratives. In this work, we propose OneStory, enabling global yet compact cross-shot context modeling for consistent and scalable narrative generation. OneStory reformulates MSV as a next-shot generation task, enabling autoregressive shot synthesis while leveraging pretrained image-to-video (I2V) models for strong visual conditioning. We introduce two key modules: a Frame Selection module that constructs a semantically-relevant global memory based on informative frames from prior shots, and an Adaptive Conditioner that performs importance-guided patchification to generate compact context for direct conditioning. We further curate a high-quality multi-shot dataset with referential captions to mirror real-world storytelling patterns, and design effective training strategies under the next-shot paradigm. Finetuned from a pretrained I2V model on our curated 60K dataset, OneStory achieves state-of-the-art narrative coherence across diverse and complex scenes in both text- and image-conditioned settings, enabling controllable and immersive long-form video storytelling.

