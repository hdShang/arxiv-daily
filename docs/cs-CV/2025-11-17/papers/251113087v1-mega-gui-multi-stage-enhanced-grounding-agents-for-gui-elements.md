---
layout: default
title: MEGA-GUI: Multi-stage Enhanced Grounding Agents for GUI Elements
---

# MEGA-GUI: Multi-stage Enhanced Grounding Agents for GUI Elements

**arXiv**: [2511.13087v1](https://arxiv.org/abs/2511.13087) | [PDF](https://arxiv.org/pdf/2511.13087.pdf)

**作者**: SeokJoo Kwak, Jihoon Kim, Boyoun Kim, Jung Jae Yoon, Wooseok Jang, Jeonghoon Hong, Jaeho Yang, Yeong-Dae Kwon

---

## 💡 一句话要点

**提出多阶段增强GUI元素定位框架以解决视觉杂乱和语义模糊问题**

**关键词**: `GUI定位` `多阶段框架` `视觉语言模型` `ROI选择` `语义消歧` `基准测试`

## 📋 核心要点

1. 核心问题：现有GUI定位系统缺乏模块化，在视觉杂乱和模糊指令下性能不佳
2. 方法要点：采用多阶段框架，分离粗粒度ROI选择和细粒度元素定位，使用双向ROI缩放和上下文重写代理
3. 实验或效果：在ScreenSpot-Pro和OSWorld-G基准上分别达到73.18%和68.63%准确率，超越先前方法

## 📄 摘要（原文）

> Graphical User Interface (GUI) grounding - the task of mapping natural language instructions to screen coordinates - is essential for autonomous agents and accessibility technologies. Existing systems rely on monolithic models or one-shot pipelines that lack modularity and fail under visual clutter and ambiguous instructions. We introduce MEGA-GUI, a multi-stage framework that separates grounding into coarse Region-of-Interest (ROI) selection and fine-grained element grounding, orchestrated by specialized vision-language agents. MEGA-GUI features a bidirectional ROI zoom algorithm that mitigates spatial dilution and a context-aware rewriting agent that reduces semantic ambiguity. Our analysis reveals complementary strengths and weaknesses across vision-language models at different visual scales, and we show that leveraging this modular structure achieves consistently higher accuracy than monolithic approaches. On the visually dense ScreenSpot-Pro benchmark, MEGA-GUI attains 73.18% accuracy, and on the semantically complex OSWorld-G benchmark it reaches 68.63%, surpassing previously reported results. Code and the Grounding Benchmark Toolkit (GBT) are available at https://github.com/samsungsds-research-papers/mega-gui.

