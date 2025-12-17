---
layout: default
title: MobileWorldBench: Towards Semantic World Modeling For Mobile Agents
---

# MobileWorldBench: Towards Semantic World Modeling For Mobile Agents

**arXiv**: [2512.14014v1](https://arxiv.org/abs/2512.14014) | [PDF](https://arxiv.org/pdf/2512.14014.pdf)

**作者**: Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: 21 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/jacklishufan/MobileWorld)

---

## 💡 一句话要点

**提出MobileWorldBench基准和MobileWorld数据集，通过语义世界建模提升移动GUI代理的任务成功率。**

🎯 **匹配领域**: **世界模型** **强化学习**

**关键词**: `语义世界建模` `移动GUI代理` `视觉语言模型` `基准评估` `大规模数据集` `规划框架` `自然语言描述` `任务成功率提升`

## 📋 核心要点

1. 现有像素空间世界模型在GUI环境中预测复杂视觉元素困难，限制了移动代理的实际应用。
2. 论文提出用自然语言描述状态转换的语义世界建模方法，替代传统像素预测，并引入基准和数据集。
3. 实验表明，集成视觉语言模型世界模型能显著提升移动代理的任务成功率，验证了语义建模的有效性。

## 📝 摘要（中文）

世界模型在提升具身代理任务性能方面显示出巨大效用。先前工作主要关注像素空间世界模型，但这些方法在GUI设置中面临实际限制，预测未来状态的复杂视觉元素通常很困难。在本工作中，我们探索了GUI代理世界建模的替代方案，其中状态转换用自然语言描述，而不是预测原始像素。首先，我们引入了MobileWorldBench，这是一个评估视觉语言模型作为移动GUI代理世界模型能力的基准。其次，我们发布了MobileWorld，一个包含140万个样本的大规模数据集，显著提升了视觉语言模型的世界建模能力。最后，我们提出了一个新颖框架，将视觉语言模型世界模型集成到移动代理的规划框架中，证明语义世界模型可以通过提高任务成功率直接使移动代理受益。代码和数据集可在https://github.com/jacklishufan/MobileWorld获取。

## 🔬 方法详解

论文提出一个集成视觉语言模型世界模型到移动代理规划框架的新颖框架。整体框架包括MobileWorldBench基准评估视觉语言模型作为世界模型的能力，以及MobileWorld数据集用于训练和提升模型性能。关键技术创新点在于将状态转换从像素空间迁移到语义空间，用自然语言描述GUI状态变化，避免了复杂视觉预测的困难。与现有方法的主要区别在于，传统方法依赖像素级预测，而本方法利用视觉语言模型的语义理解能力，更适用于GUI环境，提高了世界建模的实用性和可扩展性。

## 📊 实验亮点

实验结果显示，使用MobileWorld数据集训练的视觉语言模型世界模型在MobileWorldBench基准上表现优异，集成到移动代理规划框架后，任务成功率得到显著提升，具体数值未知，但验证了语义世界建模对移动代理性能的积极影响。

## 🎯 应用场景

该研究主要应用于移动GUI代理领域，如智能手机应用自动化、机器人界面交互和智能助手任务执行。通过语义世界建模，代理能更准确地理解和预测GUI状态变化，提升任务完成效率和成功率，具有实际部署价值。

## 📄 摘要（原文）

> World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision-language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available at https://github.com/jacklishufan/MobileWorld

