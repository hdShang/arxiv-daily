---
layout: default
title: MindPower: Enabling Theory-of-Mind Reasoning in VLM-based Embodied Agents
---

# MindPower: Enabling Theory-of-Mind Reasoning in VLM-based Embodied Agents

**arXiv**: [2511.23055v1](https://arxiv.org/abs/2511.23055) | [PDF](https://arxiv.org/pdf/2511.23055.pdf)

**作者**: Ruoxuan Zhang, Qiyun Zheng, Zhiyu Zhou, Ziqi Liao, Siyu Wu, Jian-Yu Jiang-Lin, Bin Wen, Hongxia Xie, Jianlong Fu, Wen-Huang Cheng

---

## 💡 一句话要点

**提出MindPower框架，通过机器人中心视角整合心智推理，以提升具身智能体的决策与行动生成能力。**

**关键词**: `心智理论推理` `具身智能体` `视觉语言模型` `机器人中心框架` `决策生成` `行动生成`

## 📋 核心要点

1. 核心问题：现有视觉语言具身智能体缺乏心智理论推理，且基准测试忽略自身视角，导致决策不连贯。
2. 方法要点：设计机器人中心框架，集成感知、心智推理、决策与行动，并引入Mind-Reward优化目标促进一致性。
3. 实验或效果：在决策和行动生成上分别超越GPT-4o 12.77%和12.49%，验证了框架的有效性。

## 📄 摘要（原文）

> Theory of Mind (ToM) refers to the ability to infer others' mental states, such as beliefs, desires, and intentions. Current vision-language embodied agents lack ToM-based decision-making, and existing benchmarks focus solely on human mental states while ignoring the agent's own perspective, hindering coherent decision and action generation. To address this, we propose MindPower, a Robot-Centric framework integrating Perception, Mental Reasoning, Decision Making and Action. Given multimodal inputs, MindPower first perceives the environment and human states, then performs ToM Reasoning to model both self and others, and finally generates decisions and actions guided by inferred mental states. Furthermore, we introduce Mind-Reward, a novel optimization objective that encourages VLMs to produce consistent ToM Reasoning and behavior. Our model outperforms GPT-4o by 12.77% in decision making and 12.49% in action generation.

