---
layout: default
title: TaskEval: Synthesised Evaluation for Foundation-Model Tasks
---

# TaskEval: Synthesised Evaluation for Foundation-Model Tasks

**arXiv**: [2512.04442v1](https://arxiv.org/abs/2512.04442) | [PDF](https://arxiv.org/pdf/2512.04442.pdf)

**作者**: Dilani Widanapathiranage, Scott Barnett, Stefanus Kurniawan, Wannita Takerngsaksiri

---

## 💡 一句话要点

**提出TaskEval以合成基础模型任务评估器，解决无标准评估时的自动化与人工反馈集成问题。**

**关键词**: `基础模型评估` `任务无关元模型` `评估合成` `人工反馈集成` `幻觉检测` `自动化评估`

## 📋 核心要点

1. 核心问题：基础模型应用中幻觉问题需评估，但缺乏任务特定指标或数据集时难以自动化评估。
2. 方法要点：基于任务无关元模型、高效人工反馈交互协议和评估合成器，生成定制评估程序。
3. 实验或效果：在图表数据提取和文档问答任务上初步评估，所选评估准确率分别为93%和90%。

## 📄 摘要（原文）

> Hallucinations are a key concern when creating applications that rely on Foundation models (FMs). Understanding where and how these subtle failures occur in an application relies on evaluation methods known as \textit{evals}. Prior work focuses on defining new eval methods or benchmark datasets for specific tasks. However, neither helps a software team with a task-specific FM application when there is no metric or dataset. The demand for both automated approaches and deep integration of human insight makes this a challenging problem. We address this gap by proposing an approach to synthesise a FM task-specific evaluator program that provides automation and a custom UI for capturing feedback. The core novelty of our approach lies in: (1) a task-agnostic meta-model that captures properties of any FM task, (2) an interaction protocol for efficient use of human feedback, and (3) an eval synthesiser that selects or generates an appropriate set of evals. We implement our approach in \toolname and demonstrate the concept on two diverse FM tasks: chart data extraction and document question answering. A preliminary evaluation on the quality of our selected evals shows 93\% and 90\% accuracy respectively. Our research tackles a growing problem facing engineering teams, how to evaluate and review outputs from FM tasks.

