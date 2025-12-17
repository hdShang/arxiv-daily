---
layout: default
title: UniGen-1.5: Enhancing Image Generation and Editing through Reward Unification in Reinforcement Learning
---

# UniGen-1.5: Enhancing Image Generation and Editing through Reward Unification in Reinforcement Learning

**arXiv**: [2511.14760v1](https://arxiv.org/abs/2511.14760) | [PDF](https://arxiv.org/pdf/2511.14760.pdf)

**作者**: Rui Tian, Mingfei Gao, Haiming Gang, Jiasen Lu, Zhe Gan, Yinfei Yang, Zuxuan Wu, Afshin Dehghan

---

## 💡 一句话要点

**提出UniGen-1.5模型，通过统一强化学习奖励增强图像生成与编辑能力**

**关键词**: `多模态大语言模型` `图像生成` `图像编辑` `强化学习` `奖励统一` `指令对齐`

## 📋 核心要点

1. 核心问题：多模态大模型在图像生成和编辑中性能需提升，以超越现有先进模型
2. 方法要点：采用统一强化学习策略，共享奖励模型联合优化生成与编辑任务
3. 实验或效果：在GenEval和ImgEdit基准上得分0.89和4.31，优于BAGEL等模型

## 📄 摘要（原文）

> We present UniGen-1.5, a unified multimodal large language model (MLLM) for advanced image understanding, generation and editing. Building upon UniGen, we comprehensively enhance the model architecture and training pipeline to strengthen the image understanding and generation capabilities while unlocking strong image editing ability. Especially, we propose a unified Reinforcement Learning (RL) strategy that improves both image generation and image editing jointly via shared reward models. To further enhance image editing performance, we propose a light Edit Instruction Alignment stage that significantly improves the editing instruction comprehension that is essential for the success of the RL training. Experimental results show that UniGen-1.5 demonstrates competitive understanding and generation performance. Specifically, UniGen-1.5 achieves 0.89 and 4.31 overall scores on GenEval and ImgEdit that surpass the state-of-the-art models such as BAGEL and reaching performance comparable to proprietary models such as GPT-Image-1.

