---
layout: default
title: Leveraging LLMs for reward function design in reinforcement learning control tasks
---

# Leveraging LLMs for reward function design in reinforcement learning control tasks

**arXiv**: [2511.19355v1](https://arxiv.org/abs/2511.19355) | [PDF](https://arxiv.org/pdf/2511.19355.pdf)

**作者**: Franklin Cardenoso, Wouter Caarls

---

## 💡 一句话要点

**提出LEARN-Opt框架，以自动化强化学习中的奖励函数设计**

**关键词**: `强化学习` `奖励函数设计` `大语言模型` `自动化框架` `无监督评估`

## 📋 核心要点

1. 强化学习中奖励函数设计依赖专家知识，耗时且低效
2. LEARN-Opt基于LLM自动生成和评估奖励函数，无需预定义指标
3. 实验显示性能媲美或优于现有方法，降低先验知识需求

## 📄 摘要（原文）

> The challenge of designing effective reward functions in reinforcement learning (RL) represents a significant bottleneck, often requiring extensive human expertise and being time-consuming. Previous work and recent advancements in large language models (LLMs) have demonstrated their potential for automating the generation of reward functions. However, existing methodologies often require preliminary evaluation metrics, human-engineered feedback for the refinement process, or the use of environmental source code as context. To address these limitations, this paper introduces LEARN-Opt (LLM-based Evaluator and Analyzer for Reward functioN Optimization). This LLM-based, fully autonomous, and model-agnostic framework eliminates the need for preliminary metrics and environmental source code as context to generate, execute, and evaluate reward function candidates from textual descriptions of systems and task objectives. LEARN-Opt's main contribution lies in its ability to autonomously derive performance metrics directly from the system description and the task objective, enabling unsupervised evaluation and selection of reward functions. Our experiments indicate that LEARN-Opt achieves performance comparable to or better to that of state-of-the-art methods, such as EUREKA, while requiring less prior knowledge. We find that automated reward design is a high-variance problem, where the average-case candidate fails, requiring a multi-run approach to find the best candidates. Finally, we show that LEARN-Opt can unlock the potential of low-cost LLMs to find high-performing candidates that are comparable to, or even better than, those of larger models. This demonstrated performance affirms its potential to generate high-quality reward functions without requiring any preliminary human-defined metrics, thereby reducing engineering overhead and enhancing generalizability.

