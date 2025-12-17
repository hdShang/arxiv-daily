---
layout: default
title: PerTouch: VLM-Driven Agent for Personalized and Semantic Image Retouching
---

# PerTouch: VLM-Driven Agent for Personalized and Semantic Image Retouching

**arXiv**: [2511.12998v1](https://arxiv.org/abs/2511.12998) | [PDF](https://arxiv.org/pdf/2511.12998.pdf)

**作者**: Zewei Chang, Zheng-Peng Duan, Jianxing Zhang, Chun-Le Guo, Siyu Liu, Hyungju Chun, Hyunhee Park, Zikun Liu, Chongyi Li

---

## 💡 一句话要点

**提出PerTouch框架，基于扩散模型实现个性化语义图像润色**

**关键词**: `图像润色` `扩散模型` `语义控制` `VLM代理` `个性化偏好`

## 📋 核心要点

1. 核心问题：图像润色需平衡可控性与用户主观审美偏好。
2. 方法要点：使用参数映射和VLM代理，支持语义级润色与用户意图对齐。
3. 实验效果：组件验证有效，在个性化润色中表现优越。

## 📄 摘要（原文）

> Image retouching aims to enhance visual quality while aligning with users' personalized aesthetic preferences. To address the challenge of balancing controllability and subjectivity, we propose a unified diffusion-based image retouching framework called PerTouch. Our method supports semantic-level image retouching while maintaining global aesthetics. Using parameter maps containing attribute values in specific semantic regions as input, PerTouch constructs an explicit parameter-to-image mapping for fine-grained image retouching. To improve semantic boundary perception, we introduce semantic replacement and parameter perturbation mechanisms in the training process. To connect natural language instructions with visual control, we develop a VLM-driven agent that can handle both strong and weak user instructions. Equipped with mechanisms of feedback-driven rethinking and scene-aware memory, PerTouch better aligns with user intent and captures long-term preferences. Extensive experiments demonstrate each component's effectiveness and the superior performance of PerTouch in personalized image retouching. Code is available at: https://github.com/Auroral703/PerTouch.

