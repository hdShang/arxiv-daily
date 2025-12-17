---
layout: default
title: Towards Blind and Low-Vision Accessibility of Lightweight VLMs and Custom LLM-Evals
---

# Towards Blind and Low-Vision Accessibility of Lightweight VLMs and Custom LLM-Evals

**arXiv**: [2511.10615v1](https://arxiv.org/abs/2511.10615) | [PDF](https://arxiv.org/pdf/2511.10615.pdf)

**作者**: Shruti Singh Baghel, Yash Pratap Singh Rathore, Sushovan Jena, Anurag Pradhan, Amit Shukla, Arnav Bhavsar, Pawan Goyal

---

## 💡 一句话要点

**提出轻量VLM评估框架以提升盲人和低视力用户的可访问性**

**关键词**: `视觉语言模型` `盲人可访问性` `轻量模型评估` `移动部署` `视频描述生成`

## 📋 核心要点

1. 核心问题：大型视觉语言模型资源需求高，限制盲人和低视力用户获取详细视频描述。
2. 方法要点：评估SmolVLM2变体，并设计多上下文和导航辅助评估框架。
3. 实验或效果：在AVCaps和Charades数据集测试不同提示策略和移动设备部署。

## 📄 摘要（原文）

> Large Vision-Language Models (VLMs) excel at understanding and generating video descriptions but their high memory, computation, and deployment demands hinder practical use particularly for blind and low-vision (BLV) users who depend on detailed, context-aware descriptions. To study the effect of model size on accessibility-focused description quality, we evaluate SmolVLM2 variants with 500M and 2.2B parameters across two diverse datasets: AVCaps (outdoor), and Charades (indoor). In this work, we introduce two novel evaluation frameworks specifically designed for BLV accessibility assessment: the Multi-Context BLV Framework evaluating spatial orientation, social interaction, action events, and ambience contexts; and the Navigational Assistance Framework focusing on mobility-critical information. Additionally, we conduct a systematic evaluation of four different prompt design strategies and deploy both models on a smartphone, evaluating FP32 and INT8 precision variants to assess real-world performance constraints on resource-limited mobile devices.

