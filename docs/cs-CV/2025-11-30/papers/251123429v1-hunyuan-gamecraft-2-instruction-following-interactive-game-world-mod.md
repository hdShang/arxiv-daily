---
layout: default
title: Hunyuan-GameCraft-2: Instruction-following Interactive Game World Model
---

# Hunyuan-GameCraft-2: Instruction-following Interactive Game World Model

**arXiv**: [2511.23429v1](https://arxiv.org/abs/2511.23429) | [PDF](https://arxiv.org/pdf/2511.23429.pdf)

**作者**: Junshu Tang, Jiacheng Liu, Jiaqi Li, Longhuang Wu, Haoyu Yang, Penghao Zhao, Siruis Gong, Xiang Yuan, Shuai Shao, Qinglin Lu

---

## 💡 一句话要点

**提出Hunyuan-GameCraft-2，通过指令驱动交互解决游戏世界建模中动作模式僵化和标注成本高的问题。**

**关键词**: `指令驱动交互` `生成游戏世界模型` `交互视频数据` `文本驱动控制` `因果对齐数据集` `混合专家模型`

## 📋 核心要点

1. 核心问题：现有生成世界模型受限于固定动作模式和标注成本，难以建模多样游戏交互和玩家驱动动态。
2. 方法要点：基于14B图像到视频MoE基础模型，引入文本驱动交互注入机制，支持自然语言、键盘或鼠标控制游戏视频内容。
3. 实验或效果：在InterBench基准上验证，模型能生成时间连贯、因果合理的交互游戏视频，响应自由形式指令如“开门”。

## 📄 摘要（原文）

> Recent advances in generative world models have enabled remarkable progress in creating open-ended game environments, evolving from static scene synthesis toward dynamic, interactive simulation. However, current approaches remain limited by rigid action schemas and high annotation costs, restricting their ability to model diverse in-game interactions and player-driven dynamics. To address these challenges, we introduce Hunyuan-GameCraft-2, a new paradigm of instruction-driven interaction for generative game world modeling. Instead of relying on fixed keyboard inputs, our model allows users to control game video contents through natural language prompts, keyboard, or mouse signals, enabling flexible and semantically rich interaction within generated worlds. We formally defined the concept of interactive video data and developed an automated process to transform large-scale, unstructured text-video pairs into causally aligned interactive datasets. Built upon a 14B image-to-video Mixture-of-Experts(MoE) foundation model, our model incorporates a text-driven interaction injection mechanism for fine-grained control over camera motion, character behavior, and environment dynamics. We introduce an interaction-focused benchmark, InterBench, to evaluate interaction performance comprehensively. Extensive experiments demonstrate that our model generates temporally coherent and causally grounded interactive game videos that faithfully respond to diverse and free-form user instructions such as "open the door", "draw a torch", or "trigger an explosion".

