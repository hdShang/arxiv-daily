---
layout: default
title: TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models
---

# TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models

**arXiv**: [2511.21145v1](https://arxiv.org/abs/2511.21145) | [PDF](https://arxiv.org/pdf/2511.21145.pdf)

**作者**: Jiaming He, Guanyu Hou, Hongwei Li, Zhicong Huang, Kangjie Chen, Yi Yu, Wenbo Jiang, Guowen Xu, Tianwei Zhang

---

## 💡 一句话要点

**提出TEAR框架以解决文本到视频模型中的时序安全风险**

**关键词**: `文本到视频模型` `时序安全评估` `自动化红队测试` `对抗性提示生成` `在线偏好学习`

## 📋 核心要点

1. 核心问题：现有安全评估方法无法捕捉视频生成的复杂时序动态。
2. 方法要点：采用时序感知测试生成器，通过两阶段优化和循环精炼模型。
3. 实验或效果：在开源和商业系统中攻击成功率超80%，显著提升。

## 📄 摘要（原文）

> Text-to-Video (T2V) models are capable of synthesizing high-quality, temporally coherent dynamic video content, but the diverse generation also inherently introduces critical safety challenges. Existing safety evaluation methods,which focus on static image and text generation, are insufficient to capture the complex temporal dynamics in video generation. To address this, we propose a TEmporal-aware Automated Red-teaming framework, named TEAR, an automated framework designed to uncover safety risks specifically linked to the dynamic temporal sequencing of T2V models. TEAR employs a temporal-aware test generator optimized via a two-stage approach: initial generator training and temporal-aware online preference learning, to craft textually innocuous prompts that exploit temporal dynamics to elicit policy-violating video output. And a refine model is adopted to improve the prompt stealthiness and adversarial effectiveness cyclically. Extensive experimental evaluation demonstrates the effectiveness of TEAR across open-source and commercial T2V systems with over 80% attack success rate, a significant boost from prior best result of 57%.

