---
layout: default
title: Towards Accurate UAV Image Perception: Guiding Vision-Language Models with Stronger Task Prompts
---

# Towards Accurate UAV Image Perception: Guiding Vision-Language Models with Stronger Task Prompts

**arXiv**: [2512.07302v1](https://arxiv.org/abs/2512.07302) | [PDF](https://arxiv.org/pdf/2512.07302.pdf)

**作者**: Mingning Guo, Mengwei Wu, Shaoxian Li, Haifeng Li, Chao Tao

---

## 💡 一句话要点

**提出AerialVP框架以增强任务提示，提升无人机图像感知中视觉语言模型的准确性**

**关键词**: `无人机图像感知` `视觉语言模型` `任务提示增强` `AerialVP框架` `AerialSense基准`

## 📋 核心要点

1. 无人机图像感知中，传统视觉语言模型因任务提示简单和图像复杂导致语义对齐困难，影响性能
2. AerialVP通过主动提取多维辅助信息增强任务提示，包括任务分析、工具选择和提示生成三阶段
3. 实验基于AerialSense基准，显示AerialVP能稳定提升开源和专有视觉语言模型的性能

## 📄 摘要（原文）

> Existing image perception methods based on VLMs generally follow a paradigm wherein models extract and analyze image content based on user-provided textual task prompts. However, such methods face limitations when applied to UAV imagery, which presents challenges like target confusion, scale variations, and complex backgrounds. These challenges arise because VLMs' understanding of image content depends on the semantic alignment between visual and textual tokens. When the task prompt is simplistic and the image content is complex, achieving effective alignment becomes difficult, limiting the model's ability to focus on task-relevant information. To address this issue, we introduce AerialVP, the first agent framework for task prompt enhancement in UAV image perception. AerialVP proactively extracts multi-dimensional auxiliary information from UAV images to enhance task prompts, overcoming the limitations of traditional VLM-based approaches. Specifically, the enhancement process includes three stages: (1) analyzing the task prompt to identify the task type and enhancement needs, (2) selecting appropriate tools from the tool repository, and (3) generating enhanced task prompts based on the analysis and selected tools. To evaluate AerialVP, we introduce AerialSense, a comprehensive benchmark for UAV image perception that includes Aerial Visual Reasoning, Aerial Visual Question Answering, and Aerial Visual Grounding tasks. AerialSense provides a standardized basis for evaluating model generalization and performance across diverse resolutions, lighting conditions, and both urban and natural scenes. Experimental results demonstrate that AerialVP significantly enhances task prompt guidance, leading to stable and substantial performance improvements in both open-source and proprietary VLMs. Our work will be available at https://github.com/lostwolves/AerialVP.

