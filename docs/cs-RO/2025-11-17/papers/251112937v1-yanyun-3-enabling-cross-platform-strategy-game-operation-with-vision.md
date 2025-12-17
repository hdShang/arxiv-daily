---
layout: default
title: Yanyun-3: Enabling Cross-Platform Strategy Game Operation with Vision-Language Models
---

# Yanyun-3: Enabling Cross-Platform Strategy Game Operation with Vision-Language Models

**arXiv**: [2511.12937v1](https://arxiv.org/abs/2511.12937) | [PDF](https://arxiv.org/pdf/2511.12937.pdf)

**作者**: Guoyan Wang, Yanyan Huang, Chunlin Chen, Lifeng Wang, Yuxiang Sun

---

## 💡 一句话要点

**提出Yanyun-3框架，实现跨平台策略游戏的自主操作。**

**关键词**: `跨平台游戏自动化` `视觉语言模型` `多模态数据融合` `实时操作` `泛化能力`

## 📋 核心要点

1. 核心问题：跨平台策略游戏自动化需泛化处理多样界面和动态战场。
2. 方法要点：融合Qwen2.5-VL视觉语言推理与UI-TARS精确执行能力。
3. 实验或效果：MV+S混合策略提升BLEU-4分数约12.98倍，减少推理时间63%。

## 📄 摘要（原文）

> Automated operation in cross-platform strategy games demands agents with robust generalization across diverse user interfaces and dynamic battlefield conditions. While vision-language models (VLMs) have shown considerable promise in multimodal reasoning, their application to complex human-computer interaction scenarios--such as strategy gaming--remains largely unexplored. Here, we introduce Yanyun-3, a general-purpose agent framework that, for the first time, enables autonomous cross-platform operation across three heterogeneous strategy game environments. By integrating the vision-language reasoning of Qwen2.5-VL with the precise execution capabilities of UI-TARS, Yanyun-3 successfully performs core tasks including target localization, combat resource allocation, and area control. Through systematic ablation studies, we evaluate the effects of various multimodal data combinations--static images, multi-image sequences, and videos--and propose the concept of combination granularity to differentiate between intra-sample fusion and inter-sample mixing strategies. We find that a hybrid strategy, which fuses multi-image and video data while mixing in static images (MV+S), substantially outperforms full fusion: it reduces inference time by 63% and boosts the BLEU-4 score by a factor of 12 (from 4.81% to 62.41%, approximately 12.98x). Operating via a closed-loop pipeline of screen capture, model inference, and action execution, the agent demonstrates strong real-time performance and cross-platform generalization. Beyond providing an efficient solution for strategy game automation, our work establishes a general paradigm for enhancing VLM performance through structured multimodal data organization, offering new insights into the interplay between static perception and dynamic reasoning in embodied intelligence.

