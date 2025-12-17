---
layout: default
title: PhyVLLM: Physics-Guided Video Language Model with Motion-Appearance Disentanglement
---

# PhyVLLM: Physics-Guided Video Language Model with Motion-Appearance Disentanglement

**arXiv**: [2512.04532v1](https://arxiv.org/abs/2512.04532) | [PDF](https://arxiv.org/pdf/2512.04532.pdf)

**作者**: Yu-Wei Zhan, Xin Wang, Hong Chen, Tongtong Feng, Wei Feng, Ren Wang, Guangyao Li, Qing Li, Wenwu Zhu

---

## 💡 一句话要点

**提出PhyVLLM框架，通过解耦运动与外观并集成物理动态建模，以增强视频大语言模型的物理推理能力。**

**关键词**: `视频大语言模型` `物理动态建模` `运动-外观解耦` `神经常微分方程` `自监督学习` `视频理解`

## 📋 核心要点

1. 核心问题：现有视频大语言模型依赖外观匹配，缺乏对物理动态的深层理解，导致在物理推理场景中表现不佳。
2. 方法要点：采用双分支编码器解耦外观与运动，集成神经常微分方程模块建模连续物理动态，并以自监督方式训练避免依赖物理标注。
3. 实验或效果：在物理推理和通用视频理解任务上显著超越现有先进模型，验证了显式物理建模的优势。

## 📄 摘要（原文）

> Video Large Language Models (Video LLMs) have shown impressive performance across a wide range of video-language tasks. However, they often fail in scenarios requiring a deeper understanding of physical dynamics. This limitation primarily arises from their reliance on appearance-based matching. Incorporating physical motion modeling is crucial for deeper video understanding, but presents three key challenges: (1) motion signals are often entangled with appearance variations, making it difficult to extract clean physical cues; (2) effective motion modeling requires not only continuous-time motion representations but also capturing physical dynamics; and (3) collecting accurate annotations for physical attributes is costly and often impractical. To address these issues, we propose PhyVLLM, a physical-guided video-language framework that explicitly incorporates physical motion into Video LLMs. Specifically, PhyVLLM disentangles visual appearance and object motion through a dual-branch encoder. To model physical dynamics over time, we incorporate a Neural Ordinary Differential Equation (Neural ODE) module, which generates differentiable physical dynamic representations. The resulting motion-aware representations are projected into the token space of a pretrained LLM, enabling physics reasoning without compromising the model's original multimodal capabilities. To circumvent the need for explicit physical labels, PhyVLLM employs a self-supervised manner to model the continuous evolution of object motion. Experimental results demonstrate that PhyVLLM significantly outperforms state-of-the-art Video LLMs on both physical reasoning and general video understanding tasks, highlighting the advantages of incorporating explicit physical modeling.

