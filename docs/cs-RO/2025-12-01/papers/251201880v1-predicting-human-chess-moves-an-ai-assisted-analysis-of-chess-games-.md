---
layout: default
title: Predicting Human Chess Moves: An AI Assisted Analysis of Chess Games Using Skill-group Specific n-gram Language Models
---

# Predicting Human Chess Moves: An AI Assisted Analysis of Chess Games Using Skill-group Specific n-gram Language Models

**arXiv**: [2512.01880v1](https://arxiv.org/abs/2512.01880) | [PDF](https://arxiv.org/pdf/2512.01880.pdf)

**作者**: Daren Zhong, Dingcheng Huang, Clayton Greenberg

---

## 💡 一句话要点

**提出基于技能组特定n-gram语言模型的框架，以预测人类棋步并分析不同技能水平的行为模式。**

**关键词**: `棋步预测` `n-gram语言模型` `技能组分析` `行为分析` `实时分析`

## 📋 核心要点

1. 核心问题：传统棋类引擎忽略人类棋手在不同技能水平下的变异性，难以准确预测人类棋步。
2. 方法要点：将棋手分为七个技能组，使用n-gram语言模型捕捉各组的棋步模式，并动态选择模型进行预测。
3. 实验或效果：在真实棋局数据上，技能分类准确率最高达31.7%，棋步预测准确率比基准提升最高39.1%。

## 📄 摘要（原文）

> Chess, a deterministic game with perfect information, has long served as a benchmark for studying strategic decision-making and artificial intelligence. Traditional chess engines or tools for analysis primarily focus on calculating optimal moves, often neglecting the variability inherent in human chess playing, particularly across different skill levels.
>   To overcome this limitation, we propose a novel and computationally efficient move prediction framework that approaches chess move prediction as a behavioral analysis task. The framework employs n-gram language models to capture move patterns characteristic of specific player skill levels. By dividing players into seven distinct skill groups, from novice to expert, we trained separate models using data from the open-source chess platform Lichess. The framework dynamically selects the most suitable model for prediction tasks and generates player moves based on preceding sequences.
>   Evaluation on real-world game data demonstrates that the model selector module within the framework can classify skill levels with an accuracy of up to 31.7\% when utilizing early game information (16 half-moves). The move prediction framework also shows substantial accuracy improvements, with our Selector Assisted Accuracy being up to 39.1\% more accurate than our benchmark accuracy. The computational efficiency of the framework further enhances its suitability for real-time chess analysis.

