---
layout: default
title: Evaluating Gemini Robotics Policies in a Veo World Simulator
---

# Evaluating Gemini Robotics Policies in a Veo World Simulator

**arXiv**: [2512.10675v1](https://arxiv.org/abs/2512.10675) | [PDF](https://arxiv.org/pdf/2512.10675.pdf)

**作者**: Gemini Robotics Team, Coline Devin, Yilun Du, Debidatta Dwibedi, Ruiqi Gao, Abhishek Jindal, Thomas Kipf, Sean Kirmani, Fangchen Liu, Anirudha Majumdar, Andrew Marmon, Carolina Parada, Yulia Rubanova, Dhruv Shah, Vikas Sindhwani, Jie Tan, Fei Xia, Ted Xiao, Sherry Yang, Wenhao Yu, Allan Zhou

---

## 💡 一句话要点

**提出基于Veo视频模型的机器人策略评估系统，支持分布内外泛化与安全测试。**

**关键词**: `视频基础模型` `机器人策略评估` `分布外泛化` `生成世界模型` `多视图一致性` `安全测试`

## 📋 核心要点

1. 核心问题：视频模型在机器人学中主要用于分布内评估，缺乏对分布外泛化和安全性的全面评估。
2. 方法要点：构建基于前沿视频基础模型（Veo）的生成评估系统，优化动作条件化和多视图一致性，集成图像编辑与多视图补全。
3. 实验或效果：通过1600+真实世界评估验证系统能准确预测策略性能，分析泛化轴影响，并进行红队测试以暴露安全违规行为。

## 📄 摘要（原文）

> Generative world models hold significant potential for simulating interactions with visuomotor policies in varied environments. Frontier video models can enable generation of realistic observations and environment interactions in a scalable and general manner. However, the use of video models in robotics has been limited primarily to in-distribution evaluations, i.e., scenarios that are similar to ones used to train the policy or fine-tune the base video model. In this report, we demonstrate that video models can be used for the entire spectrum of policy evaluation use cases in robotics: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety. We introduce a generative evaluation system built upon a frontier video foundation model (Veo). The system is optimized to support robot action conditioning and multi-view consistency, while integrating generative image-editing and multi-view completion to synthesize realistic variations of real-world scenes along multiple axes of generalization. We demonstrate that the system preserves the base capabilities of the video model to enable accurate simulation of scenes that have been edited to include novel interaction objects, novel visual backgrounds, and novel distractor objects. This fidelity enables accurately predicting the relative performance of different policies in both nominal and OOD conditions, determining the relative impact of different axes of generalization on policy performance, and performing red teaming of policies to expose behaviors that violate physical or semantic safety constraints. We validate these capabilities through 1600+ real-world evaluations of eight Gemini Robotics policy checkpoints and five tasks for a bimanual manipulator.

