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

**提出MobileWorldBench基准和MobileWorld数据集，通过语义世界建模提升移动GUI代理的任务成功率**

**关键词**: `语义世界建模` `移动GUI代理` `视觉语言模型` `基准测试` `大规模数据集` `自然语言描述` `任务规划` `界面自动化`

## 📋 核心要点

1. 现有像素空间世界模型在GUI环境中预测复杂视觉元素困难，限制了移动代理的实际应用。
2. 论文提出用自然语言描述状态转换的语义世界建模方法，并构建基准和数据集提升视觉语言模型能力。
3. 实验表明，集成语义世界模型的移动代理框架能显著提高任务成功率，验证了方法的有效性。

## 📝 摘要（中文）

世界模型在提升具身代理任务性能方面显示出巨大效用。先前工作主要关注像素空间世界模型，但这些方法在GUI设置中面临实际限制，预测未来状态的复杂视觉元素通常很困难。在本工作中，我们探索了GUI代理世界建模的替代方案，其中状态转换用自然语言描述而非预测原始像素。首先，我们引入了MobileWorldBench，这是一个评估视觉语言模型作为移动GUI代理世界模型能力的基准。其次，我们发布了MobileWorld，一个包含140万样本的大规模数据集，显著提升了视觉语言模型的世界建模能力。最后，我们提出了一个新颖框架，将视觉语言模型世界模型集成到移动代理的规划框架中，证明语义世界模型可以通过提高任务成功率直接使移动代理受益。代码和数据集可在https://github.com/jacklishufan/MobileWorld获取。

## 🔬 方法详解

论文提出一个集成视觉语言模型作为世界模型的移动代理框架。整体框架包括：MobileWorldBench基准用于评估视觉语言模型在GUI环境中的世界建模能力，MobileWorld数据集提供大规模训练样本以增强模型性能，以及一个规划框架将语义世界模型与代理决策过程结合。关键技术创新点在于用自然语言替代像素预测来描述状态转换，这降低了建模复杂度并提高了可解释性。与现有方法的主要区别在于从像素空间转向语义空间，避免了直接预测复杂视觉元素的困难，更适合GUI环境下的实际应用。

## 📊 实验亮点

实验结果显示，使用MobileWorld数据集训练的视觉语言模型在世界建模能力上显著提升。集成该语义世界模型的移动代理框架在任务成功率上取得明显改进，验证了语义方法相对于传统像素空间模型的优势，为GUI代理的实用化提供了新途径。

## 🎯 应用场景

该研究可应用于移动GUI代理的自动化任务执行，如智能手机应用操作、网页浏览辅助和软件测试自动化。通过语义世界建模，代理能更准确地理解和预测界面变化，提升在复杂交互环境中的任务成功率，具有实际部署价值。

## 📄 摘要（原文）

> World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision-language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available at https://github.com/jacklishufan/MobileWorld

