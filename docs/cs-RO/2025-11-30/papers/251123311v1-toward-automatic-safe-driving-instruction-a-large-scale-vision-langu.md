---
layout: default
title: Toward Automatic Safe Driving Instruction: A Large-Scale Vision Language Model Approach
---

# Toward Automatic Safe Driving Instruction: A Large-Scale Vision Language Model Approach

**arXiv**: [2511.23311v1](https://arxiv.org/abs/2511.23311) | [PDF](https://arxiv.org/pdf/2511.23311.pdf)

**作者**: Haruki Sakajo, Hiroshi Takato, Hiroshi Tsutsui, Komei Soda, Hidetaka Kamigaito, Taro Watanabe

---

## 💡 一句话要点

**提出基于大规模视觉语言模型的自动安全驾驶指令生成方法，通过双摄像头同步输入提升安全性。**

**关键词**: `大规模视觉语言模型` `安全驾驶指令` `双摄像头同步输入` `视频事件检测` `模型微调`

## 📋 核心要点

1. 核心问题：现有LVLMs在生成安全驾驶指令时，需同时处理道路和驾驶员视角视频以检测风险事件。
2. 方法要点：构建数据集并微调LVLMs，使其能处理同步双摄像头输入，生成准确的安全指令。
3. 实验或效果：微调后模型性能显著提升，但检测复杂事件仍存挑战，错误分析提供改进方向。

## 📄 摘要（原文）

> Large-scale Vision Language Models (LVLMs) exhibit advanced capabilities in tasks that require visual information, including object detection. These capabilities have promising applications in various industrial domains, such as autonomous driving. For example, LVLMs can generate safety-oriented descriptions of videos captured by road-facing cameras. However, ensuring comprehensive safety requires monitoring driver-facing views as well to detect risky events, such as the use of mobiles while driving. Thus, the ability to process synchronized inputs is necessary from both driver-facing and road-facing cameras. In this study, we develop models and investigate the capabilities of LVLMs by constructing a dataset and evaluating their performance on this dataset. Our experimental results demonstrate that while pre-trained LVLMs have limited effectiveness, fine-tuned LVLMs can generate accurate and safety-aware driving instructions. Nonetheless, several challenges remain, particularly in detecting subtle or complex events in the video. Our findings and error analysis provide valuable insights that can contribute to the improvement of LVLM-based systems in this domain.

