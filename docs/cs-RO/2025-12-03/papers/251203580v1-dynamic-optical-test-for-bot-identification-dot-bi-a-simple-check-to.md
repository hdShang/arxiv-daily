---
layout: default
title: Dynamic Optical Test for Bot Identification (DOT-BI): A simple check to identify bots in surveys and online processes
---

# Dynamic Optical Test for Bot Identification (DOT-BI): A simple check to identify bots in surveys and online processes

**arXiv**: [2512.03580v1](https://arxiv.org/abs/2512.03580) | [PDF](https://arxiv.org/pdf/2512.03580.pdf)

**作者**: Malte Bleeker, Mauro Gotsch

---

## 💡 一句话要点

**提出动态光学测试DOT-BI，利用人类运动感知区分在线调查中的机器人与人类用户。**

**关键词**: `机器人识别` `动态光学测试` `在线调查` `人类感知` `多模态模型`

## 📋 核心要点

1. 核心问题：在线调查和流程中，机器人自动化系统可能干扰数据收集，需简单有效识别方法。
2. 方法要点：通过隐藏数字与背景相同纹理，仅靠运动差异使人类可感知，算法难以处理。
3. 实验或效果：初步评估显示先进多模态模型失败，在线调查中99.5%参与者成功完成，平均用时10.7秒。

## 📄 摘要（原文）

> We propose the Dynamic Optical Test for Bot Identification (DOT-BI): a quick and easy method that uses human perception of motion to differentiate between human respondents and automated systems in surveys and online processes. In DOT-BI, a 'hidden' number is displayed with the same random black-and-white pixel texture as its background. Only the difference in motion and scale between the number and the background makes the number perceptible to humans across frames, while frame-by-frame algorithmic processing yields no meaningful signal. We conducted two preliminary assessments. Firstly, state-of-the-art, video-capable, multimodal models (GPT-5-Thinking and Gemini 2.5 Pro) fail to extract the correct value, even when given explicit instructions about the mechanism. Secondly, in an online survey (n=182), 99.5% (181/182) of participants solved the task, with an average end-to-end completion time of 10.7 seconds; a supervised lab study (n=39) found no negative effects on perceived ease-of-use or completion time relative to a control. We release code to generate tests and 100+ pre-rendered variants to facilitate adoption in surveys and online processes.

