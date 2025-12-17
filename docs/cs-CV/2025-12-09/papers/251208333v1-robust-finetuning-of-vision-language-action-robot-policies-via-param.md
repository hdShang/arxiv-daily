---
layout: default
title: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging
---

# Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging

**arXiv**: [2512.08333v1](https://arxiv.org/abs/2512.08333) | [PDF](https://arxiv.org/pdf/2512.08333.pdf)

**作者**: Yajat Yadav, Zhiyuan Zhou, Andrew Wagenmaker, Karl Pertsch, Sergey Levine

---

## 💡 一句话要点

**提出参数合并方法以解决机器人策略微调中的过拟合与泛化能力丧失问题**

**关键词**: `机器人策略` `参数合并` `微调泛化` `视觉语言动作模型` `终身学习`

## 📋 核心要点

1. 核心问题：通用机器人策略微调新任务时易过拟合，丧失原有泛化能力
2. 方法要点：通过合并微调模型与预训练模型的权重，实现新技能稳健融入
3. 实验或效果：在模拟与真实实验中，合并模型在新任务分布外变体上优于预训练和微调模型

## 📄 摘要（原文）

> Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

