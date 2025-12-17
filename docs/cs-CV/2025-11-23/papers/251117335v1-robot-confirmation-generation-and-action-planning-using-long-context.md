---
layout: default
title: Robot Confirmation Generation and Action Planning Using Long-context Q-Former Integrated with Multimodal LLM
---

# Robot Confirmation Generation and Action Planning Using Long-context Q-Former Integrated with Multimodal LLM

**arXiv**: [2511.17335v1](https://arxiv.org/abs/2511.17335) | [PDF](https://arxiv.org/pdf/2511.17335.pdf)

**作者**: Chiori Hori, Yoshiki Masuyama, Siddarth Jain, Radu Corcodel, Devesh Jha, Diego Romeres, Jonathan Le Roux

---

## 💡 一句话要点

**提出长上下文Q-Former与多模态LLM集成，以改进人机交互中的动作确认与规划。**

**关键词**: `长上下文理解` `多模态LLM` `人机交互` `动作确认生成` `视频理解`

## 📋 核心要点

1. 核心问题：现有方法依赖片段级处理，未利用长视频上下文信息。
2. 方法要点：引入长上下文Q-Former，整合左右上下文依赖和文本嵌入。
3. 实验或效果：在YouCook2语料库中，长上下文Q-Former提升确认生成和动作规划性能。

## 📄 摘要（原文）

> Human-robot collaboration towards a shared goal requires robots to understand human action and interaction with the surrounding environment. This paper focuses on human-robot interaction (HRI) based on human-robot dialogue that relies on the robot action confirmation and action step generation using multimodal scene understanding. The state-of-the-art approach uses multimodal transformers to generate robot action steps aligned with robot action confirmation from a single clip showing a task composed of multiple micro steps. Although actions towards a long-horizon task depend on each other throughout an entire video, the current approaches mainly focus on clip-level processing and do not leverage long-context information. This paper proposes a long-context Q-former incorporating left and right context dependency in full videos. Furthermore, this paper proposes a text-conditioning approach to feed text embeddings directly into the LLM decoder to mitigate the high abstraction of the information in text by Q-former. Experiments with the YouCook2 corpus show that the accuracy of confirmation generation is a major factor in the performance of action planning. Furthermore, we demonstrate that the long-context Q-former improves the confirmation and action planning by integrating VideoLLaMA3.

